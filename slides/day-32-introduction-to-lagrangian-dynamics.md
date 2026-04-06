---
marp: true
theme: graph_paper
paginate: true

title: Day 32 - Introduction to Lagrangian Dynamics
description: Slides for PHY 331 Spring 2026, Day 32: Introduction to Lagrangian Dynamics
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, Lagrangian dynamics, action principle, Lagrangian mechanics
url: https://dannycaballero.info/phy331msu/slides/day-32-introduction-to-lagrangian-dynamics.html
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

# Day 32 - Introduction to Lagrangian Dynamics

![bg right width:600px](../images/notes/week12/newton-scared.jpg)

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

## Newton's Laws

We use Newton's laws of motion to describe the dynamics of a system:
1. **First Law**: An object at rest remains at rest, and an object in motion continues in motion with the same speed and in the same direction unless acted upon by a net external force.
2. **Second Law**: The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass. Mathematically, this is expressed as:
   $$ \vec{F} = m \vec{a} $$

---

## Newton's Laws (continued)

3. **Third Law**: For every action, there is an equal and opposite reaction. This means that if object A exerts a force on object B, then object B exerts a force of equal magnitude and opposite direction on object A.

---

## Newton's Laws Expectations

* We can describe every interaction on a body using forces
* We can sum up all the forces vectorially in particular coordinate systems (Cartesian, polar, etc.)
* We can derive equations of motion for a system by applying Newton's second law

*Sometimes, these expectations can be limiting, especially when dealing with complex systems or when forces are not easily identifiable.* 

---

## Newton's Laws in Plane Polar Coordinates

In plane polar coordinates ($r,\phi$), we can express Newton's second law as follows:

$$
\vec{F} = m \vec{a} \implies
\vec{F} = m \left( \ddot{r} - r \dot{\phi}^2 \right) \hat{r} + m \left( r \ddot{\phi} + 2\dot{r}\dot{\phi} \right) \hat{\phi}
$$

where:
- $\ddot{r}$ is the radial acceleration,
- $\dot{\phi}$ is the angular velocity,
- $\ddot{\phi}$ is the angular acceleration,
- $\hat{r}$ and $\hat{\phi}$ are the unit vectors in the radial and angular directions, respectively.

**How?** And what new insights can we gain from this?

---

## Clicker Question 32-1

![bg right:40% width:500px](../images/notes/week12/coordinate-system.png)

The appropriate definition of the $\hat{r}$ vector using Cartesian coordinates ($x,y$) is:

1. $\hat{r} = \langle  \cos(\phi), \sin(\phi) \rangle$
2. $\hat{r} = \langle  \sin(\phi), \cos(\phi) \rangle$
3. $\hat{r} = \langle -\sin(\phi), \cos(\phi) \rangle$
4. $\hat{r} = \langle  \cos(\phi), -\sin(\phi) \rangle$
5. None of the above.

---

## Clicker Question 32-2

![bg right:40% width:500px](../images/notes/week12/coordinate-system.png)

The appropriate definition of the $\hat{\phi}$ vector using Cartesian coordinates ($x,y$) is:

1. $\hat{\phi} = \langle  \cos(\phi), \sin(\phi) \rangle$
2. $\hat{\phi} = \langle  \sin(\phi), \cos(\phi) \rangle$
3. $\hat{\phi} = \langle -\sin(\phi), \cos(\phi) \rangle$
4. $\hat{\phi} = \langle  \cos(\phi), -\sin(\phi) \rangle$
5. None of the above.

---

## Clicker Question 32-3

We need to take the derivative of $\hat{r}$ with respect to time. Why should we do this in Cartesian coordinates?

1. The Cartesian coordinates are easier to work with for derivatives.
2. The derivative of $\hat{r}$ in Cartesian coordinates are zero.
3. The unit vector $\hat{r}$ is location dependent.
4. The Cartesian unit vectors do not change with time.
5. Something else?

---

## Summary of Results

With $\vec{r} = r \hat{r}$,

$$\vec{v} = \dot{\vec{r}} = \dot{r} \hat{r} + r \dot{\phi} \hat{\phi}$$

$$\vec{a} = \dot{\vec{v}} = \ddot{r} \hat{r} + \dot{r} \dot{\phi} \hat{\phi} + r \ddot{\phi} \hat{\phi} + r \dot{\phi}^2 \hat{r}$$

This allows us to express Newton's second law in polar coordinates as:

$$
\vec{F} = m \left( \ddot{r} - r \dot{\phi}^2 \right) \hat{r} + m \left( r \ddot{\phi} + 2\dot{r}\dot{\phi} \right) \hat{\phi}
$$

Or

$$F_r = m \left( \ddot{r} - r \dot{\phi}^2 \right) \quad \text{and} \quad F_\phi = m \left( r \ddot{\phi} + 2\dot{r}\dot{\phi} \right)$$


---

## Euler-Lagrange Equation

We found that certain kinds of optimization problems involving functionals could be solved using the **Euler-Lagrange equation**. This equation provides a powerful method to derive the equations of motion for a system based on an action principle.

The Euler-Lagrange equation is given by:

$$
\frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right) - \frac{\partial f}{\partial y} = 0
$$

where $f(y, y', x)$ is a **functional** that depends on the dependent variable $y$, its derivative $y' = \frac{dy}{dx}$, and the independent variable $x$.

---

## The Action Integral

The action integral is central to Lagrangian dynamics. The action $S$ is defined as the integral of a **functional** $L(q,\dot{q},t)$ over time:

$$
S = \int_{t_1}^{t_2} \mathcal{L}(q, \dot{q}, t) \, dt
$$

where:
- $q$ represents the **generalized coordinates** of the system,
- $\dot{q}$ represents the **generalized velocities** (time derivatives of $q$),
- $t$ represents time.

**Hamilton's Principle:** The path the system takes **extremizes the action $S$**. 

---

## The Lagrangian

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

## Clicker Question 32-4

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

## Clicker Question 32-5

For the plane pendulum, with $\mathcal{L}(x, \dot{x}, y, \dot{y}, t) = \frac{1}{2} m \left( \dot{x}^2 + \dot{y}^2 \right) - mgy$

We found:

$$\frac{d}{dt}\left(m\dot{x}\right) = 0 \qquad \text{and} \quad \ddot{y} = - g$$

Does that seem right?

1. Yes, it's fine.
2. Maybe, but I'm not sure I can tell you why.
3. No, I know this is wrong, but I'm not sure why.
4. No, this is definitely wrong and I can prove it!

---

## Clicker Question 32-6

For the plane pendulum, we changed the Lagrangian from Cartesian coordinates to plane polar coordinates. In Cartesian, we found the Lagrangian depended on $y,\dot{x},\dot{y}$. In polar, it only depended on $\phi$ and $\dot{\phi}$.

$$\mathcal{L}(x,y,\dot{y}) \longrightarrow \mathcal{L}(\phi, \dot{\phi})$$

What does that tell you about the dimensions of the system? The system is:

1. in 3D space, so it's 3D.
2. described by two spatial dimensions ($x,y$), so it's 2D.
3. described by one spatial dimension ($\phi$), so it's 1D.