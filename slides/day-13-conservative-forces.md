---
marp: true
theme: graph_paper
paginate: true

title: Day 13 - Conservative Forces
description: Slides for PHY 321 Spring 2025, Day 13: Conservative Forces
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, energy, conservative forces, work,
url: https://dannycaballero.info/phy321msu/slides/day-13-conservative-forces.html
---

# Day 13 - Conservative Forces

![Conservative Forces bg right 100%](../images/notes/week5/conservative-forces.png)

$$\vec{F} = - \nabla U$$
$$U = - \int \vec{F} \cdot d\vec{r}$$
$$\nabla \times \vec{F} = 0$$


---

# Announcements

* HW 4 is due next Monday, Feb 17th NOT on Friday the 14th
* There are no office hours on Feb 13th
* Midterm 1 will be available on Monday as well.

---

# Reminder of our Midterm Procedures

* The take-home midterms will be open for almost two weeks; you can often start some exercises early as they cover older material.
* They are meant to be challenging, but we will provide you with the resources and support you need to complete them.
* There is no homework due during the period in which the midterm is assigned.
* In contrast to homework assignments, you must turn in your own solutions to the midterms.

You may work closely together with me, Elisha, and your classmates, but you must write up your own solutions.

---

# Seminars this week

## WEDNESDAY, February 12, 2025
* Astronomy Seminar, 1:30 pm, 1400 BPS, Rafael Luque, Univ. of Chicago, Exoplanets
* FRIB Nuclear Science Seminar, 3:30pm., FRIB 1300 Auditorium, Professor Veronica Dexheimer, Kent State University, An overview of the MUSES cyberinfrastructure and what it can do for you

## FRIDAY,  February 14, 2025 
 
* IReNA Online Seminar, 2:00 pm, FRIB 2025 Nuclear Conference Room,Kelsey Lund, University of California, Berkeley,  How The Gentle Winds Beckon: Nucleosynthesis in Neutron Star Merger Remnant Winds

---

# This Week's Goals

* Remind ourselves of the concept of energy and energy conservation
* Apply the conservation of energy to a variety of systems
* Develop the mathematical tools to analyze energy conservation in more complex systems
* Connect our new understanding of energy conservation to our previous work on forces and motion

---

# Reminders

* Energy is conserved in every process; our choice of system determines how we account for energy.
* Closed, isolated systems are often the simplest to analyze.
* A point particle is a model that allows us to ignore the internal structure of an object.
* The Work-Energy Theorem is just a statement of the conservation of energy for a point particle.

---

# Conservation of Energy

**General Principle**: Energy is conserved in every process.

$$\Delta E_{sys} = W + Q$$

**Isolated System**: No work or heat is exchanged with the surroundings.

$$\Delta E_{sys} = 0$$

**Point Particle**: A model that allows us to ignore the internal structure of an object.

$$\Delta K =  W_{\text{ext}}$$


---

# The Potential Energy Function

## Simple Harmonic Oscillator ($F_{s} = -kx$)

$$\Delta K = W_{s}$$

$$\dfrac{1}{2} m v_f^2 - \dfrac{1}{2} m v_i^2 = \int_{x_i}^{x_f} F_s dx = - \int_{x_i}^{x_f} kx dx$$

$$\dfrac{1}{2} m v_f^2 - \dfrac{1}{2} m v_i^2 = - \dfrac{1}{2} k x_f^2 + \dfrac{1}{2} k x_i^2$$

$$\dfrac{1}{2} m v_f^2 + \dfrac{1}{2} k x_f^2 = \dfrac{1}{2} m v_i^2 + \dfrac{1}{2} k x_i^2$$

$$K_f + U_{s,f} = K_i + U_{s,i}$$

$$U_s = \dfrac{1}{2} k x^2$$

---

# Clicker Question 13-1

The gravitation force near the Earth's surface is given by $F = -mg$. What is the potential energy function for this force? Choose $+z$ to be up.

1. $U = -mgz$
2. $U = mgz$
3. $U = -mgz + U_0$
4. $U = mgz + U_0$
5. None of the above

---

# Clicker Question 13-2

A model for a lattice chain acting on a electron is given by $F(x) = - F_0 \sin\left(\dfrac{2\pi x}{b}\right)$. What is the potential energy function for this force?

1. $U = -F_0 \cos\left(\dfrac{2\pi x}{b}\right)$
2. $U = F_0 \cos\left(\dfrac{2\pi x}{b}\right)$
3. $U = -\dfrac{F_0 b}{2\pi} \cos\left(\dfrac{2\pi x}{b}\right)$
4. $U = \dfrac{F_0 b}{2\pi} \cos\left(\dfrac{2\pi x}{b}\right)$
5. None of the above

---

# Clicker Question 13-3

I say "Stokes' Theorem" and you say...

1. HELL YEAH BROTHER
2. I'm not sure what that is
3. DEAR GOD WHY?!?!
