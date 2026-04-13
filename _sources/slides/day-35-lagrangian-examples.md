---
marp: true
theme: graph_paper
paginate: true

title: Day 35 - Lagrangian Examples
description: Slides for PHY 321 Spring 2025, Day 35: Lagrangian Examples
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, Lagrangian, examples
url: https://dannycaballero.info/phy321msu/slides/day-35-lagrangian-examples.html

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

# Day 35 - Lagrangian Examples II

![bg right width:500px](../images/notes/week13/lagrange-pooh.jpeg)

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


## Clicker Question 35-1a

For a hypothetical system, we have the Lagrangian that depends on two generalized coordinates, $\mathcal{L}(\rho,\phi, \dot{\rho},\dot{\phi})$. 

> Here $\rho$ has units of length and $\phi$ has units of angle.

Which of the following derivatives give the **generalized force** associated with $\rho$?

$1. \dfrac{\partial \mathcal{L}}{\partial \rho} \qquad 2. \dfrac{\partial \mathcal{L}}{\partial \dot{\rho}}$
$3. \dfrac{d}{dt} \left( \dfrac{\partial \mathcal{L}}{\partial \rho} \right) \qquad 4. \dfrac{d}{dt} \left( \dfrac{\partial \mathcal{L}}{\partial \dot{\rho}} \right)$
5. None of these

---

## Clicker Question 35-1b

For a hypothetical system, we have the Lagrangian that depends on two generalized coordinates, $\mathcal{L}(\rho,\phi, \dot{\rho},\dot{\phi})$. 

> Here $\rho$ has units of length and $\phi$ has units of angle.

What are the units of the **generalized force** associated with $\rho$?

1. Newtons (N)
2. Joules (J)
3. Newton-meters (N m)
4. Meters (m)
5. None of these

---

## Clicker Question 35-1c

For a hypothetical system, we have the Lagrangian that depends on two generalized coordinates, $\mathcal{L}(\rho,\phi, \dot{\rho},\dot{\phi})$. 

> Here $\rho$ has units of length and $\phi$ has units of angle.

Which of the following derivatives give the **generalized momentum** associated with $\rho$?

$1. \dfrac{\partial \mathcal{L}}{\partial \rho} \qquad 2. \dfrac{\partial \mathcal{L}}{\partial \dot{\rho}}$
$3. \dfrac{d}{dt} \left( \dfrac{\partial \mathcal{L}}{\partial \rho} \right) \qquad 4. \dfrac{d}{dt} \left( \dfrac{\partial \mathcal{L}}{\partial \dot{\rho}} \right)$
5. None of these

---

## Clicker Question 35-1d

For a hypothetical system, we have the Lagrangian that depends on two generalized coordinates, $\mathcal{L}(\rho,\phi, \dot{\rho},\dot{\phi})$.

> Here $\rho$ has units of length and $\phi$ has units of angle.

What are the units of the **generalized momentum** associated with $\rho$?

1. kg m/s
2. kg m$^2$/s
3. kg m$^2$/s$^2$
4. kg/s
5. None of these

---

## Clicker Question 35-1e

For a hypothetical system, we have the Lagrangian that depends on two generalized coordinates, $\mathcal{L}(\rho,\phi, \dot{\rho},\dot{\phi})$.

Which of the following derivatives give the **generalized force** associated with $\phi$?

$1. \dfrac{\partial \mathcal{L}}{\partial \phi} \qquad 2. \dfrac{\partial \mathcal{L}}{\partial \dot{\phi}}$
$3. \dfrac{d}{dt} \left( \dfrac{\partial \mathcal{L}}{\partial \phi} \right) \qquad 4. \dfrac{d}{dt} \left( \dfrac{\partial \mathcal{L}}{\partial \dot{\phi}} \right)$
5. None of these

---

## Clicker Question 35-1f

For a hypothetical system, we have the Lagrangian that depends on two generalized coordinates, $\mathcal{L}(\rho,\phi, \dot{\rho},\dot{\phi})$. 

> Here $\rho$ has units of length and $\phi$ has units of angle.

What are the units of the **generalized force** associated with $\phi$?

