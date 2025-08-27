---
marp: true
theme: graph_paper
paginate: true

title: Day 21 - Oscillations
description: Slides for PHY 321 Spring 2025, Day 21: Oscillations
author: Prof. Danny Caballero <caball20@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, oscillations
url: https://dannycaballero.info/phy321msu/slides/day-21-oscillations.html
---

# Day 21 - Oscillations

Belousov–Zhabotinsky reaction $\rightarrow$

An example of [spatiotemporal patterns](https://en.wikipedia.org/wiki/Spatiotemporal_pattern)

![bg right width:600px](https://upload.wikimedia.org/wikipedia/commons/d/d9/The_Belousov-Zhabotinsky_Reaction.gif)

---

# Announcements

* Homework 3 and Midterm 1 are being graded
* Midterm 1 solutions are posted
* Homework 5 is due on Friday
* Homework 6 will be posted soon

---

# Seminars this week

## MONDAY, March 10, 2025
* **Condensed Matter Seminar** 4:10 pm,1400 BPS,  Dominique Laroche, University of Florida, *Tunable contributions from charge-rectification and momentum transfer to 1D Coulomb drag*

## TUESDAY, March 11, 2025
 
* **Theory Seminar**, 11:00am., FRIB 1200 lab, Gregory Potel, University of Seville, Spain, *Some recent trends in nuclear reaction theory for basic science and applications*
 
* **High Energy Physics Seminar**, 1:00 pm, 1400 BPS, Elena Pinetti, Flatiron Institute at the Simons Foundation in NYC, *Hunting axions with the James Webb Space Telescope*
 
---
 
# Seminars this week

## WEDNESDAY, March 12, 2025    
 
* **High Energy Physics Seminar**, 10:00 am, BPS 1400 BPS, Shruti Paranjape, Brown University, *Modern Methods to Understand Scattering Amplitudes*
* **Astronomy Seminar**, 1:30 pm, 1400 BPS, Jack Schulte & Sierra Casten, MSU, *TBD*
* ***PER Seminar**, 3:00 pm., BPS 1400, Camille Coffie, Lecturer, Department of Physics, Spelman College, *Examining how pejorative stereotypes about students shape their experiences in physics graduate programs**
* **FRIB Nuclear Science Seminar**, 3:30pm., FRIB 1300 Auditorium, Professor Caryn Palatchi of University of Indiana, Bloomington, *Precision Parity Violating Electron Scattering Experiments*

---

# Seminars this week
## THURSDAY, March 13, 2025
 
* **Colloquium**, 3:30 pm, 1415 BPS, Dong Lai, Cornell University,*Hot Jupiters and Super-Earths:  Spin-Orbit Dynamics in Exoplanetary Systems* 
**Refreshments and social half-hour in BPS 1400 starting at 3 pm**

## FRIDAY, March 14, 2025

* **FRIB IReNA Online Seminar**, 2:00pm., online via Zoom, Evan Kirby, University of Notre Dame, *Primordial r-process dispersions in globular clusters*
<https://msu.zoom.us/j/827950260>
Password: JINA

---

# Clicker Question 21-1

*My 14 year old asked me to ask you this question.*

Just a vibe check. How are the vibes after spring break?

1. The vibes are immaculate.
2. The vibes are good.
3. The vibes are okay.
4. The vibes are not good.
5. The vibes are terrible.

---

# Reminders

We were solving nonlinear first order differential equations of the homogenous type

$$\frac{dx}{dt} + f(x) = 0$$

where $f(x)$ is a nonlinear function of $x$. We found critical points where $dx/dt = 0$.

We demonstrated the utility of phase diagrams to visualize the behavior of solutions to nonlinear differential equations.

---

# Reminders

## Example $\dot{x} = \sin{x}$

![width:900px](../images/notes/week7/1st-order-ode-ex-1.png)

---

# Reminders 

We showed that we can learn something about systems we know little about at first using this approach (i.e., Firefly synchronization).

$$\dfrac{d\phi}{d\tau} = \mu - \sin(\phi)$$

$\mu = 0 \longrightarrow$ Synchronization always (no phase difference)

![width:600px](../images/notes/week8/cq19-1a.png)

---
# Reminders 

$\mu = 0.6 \longrightarrow$ Entrainment is possible (constant phase difference)

![width:600px](../images/notes/week8/cq19-1b.png)

---
# Reminders 

$\mu=1.2 \longrightarrow$ No entrainment ($\Omega > \omega$). Stimulus is too fast.

![width:600px](../images/notes/week8/cq19-1c.png)

---

# Reminders

We then moved on to 2D phase spaces, where we had a system of two first order equations:

$$\dot{x} = v$$
$$\dot{v} = f(x, v)$$

We focused on the simple harmonic oscillator as an example.

$$\ddot{x} = -x$$
$$\dot{x} = v$$

And we graphed it's phase space diagram.

---

# Reminders

Phase space diagram for a simple harmonic oscillator. The ellipses are curves of constant energy, $E$.

$$\dfrac{1}{2}mv^2 + \dfrac{1}{2}kx^2 = E$$
$$\dfrac{v^2}{2E/m} + \dfrac{x^2}{2E/k} = 1$$

![bg left width:500px](../images/notes/week8/cq19-6.png)

---

# Large Angle Pendulum

In the case of a large angle pendulum, we have a nonlinear differential equation:

$$\ddot{\theta} = -\frac{g}{L}\sin{\theta}$$

Here, we can write this as a system of two first order equations:

$$\dot{\theta} = \omega$$
$$\dot{\omega} = -\frac{g}{L}\sin{\theta}$$

We can then plot the phase space diagram for this system.

---

# Phase Diagram for a Large Angle Pendulum

![width:700px](../images/notes/week9/large_angle_pendulum.png)

---

# Clicker Question 21-2

Consider the phase diagram for a large angle pendulum. What do the upper and lower flows represent?

1. Unrealistic solutions.
2. Solutions that are not physical.
3. Solutions that are physical.
4. Solutions well beyond small angle.
5. More than one of these.

![bg right width:600px](../images/notes/week9/large_angle_pendulum.png)

---

# Oscillations

## Table Discussion: Why do we see oscillations so frequently in nature?

* Can you think of at least two different reasons from different perspectives?
* What are some non-simple harmonic oscillators you can think of?

**Click when you and your table are done.**

---

# Clicker Question 21-3

Consider the following notation:

$$z = x + iy$$
$$z^* = x - iy$$
$$zz^* = x^2 + y^2$$

Is this an idea you've seen before? How do you feel about it?
1. Yes, seen it and comfortable with it.
2. Yes, seen it but not comfortable with it.
3. No, never seen it, but I can learn it.

*There is no option for not learning, sorry.*

--- 

# Visualizing the Complex Solution

We constructed a solution of the form:

$$Ae^{i\omega t-\delta}$$

We can plot it in the complex plane and see the real and imaginary parts, and how they change in time.

---

# Visualizing the Complex Solution

We can plot the solution on the complex plane. For this, $\delta = \pi/4$, and the amplitude is $A=1$.

The solution rotates counterclockwise in the complex plane, following the rainbow from violet to red.

![bg right width:500px](../images/notes/week9/complex_plane.png)

---

# Projecting the Real Solution

The real part is just the projection of the complex solution onto the real axis. Just how far along the real axis is the solution at any given time. 

That looks like a time trace, but not quite, it's the real projection. The colors scheme is the same as before.

![bg right width:500px](../images/notes/week9/real_part.png)


---

# The Time Trace of the Solution

We just flip the axes to produce the time trace that you are used to seeing. The color scheme is the same as before.

![bg right width:500px](../images/notes/week9/time_trace.png)