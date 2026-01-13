#!/usr/bin/env python3
"""
Unified Build Tool

A comprehensive build system for academic content including Jupyter Books,
Marp slide presentations, and custom build tasks. This tool consolidates
multiple build workflows into a single, consistent interface.

Usage:
    python ubt.py book [options]     # Build Jupyter Book
    python ubt.py slides [options]   # Build Marp slides
    python ubt.py task <task_name>    # Run predefined tasks
    python ubt.py --config file.yml  # Use configuration file

Features:
    - Jupyter Book building with full customization
    - Marp slide generation (HTML, PDF, PNG)
    - Predefined task workflows
    - Configuration file support
    - Comprehensive error handling
    - Cross-platform compatibility

Author: Unified from multiple build scripts
Date: September 2025
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import webbrowser
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Optional, Union

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# Configuration constants
DEFAULT_CONFIG = {
    "book": {
        "source_dir": ".",
        "build_dir": "_build/html", 
        "output_dir": None,
        "warnings_as_errors": False,
        "verbose": False
    },
    "slides": {
        "theme_path": "./themes/",
        "theme": "graph_paper.css", 
        "output_dir": None,
        "formats": ["html", "pdf", "png"]
    },
    "tasks": {
        "book_dir": ".",
        "build_dir": "_build/html",
        "tex_dir": "_build/latex", 
        "pdf_file": "book.pdf"
    }
}


class BuildError(Exception):
    """Custom exception for build-related errors."""
    pass


class BaseBuilder(ABC):
    """Abstract base class for all builders."""
    
    def __init__(self, config: Dict, verbose: bool = False):
        self.config = config
        self.verbose = verbose
    
    def run_command(self, cmd: Union[str, List[str]], cwd: Optional[str] = None, 
                   check: bool = True) -> subprocess.CompletedProcess:
        """
        Execute a shell command with proper error handling.
        
        Args:
            cmd: Command to execute (string or list)
            cwd: Working directory for command execution
            check: Whether to raise exception on non-zero exit code
            
        Returns:
            CompletedProcess object with result details
            
        Raises:
            BuildError: If command fails and check=True
        """
        if isinstance(cmd, list):
            cmd_str = " ".join(cmd)
        else:
            cmd_str = cmd
            
        if self.verbose:
            print(f"🔧 Running: {cmd_str}")
            if cwd:
                print(f"   Working directory: {cwd}")
        
        try:
            # For interactive commands, don't capture output so user sees it in real-time
            # Only capture output in verbose mode for additional logging
            if self.verbose:
                result = subprocess.run(
                    cmd, shell=isinstance(cmd, str), cwd=cwd, 
                    check=check, capture_output=True, text=True
                )
                # Show captured output in verbose mode
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print(result.stderr, file=sys.stderr)
            else:
                # Don't capture output - let it flow through to terminal
                result = subprocess.run(
                    cmd, shell=isinstance(cmd, str), cwd=cwd, 
                    check=check, text=True
                )
                
            return result
            
        except subprocess.CalledProcessError as e:
            error_msg = f"Command failed: {cmd_str}"
            if e.stderr:
                error_msg += f"\nError: {e.stderr}"
            raise BuildError(error_msg) from e
    
    def check_dependency(self, command: str, install_hint: str = "") -> None:
        """
        Check if a required command is available.
        
        Args:
            command: Command to check for availability
            install_hint: Installation instructions to show if missing
            
        Raises:
            BuildError: If command is not found
        """
        if not shutil.which(command):
            error_msg = f"❌ Required command '{command}' not found."
            if install_hint:
                error_msg += f"\n💡 Install with: {install_hint}"
            raise BuildError(error_msg)
    
    def ensure_dir(self, path: str) -> None:
        """Create directory if it doesn't exist."""
        Path(path).mkdir(parents=True, exist_ok=True)
    
    @abstractmethod
    def build(self, *args, **kwargs) -> bool:
        """Execute the build process. Must be implemented by subclasses."""
        pass


