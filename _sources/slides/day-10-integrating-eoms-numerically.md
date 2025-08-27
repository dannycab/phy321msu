---
marp: true
theme: graph_paper
paginate: true

title: Day 10 - Integrating EOMs Numerically
description: Slides for PHY 321 Spring 2025, Day 10: Integrating EOMs Numerically
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion, numerical integration, euler
url: https://dannycaballero.info/phy321msu/slides/day-10-integrating-eoms-numerically.html
---

# Day 10 - Integrating EOMs Numerically

![bg right width:600px](../images/notes/week4/numerical_integration.png)


---

# Announcements

* **PERMANENT CHANGE:** OFFICE HOURS
    * DC Office hours 10:00-12:00 on Fridays (No Monday office hours)
* **CHANGES THIS WEEK** (DC has a conflict):
    * Office Hrs on Zoom today 16:00-17:00 <https://msu.zoom.us/j/92295821308>
    * 15:00-16:00 on Friday -> 14:00-15:00 on Friday

---

## Seminars this week

**Astronomy Seminar**, Wednesday Feb 5th at 1:30pm in 1400 BPS
* 	Lia Corrales, Univ. of Michigan, *The cosmic journey of the elements, from dust to life*

**Physics & Astronomy Colloquium**, Thursday Feb 6th at 3:30pm in 1415 BPS
* Andreas Jung, Purdue University, *Entangled Titans:  unraveling the mysteries of Quantum Mechanics with top quarks*

**Reminder: email me your extra credit seminar write-ups**

---

# Goals for this week

![bg right width:600px](../images/notes/week4/numerical_integration.png)

* Establish a model for drag forces
* Develop an understanding of the process for modeling forces
* Produce equations of motion that can be investigated
* Start probing the behavior of these systems with math and computing

---

# Model-to-EOM Pipeline for Classical Mechanics

1. ✅ Develop conceptual description of the system; make justifiable assumptions
2. ✅ Using a framework of physics (i.e., Newton's Laws, Lagrangian Dynamics), develop a mathematical model of the system
3. ✅ Produce the equations of motion (EOM) by following the framework (i.e., ordinary differential equations)
4. 😵 **Solve for trajectories of the system** (e.g., $x(t)$, $v(t)$, $v(x)$)

## Most EOMs are nonlinear

## We need approximate methods to produce trajectories
---



# Clicker Question 6-5

For the system of **Quadratic Drag in 1D**, we found a solution for the velocity as a function of time, with $v = 0$ at $t = 0$.

$$v(t) = v_{term}\tanh(gt/v_{term})$$ 

where $v_{term} = \sqrt{mg/c}$. What happens when $t \rightarrow \infty$?

1. The object stops moving.
2. The object travels at a constant velocity.
3. The object travels at an increasing velocity.
4. The object travels at a decreasing velocity.
5. I'm not sure.

---

# Clicker Question 6-6

For the gravitational interaction, I want to compute the force acting on body B, located at $\vec{r}_B$, by body A, located at $\vec{r}_A$.

The gravitational force is given by:

$$\vec{F} = -G\dfrac{m_1 m_2}{r^2}\hat{r}$$

What is the appropriate form of $\vec{r}$?

1. $\vec{r} = \vec{r}_A - \vec{r}_B$
2. $\vec{r} = \vec{r}_B - \vec{r}_A$
3. Either is ok

--- 

# Clicker Question 6-7

We found that the equation of motion for the spring-mass system was:

$$\ddot{x} = -\dfrac{k}{m}x = -\omega^2 x$$

Your friends have proposed the following **general solutions**:

$$1.\;x(t) = A\cos(\omega t) \qquad 2.\;x(t) = B\sin(\omega t) \qquad 3.\;x(t) = A\cos(\omega t) + B\sin(\omega t) $$
$$ 4.\;x(t) = A\cos(\omega t + \phi) \qquad 5.\;x(t) = B\sin(\omega t + \phi) \qquad 6.\;x(t) = A\cos(\omega t + \phi) + B\sin(\omega t + \phi) $$

How many of them are correct? 
(1) Only one (2) Two (3) Three
(4) Four (5) All of them




