---
marp: true
theme: graph_paper
paginate: true

title: Day 23 - Homework Session
description: Slides for PHY 321 Spring 2025, Day 23: Homework Session
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-23-homework-session.html
---

# Day 23 - Homework Session

![bg right width:600px](../images/notes/week3/quack.png)

---

# Announcements

* Homework 3 is graded
* Midterm 1 is still being graded
    * Re: Problem 2 $\rightarrow$ HOLY CRAP YOU ALL ARE AMAZING
* Homework 5 is due tonight
* Homework 6 is due next Friday
* Danny will be out next Wednesday
    * Class will be on zoom (usual link)

---

# Reminders

We solved the damped harmonic oscillator equation:

$$\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = 0$$

We chose a solution (**ansatz**) of the form

$$x(t) = C_1 e^{r t} + C_2 e^{r t}$$

and computed the roots of the characteristic equation:

$$r^2 + 2 \beta r + \omega_0^2 = 0$$

We found the roots to be:

$$r = -\beta \pm \sqrt{\beta^2 - \omega_0^2}$$

---

# Weak Damping

We found that when $\beta^2 < \omega_0^2$, the roots are complex:

$$r = -\beta \pm i \sqrt{\omega_0^2 - \beta^2}$$

This means that the solution is oscillatory:

$$x(t) = e^{-\beta t} \left( C_1 \cos(\sqrt{\omega_0^2 - \beta^2} t) + C_2 \sin(\sqrt{\omega_0^2 - \beta^2} t) \right)$$

The solution is a damped oscillation with frequency $\omega_1 = \sqrt{\omega_0^2 - \beta^2}$.

---

# Strong Damping

When $\beta^2 > \omega_0^2$, the roots are real:

$$r = -\beta \pm \sqrt{\beta^2 - \omega_0^2}$$

This means that the solution is not oscillatory:
$$x(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}$$
where $r_1 = -\beta + \sqrt{\beta^2 - \omega_0^2} < 0$ and $r_2 = -\beta - \sqrt{\beta^2 - \omega_0^2} < 0$.

The solution is the sum of two exponentials with different decay rates.

---

# Critical Damping

When $\beta^2 = \omega_0^2$, the roots are real and equal (repeated roots):
$$r = -\beta$$

This means that the solution is not oscillatory, but also that our ansatz is not sufficient. The correct form of the solution is:

$$x(t) = (C_1 + C_2 t) e^{-\beta t}$$

**In most cases, we will work with weak damping.**