class JupyterBookBuilder(BaseBuilder):
    """Builder for Jupyter Book projects."""
    
    def __init__(self, config: Dict, verbose: bool = False):
        super().__init__(config, verbose)
        self.check_dependency("jupyter-book", "pip install jupyter-book")
    
    def build(self, source_dir: Optional[str] = None, 
              output_dir: Optional[str] = None,
              update: bool = False, 
              warnings_as_errors: bool = False,
              builder: str = "html") -> bool:
        """
        Build Jupyter Book with specified options.
        
        Args:
            source_dir: Book source directory
            output_dir: Custom output directory  
            update: If True, incremental build; if False, full rebuild
            warnings_as_errors: Treat warnings as errors
            builder: Builder type (html, pdflatex)
            
        Returns:
            True if build successful, False otherwise
        """
        # Use config defaults if not specified
        source_dir = source_dir or self.config.get("source_dir", ".")
        
        # Build command
        cmd = ["jupyter-book", "build", source_dir]
        
        if builder != "html":
            cmd.extend(["--builder", builder])
            
        if output_dir:
            cmd.extend(["--path-output", output_dir])
            
        if not update:  # Full rebuild
            cmd.append("--all")
            
        if self.verbose:
            cmd.append("-v")
            
        if warnings_as_errors:
            cmd.append("-W")
        
        try:
            self.run_command(cmd)
            print("✅ Jupyter Book built successfully!")
            return True
        except BuildError as e:
            print(f"❌ Jupyter Book build failed: {e}")
            return False
    
    def get_index_path(self, source_dir: str, output_dir: Optional[str] = None) -> str:
        """Get path to the built book's index.html file."""
        if output_dir:
            return os.path.join(output_dir, "html", "index.html")
        return os.path.join(source_dir, "_build", "html", "index.html")
    
    def view(self, source_dir: str, output_dir: Optional[str] = None) -> bool:
        """Open the built book in default browser."""
        index_path = self.get_index_path(source_dir, output_dir)
        
        if not os.path.exists(index_path):
            print(f"❌ Book not found at: {index_path}")
            print("💡 Try building the book first")
            return False
        
        try:
            webbrowser.open(f"file://{os.path.abspath(index_path)}")
            print(f"📖 Opened book in browser: {index_path}")
            return True
        except Exception as e:
            print(f"❌ Failed to open browser: {e}")
            return False


class MarpSlidesBuilder(BaseBuilder):
    """Builder for Marp slide presentations."""
    
    def __init__(self, config: Dict, verbose: bool = False):
        super().__init__(config, verbose)
        self.check_dependency("marp", "npm install -g @marp-team/marp-cli")
    
    def build(self, markdown_file: str, 
              theme_path: Optional[str] = None,
              theme: Optional[str] = None,
              output_dir: Optional[str] = None,
              formats: Optional[List[str]] = None,
              skip_theme: bool = False) -> bool:
        """
        Build Marp slides from markdown file.
        
        Args:
            markdown_file: Path to markdown source file
            theme_path: Directory containing CSS themes
            theme: Theme file name
            output_dir: Output directory for generated files
            formats: List of formats to generate (html, pdf, png)
            skip_theme: If True, don't apply external theme (use embedded styles)
            
        Returns:
            True if build successful, False otherwise
        """
        if not os.path.isfile(markdown_file):
            print(f"❌ Markdown file not found: {markdown_file}")
            return False
        
        # Use config defaults
        theme_path = theme_path or self.config.get("theme_path", "./themes/")
        theme = theme or self.config.get("theme", "graph_paper.css")
        output_dir = output_dir or os.path.dirname(os.path.abspath(markdown_file))
        formats = formats or self.config.get("formats", ["html", "pdf", "png"])
        
        self.ensure_dir(output_dir)
        
        # Copy images if needed
        self._copy_images(markdown_file, output_dir)
        
        # Generate each requested format
        success = True
        base_name = Path(markdown_file).stem
        
        format_map = {
            "html": {"flag": "", "ext": "html"},
            "pdf": {"flag": "--pdf", "ext": "pdf"},  
            "png": {"flag": "--image png", "ext": "png"}
        }
        
        # Only apply theme if not skipping it
        theme_flag = ""
        if not skip_theme:
            theme_file = os.path.abspath(os.path.join(theme_path, theme))
            theme_flag = f"--theme {theme_file}"
        
        for fmt in formats:
            if fmt not in format_map:
                print(f"⚠️ Unknown format: {fmt}")
                continue
                
            output_file = os.path.join(output_dir, f"{base_name}.{format_map[fmt]['ext']}")
            
            cmd = [
                "marp",
                theme_flag,  # Will be empty if skip_theme=True
                "--allow-local-files",
                format_map[fmt]["flag"],
                f"-o {os.path.abspath(output_file)}",
                os.path.basename(markdown_file)
            ]
            
            # Remove empty strings from command
            cmd = [part for part in cmd if part]
            cmd_str = " ".join(cmd)
            
            try:
                self.run_command(
                    cmd_str, 
                    cwd=os.path.dirname(os.path.abspath(markdown_file))
                )
                print(f"✅ Generated {fmt.upper()}: {output_file}")
            except BuildError as e:
                print(f"❌ Failed to generate {fmt.upper()}: {e}")
                success = False
        
        return success
    
    def _copy_images(self, markdown_file: str, output_dir: str) -> None:
        """Copy images directory to output if needed."""
        source_dir = os.path.dirname(os.path.abspath(markdown_file))
        images_source = os.path.join(source_dir, "images")
        images_dest = os.path.join(output_dir, "images")
        
        if os.path.exists(images_source) and source_dir != output_dir:
            if os.path.exists(images_dest):
                shutil.rmtree(images_dest)
            shutil.copytree(images_source, images_dest)
            if self.verbose:
                print(f"📁 Copied images: {images_source} → {images_dest}")


