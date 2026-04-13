---
marp: true
theme: graph_paper
paginate: true

title: Day 36 - Lagrangian Examples
description: Slides for PHY 321 Fall 2025, Day 36: Lagrangian Examples
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

# Announcements

* Last "Class" Week
* Homework 8 due Friday, Nov 21st (late after Nov 26th)
* Next Week: Project Work and Discussion
* Last Week: Presentations
* Final Project Due Dec 8th (no later than 11:59 pm)
* **No Final Exam**

---

# Complete Google Form

## By November 21st

Reporting your group members for the final project and a short summary of your project idea for sharing with the class.

<https://forms.gle/iPKR9EDAaHW3GirN7>

![bg left width:350px](../images/notes/week13/group_form_qr.png)

---

---

## Announcements

* Homework 8 is "Late" 24 Apr)
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

We used the scleronomic constraint $y_1 = R\phi$ to do this.

---

# Clicker Question 36-1

We derived the Lagrangian for the Atwood's machine with a rotating pulley to be:

$$\mathcal{L} = \dfrac{1}{2}(M+m)R^2\dot{\phi}^2 + \dfrac{1}{4}M_pR^2\dot{\phi}^2  - (M-m)gR\phi$$

What is generalized force, $F_{\phi} = \partial \mathcal{L} / \partial \dot{\phi}$?

1. $+(M-m)gR$
2. $-(M-m)gR$
3. $+(M+m)R^2\dot{\phi}$
4. $-(M+m)R^2\dot{\phi}$
5. Something else

---

# Clicker Question 36-2

We derived the Lagrangian for the Atwood's machine with a rotating pulley to be:

$$\mathcal{L} = \dfrac{1}{2}(M+m)R^2\dot{\phi}^2 + \dfrac{1}{4}M_pR^2\dot{\phi}^2  - (M-m)gR\phi$$

What is the generalized momentum, $p_{\phi} = \partial \mathcal{L} / \partial \dot{\phi}$?

1. $+(M-m)gR$
2. $-(M-m)gR$
3. $+(M+m)R^2\dot{\phi}$
4. $-(M+m)R^2\dot{\phi}$
5. Something else

---

# Clicker Question 36-3

For the constraint for the bead in a parabolic bowl ($z=c\rho^2$), what are the units of $c$?

1. $[L^2]$
2. $[L^{-2}]$
3. $[L]$
4. $[L^{-1}]$
5. Something else

---

# Clicker Question 36-4

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

# Clicker Question 36-5

The Lagrangian for the bead in a parabola does not depend on which of the following?

1. $\rho$
2. $\phi$
3. $z$
4. More than one of these
5. None of these


