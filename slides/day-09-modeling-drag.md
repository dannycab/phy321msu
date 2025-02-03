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

![bg right width:600px](../images/notes/week3/quack.png)

---

# Announcements

* We are behind on grading the first assignment
* Homework 2 is due today
    * Homeworks are due at 23:59
    * Gradescope is open until Sunday at 9:00
* Homework 3 is posted
    * Due next Friday
    * Also open until next Sunday at 9:00

---

# Announcements

* All handwritten notes are now posted.
* Reminder: email me your extra credit seminar write-ups.
* **DC Office Hours today on zoom from 15:00-16:00**
    * https://dannycab.github.io/meet

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
