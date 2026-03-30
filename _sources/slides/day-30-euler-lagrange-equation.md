---
marp: true
theme: graph_paper
paginate: true

title: Day 30 - Euler-Lagrange Equation
description: Slides for PHY 321 Fall 2025, Day 30: Euler-Lagrange Equation
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, Euler-Lagrange Equation, action principle, Lagrangian mechanics
url: https://dannycaballero.info/phy321msu/slides/day-30-calculus-of-variations.html
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

# Day 30 - Euler-Lagrange Equation

![width:1000px](./images/day-01/Slide1.png)


---


## Reminders

We proposed a solution to the line problem that involved an error term $\eta(x)$, which is a small perturbation to the true path $y(x)$. This leads to a perturbed function:

$$Y(x) = y(x) + \alpha \eta(x)$$

where $\alpha$ is a small parameter.

We proposed that there's a functional $f(Y,Y',x)$ that depends on a function $Y(x)$, its derivative $Y'(x)$, and the independent variable $x$ such that:

$$\int_{s_1}^{s_2} f(Y,Y',x) \, dx > \int_{s_1}^{s_2} f(y,y',x) \, dx$$

---

## Reminders

By taking the derivative of the functional with respect to $\alpha$, we can find the condition for which the functional is stationary (i.e., a minimum or maximum).

$$\frac{d}{d\alpha} \int_{s_1}^{s_2} f(Y,Y',x) \, dx \bigg|_{\alpha=0} = 0$$

This (with a lot of math) led us to the following expression:

$$\int_{s_1}^{s_2} \eta(x) \left[\dfrac{\partial f}{\partial y} - \dfrac{d}{dx}\left(\dfrac{\partial f}{\partial y'}\right)\right] \, dx = 0$$

---


## Clicker Question 30-1

We completed this derivation with the following mathematical statement:

$$\int_{s_1}^{s_2} \eta(x) \left[\dfrac{\partial f}{\partial y} - \dfrac{d}{dx}\left(\dfrac{\partial f}{\partial y'}\right)\right] \, dx = 0$$

where $\eta(x)$ is an arbitrary function. What does this imply about the term in square brackets?

1. The term in square brackets must be a pure function of $x$.
2. The term in square brackets must be a pure function of $y$.
2. The term in square brackets must be a pure function of $y'$.
3. The term in square brackets must be zero.
4. The term in square brackets must be a non-zero constant.

---

## Clicker Question 30-2

Returning to the line problem,

$$l = \int_{x_1}^{x_2} \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx$$

here, $f(y,y',x) = \sqrt{1 + (y')^2}$, where $y' = \frac{dy}{dx}$.

Apply the Euler-Lagrange equation to find the expression for the function $f(y,y',x)$ in this case. Write your result to find the expression for the term in square brackets:

$$\dfrac{d}{dx}\left[?\right] = 0$$

**Click when you have an answer!**

---

## Clicker Question 30-3

With,

$$y' = \pm\sqrt{\dfrac{c^2}{1 + c^2}}$$

where $c$ is a constant, the solution expresses a straight line.

1. True and I can prove it!
2. True, but I'm not sure how to prove it.
3. False, I think this is incorrect.
4. I don't know.

---

## Clicker Question 30-4

We derived the time that it takes to run from a point on the shore to a point in the water, $T$:

$$T = \dfrac{1}{v_1} \left(x_1^2 + (y-y_1)^2\right)^{1/2}+\dfrac{1}{v_2} \left(x_2^2 + (y_2-y)^2\right)^{1/2}$$

To find the minimal time, what derivative should we take?

1. $\dfrac{dT}{dx}$
2. $\dfrac{dT}{dy}$
3. $\dfrac{dT}{dt}$
4. Something else?

---

## Clicker Question 30-5

For the brachistochrone problem, the ball moves purely under the influence of gravity. Consider that the ball has moved a vertical distance $\Delta y$ from rest. What is the speed of the ball at this point?

1. $v = gt$
2. $v = 2 g\Delta y$
3. $v = \sqrt{2g\Delta y}$
4. I'm not sure, but $<\sqrt{2g\Delta y}$
5. Something else?