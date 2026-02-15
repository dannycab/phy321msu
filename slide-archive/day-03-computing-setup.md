---
marp: true
theme: default
paginate: true
backgroundColor: #ffffff

title: Day 03 - Computing Setup
description: Slides for PHY 321 Spring 2026, Day 03: Getting Started with VS Code
author: Prof. Brian O'Shea & Mihir Naik
keywords: vs code, python, jupyter, numerical differentiation
url: https://dannycaballero.info/phy321msu/slides/day-03-computing-setup.html
---

<style>
  :root {
    --color-spartan-green: #18453B;
    --color-msu-gold: #C1B000;
    --color-light-gray: #f5f5f5;
    --color-dark-text: #1a1a1a;
    --color-accent-green: #2d5f4f;
  }
  
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #ffffff;
    color: var(--color-dark-text);
  }
  
  h1, h2, h3 {
    color: var(--color-spartan-green);
    font-weight: 500;
  }
  
  h1 {
    font-size: 2.2rem;
    margin-bottom: 0rem;
  }
  
  h2 {
    font-size: 1.55rem;
    margin-bottom: 1.0rem;
    border-bottom: 4px solid var(--color-spartan-green);
    padding-bottom: 0.5rem;
  }
  
  h3 {
    font-size: 1.15rem;
    margin-top: 1rem;
    margin-bottom: 0.75rem;
  }
  
  section {
    padding: 2rem;
    background-color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }

  .equation {
    background-color: var(--color-light-gray);
    padding: 1.5rem;
    border-left: 4px solid var(--color-msu-gold);
    margin: 1.5rem 0;
    font-size: 1.3rem;
    text-align: center;
    color: var(--color-dark-text);
  }

  p {
    font-size: 1.15rem;
    line-height: 1.4;
    margin-bottom: 0.5rem;
  }
  
  ul, ol {
    font-size: 1.15rem;
    line-height: 1.4;
    margin-left: 0.5rem;
  }

  ul ul, ol ol, ul ol, ol ul {
    margin-left: 0.1rem;
  }
  
  li {
    margin-bottom: 0rem;
    line-height: 1.4;
  }
  
  strong {
    color: var(--color-spartan-green);
    font-weight: 600;
  }
  
  em {
    color: var(--color-accent-green);
  }

  .highlight {
    background-color: var(--color-light-gray);
    padding: 1.5rem;
    border-left: 4px solid var(--color-spartan-green);
    margin: 1.5rem 0;
  }

  .activity {
    background-color: #fff8e1;
    border: 2px solid var(--color-msu-gold);
    padding: 1.25rem;
    border-radius: 6px;
    margin: 1rem 0;
  }

  code {
    background-color: var(--color-light-gray);
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-size: 1.0rem;
  }

  .footnote {
    font-size: 0.8rem;
    color: #999;
    margin-top: 1.5rem;
    border-top: 1px solid #ddd;
    padding-top: 0.75rem;
  }
</style>

<!--
_class: title
_backgroundColor: #ffffff
_color: #18453B
-->

<div style="border-top: 12px solid #18453B; border-bottom: 4px solid #C1B000; padding: 2rem; background-color: #ffffff;">

<h1 style="color: #18453B; font-size: 2.2rem; font-weight: 700; margin-bottom: 1rem;">Day 03 - Getting Started with VS Code</h1>

<div style="background-color: #f5f5f5; border-left: 6px solid #C1B000; padding: 1.5rem; margin: 1.5rem 0;">

$$v_i \approx \frac{x_{i+1} - x_i}{\Delta t}$$

</div>

<p style="color: #1a1a1a; font-size: 1.0rem; margin-bottom: 1rem;">Today we'll set up VS Code for scientific computing and practice numerical differentiation.</p>

<div style="font-size: 0.8rem; color: #999; margin-top: 1.5rem; border-top: 1px solid #ddd; padding-top: 0.75rem;">PHY 321 Classical Mechanics I - Spring 2026</div>

</div>

![bg right:40% width:500px height:auto](https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Finite_difference_method.svg/500px-Finite_difference_method.svg.png)



<div class="footnote">PHY 321 Classical Mechanics I - Spring 2026</div>

---

# Today's Goals

After this session, you should be able to:

- **Set up VS Code** for Python scientific computing
- **Use Jupyter notebooks** in VS Code
- **Perform numerical differentiation** using finite difference methods
- **Compare** numerical results with analytical solutions

---

# Step 1: Download VS Code

