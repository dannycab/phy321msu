---
marp: true
theme: graph_paper
paginate: true

title: Day 36 - Lagrangian Examples
description: Slides for PHY 321 Spring 2026, Day 36: Lagrangian Examples III
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, Lagrangian, examples
url: https://dannycaballero.info/phy321msu/slides/day-36-lagrangian-examples.html

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

# Day 36 - Lagrangian Examples III

![bg right width:600px](../images/notes/week13/andy-lagrange.jpeg)

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

## Reminders

We found the Lagrangian for the Atwood's machine with a rotating pulley to be:

$$\mathcal{L} = \dfrac{1}{2}(M+m)R^2\dot{\phi}^2 + \dfrac{1}{4}M_pR^2\dot{\phi}^2  - (M-m)gR\phi$$

where $M$ is the mass of the left block, $m$ is the mass of the right block, $M_p$ is the mass of the pulley, $R$ is the radius of the pulley, and $\phi$ is the angle of rotation of the pulley.

We used the **scleronomic** constraint $\dot{y}_1 = R\dot{\phi}$ to do this.

> **Holonomic** constraints are those that can be expressed as a function of the coordinates and **time**, $f(q_1, q_2, ..., q_n, t) = 0$. 

---

## Clicker Question 36-1a

We derived the Lagrangian for the Atwood's machine with a rotating pulley to be:

$$\mathcal{L} = \dfrac{1}{2}(M+m)R^2\dot{\phi}^2 + \dfrac{1}{4}M_pR^2\dot{\phi}^2  - (M-m)gR\phi$$

What is generalized force, $F_{\phi} = \partial \mathcal{L} / \partial \dot{\phi}$?

1. $+(M-m)gR$
2. $-(M-m)gR$
3. $+(M+m)R^2\dot{\phi}$
4. $-(M+m)R^2\dot{\phi}$
5. Something else

---

## Clicker Question 36-1b

For the Atwood's machine with a rotating pulley, what are the units of the generalized force, $F_{\phi}$?

1. Newtons
2. Joules
3. Newton-meters
4. Joule-seconds
5. Something else

---

## Clicker Question 36-2a

We derived the Lagrangian for the Atwood's machine with a rotating pulley to be:

$$\mathcal{L} = \dfrac{1}{2}(M+m)R^2\dot{\phi}^2 + \dfrac{1}{4}M_pR^2\dot{\phi}^2  - (M-m)gR\phi$$

What is the generalized momentum, $p_{\phi} = \partial \mathcal{L} / \partial \dot{\phi}$?

1. $+(M-m)gR$
2. $-(M-m)gR$
3. $+(M+m)R^2\dot{\phi}$
4. $-(M+m)R^2\dot{\phi}$
5. Something else

---

## Clicker Question 36-2b

For the Atwood's machine with a rotating pulley, what are the units of the generalized momentum, $p_{\phi}$?

1. Newtons
2. Joules
3. Newton-meters
4. Joule-seconds
5. Something else

---


## Clicker Question 36-3a

Two blocks ($m$) connected by a spring ($k$, $L$) on a horizontal frictionless surface. The first block is described by a coordinate $x_1$ and the second block is described by a coordinate $x_2$ from a mutual origin. What is the Lagrangian for this system?

1. $\mathcal{L} = T - U = \frac{1}{2}m\dot{x}_1^2 + \frac{1}{2}m\dot{x}_2^2 - \frac{1}{2}k(x_1 - x_2 - L)^2$
2. $\mathcal{L} = T - U = \frac{1}{2}m\dot{x}_1^2 + \frac{1}{2}m\dot{x}_2^2 - \frac{1}{2}k(x_1 - x_2)^2$
3. $\mathcal{L} = T - U = \frac{1}{2}m\dot{x}_1^2 + \frac{1}{2}m\dot{x}_2^2 - \frac{1}{2}k(x_1 - x_2 + L)^2$
4. $\mathcal{L} = T - U = \frac{1}{2}m\dot{x}_1^2 + \frac{1}{2}m\dot{x}_2^2 - \frac{1}{2}k(x_1 + x_2 - L)^2$
5. Something else

---

## Clicker Question 36-3b

For the two block and spring system, what is the equation of motion for the first block?

1. $m\ddot{x}_1 = -k(x_1 - x_2)$
2. $m\ddot{x}_1 = -k(x_1 - x_2 + L)$
3. $m\ddot{x}_1 = -k(x_1 - x_2 - L)$
4. $m\ddot{x}_1 = -k(x_1 + x_2 - L)$
5. Something else

---

## Clicker Question 36-3c

For the two block and spring system, what is the equation of motion for the second block?

1. $m\ddot{x}_2 = +k(x_1 - x_2)$
2. $m\ddot{x}_2 = -k(x_1 - x_2 - L)$
3. $m\ddot{x}_2 = +k(x_1 - x_2 - L)$
4. $m\ddot{x}_2 = +k(x_1 + x_2 - L)$
5. Something else

---

## Clicker Question 36-4a

Sometimes, we can choose better or more useful generalized coordinates. For the two block and spring system, we can choose the center of mass coordinate, $x_{cm} = (x_1 + x_2)/2$, and the relative coordinate, $x = x_1 - x_2$. What is the Lagrangian for this system in these new coordinates?


1. $\mathcal{L} = T - U = m\dot{x}_{cm}^2 + \frac{1}{4}m\dot{x}^2 - \frac{1}{2}k(x - L)^2$
2. $\mathcal{L} = T - U = m\dot{x}_{cm}^2 + \frac{1}{4}m\dot{x}^2 - \frac{1}{2}k(x + L)^2$
3. $\mathcal{L} = T - U = m\dot{x}_{cm}^2 + \frac{1}{4}m\dot{x}^2 - \frac{1}{2}k(x)^2$
4. $\mathcal{L} = T - U = m\dot{x}_{cm}^2 + \frac{1}{4}m\dot{x}^2 - \frac{1}{2}k(x + L)^2$
5. Something else

---

## Clicker Question 36-4b

For this new Lagrangian, what is the equation of motion for the relative coordinate, $x$?

1. $\frac{1}{2}m\ddot{x} = -k(x - L)$
2. $\frac{1}{2}m\ddot{x} = -k(x + L)$
3. $\frac{1}{2}m\ddot{x} = -kx$
4. $\frac{1}{2}m\ddot{x} = -k(x + L)$
5. Something else

> What is the equation of motion for the center of mass coordinate, $x_{cm}$?

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


