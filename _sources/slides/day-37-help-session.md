---
marp: true
theme: graph_paper
paginate: true

title: Day 37 - Help Session
description: Slides for PHY 321 Spring 2026, Day 37: Help Session
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, motion, oscillations, resonance
url: https://dannycaballero.info/phy321msu/slides/day-37-help-session.html

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

# Day 37 - Help Session

## [Routhian Mechanics](https://en.wikipedia.org/wiki/Routhian_mechanics) 

![Routh](https://upload.wikimedia.org/wikipedia/commons/f/fc/Edward_J_Routh.jpg)

![bg right:40% width:400px](../images/notes/week13/yoda.jpeg)

---

## Announcements

* Homework 8 is "Late" 24 Apr
    * Last Exercise 0: Reflect Learning Outcomes
* Final Project is posted
    * Video Presentations due 27 Apr
    * Computational Essay due 1 May
    * Rubric for both are posted
* No class (20 Apr - 24 Apr) - DC out of country
    * Make appointment for project help (clicker extra credit)

---

## Announcements

### Rest of Semester Schedule
* CW16 - Examples of Lagrangian Dynamics (HW8)
* CW17 - Project Prep (DC out of country)
* CW18 - Final Project Due
    * Video Presentations due 27 Apr
    * Computational Essay due 1 May

### NO IN-CLASS FINAL EXAM

---

## Clicker Question 36-5a

Consider a bead sliding on a parabolic bowl described by the constraint $z = c\rho^2$ where $\rho$ is the distance from the vertical axis. The Lagrangian for this system in Cartesian coordinates is:

$$\mathcal{L} = \frac{1}{2}m(\dot{x}^2 + \dot{y}^2 + \dot{z}^2) - mgz$$

Don't use the constraint, what are the equations of motion for this system? Do they seem correct?

> Click anything to indicate you are ready to see the answer.

---

## Clicker Question 36-5b

For the constraint for the bead in a parabolic bowl ($z=c\rho^2$), what are the units of $c$?

1. $[L^2]$
2. $[L^{-2}]$
3. $[L]$
4. $[L^{-1}]$
5. Something else

---

## Clicker Question 36-5c

Now use the constraint to write the Lagrangian for the bead in a parabolic bowl in cylindrical coordinates, $(\rho, \phi, z)$. What is the Lagrangian for this system?

1. $\mathcal{L} = \frac{1}{2}m(\dot{\rho}^2 + \rho^2\dot{\phi}^2 + 4c^2\rho^2) - mgc\rho^2$
2. $\mathcal{L} = \frac{1}{2}m(\dot{\rho}^2 + \rho^2\dot{\phi}^2 + 4c^2{\rho}^2) - mgc\rho^2$
3. $\mathcal{L} = \frac{1}{2}m(\dot{\rho}^2 + \rho^2\dot{\phi}^2 + 4c^2\rho^2\dot{\rho}^4) - mgc\rho^2$
4. $\mathcal{L} = \frac{1}{2}m(\dot{\rho}^2 + \rho^2\dot{\phi}^2 + 4c^2\rho^2\dot{\rho}^2) - mgc\rho^2$
5. Something else

> Hint: $v^2(\rho,\phi,z) = \dot{\rho}^2 + \rho^2\dot{\phi}^2 + \dot{z}^2$

---

## Clicker Question 36-5d

For the bead in a parabolic bowl, there is a generic Lagrangian:

$$\mathcal{L}(\rho, \dot{\rho}, \phi, \dot{\phi}, z, \dot{z}, t)$$

How many coordinates are there, truly? **here, each variable is a coordinate**

A. 2
B. 3
C. 4
D. 5
E. None of these

**Which coordinates are independent?**

---

## Clicker Question 36-5e

The Lagrangian for the bead in a parabola does not depend on which of the following?

1. $\rho$
2. $\phi$
3. $z$
4. More than one of these
5. None of these

> When a coordinate does not appear in the Lagrangian, it is called a **cyclic** or **ignorable** coordinate. This means that the generalized momentum associated with that coordinate is conserved.