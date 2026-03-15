---
marp: true
theme: graph_paper
paginate: true

title: Day 23 - Driven Oscillations
description: Slides for PHY 321 Spring 2026, Day 23: Driven Oscillations
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, motion, oscillations, driven oscillations
url: https://dannycaballero.info/phy321msu/slides/day-23-driven-oscillations.html
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

# Day 23 - Driven Oscillations

![bg right width:300px](../images/notes/week9/animated-driven-pendulum.gif)

Resonance in a driven pendulum system. $\longrightarrow$

Source: [Wikipedia](https://upload.wikimedia.org/wikipedia/commons/2/25/Driven-pendulums-resonance-animation.gif)

---

# Welcome Richard Hallstein!

# Announcements

* HW 5 given blanket extension to this Friday.
* HW 6 still due this Friday, but will be extended if needed.
* DC will return Wednesday
* Mihir will lead workshop session for HW 6 on Friday

---


## Reminders

We solved the damped harmonic oscillator equation:

$$\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = 0$$

We chose a solution (**ansatz**) of the form

$$x(t) = C_1 e^{r t} + C_2 e^{r t}$$

and computed the roots of the characteristic equation:

$$r^2 + 2 \beta r + \omega_0^2 = 0$$

We found the roots to be:

$$r = -\beta \pm \sqrt{\beta^2 - \omega_0^2}$$

---

## Weak Damping

We found that when $\beta^2 < \omega_0^2$, the roots are complex:

$$r = -\beta \pm i \sqrt{\omega_0^2 - \beta^2}$$

This means that the solution is oscillatory:

$$x(t) = e^{-\beta t} \left( C_1 \cos(\sqrt{\omega_0^2 - \beta^2} t) + C_2 \sin(\sqrt{\omega_0^2 - \beta^2} t) \right)$$

The solution is a damped oscillation with frequency $\omega_1 = \sqrt{\omega_0^2 - \beta^2}$.

---

## Strong Damping

When $\beta^2 > \omega_0^2$, the roots are real:

$$r = -\beta \pm \sqrt{\beta^2 - \omega_0^2}$$

This means that the solution is not oscillatory:
$$x(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}$$
where $r_1 = -\beta + \sqrt{\beta^2 - \omega_0^2} < 0$ and $r_2 = -\beta - \sqrt{\beta^2 - \omega_0^2} < 0$.

The solution is the sum of two exponentials with different decay rates.

---

## Critical Damping

When $\beta^2 = \omega_0^2$, the roots are real and equal (repeated roots):
$$r = -\beta$$

This means that the solution is not oscillatory, but also that our ansatz is not sufficient. The correct form of the solution is:

$$x(t) = (C_1 + C_2 t) e^{-\beta t}$$

**In most cases, we will work with weak damping.**

---

## Clicker Question 23-1

What do we expect the phase space diagram ($x$ vs $\dot{x}$) to look like for a weakly damped harmonic oscillator?

1. A set of ellipses
2. A set of spirals
3. Depends on how weak the damping is
4. Depends on the total energy 
5. More than one of the above

---

## Clicker Question 23-2

The driven harmonic oscillator equation is:

$$\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = f(t)$$

with $w_0^2 = k/m$ and $2\beta = b/m$. What is the dimension of the driving force $f(t)$?

1. Force (Newtons, N)
2. Force per unit second (N/s)
3. Force per unit length (N/m)
4. Force per unit mass (N/kg)

---

## Clicker Question 24-3

The driven harmonic oscillator equation is:

$$\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = f(t).$$

This ODE is a ________ differential equation.

1. linear
2. nonlinear
3. first-order
4. second-order
5. more than one of the above

---

## Example: Sinusoidal Driving Force

Let $f(t) = f_0 \cos(\omega t)$, so that the driven harmonic oscillator equation is:

$$\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = f_0 \cos(\omega t)$$

**Note: $\omega \neq \omega_0$**

Note that if the driving follows a sine wave, then we have:

$$\ddot{y} + 2 \beta \dot{y} + \omega_0^2 y = f_0 \sin(\omega t)$$

Interesting, $e^{i \omega t} = \cos(\omega t) + i \sin(\omega t)$, let try to work with $z(t) = x(t) + i y(t).$

---

## Clicker Question 24-4

We found that the square amplitude of the driven harmonic oscillator is:

$$A^2 = \dfrac{f_0^2}{(\omega_0^2 - \omega^2)^2 + 4 \beta^2 \omega^2}$$

When is the amplitude of the driven oscillator maximized?

1. When the driving frequency ($\omega$) is far from the natural frequency ($\omega_0$)
2. When the driving frequency ($\omega$) is close to the natural frequency ($\omega_0$)
3. When the damping ($2\beta$) is weak
4. When the damping ($2\beta$) is strong
5. Some combination of the above
