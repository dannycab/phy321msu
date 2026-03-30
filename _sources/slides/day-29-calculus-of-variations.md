---
marp: true
theme: graph_paper
paginate: true

title: Day 29 - Calculus of Variations
description: Slides for PHY 321 Spring 2026, Day 29: Calculus of Variations
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, calculus of variations, action principle, Lagrangian mechanics
url: https://dannycaballero.info/phy321msu/slides/day-29-calculus-of-variations.html
---

<style>
  :root {
    --color-spartan-green: #18453B;
    --color-msu-gold: #C1B000;
    --color-light-gray: #f5f5f5;
    --color-dark-text: #1a1a1a;
    --color-accent-green: #2d5f4f;
  }
  
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #ffffff;
    color: var(--color-dark-text);
  }
  
  h1, h2, h3 {
    color: var(--color-spartan-green);
    font-weight: 500;
  }
  
  h1 {
    font-size: 2.2rem;
    margin-bottom: 0rem;
  }
  
  h2 {
    font-size: 1.55rem;
    margin-bottom: 1.0rem;
    border-bottom: 4px solid var(--color-spartan-green);
    padding-bottom: 0.5rem;
  }
  
  h3 {
    font-size: 1.15rem;
    margin-top: 1rem;
    margin-bottom: 0.75rem;
  }
  
  section {
    padding: 2rem;
    background-color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }

  .equation {
    background-color: var(--color-light-gray);
    padding: 1.5rem;
    border-left: 4px solid var(--color-msu-gold);
    margin: 1.5rem 0;
    font-size: 1.3rem;
    text-align: center;
    color: var(--color-dark-text);
  }

  p {
    font-size: 1.15rem;
    line-height: 1.4;
    margin-bottom: 0.5rem;
  }
  
  ul, ol {
    font-size: 1.15rem;
    line-height: 1.4;
    margin-left: 0.5rem;
  }

  ul ul, ol ol, ul ol, ol ul {
    margin-left: 0.1rem;
  }
  
  li {
    margin-bottom: 0rem;
    line-height: 1.4;
  }
  
  strong {
    color: var(--color-spartan-green);
    font-weight: 600;
  }
  
  em {
    color: var(--color-accent-green);
  }

  .highlight {
    background-color: var(--color-light-gray);
    padding: 1.5rem;
    border-left: 4px solid var(--color-spartan-green);
    margin: 1.5rem 0;
  }

  .activity {
    background-color: #fff8e1;
    border: 2px solid var(--color-msu-gold);
    padding: 1.25rem;
    border-radius: 6px;
    margin: 1rem 0;
  }

  code {
    background-color: var(--color-light-gray);
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-size: 1.0rem;
  }

  .footnote {
    font-size: 0.8rem;
    color: #999;
    margin-top: 1.5rem;
    border-top: 1px solid #ddd;
    padding-top: 0.75rem;
  }
</style>

<!--
_class: title
_backgroundColor: #ffffff
_color: #18453B
-->

# Day 29 - Calculus of Variations

![bg right width:600px](../images/notes/week11/soap_bubble.png)

---

# Announcements

* Midterm 2 is posted (Due 10 April 2026 at 11:59 pm)
* **Office Hours this week:** Midterm 2 Help

---

## Calculus of Variations

Variational calculus is a mathematical method to find functions that optimize a certain quantity. We will use variational calculus to derive the **Euler-Lagrange equations** for a set of **generalized coordinates** (i.e., $q,\dot{q}$). This is fundamental to Lagrangian mechanics.

$$L(q, \dot{q}, t) = T(\dot{q}) - U({q})$$

$$S = \int_{t_1}^{t_2} L(q, \dot{q}, t) \, dt \qquad \delta S = 0 $$

$$ \dfrac{d}{dt} \left( \dfrac{\partial L}{\partial \dot{q}} \right) - \dfrac{\partial L}{\partial q} = 0 $$



---

## Clicker Question 29-1

The generic segment, $ds$, of a curve in 2D Cartesian coordinates is given by 

$$ds = \sqrt{(dx)^2 + (dy)^2}$$

The integral of $ds$ from $s_1$ to $s_2$ gives the length of the curve, $l$. What is the correct expression for $l$?

1. $l = \int_{s_1}^{s_2} ds$
2. $l = \int_{s_1}^{s_2} \sqrt{(dx)^2 + (dy)^2}$
3. $l = \int_{s_1}^{s_2} \sqrt{1 + (dy/dx)^2} \, dx$
4. $l = \int_{s_1}^{s_2} \sqrt{(dx/dy)^2 + 1} \, dy$
5. More than one of the above

---

## Clicker Question 29-2

I can explain why:

$$\int_{s_1}^{s_2} f((Y(x), Y'(x), x) \, dx > \int_{s_1}^{s_2} f((y(x), y'(x), x) \, dx$$

where $Y(x) = y(x) + \alpha \eta(x)$, the true path plus an error term.

1. Yes, I can explain why
2. I think I can explain why
3. I'm having trouble seeing why
4. I don't think I can explain why

---

## Clicker Question 29-3

For the function $Y(x) = y(x) + \alpha \eta(x)$, where $y(x)$ is the true path, $\eta(x)$ is a small error term, and $\alpha$ is a small parameter, what is the derivative of $Y(x)$ with respect to $\alpha$?

$$\frac{dY}{d\alpha} = ?$$

1. $y(x)$
2. $\eta(x)$
3. $\eta'(x)$
4. $\alpha \eta(x)$
5. $y'(x) + \alpha \eta'(x)$

---

## Clicker Question 29-4

For the function $Y'(x) = y'(x) + \alpha \eta'(x)$, what is the derivative of $Y'(x)$ with respect to $\alpha$?

$$\frac{dY'}{d\alpha} = ?$$

1. $y'(x)$
2. $\eta'(x)$
3. $\eta''(x)$
4. $\alpha \eta'(x)$
5. $y''(x) + \alpha \eta''(x)$

---

## Clicker Question 29-5

The "surface term" that we computed for $\int_{s_1}^{s_2} \eta'(x) \frac{df}{dy'} dx$ is:

$$\left[\eta(x)\dfrac{df}{dy'}\right]_{x_1}^{x_2}=0$$

I can explain why this surface term is equal to zero:

1. Yes, I can explain why
2. I think I can explain why
3. I'm having trouble seeing why
4. I don't think I can explain why
5. I don't know what a surface term is

---

## Clicker Question 29-6

We completed this derivation with the following mathematical statement:

$$\int_{s_1}^{s_2} \eta(x) \left[\dfrac{\partial f}{\partial y} - \dfrac{d}{dx}\left(\dfrac{\partial f}{\partial y'}\right)\right] = 0$$

where $\eta(x)$ is an arbitrary function. What does this imply about the term in square brackets?

1. The term in square brackets must be a pure function of $x$.
2. The term in square brackets must be a pure function of $y$.
2. The term in square brackets must be a pure function of $y'$.
3. The term in square brackets must be zero.
4. The term in square brackets must be a non-zero constant.
