---
marp: true
theme: graph_paper
paginate: true

title: Day 25 - Help Session
description: Slides for PHY 321 Spring 2026, Day 25: Help Session
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, motion, oscillations, resonance
url: https://dannycaballero.info/phy321msu/slides/day-25-help-session.html
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

# Day 25 - Help Session

![width:800px](../images/notes/week9/tuning-fork.png)

---

## HW6 Exercise 1: Morse Potential as an SHO

If the potential has a local minimum, we can often find SHO approximation for that potential near the local minimum. 

The [Morse potential](https://en.wikipedia.org/wiki/Morse_potential) is a convenient model for the potential energy of a diatomic molecule. The potential is a radial one and thus one-dimensional. It is given by,

$$U(r) = A\left[ \left(e^{(R-r)/S}-1\right)^2-1\right]$$

where the distance between the centers of the two atoms is $r$, and the constants $A$, $R$, and $S$ are all positive. Here $S<<R$.

* 1a. Sketch (or plot) the potential as a function of $r$.

---

## HW6 Exercise 1: Morse Potential as an SHO


$$U(r) = A\left[ \left(e^{(R-r)/S}-1\right)^2-1\right]$$


* 1b. Find the equilibrium position of the potential, i.e. the position where the potential is at a minimum. We will call this $r_e$.
* 1c. Rewrite the potential in terms of the displacement from equilibrium, $r = r_e + x$. Expand the potential to second order in $x$.
* 1d. Find the effective spring constant, $k$, for the potential near the minimum. What is the frequency of small oscillations about the minimum?

---

## HW6 Exercise 3: Toy Potential

Consider a toy potential of the form,

$$U(r) = U_0\left(\dfrac{r}{R}+\lambda^2\frac{R}{r}\right)$$

where $U_0$, $R$, and $\lambda$ are all positive constants and the domain of the potential is $0<r<\infty$. 

* 3a. Sketch (or plot) the potential as a function of $r$.

---

# HW6 Exercise 3: Toy Potential

$$U(r) = U_0\left(\dfrac{r}{R}+\lambda^2\frac{R}{r}\right)$$

* 3b. Find the equilibrium position of the potential, i.e. the position where the potential is at a minimum. We will call this $r_e$.
* 3c. Rewrite the potential in terms of the displacement from equilibrium, $r = r_e + x$. Expand the potential to second order in $x$. What is the effective spring constant, $k$, for the potential near the minimum? What is the frequency of small oscillations about the minimum?