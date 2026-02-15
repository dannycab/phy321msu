---
marp: true
theme: graph_paper
paginate: true

title: Day 14 - Potential Energy and Stability
description: Slides for PHY 321 Spring 2025, Day 14: Potential Energy and Stability
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, energy, stability
url: https://dannycaballero.info/phy321msu/slides/day-14-potential-energy-and-stability.html
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

# Day 14 - Potential Energy and Stability

![bg right width:600px](../images/notes/week6/mexican-hat-potential.png)

Mexican Hat/Sombrero Potential $\longrightarrow$

---

## Mexican Hat Potential

$V(\phi) = -5|\phi|^2 + |\phi|^4$

![bg right width:80%](../images/notes/week6/mexican-hat-potential.png)

- [Spontaneous Symmetry Breaking](https://en.m.wikipedia.org/wiki/Spontaneous_symmetry_breaking#Sombrero_potential) ([Jeffery Goldstone, 1961](https://en.m.wikipedia.org/wiki/Jeffrey_Goldstone))
- Unstable vacuum state at $\phi = 0$
    - Peak of the hat
- Infinite number of stable minima 
    - $\phi = \sqrt{5/2}e^{i\phi}$


---

# Welcome Prof. Rachel Henderson!

## Announcements
* Midterm 1 is available today (Due 25 Feb; late 27 Feb)
* DC will say more about this on Wednesday, but:
  * You may work in larger groups, but solutions are submitted like homework (max 3 group members) **on Gradescope**
  * Exercise 0 is for project planning; and can be submitted individually or as a _different_ group **on D2l**

---

## This Week's Goals

- Understand the concept of potential energy
- Determine the equilibrium points of a system using potential energy
- Analyze the stability of equilibrium points
- Define and begin to apply conservation of linear and angular momentum

---

## Reminder: The Gradient Operator $\nabla$

$\nabla$ is a vector operator. In Cartesian coordinates:
$$\nabla = \hat{x}\dfrac{\partial}{\partial x}+\hat{y}\dfrac{\partial}{\partial y}+\hat{z}\dfrac{\partial}{\partial z} = \left\langle \dfrac{\partial}{\partial x}, \dfrac{\partial}{\partial y}, \dfrac{\partial}{\partial z} \right\rangle$$

Acting on a scalar function $f(x,y,z)$ produces a vector:

$$\nabla f(x,y,z) = \hat{x}\dfrac{\partial f}{\partial x}+\hat{y}\dfrac{\partial f}{\partial y}+\hat{z}\dfrac{\partial f}{\partial z} = \left\langle \dfrac{\partial f}{\partial x}, \dfrac{\partial f}{\partial y}, \dfrac{\partial f}{\partial z} \right\rangle$$

---

## Reminder: The Gradient Operator $\nabla$

$\nabla$ can act on vector field (function), $\mathbf{F}(x,y,z)$ with both dot and cross products.

### Divergence (Scalar Product) - How does the vector field change in the direction of the vector?

$$\nabla \cdot \mathbf{F}(x,y,z) = \left\langle \dfrac{\partial}{\partial x}, \dfrac{\partial}{\partial y}, \dfrac{\partial}{\partial z} \right\rangle \cdot \langle F_x, F_y, F_z \rangle$$
$$\nabla \cdot \mathbf{F}(x,y,z) = \dfrac{\partial F_x}{\partial x} + \dfrac{\partial F_y}{\partial y} + \dfrac{\partial F_z}{\partial z}$$

---

## Clicker Question 14-1a

Which of the following fields have no divergence?

<div style="display: flex; align-items: center; gap: 20px; max-width: 800px; margin: 0 auto; white-space: nowrap; height: 400px;">
  A. <img src="../images/notes/week5/cq_left_field.png" alt="A" width="400">
  B. <img src="../images/notes/week5/cq_right_field.png" alt="B" width="400">
</div>

1. A
2. B
3. Both A and B
4. Neither A nor B

---

## Reminder: The Gradient Operator $\nabla$

### Curl (Vector Product) - How does the vector field change in the direction perpendicular to the vector?

$$
\nabla \times \mathbf{F}(x,y,z) =
\begin{vmatrix}
\hat{x} & \hat{y} & \hat{z} \\
\dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\
F_x & F_y & F_z
\end{vmatrix} 
$$

$$\nabla \times \mathbf{F}(x,y,z) = \left\langle \dfrac{\partial F_z}{\partial y} - \dfrac{\partial F_y}{\partial z},\ \dfrac{\partial F_x}{\partial z} - \dfrac{\partial F_z}{\partial x},\ \dfrac{\partial F_y}{\partial x} - \dfrac{\partial F_x}{\partial y} \right\rangle$$



---


## Clicker Question 14-1b

Which of the following fields have no curl?

<div style="display: flex; align-items: center; gap: 20px; max-width: 800px; margin: 0 auto; white-space: nowrap; height: 400px;">
  A. <img src="../images/notes/week5/cq_left_field.png" alt="A" width="400">
  B. <img src="../images/notes/week5/cq_right_field.png" alt="B" width="400">
</div>

1. A
2. B
3. Both A and B
4. Neither A nor B

---

## Clicker Question 14-1c

Consider a vector field with zero curl: $\nabla \times \vec{F} = 0$. Which of the following statements is true?

1. The field is conservative
2. $\int \nabla \times \vec{F} \cdot d\vec{A} = 0$
3. $\oint \vec{F} \cdot d\vec{r} \neq 0$
4. $\vec{F}$ is the gradient of some scalar function, e.g., $\vec{F} = - \nabla U$
5. Some combination of the above

---

## Reminders: Conservative Forces

- Conservative forces are those with zero curl

$$\nabla \times \vec{F} = 0$$

- The work done by a conservative force is path-independent; on a closed path, the work done is zero

$$\oint \vec{F} \cdot d\vec{r} = 0$$

- The force can be written as the gradient of a scalar potential energy function

$$\vec{F} = - \nabla U$$

---

## Clicker Question 14-2

Here's the graph of the potential energy function $U(x)$ for a pendulum.

![bg right:40% w:450px h:auto ](../images/notes/week6/pendulum-potential-energy.png)

What can you say about the equilibrium points? There is/are:

1. One stable point
2. Two stable points
3. One stable and one unstable point
4. Two unstable and one stable point

---

## Clicker Question 14-3

Here's a potential energy function $U(x)$ for a pendulum:

$$U(\phi) = -mgL\cos(\phi) + U_0$$

1. Find the equilibrium points ($\phi^*$) of the pendulum by setting:

$$\frac{dU(\phi^*)}{d\phi} = 0.$$

2. Characterize the stability of the equilibrium points ($\phi^*$) by examining the second derivative:

$$\frac{d^2U(\phi^*)}{d\phi^2}>0? \qquad \frac{d^2U(\phi^*)}{d\phi^2}<0?$$

**Click when done.**

---

## Clicker Question 14-4

A double-well potential energy function $U(x)$ is given by

$$U(x) = -\frac{1}{2}kx^2 + \frac{1}{4}kx^4.$$

*We assume we have scaled the potential energy so that all the units are consistent.*

How many equilibrium points does this system have?

1. 1
2. 2
3. 3
4. 4

---

## Clicker Question 14-5

A double-well potential energy function $U(x)$ is given by

$$U(x) = -\frac{1}{2}kx^2 + \frac{1}{4}kx^4.$$


1. Find the equilibrium points ($x^*$) of the pendulum by setting:

$$\frac{dU(x^*)}{dx} = 0.$$

2. Characterize the stability of the equilibrium points ($x^*$):

$$\frac{d^2U(x^*)}{dx^2}>0? \qquad \frac{d^2U(x^*)}{dx^2}<0?$$

**Click when done.**

---

## Clicker Question 14-6

Here's a graph of the potential energy function $U(x)$ for a double-well potential.

![bg right:52% width:600px height:auto](../images/notes/week6/cq14-5.png)

Describe the motion of a particle with the total energy, $E=$

1. $0.4\,\mathrm{J}$, $<$ barrier height
2. $1.2\,\mathrm{J}$, $>$ barrier height
3. $1.0\,\mathrm{J}$, $=$ barrier height

**Click when done.**