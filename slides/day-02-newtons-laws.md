---
marp: true
theme: default
paginate: true
backgroundColor: #ffffff

title: Day 02 - Newton's Laws
description: Slides for PHY 321 Spring 2026, Day 02: Newton's Laws
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, newton's laws, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-02-newtons-laws.html
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
  
  section.title {
    background-color: #ffffff !important;
    color: var(--color-spartan-green) !important;
    border-top: 12px solid var(--color-spartan-green) !important;
    border-bottom: 4px solid var(--color-msu-gold) !important;
    padding: 3rem !important;
  }

  section.title h1, section.title h2 {
    color: var(--color-spartan-green) !important;
    font-size: 1.8rem !important;
    margin-bottom: 0.8rem !important;
    font-weight: 700 !important;
  }

  section.title p {
    color: var(--color-dark-text) !important;
    font-size: 1.0rem !important;
  }

  section.title .equation {
    background-color: var(--color-light-gray) !important;
    color: var(--color-dark-text) !important;
    border-left: 6px solid var(--color-msu-gold) !important;
    padding: 1.5rem !important;
    margin: 1.5rem 0 !important;
  }

  section.title .footnote {
    color: #666666 !important;
    font-size: 1rem !important;
    margin-top: 2rem !important;
  }

  section.title strong {
    color: var(--color-spartan-green) !important;
    font-weight: 700 !important;
  }

  /* Physics equation styling */
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
  margin-left: 0.5rem;  /* Reduced from 2rem */
}

