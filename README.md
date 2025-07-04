
# PHY321: Classical Mechanics at Michigan State University

This repository contains the complete set of course materials for PHY321: Classical Mechanics at MSU, including lecture notes, assignments, slides, resources, and environment setup for reproducible computational work.

---

## Course Overview

PHY321 covers the foundations of classical mechanics, including:
- Newton’s laws and equations of motion
- Inertial and non-inertial frames
- Forces, work, energy, and conservation laws
- Motion in various fields and effective potentials
- Oscillations and harmonic motion
- Central forces, two-body problems, and scattering
- Variational calculus and the Lagrangian formalism

The course emphasizes both analytical and computational approaches, with Jupyter notebooks and Python code throughout.

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

## Environment Setup

### Using Docker (Recommended)

A `Dockerfile` is provided for a fully reproducible environment. This includes all system and Python dependencies needed for the course.

**To build and run the Docker environment:**
```sh
docker build -t phy321 .
docker run -it --rm -p 8888:8888 -v $(pwd):/mnt/jbook phy321
```
This will launch a Jupyter environment with all required packages (see `Dockerfile` for details).

### Manual Setup

Alternatively, you can install dependencies directly:
```sh
pip install -r requirements.txt
```

---

## Building the Jupyter Book & Slides

- To build all slides:
  ```sh
  ./build-all-slides.sh
  ```
- To build a specific slide:
  ```sh
  ./build-slide.sh slides/day-01-introduction.md
  ```
- To build the full Jupyter Book:
  ```sh
  jupyter-book build .
  ```

---

## Contributing

Contributions, corrections, and suggestions are welcome! Please open an issue or submit a pull request.

---

## License

See the `LICENSE` file for details.

---

*README.md written by [Ollama](https://ollama.com/).*