Go to: **https://code.visualstudio.com/download**

Choose your operating system:
- **macOS**: Universal download (Intel + Apple Silicon)
- **Windows**: User Installer
- **Linux**: .deb, .rpm, or .tar.gz

The download is ~200 MB and takes just a minute or two.

---

# Step 2: Install VS Code

**On macOS:**
1. Open the downloaded `.zip` file
2. Drag `Visual Studio Code.app` to **Applications**
3. Launch from Applications

**On Windows:**
1. Double-click the `.exe` installer
2. Follow the wizard (default settings are fine)
3. VS Code launches automatically

---

# Step 3: Install Required Extensions

Click the **Extensions** icon (4 squares) on the left sidebar
- Or press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac)

Install these two extensions:
1. **Jupyter** by Microsoft
2. **Python** by Microsoft

Click **Reload** when prompted.

---

# Step 4: Verify Python

Open VS Code's Terminal: **View → Terminal** (or `` Ctrl+` ``)

Type:
```
python --version
```
or
```
python3 --version
```

You should see something like `Python 3.10.0` or newer.

If not, install Python from: **https://www.python.org/downloads/**

---

# Download Today's Activity

Open the notebook for today's activity:

**https://dannycaballero.info/phy321msu/resources/vscode-setup-numerics-activity.html**

Or find it in the course website under **Resources**.

Download the `.ipynb` file and open it in VS Code.

---

# Libraries We'll Use

```python
import numpy as np          # Numerical computations
import matplotlib.pyplot as plt  # Plotting
import pandas as pd         # Data manipulation
```

Run the first code cell to load these libraries.

If you get an error, you may need to install them:
```
pip install numpy matplotlib pandas
```

---

# The Physics: Numerical Derivatives

In experiments, we measure **positions** at different times.

To get velocities or accelerations, we **numerically differentiate** our data.

<div class="equation">

$$v_i \approx \frac{x_{i+1} - x_i}{\Delta t}$$

</div>

This is the **forward difference** method.

---

# Finite Difference Methods

<div class="activity">

**Three common methods:**

- **Forward**: $f'(x_i) \approx \dfrac{f(x_{i+1}) - f(x_i)}{\Delta x}$

- **Backward**: $f'(x_i) \approx \dfrac{f(x_i) - f(x_{i-1})}{\Delta x}$

- **Central**: $f'(x_i) \approx \dfrac{f(x_{i+1}) - f(x_{i-1})}{2\Delta x}$

</div>

Central difference is more accurate but uses both neighboring points.

---

# The Synthetic Data

We've generated position data for a ball tossed with air resistance:

$$\mathbf{F}_{\text{net}} = -m\mathbf{g} - C_D |\mathbf{v}|\mathbf{v}$$

Run the data generation cells in the notebook to create:
- `t` - time array (seconds)
- `x` - x-position array (meters)
- `y` - y-position array (meters)

---

# Your Task

<div class="activity">

**Using only finite difference methods:**

1. Compute and plot the **numerically-derived velocities** ($v_x$, $v_y$)
2. Compute and plot the **numerically-derived accelerations** ($a_x$, $a_y$)
3. Compare your numerical derivatives with the "true" values
4. What do you notice about the accuracy?

</div>

Work through the notebook with your neighbors!

---

# Hints

To compute velocity from position:
```python
dt = t[1] - t[0]  # time step
vx = (x[1:] - x[:-1]) / dt  # forward difference
```

Note: Your derivative arrays will be **one element shorter** than the original!

To plot against the right time values:
```python
plt.plot(t[:-1], vx)  # use t[:-1] not t
```

---

# Exporting Notebooks to PDF

For homework submissions on Gradescope:

**Option A: VS Code Extension**
- Install "Jupyter PDF Export" extension
- Right-click notebook → Export as PDF

**Option B: Command Line**
```
jupyter nbconvert --to pdf your_notebook.ipynb
```

**Option C: Print to PDF**
- Use `Ctrl+P` / `Cmd+P` → Print

---

# Reminders

- **Homework 1** is due next Friday (late after Sunday)
- **Help sessions** start next week
  - Fill out the [help session poll](https://crab.fit/phy-321-spring-2026-office-hours-poll-464860)
- Complete the [student information survey](https://forms.cloud.microsoft/r/7Ar26hXDgm)

---

# Get Started!

1. Download the notebook from the course website
2. Open it in VS Code
3. Work through the cells
4. Complete the analysis task with your neighbors

**Ask questions as you go!** 