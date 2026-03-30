---
marp: true
theme: graph_paper
paginate: true

title: Day 27 - Hallmarks of Chaos
description: Slides for PHY 321 Spring 2026, Day 27: Hallmarks of Chaos
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, motion, oscillations, rduffing, lorenz, strange attractors
url: https://dannycaballero.info/phy321msu/slides/day-27-hallmarks-of-chaos.html
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

# Day 27 - Hallmarks of Chaos

![bg right width:600px](../images/notes/week10/lyapunov.png)

## Conceptualizing the Lyapunov Exponent

*Trajectories diverge exponentially in time*

---

## Hallmarks of a Classically Chaotic System

1. **Deterministic**
2. **Sensitive to Initial Conditions** 
3. **Non-periodic Behavior**
4. **Strange Attractors**
5. **Parameter Sensitivity**
6. (Sometimes) **Periodic Behavior**

---

## Limit Cycle

A **limit cycle** is a closed trajectory in phase space that is an attractor for a dynamical system.

![bg right](../images/notes/week10/van-der-pol-limit-cycle.gif)

The **Van der Pol Oscillator** exhibits a limit cycle. 

$$\ddot{x} - \mu (1 - x^2) \dot{x} + x = 0$$

Random initial conditions converge to a limit cycle. Modeled with $\mu=2$.

---

## The Lyapunov Exponent

![bg right width:700px](../images/notes/week10/lyapunov.png)

$\vec{\delta}(t)$ is the separation vector between two trajectories in phase space $\vec{\delta}(t) = \vec{x}_2(t) - \vec{x}_1(t)$.

Do trajectories diverge exponentially in time, $|\vec{\delta}(t)| \approx |\vec{\delta}(0)| e^{\lambda t}$?

Each phase coordinate can change at a different rate: $\vec{\lambda} = \langle \lambda_1, \lambda_2, \dots, \lambda_n \rangle$.

Largest $\lambda_i > 0$? Chaotic system.

---

## Strange Attractors

A **strange attractor** is a set of points in phase space that a chaotic system approaches.

**Chen Attractor**

![Chen Attractor bg left ](../images/notes/week10/chen.png)

$$\dot{x} = \alpha x-yz$$
$$\dot{y} = \beta y + xz$$
$$\dot{z} = \gamma z + xy/3$$

$\alpha=5$, $\beta=-10$, $\gamma=-0.38$.

[Interactive 3D Model](https://jcponce.github.io/calculus/velfields/Chen)

---

## Example 1: Duffing Equation

$$\ddot{x} + \beta \dot{x} + \alpha x + \gamma x^3 = F_0 \cos(\omega t)$$

![width:1200px](../images/notes/week10/duffing.png)

**Exhibits Periodic and Chaotic Behavior**

**Illustrates period doubling bifurcations as route to chaos**

---

## Example 2: Lorenz System

$$\dot{x} = \sigma (y - x)$$
$$\dot{y} = x (\rho - z) - y$$
$$\dot{z} = x y - \beta z$$

![bg right width:600px](../images/notes/week10/lorenz-trajectories.png)

**Exhibits sensitive dependence on initial conditions**
**Demonstrates the concept of a strange attractor**
