---
marp: true
theme: king
paginate: true

title: Day 04 - Vector Reminders
description: Slides for PHY 321 Spring 2025, Day 04: Vector Reminders
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-04-vector-reminders.html
---

# Day 04 - Vector Reminders

![bg right:60%](./images/vector.jpeg)

---

# Announcements

* Homework 1 is due this Friday
* Homework 2 is posted now
* Help sessions start this week
    * DC today at 4pm; Friday at 3pm (1248 BPS)

---

# Seminars this week (Tuesday and Wednesday)

TUESDAY, January 21, 2025

* **High Energy Physics Theory Seminar**
    * 11:00am, FRIB 1200 lab; Speaker: **Alexei Bazavov**, MSU-CMSE/PA
    * Title: *Lattice QCD: From classical computation to quantum simulation*
           
WEDNESDAY, January 22, 2025    
                                     
* **Astronomy Seminar**
    * 1:30 pm, 1400 BPS; Speaker: **Allyson Bieryla**, CfA | Harvard & Smithsonian
    * Title:  *Exoplanets and Solar Eclipses for Research and Community Engagement*

---

# Seminars this week (Wednesday, cont.)   

* **PER Seminar**
    * 3:00 pm., BPS 1400; Speaker: **Justin Gambrell**, Assistant Professor, Department of Computational Mathematics, Science, and Engineering, Michigan State University - **MSU PA ALUMNUS**
    * Title: *Computational Thinking Assessment for Introductory Physics: Design, Implementation, and Future Directions*

* **FRIB Nuclear Science Seminar**
    * 3:30pm., FRIB 1300 Auditorium; Speaker: Calem Hoffman of Argonne National Laboratory
    * Title:  The Influence of Near-Threshold States on Nuclear Observables

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

--- 

# Clicker Question 4-1

Consider the generic position vector $\vec{R}$ for a particle in 2D space. Which of the following describes the direction of the vector in plane polar coordinates ($r$, $\phi$)?

1. $\hat{R}$
2. $\hat{r}$
3. $\hat{\phi}$
4. Some combination of $\hat{r}$ and $\hat{\phi}$
5. I'm not sure.

---

# Group Discussion 4-1

Consider the generic position vector $\vec{R}$ for a particle in 2D space. Find the velocity vector $\vec{V}$ for the particle in Cartesian coordinates ($x$, $y$).

## What happens in plane polar coordinates? 

$$\vec{R} = r \hat{r} + \phi \hat{\phi}$$

Note: 

$$\hat{r} = \cos(\phi) \hat{x} + \sin(\phi) \hat{y}$$

$$\hat{\phi} = -\sin(\phi) \hat{x} + \cos(\phi) \hat{y}$$