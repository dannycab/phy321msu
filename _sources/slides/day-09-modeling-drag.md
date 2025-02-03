---
marp: true
theme: graph_paper
paginate: true

title: Day 09 - Modeling Drag
description: Slides for PHY 321 Spring 2025, Day 09: Modeling Drag
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-09-modeling-drag.html
---

# Day 09 - Modeling Drag

![bg right width:600px](../images/notes/week4/paramecium-swimming.png)

Somersault of Paramecium in extremely confined environments ->

source: <https://www.nature.com/articles/srep13148>

---

# Announcements

* All hand-written notes are now posted
* Week 5 notes and HW 4 will be posted by tomorrow night
* **PERMANENT CHANGE:** OFFICE HOURS
    * DC Office hours 10:00-12:00 on Fridays (No Monday office hours)
* **CHANGE THIS WEEK** (DC has a conflict):
    * 15:00-16:00 on Friday -> 14:00-15:00 on Friday

---

## Seminars this week

**CMP Seminar**, Monday Feb 3rd at 4:10pm in 1400 BPS
* Xiaoming Mao, University of Michigan, *Topological mechanics in Maxwell lattices and continuum*

**Astronomy Seminar**, Wednesday Feb 5th at 1:30pm in 1400 BPS
* 	Lia Corrales, Univ. of Michigan, *The cosmic journey of the elements, from dust to life*

**Physics & Astronomy Colloquium**, Thursday Feb 6th at 3:30pm in 1415 BPS
* Andreas Jung, Purdue University, *Entangled Titans:  unraveling the mysteries of Quantum Mechanics with top quarks*

**Reminder: email me your extra credit seminar write-ups**

---

# Goals for this week

![bg right width:600px](../images/notes/week4/paramecium-swimming.png)

* Establish a model for drag forces
* Develop an understanding of the process for modeling forces
* Produce equations of motion that can be investigated
* Start probing the behavior of these systems with math and computing

---

# Reminders

## Force Models

We have been modeling the drag force using a functional dependence on velocity.

$$\vec{F}_{\text{drag}} = -f(v)\hat{v}$$

where $f(v)$ is a function of velocity.

We established (in 1D) there are two common forms of drag force:

$$f(v) = bv \quad \text{Linear Drag}$$

$$f(v) = cv^2 \quad \text{Quadratic Drag}$$

---

# Reminders

## Equations of Motion

The next step is to use Newton's 2nd Law to write the equations of motion for the system. We found those equation of motion to be:

$$m\dot{v} = -f(v)$$

where $f(v)$ is the drag force. So for each form of drag we have:

$$\dot{v} = g-\frac{b}{m}v \quad \text{Linear Drag}$$

$$\dot{v} = g-\frac{c}{m}v^2 \quad \text{Quadratic Drag}$$

---

# Reminders

## Trajectories

We can integrate these equations of motion to find the velocity as a function of time. We found:

$$v(t) = v_{\text{t,lin}}\left(1-e^{-\frac{bt}{m}}\right) \quad \text{Linear Drag}$$

$$v(t) = v_{\text{t,quad}}\tanh\left(\frac{gt}{v_{\text{t,quad}}}\right) \quad \text{Quadratic Drag}$$

where $v_{\text{t,lin}} = \frac{mg}{b}$ for linear drag and $v_{\text{t,quad}} = \sqrt{\frac{mg}{c}}$ for quadratic drag.

---

# Our Current Investigatory Process

## The Model-to-Trajectory Pipeline

1. Model the forces acting on the system
2. Write the equations of motion using Newton's 2nd Law
3. Solve the equations of motion to find trajectories

This is incomplete. We will need to learn how stability, critical points, and phase space can help us understand the behavior of these systems.

We have also only done step 3 analytically. We will need to learn how to use computing to investigate these systems.

---


# Clicker Question 6-3

For the system of **Linear Drag in 1D**, we found a solution for the velocity as a function of time, with $v = 0$ at $t = 0$.
$$v(t) = v_{term}\left(1-e^{-\dfrac{bt}{m}}\right)$$

where $v_{term} = \sqrt{\frac{mg}{b}}$. 

---

![bg right w:100%](../images/notes/week3/cq6-3.png)


# CQ 6-3

**Which sketch could be correct for the velocity of the ball?**

---

# Clicker Question 6-4

For the system of **Quadratic Drag in 1D**, we found a solution for the velocity as a function of time, with $v = 0$ at $t = 0$.

$$v(t) = v_{term}\tanh(gt/v_{term})$$

where $v_{term} = (mg/c)^{1/2}$. Do the units make sense? What are the units of $\left[gt/v_{term}\right]$? 
1. Yes, the units for $\left[gt/v_{term}\right]$ are $m/s$;both sides have the same units.
2. No, the units for $\left[gt/v_{term}\right]$ are m/s; each side has different units.
3. Yes, the units for $\left[gt/v_{term}\right]$ are unit-less; both sides have the same units.
4. No, the units for $\left[gt/v_{term}\right]$ are unit-less; each side has the different units.

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
