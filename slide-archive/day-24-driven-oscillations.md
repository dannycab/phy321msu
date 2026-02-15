---
marp: true
theme: graph_paper
paginate: true

title: Day 24 - Driven Oscillations
description: Slides for PHY 321 Fall 2025, Day 24: Driven Oscillations
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, motion, oscillations, driven oscillations
url: https://dannycaballero.info/phy321msu/slides/day-24-homework-session.html
---

# Day 24 - Driven Oscillations

![bg right width:300px](../images/notes/week9/animated-driven-pendulum.gif)

Resonance in a driven pendulum system. $\longrightarrow$

Source: [Wikipedia](https://upload.wikimedia.org/wikipedia/commons/2/25/Driven-pendulums-resonance-animation.gif)

---

# Announcements

* Midterm 1 is still being graded (sorry, bit off more than I can chew)
* Homework 6 is due Friday
* Homework 7 is posted, due next Friday
    * Final project check-in #1
* **Friday's Class**: We will complete HW 6 Exercises 2 and 4 together.

---

# Seminars this week

## TUESDAY, October 21, 2025
 
 
Theory Seminar, 11:00am., FRIB 1200 lab, In person and online via Zoom
Speaker: Antonio Bjelcic, LLNL
Title: Small and Large Amplitude Collective Dynamics within Nuclear Density Functional Theory
Zoom Link: 964 7281 4717
Meeting ID: 48824

---

# Seminars this week

## WEDNESDAY, October 22, 2025
 
 
FRIB Nuclear Science Seminar, 3:30pm., FRIB 1300 Auditorium and online via Zoom 
Speaker: Dr. Nan Liu of Boston University 
Title: Presolar Grains as Probes of Type II Supernova Nucleosynthesis
Please click the link below to join the webinar:
Join Zoom Meeting: https://msu.zoom.us/j/93944167137?pwd=jzvwvbL8YqDnJNpzDPat8IHcrFdtC5.1
Meeting ID: 939 4416 7137
Passcode: 239049
 
---

# Seminars this week

##  THURSDAY, October 23, 2025
 
Colloquium, 3:30 pm, 1415 BPS, in person and zoom.  Host ~ 
Refreshments and social half-hour in BPS 1400 starting at 3 pm
Speaker: Darryl Seligman, MSU
Title: Divergent Small Bodies:  Interstellar Interlopers and Dark Comets 
Zoom Link: https://msu.zoom.us/j/94951062663
Password: 2002  Or complete link:  https://msu.zoom.us/j/94951062663?pwd=c48uM25P9UsRVuR74rkOioOWgpoxgC.1
 
---

# Seminars this week

## FRIDAY, October 24, 2025 
 
QuIC Seminar, 12:30pm, -1:30pm, 1300 BPS, Virtual only today
Speaker: James Whitefield, Dartmouth
Title: TBA
Full Schedule is at: https://sites.google.com/msu.edu/quic-seminar/

---

# Seminars this week

## FRIDAY, October 24, 2025 

IReNA Online Seminar, 2:00 pm, In Person and Zoom, FRIB 2025 Nuclear Conference Room, Light refreshments will be served at 1:50pm. 
Hosted by: Hosted by: Linda Lombardo (INAF Trieste)
Speaker: Marta Molero, TU Darmstadt
Title: Chemical evolution of neutron-capture elements: a multi-objective approach
Zoom Link: https://msu.zoom.us/j/827950260
Password: JINA

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

---

# Clicker Question 24-1

How are you doing?

1. Semester is going well; I'm locked in.
2. Semester is going alright; Tough but I'm working on it.
3. Semester is not going great TBH; I need to make some changes.
4. Danny, this semester is some BS.

---

# Clicker Question 24-2

What do we expect the phase space diagram ($x$ vs $\dot{x}$) to look like for a weakly damped harmonic oscillator?

1. A set of ellipses
2. A set of spirals
3. Depends on how weak the damping is
4. Depends on the total energy 
5. More than one of the above

---

# Clicker Question 24-3

The driven harmonic oscillator equation is:

$$\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = f(t)$$

with $w_0^2 = k/m$ and $2\beta = b/m$. What is the dimension of the driving force $f(t)$?

1. Force (Newtons, N)
2. Force per unit second (N/s)
3. Force per unit length (N/m)
4. Force per unit mass (N/kg)

---

# Clicker Question 24-4

The driven harmonic oscillator equation is:

$$\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = f(t).$$

This ODE is a ________ differential equation.

1. linear
2. nonlinear
3. first-order
4. second-order
5. more than one of the above

---

# Example: Sinusoidal Driving Force

Let $f(t) = f_0 \cos(\omega t)$, so that the driven harmonic oscillator equation is:

$$\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = f_0 \cos(\omega t)$$

**Note: $\omega \neq \omega_0$**

Note that if the driving follows a sine wave, then we have:

$$\ddot{y} + 2 \beta \dot{y} + \omega_0^2 y = f_0 \sin(\omega t)$$

Interesting, $e^{i \omega t} = \cos(\omega t) + i \sin(\omega t)$, let try to work with $z(t) = x(t) + i y(t).$

---

# Clicker Question 24-5

We found that the square amplitude of the driven harmonic oscillator is:

$$A^2 = \dfrac{f_0^2}{(\omega_0^2 - \omega^2)^2 + 4 \beta^2 \omega^2}$$

When is the amplitude of the driven oscillator maximized?

1. When the driving frequency ($\omega$) is far from the natural frequency ($\omega_0$)
2. When the driving frequency ($\omega$) is close to the natural frequency ($\omega_0$)
3. When the damping ($2\beta$) is weak
4. When the damping ($2\beta$) is strong
5. Some combination of the above