ul ul, ol ol, ul ol, ol ul {
  margin-left: 0.1rem;  /* Even less for nested lists */
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
  
  .physics-concept {
    background-color: #f0f8f7;
    border: 2px solid var(--color-spartan-green);
    padding: 1.25rem;
    border-radius: 6px;
    margin: 1rem 0;
  }

  .activity {
    background-color: #fff8e1;
    border: 2px solid var(--color-msu-gold);
    padding: 1.25rem;
    border-radius: 6px;
    margin: 1rem 0;
  }

  blockquote {
    background-color: #f9f9f9;
    border-left: 4px solid var(--color-accent-green);
    padding: 1rem 1.5rem;
    margin: 1rem 0;
    font-style: italic;
  }

  table {
    margin-left: auto;
    margin-right: auto;
    border-collapse: collapse;
    font-size: 1.0rem;
  }

  table th, table td {
    padding: 0.25rem;
    text-align: left;
    border: 3px solid #ddd;
  }

  table th {
    background-color: var(--color-light-gray);
    color: var(--color-spartan-green);
    font-weight: 600;
  }
  
  footer {
    font-size: 0.8rem;
    color: #999;
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

<div style="border-top: 12px solid #18453B; border-bottom: 4px solid #C1B000; padding: 3rem; background-color: #ffffff;">

<h1 style="color: #18453B; font-size: 2.2rem; font-weight: 700; margin-bottom: 0.8rem;">Day 02 - Newton's Laws</h1>

<div style="background-color: #f5f5f5; border-left: 6px solid #C1B000; padding: 1.5rem; margin: 1.5rem 0;">

$$\mathbf{F}_{net} = m \mathbf{a}$$

</div>

<p style="color: #1a1a1a; font-size: 1.0rem;">Not shown in this picture of Newton are the countless illiterate mechanics and farmers, immigrant laborers, indigenous scholars, and other non elite members of society upon whose backs and accomplishments Newton's Principia was written.</p>

![bg right:40%](./images/newton.jpg)

<p style="color: #666666; font-size: 0.9rem; margin-top: 2rem; border-top: 1px solid #ddd; padding-top: 0.75rem;">PHY 321 Classical Mechanics I - Spring 2026</p>

</div>

---

# Announcements

- **Homework 1** is due next Friday (late after Sunday)
- **Help sessions** will start next week
  - Please complete the [student information survey](https://forms.cloud.microsoft/r/7Ar26hXDgm); [help session survey](https://crab.fit/phy-321-spring-2026-office-hours-poll-464860)
- **Friday's class** will be lead by Prof. Brian O'Shea & Mihir Naik
    - Getting started with VS Code
    - Introduce a few extensions and libraries
    - Perform numerical differentiation of a trajectory

---

# Goals for this week

## Be able to answer the following questions:

- What is Classical Mechanics?
- How can we formulate it?
- What are the essential physics models for single particles?
- What mathematics do we need to get started?

---

# Think About This

<div class="activity">

## Take 2 minutes to write down what comes to mind when asked:

### What is "Classical" Physics?

</div>

---

# Modeling large, slow-moving objects

Newton's Laws are but one of a number of formulations:
- **Lagrangian Mechanics**
- **Hamiltonian Mechanics** 
- **Dynamical Systems Theory**
- ...

<div class="physics-concept">

**Key insight:** Different mathematical formulations can describe the same physical phenomena, each with their own advantages for different types of problems.

</div>

---

<!-- _backgroundColor: #4682B4 -->
<!-- _color: white -->

# An Overview of Different Physics

![drop-shadow width:1000px](https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Modernphysicsfields.svg/640px-Modernphysicsfields.svg.png)

--- 

# Classical Mechanics has a long history

> Wherever folks were figuring out their world, there was classical mechanics

- [Astronomical analyses in Sub-Saharan Africa](https://www.science.org/doi/10.1126/science.200.4343.766) in 300 BCE
- [Scientific expansion in China](https://en.wikipedia.org/wiki/Science_and_technology_of_the_Song_dynasty) during the Song dynasty
- [The Islamic Golden Age](https://en.wikipedia.org/wiki/Islamic_Golden_Age) 
- [Indigenous astronomy](https://en.wikipedia.org/wiki/Indigenous_astronomy)

---

# Historical Example: Chinese Astronomy

![center width:600px](./images/Su_Song_Star_Map_1.jpeg)

*Song Dynasty star map showing sophisticated astronomical observations*

---

# Classical Mechanics is still very relevant

**Tiny Limbs and Long Bodies: Coordinating Lizard Locomotion**  
[Research Lab](https://research.gatech.edu/tiny-limbs-and-long-bodies-coordinating-lizard-locomotion) 

[![Tiny Limbs and Long Bodies: Coordinating Lizard Locomotion](https://markdown-videos-api.jorgenkh.no/youtube/Qme07fA3Fj4.gif?width=640&height=360&duration=800)](https://youtu.be/Qme07fA3Fj4)

Source: <https://youtu.be/Qme07fA3Fj4>

---

# Canonical Example from Introductory Physics

**Classic problem setup:**
- Box on a ramp with a frictional interaction
- At what angle does it slide for a given $\mu_s$?

![bg right:45% width:500px height:auto](../images/vector-graphics/block_on_ramp_sliding_fbd.png)

---

# Canonical Example from Introductory Physics

<div class="physics-concept">

**Key physics:** Balance of forces determines the critical angle where static friction can no longer hold the box in place.

**Analysis approach:**
- Decompose gravitational force into components
- Apply Newton's second law in each direction
- Set acceleration to zero at the critical angle

</div>

---

# Think-Pair-Share

<div class="activity">

We used a tilted coordinate system ($x-y$ plane) to analyze the motion of a block on an inclined plane. **How can we check that we did the gravitational force decomposition correctly?**

Recall:
- $F_{\text{gravity},x} = m g \sin(\theta)$
- $F_{\text{gravity},y} = m g \cos(\theta)$

**Come up with at least two checks.**

</div>

---

# Clicker Question 2-1

The formal definition of a Taylor series expansion around a point $a$ is:

<div class="equation">

$$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \ldots$$

</div>

**This formula makes me feel:**

1. Confident, I got this.
2. A little nervous, but I think I remember.
3. Uncomfortable, I don't remember this.
4. I have no idea what this is.

---

# Think-Pair-Share

<div class="activity">

We derived the following differential equation for the falling ball in one-dimension:

$$\frac{d^2 y}{dt^2} = +g - \frac{b}{m} \frac{dy}{dt} - \frac{c}{m} \left(\frac{dy}{dt}\right)^2$$

Let's assume the turbulent drag term is negligible. **Is there an anti-derivative of the right-hand side of this equation? If so, what is it?**

$$\frac{dv}{dt} = +g - \frac{b}{m}v$$

</div>

--- 

# Example: Ball Falling in 1D in Air

We derived the following differential equation for the motion of a ball falling in air:

<div class="equation">

$$m\ddot{y} = mg - b v - c v^2$$

</div>

We argued for low speeds, we neglect the $v^2$ term:

<div class="equation">

$$m\ddot{y} = mg - b v$$

</div>

We can instead write this differential equation for $v$:

<div class="equation">

$$\dot{v} = g - \frac{b}{m}v$$

</div>

---

# Example: Ball Falling in 1D in Air

**Is this integrable? Yes!**

<div class="equation">

$$\frac{dv}{dt} = g - \frac{b}{m}v$$

$$\frac{dv}{g - \frac{b}{m}v} = dt$$

$$\int \frac{dv}{g - \frac{b}{m}v} = \int dt$$

</div>

<div class="highlight">

We will come back to this next week.

</div>

---

# Vector Properties

Newtonian Mechanics is a **vector theory**. Here are a few mathematical properties of vectors:

- **Addition**: $\mathbf{A} + \mathbf{B} = (A_x + B_x)\hat{x} + (A_y + B_y)\hat{y} + (A_z + B_z)\hat{z}$
- **Scalar Multiplication**: $c\mathbf{A} = \langle cA_x, cA_y, cA_z\rangle$
- **Dot Product**: $\mathbf{A}\cdot\mathbf{B} = A_xB_x + A_yB_y + A_zB_z = AB\cos\theta$
- **Cross Product**: $\mathbf{A}\times\mathbf{B} = \langle A_yB_z - A_zB_y, A_zB_x - A_xB_z, A_xB_y - A_yB_x\rangle$
- **Unit Vectors**: $\hat{A} = \frac{\mathbf{A}}{|\mathbf{A}|} \qquad |\hat{A}| = 1$
