---
marp: true
theme: graph_paper
paginate: true

title: Day 10 - Integrating EOMs Numerically
description: Slides for PHY 321 Spring 2026, Day 10: Integrating EOMs Numerically
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion, numerical integration, euler
url: https://dannycaballero.info/phy321msu/slides/day-10-integrating-eoms-numerically.html
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

## Day 10 - Integrating EOMs Numerically

![bg right:40% width:500px height:auto](../images/notes/week4/numerical_integration.png)

For Friday, please submit questions.
![qrcode width:350px height:auto](../images/qrcodes/day11-s2026.png)

---

## Announcements

* Homework 3 is posted (due Friday; late after Sunday)
* Homework 4 is posted (due next Friday; late after Sunday)
* **First midterm is coming up** (assigned 16 Feb)
    * One exercise will ask you to get started on your final project planning. 
    * *Who are you gonna work with? What are you interested in studying?* Start thinking about this!
* Limiting using [RaiseMyHand](https://raisemyhand.msucerl.org) to Workshop Days on (Fridays) only. 
  * *Will start posting the link to collect your questions for those days.*

------

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

![bg right width:600px](../images/notes/week4/numerical_integration.png)

* Establish a model for drag forces
* Develop an understanding of the process for modeling forces
* Produce equations of motion that can be investigated
* Start probing the behavior of these systems with math and computing

---

## Model-to-EOM Pipeline for Classical Mechanics

1. ✅ Develop conceptual description of the system; make justifiable assumptions
2. ✅ Using a framework of physics (i.e., Newton's Laws, Lagrangian Dynamics), develop a mathematical model of the system
3. ✅ Produce the equations of motion (EOM) by following the framework (i.e., ordinary differential equations)
4. 😵 **Solve for trajectories of the system** (e.g., $x(t)$, $v(t)$, $v(x)$)

**Most EOMs are nonlinear**
**We need approximate methods to produce trajectories.**

---


## Clicker Question 10-1

We found that the equation of motion for the spring-mass system was:

$$\ddot{x} = -\dfrac{k}{m}x = -\omega^2 x$$

Your friends have proposed the following **particular solutions**:

$$1.\;x(t) = A\cos(\omega t) \qquad 2.\;x(t) = B\sin(\omega t) \qquad 3.\;x(t) = A\cos(\omega t) + B\sin(\omega t) $$
$$ 4.\;x(t) = A\cos(\omega t + \phi) \qquad 5.\;x(t) = B\sin(\omega t + \phi) \qquad 6.\;x(t) = A\cos(\omega t + \phi) + B\sin(\omega t + \phi) $$

How many of them are possible ok? 
(1) Only one (2) Two (3) Three
(4) Four (5) All of them

**Should we start with general solutions or particular solutions?**

---

## Clicker Question 10-2

To convert the second order ODE for a spring mass system,

$$\ddot{x} = -\dfrac{k}{m}x = -\omega^2 x$$

to two first order ODEs, we first introduce an equation for the velocity:

$$v = \dot{x}.$$ 

This is a first order ODE, and the first one we need. What is the other first order ODE?

---

## Clicker Question 10-2

For spring-mass system ($\ddot{x} = -\omega^2 x$), and using the first order ODE the defines velocity $v = \dot{x}$, which other first order ODE can be used with the velocity equation to represent the spring mass system?

1. $\dot{x} = -\omega^2 x$
2. $\dot{v} = -\omega^2 x$
3. $\ddot{x} = a$
4. $\dot{v} = a$
5. Something else

---

## Clicker Question 10-3

We derived the Euler step for constant acceleration:

$$v[i+1]=v[i]+a*\Delta t$$
$$x[i+1]=x[i]+v[i]*\Delta t$$

We can implement in Python for arrays `x` and `v` with: 

```python
v[i+1]=v[i]+a*deltat        # Constant Acceleration
x[i+1]=x[i]+v[i]*deltat     # Euler Step
```

How can we implement a non-constant acceleration?

---

## Clicker Question 10-3

How can we implement a non-constant acceleration?

```python
v[i+1]=v[i]+a*deltat        # Constant Acceleration
x[i+1]=x[i]+v[i]*deltat     # Euler Step
```

1. Add in `a[i]` to the first equation
2. Pre-compute the array `a` outside the loop 
3. Compute `a[i]` in the loop
4. Change `v[i]` to `v[i+1]`
5. More than one of these

---

## Numerical Integration Techniques for EOMs

### Euler Method (Forward Euler)

* Simple, but not very accurate
* Does not conserve energy in many systems (especially oscillatory systems)

$$v[i+1]=v[i]+a[i]*\Delta t$$
$$x[i+1]=x[i]+v[i]*\Delta t$$

**Notice that we use the acceleration at the beginning of the time step.**

---

## Numerical Integration Techniques for EOMs

### Euler-Cromer Method (Semi-Implicit Euler)

* Simple, more accurate than Euler
* Conserves energy in many oscillatory systems

$$v[i+1]=v[i]+a[i]*\Delta t$$
$$x[i+1]=x[i]+v[i+1]*\Delta t$$

**Notice that we use the updated velocity at the end of the time step.**

---

## Numerical Integration Techniques for EOMs

### Velocity Verlet Method

* More accurate than Euler and Euler-Cromer
* Conserves energy in many oscillatory systems

$$x[i+1]=x[i]+v[i]*\Delta t + \dfrac{1}{2}a[i]*\Delta t^2$$
$$v[i+1]=v[i] + \dfrac{a[i] + a[i+1]}{2}*\Delta t$$

**Notice that we use the average acceleration over the time step.**
*Be careful not to confuse this with your kinematic equations!*

---

## Other Common Numerical Integration Techniques for EOMs

* Runge-Kutta 2nd Order (RK2)
* Runge-Kutta 4th Order (RK4)
* Leapfrog Method
* Beeman's Algorithm
* $\dots$

Many of these methods are more accurate, but also more complex to implement. 

They are available in Python's scientific computing libraries (e.g., `scipy`.)