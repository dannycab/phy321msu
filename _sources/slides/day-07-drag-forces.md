---
marp: true
theme: graph_paper
paginate: true

title: Day 07 - Drag Forces
description: Slides for PHY 321 Spring 2025, Day 07: Drag Forces
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, drag, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-07-drag-forces.html

---

# Day 07 - Drag Forces

![bg right width:100%](../images/notes/week3/drag.png)

---

# Big Announcement

---

# MSU Tenure System Faculty Union Recognized

## What does that mean for you?

* Faculty can bargain with the university for what's needed to meet our educational needs
- For example, there's more of y'all every year, but not more of us.
![bg right 90%](./images/union_square.png)

---

# Announcements

- Homework 2 is due Friday; late after Sunday 11:59pm (always)
- Homework 3 is now posted; due next Friday; late after Sunday...
- Office hours, for now (Mihir-MN; Danny-DC):
  - Tuesday 6-8pm (MN, Zoom)
  - Thursday 6-8pm (MN, Zoom)
  - Friday 2-4pm (DC, 1248 BPS)
- Zoom Link: <https://msu.zoom.us/j/96882248075> 
    - password: `phy321msu`
- Friday's Class: **Will work Exercises 3a, 5a, & 5b form HW 3 together + questions**

---

# Seminars this week


## WEDNESDAY, September 10, 2025    
 
                                    
Astronomy Seminar, 1:30 pm, 1400 BPS, In Person and Zoom, Host~ 
Speaker: Rachael Roettenbacher,  University of Michigan
Title: Imaging Spotted Stars for an Improved Understanding of Stars and Exoplanets
Zoom Link: https://msu.zoom.us/j/887295421?pwd=N1NFb0tVU29JL2FFSkk0cStpanR3UT09
Meeting ID: 887-295-421
Passcode: 002454
 
---

# Seminars this week


## WEDNESDAY, September 10, 2025 
 
FRIB Nuclear Science Seminar, 3:30pm., FRIB 1300 Auditorium and online via Zoom 
Speaker: Suzanne Lapi of the University of Alabama at Birmingham
Title: Development of new isotopes for theranostic applications
Please see website for full abstract.
Please click the link below to join the webinar:
Join Zoom: https://msu.zoom.us/j/96485010083?pwd=O0rXwspn80aYGEI06QEZag6Ao4siq7.1
Meeting ID: 964 8501 0083
Passcode: 261744
 
---

# Seminars this week

## THURSDAY, September 11, 2025
 
Colloquium, 3:30 pm, 1415 BPS, in person and zoom.  Host ~ 
Refreshments and social half-hour in BPS 1400 starting at 3 pm
Speaker: Laura Chomiuk,  MSU
Title:  Fall 2025 Physics and Astronomy Kickoff
Background: 
For more information and to schedule time with the speaker, see the colloquium calendar at https://pa.msu.edu/news-events-seminars/colloquium-schedule.aspx
Zoom Link: https://msu.zoom.us/j/94951062663
Password: 2002  Or complete link:  https://msu.zoom.us/j/94951062663?pwd=c48uM25P9UsRVuR74rkOioOWgpoxgC.1
 
 
 
---

# Seminars this week

## FRIDAY, September 12, 2025 
 
 
QuIC Seminar, 12:30pm, -1:30pm, 1300 BPS, In Person  
Speaker: Jean Paul Sadia, MSU
Title: Introduction to Quantum Information and Computation
Full Scheule is at: https://sites.google.com/msu.edu/quic-seminar/
For more information, reach out to Ryan LaRose
 
---

# Seminars this week

## FRIDAY, September 12, 2025 

IReNA Online Seminar, 2:00 pm, via Zoom.
Hosted by: Artemis Tsantiri (University of Regina, Canada)
Speaker:  Lorenzo Roberti, INFN-LNS, Italy/Konkoly, Observatory Hungary
Title: Carbon-Oxygen Shell Mergers in Massive Stars
Zoom Link: https://msu.zoom.us/j/827950260
Password: JINA

---

# AI Policy Proposals

* **Proposal 1:** We adopt a policy that does not allow AI use at all.
* **Proposal 2:** We adopt a policy that allows AI use for brainstorming, help, and editing. 
* **Proposal 3:** We adopt a policy that allows AI for use in nearly any way.
* **Proposal 4:** We adopt a policy that allows AI for use in any way with no documentation required.

---

# Updated AI Policy

![](./images/ai_policy_vote_f2025.png)

---

# Proposal 2

**We adopt a policy that allows AI use for brainstorming, help, and editing.**
- AI cannot be used for direct answers or completion of assignments.
- We expect documentation of AI use, but it can be informal.
- Violations are discussed with Danny; the first violation requires a redo of the assignment, and repeated violations result in a failing grade.

**Received 75% of first choice votes**

---


# Goals for Week 3

- Be able to answer the following questions.
    - What is Mathematical Modeling?
    - What is the process for analyzing these models?
- Be able to solve "Simple" Motion Problems with Newton's Laws.

---

# Our man, Reynolds

![bg right width:300px](../images/notes/week3/stokes.png)

- The Reynolds number is a dimensionless quantity.
- It is a ratio of inertial forces to viscous forces.

$$Re = \frac{\rho v L}{\mu}$$

* $\rho$ - density of the fluid
* $v$ - velocity of the object
* $L$ - characteristic length
* $\mu$ is the dynamic viscosity

---

# Our man, Reynolds

![bg right width:300px](../images/notes/week3/stokes.png)

BTW, this is not a photo of Reynolds. 
- This is Stokes. 
  - He developed the concept of the Reynolds number. 
  - Reynolds "popularized" it according to the Wikipedia.

$$Re = \frac{\rho v L}{\mu}$$

**Discussion:** What kinds of systems have a high/low Reynolds number?

---

# Clicker Question 6-2a

I made a mistake explaining our linear drag model derivation. 

Consider a ball falling down with a coordinate system such that $y$ is positive downward (as before). Which of the following is correct for the differential equation:

1. $m\ddot{y}=-mg+bv_y$
2. $m\ddot{y}=-mg-bv_y$
3. $m\ddot{y}=+mg+bv_y$
4. $m\ddot{y}=+mg-bv_y$

**Think about the SIGN of $v_y$; it's a component not a speed!**

---

# Clicker Question 6-2b

Assuming a **linear model** for Air Resistance $\sim bv$, we can obtain this EOM for the velocity a falling ball, after *separation of variables*:

$$\dfrac{dv_y}{v_y - v_{term}} = -\frac{b}{m}dt$$

 
Assume we try to integrate this equation from $v_y = v_{y0}$ at $t=0$ to $v_y(t)$ at time $t$.

**Write the integral (on both sides) that is needed to solve this equation.**

*This integral setup is common in physics derivations with ODEs; provided we can find an anti-derivative.*

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

where $v_{term} = (mg/c)^{1/2}$. Do the units make sense? What are the units $\left[gt/v_{term}\right]$? 
1. Yes,**$v$ and $(mg/c)^{1/2}$ have the same units**; the units for $\left[gt/v_{term}\right]$ are m/s.
2. No, **$v$ and $(mg/c)^{1/2}$ have different units**; the units for $\left[gt/v_{term}\right]$ are m/s.
3. Yes, **$v$ and $(mg/c)^{1/2}$ have the same units**; the units for $\left[gt/v_{term}\right]$ are unit-less.
4. No, **$v$ and $(mg/c)^{1/2}$ have different units**; the units for $\left[gt/v_{term}\right]$ are unit-less.

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









