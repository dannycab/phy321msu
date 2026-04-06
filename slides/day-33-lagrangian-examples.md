---
marp: true
theme: graph_paper
paginate: true

title: Day 33 - Lagrangian Examples
description: Slides for PHY 321 Spring 2026, Day 33: Lagrangian Examples
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, Lagrangian, examples
url: https://dannycaballero.info/phy321msu/slides/day-33-lagrangian-examples.html

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

# Day 33 - Lagrangian Examples

![bg right width:500px](../images/notes/week13/lion-lagrange.jpg)

---

## Announcements

* Homework 8 has been posted (Last HW; Due 17 Apr, "Late" 24 Apr)
    * Last Exercise 0: Reflect Learning Outcomes
* Final Project is posted
    * Video Presentations due 27 Apr
    * Computational Essay due 1 May
    * Rubric for both are posted
* No class (20 Apr - 24 Apr) - DC out of country
    * Make appointment for project help (clicker extra credit)

---

## Reminder: The Lagrangian

The Lagrangian $\mathcal{L}$ is a function that summarizes the dynamics of the system:

$$
\mathcal{L}(q, \dot{q}, t) = T - V
$$

where:
- $T$ is the **kinetic energy** of the system (depends on **gen. vel.**, $\dot{q}$),
- $V$ is the **potential energy** of the system (depends on **gen. pos.**, $q$).

The equation of motion is recovered by applying the Euler-Lagrange equation to the Lagrangian (*minimizing the action integral*).

$$
\frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{q}}\right) - \frac{\partial \mathcal{L}}{\partial q} = 0
$$

---

## Clicker Question 33-1

For a 1D SHO, the kinetic and potential energy are given by:

$$
T = \frac{1}{2} m \dot{x}^2 \quad \text{and} \quad V = \frac{1}{2} k x^2
$$

What are the derivatives of the Lagrangian $\mathcal{L} = T - V$ with respect to $x$ and $\dot{x}$?

1. $\frac{\partial \mathcal{L}}{\partial x} = kx$ and $\frac{\partial \mathcal{L}}{\partial \dot{x}} = m\dot{x}$
2. $\frac{\partial \mathcal{L}}{\partial x} = -kx$ and $\frac{\partial \mathcal{L}}{\partial \dot{x}} = m\dot{x}$
3. $\frac{\partial \mathcal{L}}{\partial x} = kx$ and $\frac{\partial \mathcal{L}}{\partial \dot{x}} = -m\dot{x}$
4. $\frac{\partial \mathcal{L}}{\partial x} = -kx$ and $\frac{\partial \mathcal{L}}{\partial \dot{x}} = -m\dot{x}$
5. None of the above.

---

## Clicker Question 33-2

For the plane pendulum, with $\mathcal{L}(x, \dot{x}, y, \dot{y}, t) = \frac{1}{2} m \left( \dot{x}^2 + \dot{y}^2 \right) - mgy$

We found:

$$\frac{d}{dt}\left(m\dot{x}\right) = 0 \qquad \text{and} \quad \ddot{y} = - g$$

Does that seem right?

1. Yes, it's fine.
2. Maybe, but I'm not sure I can tell you why.
3. No, I know this is wrong, but I'm not sure why.
4. No, this is definitely wrong and I can prove it!

---

## Clicker Question 33-3

For the plane pendulum, we changed the Lagrangian from Cartesian coordinates to plane polar coordinates. In Cartesian, we found the Lagrangian depended on $y,\dot{x},\dot{y}$. In polar, it only depended on $\phi$ and $\dot{\phi}$.

$$\mathcal{L}(x,y,\dot{y}) \longrightarrow \mathcal{L}(\phi, \dot{\phi})$$

What does that tell you about the dimensions of the system? The system is:

1. in 3D space, so it's 3D.
2. described by two spatial dimensions ($x,y$), so it's 2D.
3. described by one spatial dimension ($\phi$), so it's 1D.

---

## We chose our generalized coordinates poorly

We used the Lagrangian formalism to derive the equations of motion for a plane pendulum. We chose the $x$ and $y$ coordinates.

$$T(\dot{x}, \dot{y}) = \dfrac{1}{2} m (\dot{x}^2 + \dot{y}^2), \quad V(y) = mgy \longrightarrow \mathcal{L} = T - V = \dfrac{1}{2} m (\dot{x}^2 + \dot{y}^2) - mgy$$

This gave us the following derivatives for the Lagrangian:

$$\frac{\partial \mathcal{L}}{\partial x} = 0 \quad \frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{x}} \right) = \frac{d}{dt} \left( m\dot{x} \right) = 0$$
$$\frac{\partial \mathcal{L}}{\partial y} = -mg \quad \frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{y}} \right) = -m\ddot{y}$$

---

## We made a mistake by not including the constraint

We made a mistake by not including the constraint $x^2 + y^2 = L^2$ in our Lagrangian.

We can change variables to $r$ and $\phi$.
$$x = r \cos(\phi) \quad y = r \sin(\phi)$$

