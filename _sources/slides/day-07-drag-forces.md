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
- Video recordings have continued to fail.
    - Zoom password: phy321
- Updated office hours (Danny-DC; Elisha-EA):
  - Monday 4-5pm (DC) - change?
  - Tuesday 5-6pm (EA)
  - Wednesday 4-5pm (DC)
  - Thursday 5-6pm  (EA)
  - Friday 10-12pm (DC then EA); 3-4pm (DC)

---

# Seminars this week

WEDNESDAY, January 29, 2025    
                                     
- Astronomy Seminar, 1:30 pm, 1400 BPS, Michiel Lambrechts, Univ. of Copenhagen, *Planet formation*
- FRIB Nuclear Science Seminar, 3:30pm., FRIB 1300 Auditorium, Brenden Longfellow of Lawrence Livermore National Laboratory, *From Tensor Current Limits to Solar Neutrinos: 8Li and 8B Studies with the Beta-decay Paul Trap*

---



# Goals for Week 3

- Be able to answer the following questions.
    - What is Mathematical Modeling?
    - What is the process for analyzing these models?
- Be able to solve "Simple" Motion Problems with Newton's Laws.

---

# Clicker Question 6-2

Assuming a **linear model** for Air Resistance $\sim bv$, we obtained this EOM for a falling ball:

$$\ddot{y} = -g + \frac{b}{m}\dot{y}$$


What happens when $\ddot{y} = 0$?
1. The ball stops moving ($v = 0$).
2. The ball reaches a velocity of $mg/b$.
3. The ball reaches a terminal velocity.
4. I'm not sure.

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








