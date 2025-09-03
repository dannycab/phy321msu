---
marp: true
theme: graph_paper
paginate: true

title: Day 04 - Mathematical Preliminaries
description: Slides for PHY 321 Spring 2025, Day 04: Mathematical Preliminaries
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-04-mathematical-prelims.html
---

# Day 04 - Mathematical Preliminaries

![bg right:60%](./images/vector.jpeg)

---

# Announcements

* Homework 1 is due this Friday
* Homework 2 is posted now
* Help sessions start this week
    * DC Friday at 2-4pm (1248 BPS)
* Mihir (ULA) will host additional help hours soon

---

# Seminars this week (Wednesday)


## WEDNESDAY, September 3, 2025
 
Astronomy Seminar, 1:30 pm, 1400 BPS, In Person and Zoom, Host~
Speaker:   Group Introductions
Title:
Zoom Link: https://msu.zoom.us/j/887295421?pwd=N1NFb0tVU29JL2FFSkk0cStpanR3UT09
Meeting ID: 887-295-421
Passcode: 002454

---

# Seminars this week (Wednesday)


## WEDNESDAY, September 3, 2025

Nuclear Science Seminar, 3:30Pm., FRIB 1300 lab in person and online via Zoom
Speaker: Mark Spieker, Florida State University
Title: Experimental studies of the pygmy dipole resonance
Zoom Link: https://msu.zoom.us/j/95277003505?pwd=hTILu1oLqmhTCU7jlVKFTlXXZBmuGb.1
Meeting ID: 952 7700 3505
Passcode: 404830

---

# Goals for this week

## Be able to answer the following questions.

* What are the essential physics models for single particles?
* How do we setup problems in classical mechanics?
* What mathematics do we need to get started?
* How do we solve the equations of motion?

---

# Reminders from Day 03

* In a Newtonian world, we start from a vector description of motion
* Differential equations are mathematical models that describe the motion of particles
* We can use different methods to solve these differential equations

**i-Clicker: https://join.iclicker.com/QTEC**

--- 

# Projectile Motion

$$\mathbf{a} = \langle a_x, a_y \rangle$$

$$x_f = x_i + v_{x,i}t + \dfrac{1}{2}a_x t^2$$

$$y_f = y_i + v_{y,i}t + \dfrac{1}{2}a_y t^2$$

![bg left:60%](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/ParabolicWaterTrajectory.jpg/960px-ParabolicWaterTrajectory.jpg)

---

# Clicker Question 4-1

For this fountain, what is the best guess for the acceleration ($\mathbf{a} = ??$) experienced by a fluid particle? <br> *Assume $y$ is positive upward; $x$ is positive to the right.*

1. $a_x \neq 0, a_y = g$
2. $a_x = 0, a_y = g$
3. $a_x \neq 0, a_y = -g$
4. $a_x = 0, a_y = -g$
5. Something else


![bg left:40%](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/ParabolicWaterTrajectory.jpg/960px-ParabolicWaterTrajectory.jpg)

---

# Clicker Question 4-2

The average velocity for a macroscopic time step $\Delta t = t_f - t_i$ is given by:

$$\mathbf{v}_{avg} = \dfrac{\Delta \mathbf{r}}{dt}$$

where $\Delta \mathbf{r} = \mathbf{r}_f - \mathbf{r}_i$. At what time do we estimate the average velocity occurs?

1. $t_i$
2. $t_f$
3. Sometime between $t_f$ and $t_i$
4. $\dfrac{t_f-t_i}{2}$


---

# Clicker Question 4-3

Consider the generic position vector $\vec{R}$ for a particle in 2D space. Which of the following describes the direction of the vector in plane polar coordinates ($r$, $\phi$)?

1. $\hat{R}$
2. $\hat{r}$
3. $\hat{\phi}$
4. Some combination of $\hat{r}$ and $\hat{\phi}$
5. I'm not sure.

---

# Group Discussion 4-1

We found the following expression for the equation of motion of a falling ball subject to air resistance:

$$m \ddot{y} = +mg - b \dot{y} - c \dot{y}^2$$

What are the units of the constants $b$ and $c$?

<!-- ---

# Group Discussion 4-2

Consider the generic position vector $\vec{R}$ for a particle in 2D space. Find the velocity vector $\vec{V}$ for the particle in Cartesian coordinates ($x$, $y$).

## What happens in plane polar coordinates? 

$$\vec{R} = r \hat{r} + \phi \hat{\phi}$$

Note: 

$$\hat{r} = \cos(\phi) \hat{x} + \sin(\phi) \hat{y}$$

$$\hat{\phi} = -\sin(\phi) \hat{x} + \cos(\phi) \hat{y}$$ -->

