
# 📚 Classical Mechanics - PHY321 MSU

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Jupyter Book](https://jupyterbook.org/en/stable/_images/badge.svg)](https://jupyterbook.org)

A comprehensive course on Classical Mechanics taught at Michigan State University, combining traditional analytical methods with modern computational approaches.

## 🎯 Course Overview

- Newton's Laws of Motion and their applications
- Lagrangian and Hamiltonian mechanics  
- Differential equations in physics
- Numerical methods and computational modeling
- Real-world applications in research and industry

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ 
- Git
- Basic familiarity with Jupyter notebooks

### 📥 Cloning the Repository

```bash
git clone https://github.com/dannycab/phy321msu.git
cd phy321msu
```

### 🐍 Setting Up the Environment

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Jupyter kernel (for development):**
   ```bash
   pip install ipykernel
   python -m ipykernel install --user --name=.venv --display-name "Python (.venv)"
   ```

## 🔧 Building the Book

### Using the Unified Build Tool

The easiest way to build the book is using the unified build tool (`ubt.py`):

```bash
# Quick commands for common tasks
python ubt.py task update     # Build HTML incrementally  
python ubt.py task rebuild    # Update kernels and full rebuild
python ubt.py task pdf        # Build PDF version
python ubt.py task viewhtml   # Open HTML in browser
python ubt.py task viewpdf    # Open PDF in viewer
python ubt.py task all        # Full build pipeline

# More control with direct commands
python ubt.py book            # Build HTML version
python ubt.py book --builder pdflatex  # Build PDF
python ubt.py book --view     # Build and open in browser
python ubt.py slides slides/day-01.md  # Build specific slide
```

> 📖 **See [USAGE.md](USAGE.md) for complete command reference and examples**

### Manual Building

If you prefer to use Jupyter Book directly:

```bash
# Activate virtual environment first
source .venv/bin/activate

# Build HTML
jupyter-book build .

# Build PDF (requires LaTeX)
jupyter-book build . --builder pdflatex
```

## 📁 Project Structure

```
phy321msu/
├── 📖 intro.md                    # Main landing page
├── 📋 _toc.yml                    # Table of contents
├── ⚙️ _config.yml                 # Jupyter Book configuration
├── 🔧 ubt.py                     # Unified build tool (replaces build.py)
├── 📝 requirements.txt           # Python dependencies
├── 📚 lecture-notes/              # Combined weekly materials
│   ├── 01_notes.ipynb
│   ├── 02_notes.ipynb
│   └── ...
├── 👥 admin/                      # Course administration
│   ├── getting-started.ipynb
│   ├── teachers.md
│   └── textbooks.md
├── 🖼️ images/                     # Course images and figures
├── 📊 slides/                     # Lecture slides (Marp format)
├── 🎯 homeworks/                  # Problem sets (excluded from build)
├── 📝 midterms/                   # Exams (excluded from build)
├── 🔬 resources/                  # Additional materials (excluded from build)
└── 🏆 honors-projects/            # Advanced projects (excluded from build)
```

## 🛠️ Development Workflow

### Adding New Content

1. **Weekly materials**: Add new notebook files to the `lecture-notes/` directory
2. **Update TOC**: Edit `_toc.yml` to include new files
3. **Build and test**: Run `python ubt.py task rebuild` to ensure everything works

### Combining Week Files

The project includes scripts to combine separate start and notes files:

```bash
# Combine individual week files (if needed)
python combine_all_weeks.py

# Update notebook kernels (done automatically by ubt.py)
python update_kernels.py
```

### Working with Images

- Store images in the `images/` directory with appropriate subdirectories
- Use relative paths: `../images/folder/image.png` from lecture notes
- Supported formats: PNG, JPG, SVG, GIF

## 🎨 Customization

### Configuration

Key settings in `_config.yml`:

- **Execution**: Notebooks are executed on every build (`execute_notebooks: force`)
- **Math rendering**: Uses MathJax 3 for LaTeX equations
- **Exclusions**: Homework and exam files are excluded from the build
- **License**: Content is licensed under CC BY-NC-SA 4.0

### Themes and Styling

The book uses Jupyter Book's default theme with custom:
- MSU Spartan helmet logo
- Creative Commons license footer
- GitHub integration buttons

## 📖 Content Organization

### Weekly Structure

Each week typically contains:
- **Introduction/Overview**: Setting up the week's topics
- **Lecture Notes**: Detailed explanations with examples
- **Interactive Elements**: Code cells for demonstrations
- **Mathematical Content**: LaTeX-formatted equations

### Special Features

- 🎥 **Embedded Videos**: YouTube videos playable directly in pages
- 🧮 **Interactive Code**: Python examples and calculations
- 📊 **Visualizations**: Matplotlib and other plotting libraries
- 📚 **References**: Bibliography support with BibTeX

## 🤝 Contributing

### For Instructors

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-content`
3. Make your changes and test locally
4. Submit a pull request with clear description

### For Students

- Report issues via GitHub Issues
- Suggest improvements or corrections
- Share interesting applications or extensions

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Include docstrings for functions
- Comment complex equations and algorithms

## 🔍 Troubleshooting

### Common Issues

**Build Failures:**
```bash
# Clean and rebuild
rm -rf _build/
python ubt.py task rebuild
```

**Kernel Issues:**
```bash
# Update all notebook kernels (or use rebuild which does this automatically)
python update_kernels.py
# Or use the unified tool:
python ubt.py task rebuild
```

**Missing Dependencies:**
```bash
# Reinstall requirements
pip install -r requirements.txt --upgrade
```

**Image Path Problems:**
- Check that image paths are relative to the notebook location
- Ensure images exist in the `images/` directory
- Use forward slashes in paths (even on Windows)

### Getting Help

- 📧 Contact course instructors
- 🐛 Open a GitHub Issue
- 💬 Check existing discussions

## 📜 License

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

You are free to:
- **Share** — copy and redistribute the material
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — Give appropriate credit
- **NonCommercial** — Not for commercial purposes
- **ShareAlike** — Distribute under the same license

## 👨‍🏫 Authors

- **Danny Caballero** - Michigan State University
- **Morten Hjorth-Jensen** - Michigan State University
- **Rachel Henderson** - Michigan State University

## 🙏 Acknowledgments

- Michigan State University Physics Department
- Jupyter Book community
- Open source scientific Python ecosystem
- Students and colleagues who provided feedback

---

*Built with ❤️ using [Jupyter Book](https://jupyterbook.org) and the scientific Python ecosystem.*

---

## Repository Structure & Order of Materials

The course is organized in the following order, matching the learning progression:

1. **About the Course**
   - Getting started, instructor info, and textbooks (`admin/`)
2. **Calendar & Lecture Materials**
   - Course schedule, links, slides, and handwritten notes (`admin/`)
3. **Weekly Course Materials**
   - Sequential lecture notes and starter notebooks for each week (`lecture-notes/week*/`)
   - Example: `lecture-notes/week1/01_start.ipynb`, `lecture-notes/week1/01_notes.ipynb`, ...
4. **Assignments**
   - Homeworks and midterms in order of assignment (`homeworks/`, `midterms/`)
   - Example: `homeworks/hw1.ipynb`, ..., `midterms/midterm1.ipynb`, ...
5. **Resources**
   - Rubrics, guides, computational essays, integrators, phase diagrams, and more (`resources/`)
6. **Honors Projects**
   - Advanced and honors-level project topics (`honors-projects/`)
7. **Slides & Images**
   - All lecture slides in multiple formats and supporting images (`slides/`, `images/`)
8. **Themes**
   - Custom CSS and themes for slides and notes (`themes/`)

The order and structure are defined in `_toc.yml` and are reflected in the Jupyter Book build.

---

## Contributing

Contributions, corrections, and suggestions are welcome! Please open an issue or submit a pull request.

---

## License

See the `LICENSE` file for details.

---

*README.md written by [Ollama](https://ollama.com/).*
