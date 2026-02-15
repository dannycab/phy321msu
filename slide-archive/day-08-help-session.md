---
marp: true
theme: graph_paper
paginate: true

title: Day 08 - Workshop Day
description: Slides for PHY 321 Spring 2026, Day 08: Workshop Day
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-08-help-session.html
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

# Day 08 - Workshop Day

Fridays are reserved for your questions, homework issues, and general support

![bg right:60% width:600px height:auto](./images/units-meme.jpeg)

<div class="footnote">PHY 321 Classical Mechanics I - Spring 2026</div>

---


# Announcements

* Homework 2 is due today (there is no penalty for late submission)
* Homework 3 is posted (due next Friday; late after Sunday)
* Afternoon help session (with Mihir, 3-5pm) on Zoom:
    * Zoom Link: <https://msu.zoom.us/j/99550311023> 
    * password: `phy321msu`
* **First midterm is coming up** (assigned 16 Feb)
    * One exercise will ask you to get started on your final project planning. 
    * *Who are you gonna work with? What are you interested in studying?* Start thinking about this!



---

# At your table, chat for 3 minutes.

**What questions do you have?**

⬆️ **Make sure you upvote other's questions.**

![bg right:50% width:500px height:auto](../images/qrcodes/day08-s2026.png)

---

## HW 2; Exercise 5, ball thrown along a sloped ramp

A ball is thrown with initial speed $v_0$ up an inclined plane. The plane is inclined at an angle $\phi$ above the horizontal, and the ball's initial velocity is at an angle $\theta$ above the plane. Choose axes with $x$ measured up the slope, $y$ normal to the slope, and $z$ across it.

* 5a: Write down Newton's second law using these axes and find the ball's position as a function of time. **Make sure to include the FBD and any assumptions you make.**

---

## HW 2; Exercise 5, ball thrown along a sloped ramp

A ball is thrown with initial speed $v_0$ up an inclined plane. The plane is inclined at an angle $\phi$ above the horizontal, and the ball's initial velocity is at an angle $\theta$ above the plane. Choose axes with $x$ measured up the slope, $y$ normal to the slope, and $z$ across it.

* 5b: Show that the ball lands a distance 

$$R=2v_0^2\dfrac{\sin\theta\cos\left(\theta + \phi\right)}{g \cos^2 \phi}$$

from its launch point. **This is measured up the ramp (i.e., along it).**

---

## HW 2; Exercise 5, ball thrown along a sloped ramp

A ball is thrown with initial speed $v_0$ up an inclined plane. The plane is inclined at an angle $\phi$ above the horizontal, and the ball's initial velocity is at an angle $\theta$ above the plane. Choose axes with $x$ measured up the slope, $y$ normal to the slope, and $z$ across it.

* 5c: Show that for given $v_0$ and $\phi$, the maximum range up the inclined plane is:

$$R_{\text{max}}=\dfrac{v_0^2}{g(1+\sin\phi)}$$

---

# HW 3; Exercise 3, Drag force

We can observe that the models for linear and quadratic drag forces are given by:

$$f_{lin} = 3\pi \eta D v \qquad f_{quad} = \kappa \rho A v^2$$

where $D$ is the "length scale" of the object (e.g., the diameter of the sphere), $\eta$ is the viscosity of the fluid, $\rho$ is the density of the fluid, $A$ is the cross-sectional area of the object, and $\kappa$ is a constant of order unity (larger for flat and blunt bodies; smaller for streamlined bodies).

---

# Parts 3a and 3b 

* The Reynolds number is defined as $Re = \rho v D / \eta$. What is the physical meaning of this number? For a spherical object, show that the ratio of the quadratic drag force to the linear drag force is given by $f_{quad}/f_{lin} = Re/48$. Use this to explain the physical meaning of the Reynolds number. **Note: you may assume that $\kappa = 0.25$ for a sphere.**
* Explain a situation where there would be a low Reynolds number. What about a high Reynolds number? Estimate the Reynolds number for a falling rain drop, a parachutist, a car, and a plane.


