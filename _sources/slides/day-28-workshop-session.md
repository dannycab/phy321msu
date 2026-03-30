---
marp: true
theme: graph_paper
paginate: true

title: Day 28 - Workshop Session
description: Slides for PHY 321 Spring 2026, Day 28: Workshop Session
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, motion, oscillations, resonance
url: https://dannycaballero.info/phy321msu/slides/day-28-workshop-session.html
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

# Day 28 - Workshop Session

![bg right width:600px](../images/notes/week10/trojan_horse_maths.jpeg)

---

## Exercise 2 Where does the energy go?

The damped harmonic oscillator is described by the equation of motion is:

$$m\ddot{x} + b\dot{x} + kx = 0$$

where $m$ is the mass, $b$ is the damping coefficient, and $k$ is the spring constant.

The damping term ($F_{damp} = - b\dot{x}$) models the dissipative forces acting on the oscillator. The total energy for the oscillator is given by the sum of the kinetic and potential energies,

$$E = \frac{1}{2}m\dot{x}^2 + \frac{1}{2}kx^2.$$

* 2a What is the energy per unit time dissipated by the damping force?

---

## Exercise 2 Where does the energy go?

$$m\ddot{x} + b\dot{x} + kx = 0$$


$$E = \frac{1}{2}m\dot{x}^2 + \frac{1}{2}kx^2$$

* 2b Take the time derivative of the total energy and show that it is equal (in magnitude) to the energy dissipated by the damping force.
* 2c What is the sign relationship between the energy dissipated by the damping force and the time derivative of the total energy?

---

## Exercise 3, Unpacking the critically damped solution

The solution for critical damping ($\beta = \omega_0$) is given by,

$$x(t) = x_1(t) + x_2(t) = Ae^{-\beta t} + Bte^{-\beta t},$$

where $A$ and $B$ are constants. 

Notice the second solution $x_2(t) = Bte^{-\omega_0t}$ has an additional linear term $t$. We glossed over this solution in class, but it is important to understand why this term is present because it tells us about solving differential equations with pathologically difficult-to-see solutions.

----

## Exercise 3, Unpacking the critically damped solution

Start with the under damped solutions, 

$$y_1(t) = e^{-\beta t}\cos(\omega_1 t) \quad \text{and} \quad y_2(t) = e^{-\beta t}\sin(\omega_1 t),$$

where we have used the notation $\omega_1 = \sqrt{\omega_0^2 - \beta^2}$.

* 3a (3pt). Show that you can recover the first solution $x_1(t)$ by taking the limit of $\beta \rightarrow \omega_0$ of $y_1(t)$.
* 3b (3pt). Show that you cannot recover the second solution $x_2(t)$ by taking the limit of $\beta \rightarrow \omega_0$ of $y_2(t)$ directly. What do you get?
* 3c (4pt). If $\beta \neq \omega_0$, you can divide $y_2(t)$ by $\omega_1$. Now show that in the limit $\beta \rightarrow \omega_0$ of $y_2(t)/\omega_1$, we recover the form of $x_2(t)$.

