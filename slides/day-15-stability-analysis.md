---
marp: true
theme: graph_paper
paginate: true

title: Day 15 - Stability Analysis
description: Slides for PHY 321 Spring 2025, Day 15: Stability Analysis
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, energy, stability
url: https://dannycaballero.info/phy321msu/slides/day-15-stability-analysis.html
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

# Day 15 - Potential Energy and Stability

![bg right width:600px](./images/InfiniteSquareWellAnimation.gif)

Infinite Potential Well $\longrightarrow$

---

## Infinite Potential Well

$$V(x) = \begin{cases} 
      0 & 0 < x < L \\
      \infty & \text{otherwise}
   \end{cases}$$


### Classical Motion in an Infinite Potential Well

Particle bounces back and forth between the walls of the well with constant speed.

### Quantum Motion in an Infinite Potential Well

Particle has quantized energy levels and corresponding wavefunctions that are sinusoidal within the well and zero outside the well.


---

## Announcements

* Midterm 1 is available (Due 27 Feb; late 1 Mar)
  * You may work in larger groups, but solutions are submitted like homework (max 3 group members) **on Gradescope**
  * Exercise 0 is for project planning; and can be submitted individually or as a _different_ group **on D2l**
* **Friday's Class:** Work period for Midterm 1; you can ask us questions and check in on your progress.

---

## Midterm 1 - Exercise 0

**Can be completed individually or as a group (different from your homework/midterm group)**
* Read about Computational Essays
  * Respond to two questions (~200 words each) about your readings.
* Think about the topic and research question you want to explore for your project
  * All together, write about ~500 words describing your project idea.

**Submitting on D2L because DC will give you feedback on your project idea.**

---

## Midterm 1 - Exercise 1

### Modeling Spin Dependent Forces

$$\mathbf{F}_{magnus} = S \mathbf{\omega} \times \mathbf{v}$$

* The next complication beyond air drag
* You may use prior codes or solutions from homework, but you must modify them to include the Magnus force.
* The model should be of your own choosing (i.e., your choice of sports ball)

**Submit on Gradescope (including PDF of Jupyter notebook).**

**What you are learning:** How to model a new situation that is just a little more complicated than what we've done before. 

---

## Midterm 1 - Exercise 2

### Particle in a one-dimensional potential

$$V(x) = \frac{V_0}{d^4}(x^4 - 2x^2d^2+d^4)$$

* Complete a full analysis of the potential using all tools we have learned so far
* Demonstrate your understanding of the potential by modeling motion of a particle

**Submit on Gradescope (including PDF of Jupyter notebook).**

**What you are learning:** How to analyze a new potential energy function based on the theoretical tools and computational tools we have learned so far.

---

## Midterm 1 - Exercise 3

### Model your own system

$$V(x) = ?$$

* Choose a 1D potential energy function that you find interesting
* Analyze the potential energy function using all tools we have learned so far
* Model the motion of a particle in this potential energy function

**Submit on Gradescope (including PDF of Jupyter notebook).**

**What you are learning:** Taking agency over your learning by applying what you have been scaffolded to learn to a system of your own choosing.

---

## Reminders: Finding Equilibrium Points

Given a potential energy function $U(x)$, we can find the equilibrium points by setting the derivative of the potential energy function to zero:

$$\frac{dU(x^*)}{dx} = 0.$$

The stability of the equilibrium points can be determined by examining the second derivative of the potential energy function:

$$\frac{d^2U(x^*)}{dx^2}>0? \qquad \frac{d^2U(x^*)}{dx^2}<0?$$

If the second derivative is positive, the equilibrium point is stable. If the second derivative is negative, the equilibrium point is unstable.

---


## Clicker Question 15-1

Here's the graph of the potential energy function $U(x)$ for a pendulum.

![bg right:40% w:450px h:auto ](../images/notes/week6/pendulum-potential-energy.png)

What can you say about the equilibrium points? There is/are:

1. One stable point
2. Two stable points
3. One stable and one unstable point
4. Two unstable and one stable point

---

## Clicker Question 15-2 (similar to Midterm 1 Exercise 2)

A double-well potential energy function $U(x)$ is given by

$$U(x) = -\frac{1}{2}kx^2 + \frac{1}{4}kx^4.$$

*We assume we have scaled the potential energy so that all the units are consistent.*

How many equilibrium points does this system have?

1. 1
2. 2
3. 3
4. 4

---

## Clicker Question 15-3

A double-well potential energy function $U(x)$ is given by

$$U(x) = -\frac{1}{2}kx^2 + \frac{1}{4}kx^4.$$


1. Find the equilibrium points ($x^*$) of the pendulum by setting:

$$\frac{dU(x^*)}{dx} = 0.$$

2. Characterize the stability of the equilibrium points ($x^*$):

$$\frac{d^2U(x^*)}{dx^2}>0? \qquad \frac{d^2U(x^*)}{dx^2}<0?$$

**Click when done.**

---

## Clicker Question 15-4

Here's a graph of the potential energy function $U(x)$ for a double-well potential.

![bg right:52% width:600px height:auto](../images/notes/week6/cq14-5.png)

Describe the motion of a particle with the total energy, $E=$

1. $0.4\,\mathrm{J}$, $<$ barrier height
2. $1.2\,\mathrm{J}$, $>$ barrier height
3. $1.0\,\mathrm{J}$, $=$ barrier height

**Click when done.**


---

## Clicker Question 15-5

Here's the graph of the potential energy function $V(x)$ that is a model of quark confinement in quantum chromodynamics.

![bg right:45% width:500px](../images/notes/week6/quark-potential.png)

What can you say about the equilibrium points? There is/are:

1. One stable point
2. One stable and one unstable point
3. Can't tell

--- 

## Clicker Question 15-6

Here's the equation for this potential energy function (constants: $\gamma$, $\delta$, and $\kappa$):

$$V(v) = -\frac{\gamma}{x}  + \frac{\delta}{x^2} + \kappa x,$$



![bg right:45% width:500px](../images/notes/week6/quark-potential.png)

What can you say about the motion of a particle with energy $E$?

1. $E < 0$ $\;$ 2. $E = 0$ $\;$ 3. $E > 15$

**Careful with #3!** 
Send $x$ to $\infty$: $\lim_{x\to\infty} V(x) = ?$