1. Newtons (N)
2. Joules (J)
3. Newton-meters (N m)
4. Radians (rad)
5. None of these

---

## Clicker Question 35-1g

For a hypothetical system, we have the Lagrangian that depends on two generalized coordinates, $\mathcal{L}(\rho,\phi, \dot{\rho},\dot{\phi})$.

> Here $\rho$ has units of length and $\phi$ has units of angle.

Which of the following derivatives give the **generalized momentum** associated with $\phi$?

$1. \dfrac{\partial \mathcal{L}}{\partial \phi} \qquad 2. \dfrac{\partial \mathcal{L}}{\partial \dot{\phi}}$
$3. \dfrac{d}{dt} \left( \dfrac{\partial \mathcal{L}}{\partial \phi} \right) \qquad 4. \dfrac{d}{dt} \left( \dfrac{\partial \mathcal{L}}{\partial \dot{\phi}} \right)$
5. None of these

---

## Clicker Question 35-1h

For a hypothetical system, we have the Lagrangian that depends on two generalized coordinates, $\mathcal{L}(\rho,\phi, \dot{\rho},\dot{\phi})$.

> Here $\rho$ has units of length and $\phi$ has units of angle.

What are the units of the **generalized momentum** associated with $\phi$?

1. kg m/s
2. kg m$^2$/s
3. kg m$^2$/s$^2$
4. kg/s
5. None of these

---

## Clicker Question 35-2

For the Atwood's machine, $M$ is connected to $m$ by a string of length $l$. Each mass has a length of string extended as measured from the center of the pulley ($R$) of $y_1$ and $y_2$, respectively. The string wraps around half the pulley. 

Which of the following represents the equation of constraint for the system?

1. $y_1 + y_2 = l - R \phi$
2. $y_1 - y_2 = l + R \phi$
3. $y_1 + y_2 = l - \pi R$
4. $y_1 - y_2 = l + \pi R$
5. None of these

**Take the time derivative of the constraint equation.** What do you notice?

---

## Clicker Question 35-3

With a Lagrangian of the form $\mathcal{L} = \frac{1}{2}(M+m)\dot{y}^2_1 - (M-m)gy_1$, we can find the **generalized forces** and **generalized momenta**.

$$F_{y_1} = \frac{\partial \mathcal{L}}{\partial y_1} = -\frac{\partial V}{\partial y_1} \quad p_{y_1} = \frac{\partial \mathcal{L}}{\partial \dot{y}_1} = \frac{\partial T}{\partial \dot{y}_1}$$

What are $F_{y_1}$ and $p_{y_1}$ for the Atwood's machine?

1. $F_{y_1} = -mg$ and $p_{y_1} = m\dot{y}_1$
2. $F_{y_1} = -Mgy_1$ and $p_{y_1} = M\dot{y}_1$
3. $F_{y_1} = -(M-m)g$ and $p_{y_1} = (M+m)\dot{y}_1$
4. $F_{y_1} = -(M+m)g$ and $p_{y_1} = (M-m)\dot{y}_1$
5. None of these

---

## Clicker Question 35-4

Now, we allow the pulley (mass, $M_p$) to rotate. The Lagrangian is given by:
$$\mathcal{L} = \frac{1}{2}(M+m)\dot{y}_1^2 + \frac{1}{2}I\dot{\phi}^2 - (M-m)gy_1$$

Where $I$ is the moment of inertia of the pulley. What is the moment of inertia of the pulley?

1. $I = \frac{1}{2}M_pR^2$
2. $I = \frac{1}{3}M_pR^2$
3. $I = M_pR^2$
4. $I = \frac{1}{4}M_pR^2$
5. None of these

---

## Clicker Question 35-5

The rope moves without slipping on the pulley. A rotation of $R d\phi$ corresponds to a displacement of $dy_1$ for the first mass, $M$. What is the **new** equation of constraint for the system?

1. $y_1 + y_2 = l - R \phi$
2. $dy_1 = R d\phi$
3. $y_1 = R\phi$
4. $\dot{y}_1 = R \dot{\phi}$
5. More than one of these
