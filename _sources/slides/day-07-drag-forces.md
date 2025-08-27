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

# Announcements

- Homework 2 is due Friday
- Video recordings will cease; I will try to record my tablet writing next week.
    - Class can still join zoom with password: phy321
- Updated office hours (Danny-DC; Elisha-EA):
  - Monday 4-5pm (DC) - change?
  - Tuesday 5-6pm (EA)
  - Wednesday 4-5pm (DC)
  - Thursday 5-6pm  (EA)
  - Friday 10-12pm (DC then EA); 3-4pm (DC)

---

# Calendar changes and apologies

- I'm very behind on class prep. And I'm very distracted right now.
- The notes for next week will be posted by Friday. 
  - If you need anything or I'm missing, just drop me a note. I probably just missed it.
- There will be no homework 9, and there will be no new material for the last week of class.
  - Instead, that week will be final prep for your projects that will be due Monday of finals week at midnight.
  - More details soon, but we will also use homework and midterms to help you make progress on your final projects.


---

# Seminars this week

WEDNESDAY, January 29, 2025    
                                     
- Astronomy Seminar, 1:30 pm, 1400 BPS, Michiel Lambrechts, Univ. of Copenhagen, *Planet formation*
- FRIB Nuclear Science Seminar, 3:30pm., FRIB 1300 Auditorium, Brenden Longfellow of Lawrence Livermore National Laboratory, *From Tensor Current Limits to Solar Neutrinos: 8Li and 8B Studies with the Beta-decay Paul Trap*

---

# Tomorrow's Seminar
![w:1000px](../images/notes/week3/trans_rally.png)

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

# Clicker Question 6-2

Assuming a **linear model** for Air Resistance $\sim bv$, we obtained this EOM for a falling ball:

$$\ddot{y} = -g + \frac{b}{m}\dot{y}$$


What happens when $\ddot{y} = 0$?
1. The ball stops moving ($v = 0$).
2. The ball reaches a velocity of $mg/b$.
3. The ball reaches a terminal velocity.
4. I'm not sure.









