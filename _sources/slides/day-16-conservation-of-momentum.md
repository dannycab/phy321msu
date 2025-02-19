---
marp: true
theme: graph_paper
paginate: true

title: Day 16 - Conservation of Linear and Angular Momentum
description: Slides for PHY 321 Spring 2025, Day 16: Conservation of Linear and Angular Momentum
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, energy, stability
url: https://dannycaballero.info/phy321msu/slides/day-16-conservation-of-momentum.html
---

# Day 16 - Conservation of Linear and Angular Momentum

![bg right width:600px](../images/notes/week6/quarks.png)


---

# Announcements

- Midterm 1 is due Feb 28th
- Office hours this week:
  - Today, 4:00-5:00 pm
  - Thursday, 5:00-6:00 pm
  - Friday, 10:00am-12:00pm and 3:00-4:00pm

---

# Seminars this week

## WEDNESDAY, February 19, 2025    

* Astronomy Seminar, 1:30 pm, 1400 BPS, Aaron Bello-Arufa, *The atmospheres of small exoplanets with JWST*
* **PER Seminar**, 3:00 pm., BPS 1400, Anthony Escuardo, *OPTYCS: A Community of Practice Supporting Teaching and Scholarship at Two-Year College*
* FRIB Nuclear Science Seminar, 3:30pm., FRIB 1300 Auditorium, Elise Novitski, *A new approach to measuring neutrino mass*

---

# Seminars this week

## THURSDAY, February 20, 2025

* High Energy Physics Seminar, 1:30pm, BPS 1400 BPS, Ben Assi, *Precision QCD and EFT for Next-Generation Collider Studies*
* Physics and Astronomy sColloquium, 3:30 pm, 1415 BPS, Eric Hudson, *Laser spectroscopy of a nucleus*

 ---

# This Week's Goals

- Understand the concept of potential energy
- Determine the equilibrium points of a system using potential energy
- Analyze the stability of equilibrium points
- Define and begin to apply conservation of linear and angular momentum

---

# Reminders: Finding Equilibrium Points

Given a potential energy function $U(x)$, we can find the equilibrium points by setting the derivative of the potential energy function to zero:

$$\frac{dU(x^*)}{dx} = 0.$$

The stability of the equilibrium points can be determined by examining the second derivative of the potential energy function:

$$\frac{d^2U(x^*)}{dx^2}>0? \qquad \frac{d^2U(x^*)}{dx^2}<0?$$

If the second derivative is positive, the equilibrium point is stable. If the second derivative is negative, the equilibrium point is unstable.

---

# Clicker Question 16-1

Here's the graph of the potential energy function $V(x)$ that is a model of quark confinement in quantum chromodynamics.

![bg right width:80%](../images/notes/week6/quark-potential.png)

What can you say about the equilibrium points? There is/are:

1. One stable point
2. One stable and one unstable point
3. Can't tell

--- 

# Clicker Question 16-2

Here's the equation for this potential energy function:

$$V(v) = -\frac{\gamma}{x}  + \frac{\delta}{x^2} + \kappa x,$$

- $\gamma$, $\delta$, and $\kappa$ are constants.

![bg right width:80%](../images/notes/week6/quark-potential.png)

What can you say about the motion of a particle with energy $E$?

1. $E < 0$ $\;$ 2. $E = 0$ $\;$ 3. $E > 15$

**Careful with #3!** 
Send $x$ to $\infty$: $\lim_{x\to\infty} V(x) = ?$

---

# Clicker Question 16-3

Consider the sum of internal forces on a system of two particles:

$$\sum_i \vec{F}_i^{int} = \sum_{i=1}^{N=2} \sum_{j\neq i}^{N=2} \vec{F}_{ij} = \vec{F}_{12} + \vec{F}_{21}.$$

This sum is equal to:

1. $2\vec{F}_{12}$
2. $-2\vec{F}_{12}$
3. $\vec{F}_{12}$
4. $0$
5. ???

---

# Clicker Question 16-4

In general the sum of internal forces on a system of $N$ particles is:

$$\sum_i \vec{F}_i^{int} = \sum_{i=1}^{N} \sum_{j> i}^{N} \left(\vec{F}_{ij} + \vec{F}_{ji}\right).$$

This sum is **always** equal to:

1. $2\sum_i\vec{F}_{i}$
2. $-2\sum_i\vec{F}_{i}$
3. $\infty$
4. $0$
5. ???

--- 

# Clicker Question 16-5

The change in the total angular momentum of a system of particles is given by:

$$\dfrac{d\vec{L}_{\text{sys}}}{dt} = \sum_i \vec{\tau}_i.$$

There is no change in the total angular momentum of a system of particles when:

1. The net external torque on the system is zero.
2. The net external force on the system is zero.
3. The net internal force on the system is zero.
4. The net internal torque on the system is zero.
5. ???

---

# Clicker Question 16-6

We derived that the change in the total angular momentum of a system of particles is given by:

$$\dfrac{d\vec{L}_{\text{sys}}}{dt} = \sum_{i=1}^N \sum_{j>i}^{N} \left(\vec{r}_i - \vec{r}_j\right) \times \vec{F}_{ij}.$$

What geometric relationship is there between the vectors $\vec{r}_i - \vec{r}_j$ and $\vec{F}_{ij}$ if the angular momentum of the system is conserved?

1. They are parallel.
2. They are perpendicular.
3. They are anti-parallel.
4. I can't tell