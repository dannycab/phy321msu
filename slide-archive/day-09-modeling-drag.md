---
marp: true
theme: graph_paper
paginate: true

title: Day 09 - Modeling Drag
description: Slides for PHY 321 Spring 2026, Day 09: Modeling Drag
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-09-modeling-drag.html
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

# Day 09 - Modeling Drag

![bg right width:600px](../images/notes/week4/paramecium-swimming.png)

Somersault of Paramecium in extremely confined environments ->

source: <https://www.nature.com/articles/srep13148>

<div class="footnote">PHY 321 Classical Mechanics I - Spring 2026</div>

---

## Announcements

* Homework 3 is posted (due Friday; late after Sunday)
* Homework 4 is posted (due next Friday; late after Sunday)
* **First midterm is coming up** (assigned 16 Feb)
    * One exercise will ask you to get started on your final project planning. 
    * *Who are you gonna work with? What are you interested in studying?* Start thinking about this!
* Limiting using [RaiseMyHand](https://raisemyhand.msucerl.org) to Workshop Days on (Fridays) only. 
  * *Will start posting the link to collect your questions for those days.*

---

## HW1 Feedback

* Overall, folks did well; some issues with uploading/submitting
  * Submit a regrade request if you think something was graded incorrectly
* Kang has **ALOT** of grading to do
* Grading of your HW will be completed by the Monday a week following the Sunday due date
* We will not grade homework that has not been submitted properly
  * Delays will be handled on a case-by-case basis

**Please assign problem sections to your assignment.** *It takes five more minutes.*
**Please submit your assignment as a single PDF file.** *It makes sure your grade is correct.*


---

## Clicker Question 9-0

I need help making sure my homework submissions are done correctly.

1. I think I am doing it correctly.
2. I am not sure if I am doing it correctly.
3. I know I am not doing it correctly. Please help.

*If you select 2 or 3, make a mental note to please see me soon and so we can go through it together or debug your process.*

---

## Weekly Seminars

### TUESDAY, February 3, 2026    
  
Nuclear Theory Seminar, 11:00 a.m., FRIB 1200 Lab & Zoom 
Speaker: Ryan LaRose, MSU
Title: Error mitigation for partially-error corrected quantum computers
Zoom Link: 964 7281 4717
Passcode:  48824
 
---

## Weekly Seminars

### WEDNESDAY, February 4, 2026    
 
Astronomy Seminar, 1:30 p.m., BPS 1400 & Zoom 
Speaker: Marvin Morgan, UCSB
Title: TBA
Zoom Link: https://msu.zoom.us/j/93334479606?pwd=OtIXPWhRPBfzYu53sl3trSJlaBYI7C.1
Passcode:  825824
  
---

## Weekly Seminars

### THURSDAY, February 5, 2026    
 
Colloquium, Seminar, 3:30 p.m., BPS 1415 & Zoom
Refreshments at 3:00 BPS in BPS 1400
Speaker: Glennys Farrar, New York University
Title: Origin of ultrahigh-energy cosmic rays in Binary Neutron Star Collisions and the crucial roles of Nuclear Physics
Zoom Link: https://msu.zoom.us/j/94951062663
Password: 2002
 
---

## Weekly Seminars

### FRIDAY, February 6, 2026    
 
QuIC, Seminar, 12:40 p.m., BPS 1300 & Zoom 
Speaker: Gregory Quiroz, APL
Title: Classical Non-Markovian Noise in Symmetry-Preserving Quantum Dynamics
*For the full schedule, please see: https://sites.google.com/msu.edu/quic-seminar/ or for more information, please reach out to Ryan LaRosa directly

**Reminder:**
*Email Danny (<caball14@msu.edu>) your extra credit seminar write-ups*

---

## Goals for this week

![bg right width:600px](../images/notes/week4/paramecium-swimming.png)

* Establish a model for drag forces
* Develop an understanding of the process for modeling forces
* Produce equations of motion that can be investigated
* Start probing the behavior of these systems with math and computing

---

## Reminders

### Force Models

We have been modeling the drag force using a functional dependence on velocity.

$$\vec{F}_{\text{drag}} = -f(v)\hat{v}$$

where $f(v)$ is a function of velocity.

We established (in 1D) there are two common forms of drag force:

$$f(v) = bv \quad \text{Linear Drag}$$

$$f(v) = cv^2 \quad \text{Quadratic Drag}$$

---

## Reminders

### Reynolds Number

The choice of which drag model to use depends on the Reynolds number of the system:

$$\text{Re} = \dfrac{\rho v L}{\eta}$$

where $\rho$ is the density of the fluid, $v$ is the velocity of the object relative to the fluid, $L$ is a characteristic linear dimension (e.g., diameter of a sphere), and $\eta$ is the dynamic viscosity of the fluid.

---


## Reminders

### Equations of Motion

The next step is to use Newton's 2nd Law to write the equations of motion for the system. We found those equation of motion to be:

$$m\dot{v} = -f(v)$$

where $f(v)$ is the drag force. So for each form of drag we have:

$$\dot{v} = g-\frac{b}{m}v \quad \text{Linear Drag}$$

$$\dot{v} = g-\frac{c}{m}v^2 \quad \text{Quadratic Drag}$$

---

## Reminders

### Trajectories

We can integrate these equations of motion to find the velocity as a function of time. We found:

$$v(t) = v_{\text{t,lin}}\left(1-e^{-\frac{bt}{m}}\right) \quad \text{Linear Drag}$$

$$v(t) = v_{\text{t,quad}}\tanh\left(\frac{gt}{v_{\text{t,quad}}}\right) \quad \text{Quadratic Drag}$$

where $v_{\text{t,lin}} = \frac{mg}{b}$ for linear drag and $v_{\text{t,quad}} = \sqrt{\frac{mg}{c}}$ for quadratic drag.

---

## Our Current Investigatory Process

### The Model-to-Trajectory Pipeline

1. Model the forces acting on the system
2. Write the equations of motion using Newton's 2nd Law
3. Solve the equations of motion to find trajectories

This is incomplete. We will need to learn how stability, critical points, and phase space can help us understand the behavior of these systems.

We have also only done step 3 analytically. We will need to learn how to use computing to investigate these systems.

---

## Clicker Question 9-1

The Reynolds number can be thought of as a comparison between two forces acting on an object moving through a fluid: (1) inertial forces and (2) viscous forces. The ratio gives a sense of which force dominates the behavior of the object. 

$$\text{Re} = \dfrac{\rho v L}{\eta}$$


---

## Clicker Question 9-1

With this in mind, consider again the Reynolds number formula:

$$\text{Re} = \dfrac{\rho v L}{\eta},$$

Consider three scenarios:

1. A person swimming through water at moderate speed.
2. A small bacterium swimming through water at low speed.
3. A large airplane flying through the air at high speed.

**Order these scenarios from lowest to highest Reynolds number.**

**1.** 1, 3, 2; **2.** 2, 3, 1; **3.** 1, 2, 3, **4.** 3, 1, 2; **5.** Something else

---


![bg right:50% w:600px height:auto](../images/notes/week3/cq6-3.png)


## Clicker Question 9-2

For the system of **Linear Drag in 1D**, we found a solution for the velocity as a function of time, with $v = 0$ at $t = 0$.
$$v(t) = v_{term}\left(1-e^{-\frac{bt}{m}}\right)$$

where $v_{term} = \sqrt{\frac{mg}{b}}$. 

**Which sketch could be correct for the velocity of the ball?**

---

## Clicker Question 9-3

For the system of **Quadratic Drag in 1D**, we found a solution for the velocity as a function of time, with $v = 0$ at $t = 0$.

$$v(t) = v_{term}\tanh(gt/v_{term})$$ 

where $v_{term} = \sqrt{mg/c}$. What happens when $t \rightarrow \infty$?

1. The object stops moving.
2. The object travels at a constant velocity.
3. The object travels at an increasing velocity.
4. The object travels at a decreasing velocity.
5. I'm not sure.

---

## Clicker Question 9-4

For quadratic drag in 2D, we found the following pair of differential equations:

$$\dot{v}_x = -\tilde{D}v_x\sqrt{v_x^2+v_y^2}$$
$$\dot{v}_y = -\tilde{D}v_y\sqrt{v_x^2+v_y^2}-g$$

**True or False:** This pair of differential equations can be decoupled.

1. True
2. False
3. ???

---

## Clicker Question 9-5

For linear drag in 2D, we found the following pair of differential equations:

$$\dot{v}_x = -\gamma v_x$$
$$\dot{v}_y = -\gamma v_y-g$$

**True or False:** This pair of differential equations is decoupled.

1. True
2. False
3. ???

---

## Clicker Question 9-6

For the gravitational interaction, I want to compute the force acting on body B, located at $\vec{r}_B$, by body A, located at $\vec{r}_A$.

The gravitational force is given by:

$$\vec{F} = -G\dfrac{m_1 m_2}{r^2}\hat{r}$$

What is the appropriate form of $\vec{r}$?

1. $\vec{r} = \vec{r}_A - \vec{r}_B$
2. $\vec{r} = \vec{r}_B - \vec{r}_A$
3. Either is ok

--- 

## Clicker Question 9-7

We found that the equation of motion for the spring-mass system was:

$$\ddot{x} = -\dfrac{k}{m}x = -\omega^2 x$$

Your friends have proposed the following **general solutions**:

$$1.\;x(t) = A\cos(\omega t) \qquad 2.\;x(t) = B\sin(\omega t) \qquad 3.\;x(t) = A\cos(\omega t) + B\sin(\omega t) $$
$$ 4.\;x(t) = A\cos(\omega t + \phi) \qquad 5.\;x(t) = B\sin(\omega t + \phi) \qquad 6.\;x(t) = A\cos(\omega t + \phi) + B\sin(\omega t + \phi) $$

How many of them are correct? 
(1) Only one (2) Two (3) Three
(4) Four (5) All of them