$$T(\dot{x}, \dot{y}) = \dfrac{1}{2} m (\dot{x}^2 + \dot{y}^2) = \dfrac{1}{2} m \left( r^2 \dot{\phi}^2 + 2r\dot{r}\dot{\phi} + \dot{r}^2 \right) = T(r, \dot{r}, \phi, \dot{\phi})$$
$$V(y) = mgy = mg r \sin(\phi) = V(r, \phi)$$

---

## We made a mistake by not including the constraint

Now we include the constraint $r = L$, so that $\dot{r} = 0$.

$$T(\phi, \dot{\phi}) = \dfrac{1}{2} m L^2 \dot{\phi}^2 \quad V(\phi) = mgL \cos(\phi)$$

$$\mathcal{L} = \dfrac{1}{2} m L^2 \dot{\phi}^2 - mgL \cos(\phi)$$

---

## Clicker Question 33-4

For the plane pendulum, we changed the Lagrangian from Cartesian coordinates to plane polar coordinates. In Cartesian, we found the Lagrangian depended on $y,\dot{x},\dot{y}$. In polar, it only depended on $\phi$ and $\dot{\phi}$.

$$\mathcal{L}(x,y,\dot{y}) \longrightarrow \mathcal{L}(\phi, \dot{\phi})$$

What does that tell you about the dimensions of the system? The system is:

1. in 3D space, so it's 3D.
2. described by two spatial dimensions ($x,y$), so it's 2D.
3. described by one spatial dimension ($\phi$), so it's 1D.

---

## Clicker Question 33-5

With $\mathcal{L} = \dfrac{1}{2} m L^2 \dot{\phi}^2 - mgL \cos(\phi)$, we can find the equations of motion. 

$$\dfrac{\partial \mathcal{L}}{\partial \phi} - \dfrac{d}{dt} \left( \dfrac{\partial \mathcal{L}}{\partial \dot{\phi}} \right) = 0$$

Which of the following equations of motion is correct?

$1.\quad \ddot{\phi} = -\frac{g}{L} \sin(\phi) \qquad 2. \quad \ddot{\phi} = -\frac{g}{L} \cos(\phi)$
$3.\quad \ddot{\phi} = -\sqrt{\frac{g}{L} \sin(\phi)} \qquad 4.\quad \ddot{\phi} = -\sqrt{\frac{g}{L} \cos(\phi)}$
$5.\quad \textrm{None of these}$

---

## Clicker Question 33-6

For the Atwood's machine, $M$ is connected to $m$ by a string of length $l$. Each mass has a length of string extended as measured from the center of the pulley ($R$) of $y_1$ and $y_2$, respectively. The string wraps around half the pulley. 

Which of the following represents the equation of constraint for the system?

$1. \quad y_1 + y_2 = l - R \phi \qquad 2. \quad y_1 - y_2 = l + R \phi$
$3. \quad y_1 + y_2 = l - \pi R \qquad 4. \quad y_1 - y_2 = l + \pi R$
$5. \quad \textrm{None of these}$

**Take the time derivative of the constraint equation.** What do you notice?

---

## Clicker Question 33-7

With a Lagrangian of the form $\mathcal{L} = \frac{1}{2}(M+m)\dot{y}^2_1 - (M-m)gy_1$, we can find the **generalized forces** and **generalized momenta**.

$$F_{y_1} = \frac{\partial \mathcal{L}}{\partial y_1} = -\frac{\partial V}{\partial y_1} \quad p_{y_1} = \frac{\partial \mathcal{L}}{\partial \dot{y}_1} = \frac{\partial T}{\partial \dot{y}_1}$$

What are $F_{y_1}$ and $p_{y_1}$ for the Atwood's machine?

$1. \quad F_{y_1} = -mg \textrm{ and } p_{y_1} = m\dot{y}_1 \qquad 2. \quad F_{y_1} = -Mgy_1 \textrm{ and } p_{y_1} = M\dot{y}_1$
$3. \quad F_{y_1} = -(M-m)g \textrm{ and } p_{y_1} = (M+m)\dot{y}_1$
$4. \quad F_{y_1} = -(M+m)g \textrm{ and } p_{y_1} = (M-m)\dot{y}_1$
$5. \quad \textrm{None of these}$

---

## Clicker Question 33-8

Now, we allow the pulley (mass, $M_p$) to rotate. The Lagrangian is given by:
$$\mathcal{L} = \frac{1}{2}(M+m)\dot{y}_1^2 + \frac{1}{2}I\dot{\phi}^2 - (M-m)gy_1$$

Where $I$ is the moment of inertia of the pulley. What is the moment of inertia of the pulley?

$1. \quad I = \frac{1}{2}M_pR^2 \qquad 2. \quad I = \frac{1}{3}M_pR^2$
$3. \quad I = M_pR^2 \qquad 4. \quad I = \frac{1}{4}M_pR^2$
$5. \quad \textrm{None of these}$

---

## Clicker Question 33-9

The rope moves without slipping on the pulley. A rotation of $R d\phi$ corresponds to a displacement of $dy_1$ for the first mass, $M$. What is the **new** equation of constraint for the system?

1. $y_1 + y_2 = l - R \phi$
2. $dy_1 = R d\phi$
3. $y_1 = R\phi$
4. $\dot{y}_1 = R \dot{\phi}$
5. More than one of these
