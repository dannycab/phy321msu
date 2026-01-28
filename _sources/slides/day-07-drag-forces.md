---
marp: true
theme: graph_paper
paginate: true

title: Day 07 - Drag Forces
description: Slides for PHY 321 Spring 2026, Day 07: Drag Forces
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, drag, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-07-drag-forces.html

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

# Day 07 - Drag Forces

![blah width:300px height:auto](../images/qrcodes/day07-s2026.png)


![bg right width:100%](../images/notes/week3/drag.png)

---

# Announcements

- Homework 2 is due Friday (late Sunday)
- Homework 3 is now posted
- Office hours, for now (Mihir-MN; Danny-DC):
  - Thursday 3-5pm (MN, 1248 BPS)
  - Friday 10-12pm (DC, 1248 BPS)
  - Friday 3-5pm (MN, Zoom only)
- Zoom Link for class: <https://msu.zoom.us/j/99550311023> 
    - password: `phy321msu`

---

# Seminars this week

**WEDNESDAY, January 28, 2026**
 
Astronomy Seminar, 1:30pm, BPS 1400 & Zoom 
Speaker: Rebecca Kyer & Emily Elizondo, MSU
Title: TBA
Zoom Link: https://msu.zoom.us/j/93334479606?pwd=OtIXPWhRPBfzYu53sl3trSJlaBYI7C.1
Passcode:  825824

---

# Seminars this week

**WEDNESDAY, January 28, 2026**
 
Physics Education Research Seminar, 3:00pm, BPS 1400 & Zoom
Speaker: Jennifer Doherty, MSU
Title:  Principle-based reasoning: A strategy for developing expertise in Physiology
Zoom Link: https://msu.zoom.us/j/96470703707
Passcode: PERSeminar

---

# Seminars this week

**WEDNESDAY, January 28, 2026**
 
FRIB Nuclear Science Seminar, 3:30pm, Zoom Only
Speaker: Gwen Grinyer, University of Regina
Title: Precision Spectroscopy of Rare Isotopes
Zoom Link: https://msu.zoom.us/j/91051885898?pwd=S423bks5tzaeOwNb1tLaUaHDUScm5A.1
Passcode: 949110
 

---

# Seminars this week

**FRIDAY, January 30, 2026**
 
QuIC, Seminar, 12:40 p.m., BPS 1300 & Zoom 
Speaker: Ben DalFavero, MSU
Title: Fault tolerant quantum computing II
*For the full schedule, please see: https://sites.google.com/msu.edu/quic-seminar/ or for more information, please reach out to Ryan LaRosa directly

---

# Seminars this week

**FRIDAY, January 30, 2026**

IReNA Online Seminar, 2:00 pm, Zoom
Light refreshments at 1:50pm in 2025 Nuclear Conference Room - FRIB
Hosted by: Aldana Grichener (University of Arizona & Observatory)
Speaker: Mengke Li, University of California, Berkeley
Title: Implications of a Weakening N = 126 Shell Closure Away from Stability for r-Process Astrophysical Conditions
Zoom Link: https://msu.zoom.us/j/827950260
Password: CENAM

---


# Goals for Week 3

- Be able to answer the following questions.
    - What is Mathematical Modeling?
    - What is the process for analyzing these models?
- Be able to solve "Simple" Motion Problems with Newton's Laws.

---

# Our man, Reynolds

![bg right:30% width:300px height:auto](../images/notes/week3/stokes.png)

**The Reynolds number is a dimensionless quantity.** It is a ratio of inertial forces to viscous forces.

$$Re = \frac{\rho v L}{\mu}$$

* $\rho$ - density of the fluid
* $v$ - velocity of the object
* $L$ - characteristic length
* $\mu$ is the dynamic viscosity

---

# Our man, Reynolds

![bg right:30% width:300px height:auto](../images/notes/week3/stokes.png)

BTW, this is not a photo of Reynolds. **This is Stokes.** 
  - He developed the concept of the Reynolds number. 
  - Reynolds "popularized" it according to the Wikipedia.

$$Re = \frac{\rho v L}{\mu}$$

**Discussion:** What kinds of systems have a high/low Reynolds number?

---

