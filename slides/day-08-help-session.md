---
marp: true
theme: graph_paper
paginate: true

title: Day 08 - Help Session
description: Slides for PHY 321 Spring 2025, Day 08: Help Session
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-08-help-session.html
---

# Day 08 - Help Session

![bg right width:600px](../images/notes/week3/quack.png)

---

# Announcements

* Reminder: email me your extra credit seminar writeups.
* **DC Office Hours today from 14:00-16:00**
    * And on zoom: https://dannycab.github.io/meet

---

# Exercise 3 (10 pt), Drag force

We can observe that the models for linear and quadratic drag forces are given by:

$$f_{lin} = 3\pi \eta D v \qquad f_{quad} = \kappa \rho A v^2$$

where $D$ is the "length scale" of the object (e.g., the diameter of the sphere), $\eta$ is the viscosity of the fluid, $\rho$ is the density of the fluid, $A$ is the cross-sectional area of the object, and $\kappa$ is a constant of order unity (larger for flat and blunt bodies; smaller for streamlined bodies).

---

# Parts 3a and 3b 

* The Reynolds number is defined as $Re = \rho v D / \eta$. What is the physical meaning of this number? For a spherical object, show that the ratio of the quadratic drag force to the linear drag force is given by $f_{quad}/f_{lin} = Re/48$. Use this to explain the physical meaning of the Reynolds number. **Note: you may assume that $\kappa = 0.25$ for a sphere.**
* Explain a situation where there would be a low Reynolds number. What about a high Reynolds number? Estimate the Reynolds number for a falling rain drop, a parachutist, a car, and a plane.

---

# Exercise 5

Finding and exploring equations of motion is the central enterprise of classical mechanics. You will encounter (and derive) many equations you have not seen before, and you will need to explain them. Consider a hypothetical one-dimensional system where a mass $m$ has a speed of $v_0$ and coasts along the x-axis. The surrounding medium produces a drag force that is modeled using:

$$F(v) = -c v^{3/2}.$$

When the force is a pure function of velocity, using the technique called separation of variables on Newton's 2nd Law, we can find the velocity as a function of time.

---

# Exercise 5

We can separate variables and write:

$$F(v) = m a = m \dfrac{dv}{dt}$$


Divide both sides by $F(v)$ and multiply both sides by $dt$:

$$dt = \dfrac{m}{F(v)}dv$$

And then, given starting (initial) conditions, we integrate both sides to find an expression for $t$ as a function of $v$.

$$t = m \int_{v_0}^v \dfrac{dv'}{F(v')}$$

---

# Parts 5a and 5b

* For the given force above, write the equation of motion in a form: $\dfrac{m dv}{F(v)} = dt$. Integrate both sides to find an expression for the velocity $v$ as a function of $t$ ($v(t)$ not $t(v)$). 
* Check your answer by looking at the limits of its behavior. Does it agree with your intuition?
