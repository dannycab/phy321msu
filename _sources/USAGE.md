# 🛠️ UBT (Unified Build Tool) Usage Guide

The Unified Build Tool (`ubt.py`) consolidates all build workflows for the PHY321 course into a single, consistent interface. This tool handles Jupyter Book building, Marp slide generation, and common development tasks.

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Command Overview](#-command-overview)
- [Book Building](#-book-building)  
- [Slide Generation](#-slide-generation)
- [Predefined Tasks](#-predefined-tasks)
- [Configuration](#-configuration)
- [Examples](#-examples)
- [Troubleshooting](#-troubleshooting)

## 🚀 Quick Start

```bash
# Most common commands
python ubt.py task update     # Quick incremental build
python ubt.py task rebuild    # Full rebuild with kernel updates
python ubt.py task viewhtml   # Build and open in browser
python ubt.py book --view     # Build book and open immediately
python ubt.py slides slides/day-01-introduction.md  # Build specific slide
```

## 📖 Command Overview

UBT has three main command types:

1. **`book`** - Build Jupyter Books with full control
2. **`slides`** - Generate Marp slide presentations  
3. **`task`** - Run predefined workflows (recommended for common tasks)

### Global Options

```bash
python ubt.py [GLOBAL_OPTIONS] COMMAND [COMMAND_OPTIONS]

Global Options:
  -h, --help              Show help message
  -v, --verbose           Enable verbose output
  --config FILE           Use custom configuration file (YAML/JSON)
  --create-config FILE    Create sample configuration file
```

## 📚 Book Building

The `book` command builds Jupyter Books with comprehensive options:

### Basic Usage

```bash
# Build HTML version (default)
python ubt.py book

# Build from specific directory
python ubt.py book /path/to/book

# Build and open in browser
python ubt.py book --view
```

### Advanced Options

```bash
python ubt.py book [SOURCE_DIR] [OPTIONS]

Positional Arguments:
  SOURCE_DIR              Book source directory (default: current directory)

Options:
  -o, --output-dir DIR    Custom output directory
  --update                Incremental build (faster)
  -W, --warnings-as-errors Treat warnings as build errors
  --builder TYPE          Builder type: html, pdflatex (default: html)
  --view                  Open result in browser/viewer after build
```

### Examples

```bash
# Incremental HTML build
python ubt.py book --update

# Build PDF version
python ubt.py book --builder pdflatex

# Build with custom output directory
python ubt.py book -o /tmp/my-book

# Build treating warnings as errors (strict mode)
python ubt.py book -W

# Full build and immediately view
python ubt.py book --view
```

## 🎯 Slide Generation

The `slides` command generates Marp presentations in multiple formats:

### Basic Usage

```bash
# Build slide in all default formats (HTML, PDF, PNG)
python ubt.py slides slides/day-01-introduction.md

# Build with custom theme
python ubt.py slides slides/day-01.md --theme custom.css
```

### Advanced Options

```bash
python ubt.py slides MARKDOWN_FILE [OPTIONS]

Required Arguments:
  MARKDOWN_FILE           Marp markdown file to build

Options:
  -t, --theme-path DIR    Theme directory path
  --theme THEME           Theme CSS file name
  -o, --output-dir DIR    Output directory for generated files
  --formats FORMAT [FORMAT ...]  Output formats: html, pdf, png
```

### Examples

```bash
# Build only HTML version
python ubt.py slides slides/day-01.md --formats html

# Build with custom theme directory and theme
python ubt.py slides slides/lecture.md -t ./custom-themes --theme dark.css

# Build to specific output directory
python ubt.py slides slides/day-01.md -o ./output/slides

# Build multiple formats
python ubt.py slides slides/day-01.md --formats html pdf
```

## ⚡ Predefined Tasks

Tasks provide convenient shortcuts for common workflows:

### Available Tasks

```bash
python ubt.py task TASK_NAME [OPTIONS]

Tasks:
  update      Build HTML incrementally (fast)
  rebuild     Update kernels + full rebuild  
  pdf         Build PDF version
  web         Deploy to GitHub Pages
  viewhtml    Build HTML and open in browser
  viewpdf     Build PDF and open in viewer
  all         Complete build pipeline
```

### Task Options

```bash
Options:
  --book-dir DIR         Book directory for tasks (default: current)
```

### Task Details

#### `update` - Incremental Build
- Fast incremental HTML build
- Reuses cached execution results
- Good for content changes

```bash
python ubt.py task update
```

#### `rebuild` - Full Rebuild
- Updates notebook kernels to "python3"
- Performs complete rebuild
- Use after environment changes

```bash
python ubt.py task rebuild
```

#### `pdf` - PDF Generation  
- Builds LaTeX/PDF version
- Requires LaTeX installation
- Takes longer than HTML

```bash
python ubt.py task pdf
```

#### `viewhtml` / `viewpdf` - Build and View
- Builds then opens result
- `viewhtml` opens in web browser
- `viewpdf` opens in system PDF viewer

```bash
python ubt.py task viewhtml
python ubt.py task viewpdf
```

#### `all` - Complete Pipeline
- Updates kernels
- Builds HTML and PDF
- Most comprehensive build

```bash
python ubt.py task all
```

## ⚙️ Configuration

UBT supports configuration files for customizing default behavior:

### Creating Configuration

```bash
# Create sample configuration file
python ubt.py --create-config my-config.yml
```

### Configuration Structure

```yaml
book:
  source_dir: "."
  build_dir: "_build/html"
  output_dir: null
  warnings_as_errors: false
  verbose: false

slides:
  theme_path: "./themes/"
  theme: "graph_paper.css"
  output_dir: null
  formats: ["html", "pdf", "png"]

tasks:
  book_dir: "."
  build_dir: "_build/html"
  tex_dir: "_build/latex"
  pdf_file: "book.pdf"
```

### Using Configuration

```bash
# Use configuration file
python ubt.py --config my-config.yml book

# Configuration applies to all commands
python ubt.py --config custom.yml task rebuild
```

## 💡 Examples

### Common Development Workflow

```bash
# 1. Make content changes to notebooks
# 2. Quick test build
python ubt.py task update

# 3. Full rebuild for final check
python ubt.py task rebuild

# 4. Generate PDF for sharing
python ubt.py task pdf

# 5. View results
python ubt.py task viewhtml
```

### Slide Development Workflow

```bash
# 1. Edit markdown slide file
# 2. Build and test
python ubt.py slides slides/my-lecture.md --formats html

# 3. Generate final versions
python ubt.py slides slides/my-lecture.md --formats html pdf png

# 4. Build all slides
./build-all-slides.sh  # Uses individual build scripts
```

### Batch Operations

```bash
# Build everything from scratch
python ubt.py task rebuild && python ubt.py task pdf

# Quick development cycle with viewing
python ubt.py task update && python ubt.py task viewhtml

# Full pipeline with custom configuration
python ubt.py --config production.yml task all
```

## 🔧 Troubleshooting

### Common Issues

#### Build Failures

```bash
# Clean build directory and retry
rm -rf _build/
python ubt.py task rebuild
```

#### Kernel Issues

```bash
# The 'rebuild' task automatically updates kernels
python ubt.py task rebuild

# Or manually update kernels
python update_kernels.py
```

#### Dependency Issues

```bash
# Reinstall requirements
pip install -r requirements.txt --upgrade

# Check Python environment
python ubt.py --verbose book  # Shows detailed output
```

#### Slide Build Issues

```bash
# Check if Marp is installed
marp --version

# Install Marp CLI if needed
npm install -g @marp-team/marp-cli

# Test with simple slide
python ubt.py slides slides/simple.md --verbose
```

### Verbose Mode

Use `-v/--verbose` for detailed output:

```bash
python ubt.py -v book
python ubt.py -v slides slides/day-01.md
python ubt.py -v task rebuild
```

### Error Messages

UBT provides clear error messages:

- **Build errors**: Show command that failed and output
- **File not found**: Check paths and file existence  
- **Permission errors**: Check file/directory permissions
- **Configuration errors**: Validate YAML/JSON syntax

### Getting Help

```bash
# General help
python ubt.py -h

# Command-specific help
python ubt.py book -h
python ubt.py slides -h
python ubt.py task -h
```

## 🔄 Migration from build.py

If you're migrating from the old `build.py`:

| Old Command | New UBT Command |
|-------------|-----------------|
| `python build.py` | `python ubt.py task update` |
| `python build.py update` | `python ubt.py task update` |
| `python build.py rebuild` | `python ubt.py task rebuild` |
| `python build.py pdf` | `python ubt.py task pdf` |
| `python build.py viewhtml` | `python ubt.py task viewhtml` |
| `python build.py viewpdf` | `python ubt.py task viewpdf` |
| `python build.py all` | `python ubt.py task all` |

### Key Improvements in UBT

- **Unified interface**: Single tool for books and slides
- **Better error handling**: Clearer error messages and recovery
- **Configuration support**: Customize behavior with config files
- **Cross-platform**: Works consistently across operating systems
- **Extensible**: Easy to add new tasks and builders

---

*For more help or to report issues, see the main [README.md](README.md) or open a GitHub issue.*