# Clicker Question 7-1

Consider a ball falling down with a coordinate system such that $y$ is positive downward. Which of the following is correct for the differential equation?

1. $m\ddot{y}=-mg+bv_y$
2. $m\ddot{y}=-mg-bv_y$
3. $m\ddot{y}=+mg+bv_y$
4. $m\ddot{y}=+mg-bv_y$

**Think about the SIGN of $v_y$; it's a component not a speed!**

---

Assuming a **linear model** for Air Resistance $\sim bv$, we can obtain this EOM for the velocity a falling ball, after *separation of variables*:

$$\dfrac{dv_y}{v_y - v_{term}} = -\frac{b}{m}dt$$

 
Let's try to integrate this equation from $v_y = v_{y0}$ at $t=0$ to $v_y(t)$ at time $t$.

**We can write the integral (on both sides) that is needed to solve this equation.**

*This integral setup is common in physics derivations with ODEs; provided we can find an anti-derivative.*

---

# Clicker Question 7-2

Assuming a **quadratic model** for Air Resistance $\sim cv^2$, what is the EOM for a falling ball, with $y$ positive upward?

1. $m\ddot{y}=-mg+c v_y^2$
2. $m\ddot{y}=-mg - c v_y^2$
3. $m\ddot{y}=+mg + c v_y^2$
4. $m\ddot{y}=+mg - c v_y^2$
5. ???

> Draw a picture, remember $v_y$ is a component, and consider upward and downward motion!

---

# Clicker Question 7-3

For the system of **Quadratic Drag in 1D**, we found a solution for the velocity as a function of time, with $v = 0$ at $t = 0$.

$$v(t) = v_{term}\tanh(gt/v_{term})$$

where $v_{term} = (mg/c)^{1/2}$. Do the units make sense? What are the units $\left[gt/v_{term}\right]$? 
1. Yes, **they have the same units**; the units for $\left[gt/v_{term}\right]$ are m/s.
2. No,  **they have different units**; the units for $\left[gt/v_{term}\right]$ are m/s.
3. Yes,  **they have the same units**; the units for $\left[gt/v_{term}\right]$ are unit-less.
4. No,  **they have different units**; the units for $\left[gt/v_{term}\right]$ are unit-less.

---

# Clicker Question 7-4

For the system of **Quadratic Drag in 1D**, we found a solution for the velocity as a function of time, with $v = 0$ at $t = 0$.

$$v(t) = v_{term}\tanh(gt/v_{term})$$ 

where $v_{term} = \sqrt{mg/c}$. What happens when $t \rightarrow \infty$?

1. The object stops moving.
2. The object travels at a constant velocity.
3. The object travels at an increasing velocity.
4. The object travels at a decreasing velocity.
5. I'm not sure.

---

# Clicker Question 7-5

Assuming a **quadratic model** for Air Resistance $\sim cv^2$, what is the EOM for a ball initially sent upward and to the right, with $y$ positive upward and $x$ positive to the right?

1. $m\ddot{x}=-c v_x\sqrt{v_x^2+v_y^2}; \quad m\ddot{y}=-mg - c v_y\sqrt{v_x^2+v_y^2}$
2. $m\ddot{x}=-c v_x\sqrt{v_x^2+v_y^2}; \quad m\ddot{y}=+mg - c v_y\sqrt{v_x^2+v_y^2}$
3. $m\ddot{x}=+c v_x\sqrt{v_x^2+v_y^2}; \quad m\ddot{y}=-mg + c v_y\sqrt{v_x^2+v_y^2}$
4. $m\ddot{x}=+c v_x\sqrt{v_x^2+v_y^2}; \quad m\ddot{y}=+mg + c v_y\sqrt{v_x^2+v_y^2}$
5. None of the above.

---

# Clicker Question 7-6

For linear drag in 2D, we found the following equations of motion:

$$\dot{v}_x = -\gamma v_x$$
$$\dot{v}_y = -g - \gamma v_y$$

Are these equations integrable? *Can we find anti-derivatives for both equations?*

1. Yes, both equations are integrable.
2. No, neither equation is integrable.
3. Only the $x$ equation is integrable.
4. Only the $y$ equation is integrable.












