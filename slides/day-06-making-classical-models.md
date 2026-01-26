---
marp: true
theme: graph_paper
paginate: true

title: Day 06 - Making Classical Models
description: Slides for PHY 321 Spring 2026, Day 06: Making Classical Models
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-06-making-classical-models.html

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

# Day 06 - Making Classical Models

![blah width:400px](../images/qrcodes/day06-s2026.png)

![bg right:50% width:600px height:auto](../images/notes/week3/von_karman.png)

---

# Plane Polar Coordinates Warm-Up

We introduced plane polar coordinates ($r,\phi$). For any position vector, $\vec{R}$, we can write:

$$\vec{R} = \left|\vec{R}\right|\hat{r} = r\hat{r}$$

where $r$ is the magnitude of $\vec{R}$, and $\hat{r}$ is the radial unit vector.

Find $\dot{\vec{R}} = \frac{d\vec{R}}{dt}$. Get as far as you can. Our answer will be in terms of $\hat{r}$ and $\hat{\phi}$.

**Remember the chain rule and Cartesian unit vectors are fixed in space/time**

$\hat{r} = \cos(\phi)\hat{x} + \sin(\phi)\hat{y} \qquad \hat{\phi} = -\sin(\phi)\hat{x} + \cos(\phi)\hat{y}$
$\frac{d}{d\phi} \cos \phi = -\sin \phi \qquad \frac{d}{d\phi} \sin \phi = \cos \phi$

---

# Announcements

- Homework 2 is due Friday (late Sunday)
- Homework 3 is now posted
- Office hours, for now (Mihir-MN; Danny-DC):
  - Friday 10-12pm (DC, 1248 BPS)
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

# Modeling Video

[<img src="https://img.youtube.com/vi/dkTncoPqo5Y/maxresdefault.jpg" width="800" alt="Modeling Video" />](https://www.youtube.com/watch?v=dkTncoPqo5Y)

Source: <https://www.youtube.com/watch?v=dkTncoPqo5Y>

--- 

# What is your experience with modeling?

## Take 2-3 min to think about your prior physics classes
- What models have you used? What makes that a model?
- What made a that model good or not so good?
- What kinds of things could you do to make a better model?

---

# Vortex Shedding

- At higher Reynolds numbers, flow around objects becomes unstable.
- This instability can lead to the formation of vortices.
- This "shedding" of vortices can lead to vibrations and noise.

![bg right:40% width:500px height:auto](../images/notes/week3/von_karman.png)

---

# Model of vortex shedding behind a cylinder

- Controlling vortex shedding is important in many engineering applications.

![width:1000px](../images/notes/week3/vortex-shedding.png)
<!-- <img src="../images/notes/week3/vortex-shedding.png" width="100%"> -->

<p><small><i>Giosan, Ioan, and P. Eng. "<b>Vortex shedding induced loads on free standing structures</b>" Structural Vortex Shedding Response Estimation Methodology and Finite Element Simulation 42 (2013).</i></small></p>

---

# Renewables: Wind Turbines

## Thorntonbank Wind Farm 

### North Sea off the coast of Belgium

*Notice the cylindrical shape of the support structure.*

![bg right:40%](https://upload.wikimedia.org/wikipedia/commons/b/ba/Windmills_D1-D4_%28Thornton_Bank%29.jpg)



---

# Clicker Question 6-1

The SHO is a useful model: $m\ddot{x} = -kx$. 

Assume the **restoring force is anti-symmetric** about the equilibrium position, what is the next term model?

1. $\sim x^2$ 
2. $\sim x^3$
3. $\sim x^4$
4. $\sim x^5$

![bg right:40% width:400px height:auto](../images/vector-graphics/simple_harmonic_oscillator_setup_1D_horizontal.png)


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