class TaskRunner(BaseBuilder):
    """Runner for predefined build tasks."""
    
    def __init__(self, config: Dict, verbose: bool = False):
        super().__init__(config, verbose)
        self.book_builder = JupyterBookBuilder(config.get("book", {}), verbose)
        self.book_dir = config.get("book_dir", ".")
    
    def build(self, task_name: str) -> bool:
        """
        Execute a predefined task.
        
        Args:
            task_name: Name of the task to execute
            
        Returns:
            True if task completed successfully, False otherwise
        """
        tasks = {
            "pdf": self._build_pdf,
            "web": self._deploy_web,  
            "update": self._update_book,
            "rebuild": self._rebuild_book,
            "viewhtml": self._view_html,
            "viewpdf": self._view_pdf,
            "all": self._build_all
        }
        
        if task_name not in tasks:
            print(f"❌ Unknown task: {task_name}")
            print(f"💡 Available tasks: {', '.join(tasks.keys())}")
            return False
        
        try:
            return tasks[task_name]()
        except Exception as e:
            print(f"❌ Task '{task_name}' failed: {e}")
            return False
    
    def _build_pdf(self) -> bool:
        """Build book as PDF using pdflatex."""
        return self.book_builder.build(self.book_dir, builder="pdflatex")
    
    def _deploy_web(self) -> bool:
        """Deploy HTML build to GitHub Pages."""
        build_dir = os.path.join(self.book_dir, self.config.get("build_dir", "_build/html"))
        try:
            self.run_command(f"ghp-import -n -p -f {build_dir}")
            print("✅ Deployed to GitHub Pages!")
            return True
        except BuildError:
            return False
    
    def _update_book(self) -> bool:
        """Build book with incremental updates."""
        return self.book_builder.build(self.book_dir, update=True)
    
    def _rebuild_book(self) -> bool:
        """Full rebuild including kernel updates."""
        # Update kernels if script exists
        update_script = os.path.join(self.book_dir, "update_kernels.py")
        if os.path.exists(update_script):
            try:
                self.run_command(f"python {update_script}")
            except BuildError:
                print("⚠️ Kernel update failed, continuing with build...")
        
        return self.book_builder.build(self.book_dir, update=False)
    
    def _view_html(self) -> bool:
        """Open HTML book in browser."""
        return self.book_builder.view(self.book_dir)
    
    def _view_pdf(self) -> bool:
        """Open PDF book in default viewer."""
        tex_dir = self.config.get("tex_dir", "_build/latex")
        pdf_file = self.config.get("pdf_file", "book.pdf")
        pdf_path = os.path.join(self.book_dir, tex_dir, pdf_file)
        
        if not os.path.exists(pdf_path):
            print(f"❌ PDF not found: {pdf_path}")
            return False
        
        try:
            if sys.platform == "darwin":
                self.run_command(f"open {pdf_path}")
            elif sys.platform == "win32":
                os.startfile(pdf_path)
            else:
                self.run_command(f"xdg-open {pdf_path}")
            print(f"📖 Opened PDF: {pdf_path}")
            return True
        except Exception as e:
            print(f"❌ Failed to open PDF: {e}")
            return False
    
    def _build_all(self) -> bool:
        """Run complete build pipeline."""
        tasks = ["rebuild", "pdf", "rebuild", "web"]
        for task in tasks:
            if not self.build(task):
                return False
        return True


def load_config(config_file: str) -> Dict:
    """
    Load configuration from YAML or JSON file.
    
    Args:
        config_file: Path to configuration file
        
    Returns:
        Configuration dictionary
        
    Raises:
        BuildError: If config file cannot be loaded
    """
    if not os.path.exists(config_file):
        raise BuildError(f"Config file not found: {config_file}")
    
    try:
        with open(config_file, 'r') as f:
            if config_file.endswith('.yml') or config_file.endswith('.yaml'):
                if not HAS_YAML:
                    raise BuildError("YAML support requires 'pyyaml' package. Install with: pip install pyyaml")
                import yaml  # Import here when needed
                return yaml.safe_load(f) or {}
            elif config_file.endswith('.json'):
                return json.load(f)
            else:
                raise BuildError("Config file must be .yml, .yaml, or .json")
    except Exception as e:
        raise BuildError(f"Failed to load config: {e}") from e


def merge_configs(base: Dict, override: Dict) -> Dict:
    """Recursively merge configuration dictionaries."""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    return result


