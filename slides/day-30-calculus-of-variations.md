---
marp: true
theme: graph_paper
paginate: true

title: Day 30 - Calculus of Variations
description: Slides for PHY 321 Spring 2025, Day 30: Calculus of Variations
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, calculus of variations, action principle, Lagrangian mechanics
url: https://dannycaballero.info/phy321msu/slides/day-30-calculus-of-variations.html
---

# Day 30 - Calculus of Variations

![bg right width:600px](../images/notes/week11/soap_bubble.png)

---

# Announcements

* Midterm 2 is posted
* Look for feedback from DC on projects

---

# Clicker Question 30-1

The generic segment, $ds$, of a curve in 2D Cartesian coordinates is given by 

$$ds = \sqrt{(dx)^2 + (dy)^2}$$

The integral of $ds$ from $s_1$ to $s_2$ gives the length of the curve, $l$. What is the correct expression for $l$?

1. $l = \int_{s_1}^{s_2} ds$
2. $l = \int_{s_1}^{s_2} \sqrt{(dx)^2 + (dy)^2}$
3. $l = \int_{s_1}^{s_2} \sqrt{1 + (dy/dx)^2} \, dx$
4. $l = \int_{s_1}^{s_2} \sqrt{(dx/dy)^2 + 1} \, dy$
5. More than one of the above

---

# Clicker Question 30-2

I can explain why:

$$\int_{s_1}^{s_2} f((Y(x), Y'(x), x) \, dx > \int_{s_1}^{s_2} f((y(x), y'(x), x) \, dx$$

where $Y(x) = y(x) + \alpha \eta(x)$, the true path plus an error term.

1. Yes, I can explain why
2. I think I can explain why
3. I'm having trouble seeing why
4. I don't think I can explain why

---

# Clicker Question 30-3

For the function $Y(x) = y(x) + \alpha \eta(x)$, where $y(x)$ is the true path, $\eta(x)$ is a small error term, and $\alpha$ is a small parameter, what is the derivative of $Y(x)$ with respect to $\alpha$?

$$\frac{dY}{d\alpha} = ?$$

1. $y(x)$
2. $\eta(x)$
3. $\eta'(x)$
4. $\alpha \eta(x)$
5. $y'(x) + \alpha \eta'(x)$

---

# Clicker Question 30-4

For the function $Y'(x) = y'(x) + \alpha \eta'(x)$, what is the derivative of $Y'(x)$ with respect to $\alpha$?

$$\frac{dY'}{d\alpha} = ?$$

1. $y'(x)$
2. $\eta'(x)$
3. $\eta''(x)$
4. $\alpha \eta'(x)$
5. $y''(x) + \alpha \eta''(x)$

---

# Clicker Question 30-5

The "surface term" that we computed for $\int_{s_1}^{s_2} \eta'(x) \frac{df}{dy'} dx$ is:

$$\left[\eta(x)\dfrac{df}{dy'}\right]_{x_1}^{x_2}=0$$

I can explain why this surface term is equal to zero:

1. Yes, I can explain why
2. I think I can explain why
3. I'm having trouble seeing why
4. I don't think I can explain why
5. I don't know what a surface term is

---