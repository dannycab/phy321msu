---
marp: true
theme: graph_paper
paginate: true

title: Day 28 - Homework Session
description: Slides for PHY 321 Fall al 2025, Day 29: Homework Session
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, motion, oscillations, resonance
url: https://dannycaballero.info/phy321msu/slides/day-28-homework-session.html
---

# Day 28 - Homework Session

![bg right width:600px](../images/notes/week10/trojan_horse_maths.jpeg)

---

# Announcements

* Homework 7 is due Sunday
* Midterm 2 will be posted Monday
* Instructions for final project will be posted next week
    * We have one midterm and one homework assignment left!
* DC's group is looking for a research assistant
    * Our group pays ASMSU recommended living wage: $21/hr
    * Current project has 50+ hours worth of work
    * Max employment: 10 hrs/week

---

# Exercise 2 Where does the energy go?

The damped harmonic oscillator is described by the equation of motion is:

$$m\ddot{x} + b\dot{x} + kx = 0$$

where $m$ is the mass, $b$ is the damping coefficient, and $k$ is the spring constant.

The damping term ($F_{damp} = - b\dot{x}$) models the dissipative forces acting on the oscillator. The total energy for the oscillator is given by the sum of the kinetic and potential energies,

$$E = \frac{1}{2}m\dot{x}^2 + \frac{1}{2}kx^2.$$

* 2a What is the energy per unit time dissipated by the damping force?

---

# Exercise 2 Where does the energy go?

$$m\ddot{x} + b\dot{x} + kx = 0$$


$$E = \frac{1}{2}m\dot{x}^2 + \frac{1}{2}kx^2$$

* 2b Take the time derivative of the total energy and show that it is equal (in magnitude) to the energy dissipated by the damping force.
* 2c What is the sign relationship between the energy dissipated by the damping force and the time derivative of the total energy?

---

## Exercise 3, Unpacking the critically damped solution

The solution for critical damping ($\beta = \omega_0$) is given by,

$$x(t) = x_1(t) + x_2(t) = Ae^{-\beta t} + Bte^{-\beta t},$$

where $A$ and $B$ are constants. 

Notice the second solution $x_2(t) = Bte^{-\omega_0t}$ has an additional linear term $t$. We glossed over this solution in class, but it is important to understand why this term is present because it tells us about solving differential equations with pathologically difficult-to-see solutions.

----

## Exercise 3, Unpacking the critically damped solution

Start with the under damped solutions, 

$$y_1(t) = e^{-\beta t}\cos(\omega_1 t) \quad \text{and} \quad y_2(t) = e^{-\beta t}\sin(\omega_1 t),$$

where we have used the notation $\omega_1 = \sqrt{\omega_0^2 - \beta^2}$.

* 3a (3pt). Show that you can recover the first solution $x_1(t)$ by taking the limit of $\beta \rightarrow \omega_0$ of $y_1(t)$.
* 3b (3pt). Show that you cannot recover the second solution $x_2(t)$ by taking the limit of $\beta \rightarrow \omega_0$ of $y_2(t)$ directly. What do you get?
* 3c (4pt). If $\beta \neq \omega_0$, you can divide $y_2(t)$ by $\omega_1$. Now show that in the limit $\beta \rightarrow \omega_0$ of $y_2(t)/\omega_1$, we recover the form of $x_2(t)$.