def create_sample_config(path: str) -> None:
    """Create a sample configuration file."""
    with open(path, 'w') as f:
        if path.endswith('.json'):
            json.dump(DEFAULT_CONFIG, f, indent=2)
        else:
            if not HAS_YAML:
                raise BuildError("YAML support requires 'pyyaml' package. Install with: pip install pyyaml")
            import yaml  # Import here when needed
            yaml.dump(DEFAULT_CONFIG, f, default_flow_style=False, indent=2)
    print(f"✅ Created sample config: {path}")


def main():
    """Main entry point for the unified build tool."""
    parser = argparse.ArgumentParser(
        description="Unified build tool for academic content",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Global options
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--config", help="Configuration file (YAML/JSON)")
    parser.add_argument("--create-config", help="Create sample config file and exit")
    
    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Book subcommand
    book_parser = subparsers.add_parser("book", help="Build Jupyter Book")
    book_parser.add_argument("source_dir", nargs="?", default=".", help="Book source directory")
    book_parser.add_argument("-o", "--output-dir", help="Custom output directory")
    book_parser.add_argument("--update", action="store_true", help="Incremental build")
    book_parser.add_argument("-W", "--warnings-as-errors", action="store_true", help="Treat warnings as errors")
    book_parser.add_argument("--builder", default="html", choices=["html", "pdflatex"], help="Builder type")
    book_parser.add_argument("--view", action="store_true", help="Open in browser after build")
    
    # Slides subcommand  
    slides_parser = subparsers.add_parser("slides", help="Build Marp slides")
    slides_parser.add_argument("markdown_file", help="Markdown file to build")
    slides_parser.add_argument("-t", "--theme-path", help="Theme directory path")
    slides_parser.add_argument("--theme", help="Theme CSS file name")
    slides_parser.add_argument("-o", "--output-dir", help="Output directory")
    slides_parser.add_argument("--formats", nargs="+", choices=["html", "pdf", "png"], help="Output formats")
    slides_parser.add_argument("--skip-theme", action="store_true", help="Skip external theme, use embedded styles")
    slides_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    
    # Task subcommand
    task_parser = subparsers.add_parser("task", help="Run predefined task")
    task_parser.add_argument("task_name", choices=["pdf", "web", "update", "rebuild", "viewhtml", "viewpdf", "all"], help="Task to run")
    task_parser.add_argument("--book-dir", default=".", help="Book directory for tasks")
    
    args = parser.parse_args()
    
    # Handle config file creation
    if args.create_config:
        create_sample_config(args.create_config)
        return
    
    # Load configuration
    config = DEFAULT_CONFIG.copy()
    
    # Auto-detect config file if not specified
    config_file = args.config
    if not config_file:
        # Look for common config file names in current directory
        for candidate in ['build_config.yml', 'build_config.yaml', 'ubt_config.yml', 'ubt_config.yaml', 'config.yml', 'config.yaml']:
            if os.path.exists(candidate):
                config_file = candidate
                if args.verbose:
                    print(f"🔧 Auto-detected config file: {config_file}")
                break
    
    # Load the config file if found
    if config_file:
        try:
            user_config = load_config(config_file)
            config = merge_configs(config, user_config)
        except BuildError as e:
            print(f"❌ {e}")
            sys.exit(1)
    
    # Execute command
    try:
        if args.command == "book":
            builder = JupyterBookBuilder(config.get("book", {}), args.verbose)
            
            # Use config values if args are defaults
            source_dir = args.source_dir if args.source_dir != "." else None
            output_dir = args.output_dir if args.output_dir else None
            
            success = builder.build(
                source_dir=source_dir,
                output_dir=output_dir,
                update=args.update,
                warnings_as_errors=args.warnings_as_errors,
                builder=args.builder
            )
            if success and args.view:
                view_source = source_dir or config.get("book", {}).get("source_dir", ".")
                builder.view(view_source, output_dir)
                
        elif args.command == "slides":
            builder = MarpSlidesBuilder(config.get("slides", {}), args.verbose)
            success = builder.build(
                markdown_file=args.markdown_file,
                theme_path=args.theme_path,
                theme=args.theme,
                output_dir=args.output_dir,
                formats=args.formats,
                skip_theme=args.skip_theme
            )
            
        elif args.command == "task":
            task_config = config.get("tasks", {})
            
            # Use config values if args are defaults
            book_dir = args.book_dir if args.book_dir != "." else None
            if book_dir:
                task_config["book_dir"] = book_dir
            
            runner = TaskRunner(task_config, args.verbose)
            success = runner.build(args.task_name)
            
        else:
            parser.print_help()
            return
            
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n❌ Build interrupted by user")
        sys.exit(1)
    except BuildError as e:
        print(f"❌ {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()