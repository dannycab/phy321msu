---
marp: true
theme: graph_paper
paginate: true

title: Day 17 - Introduction to Nonlinear Dynamics
description: Slides for PHY 321 Fall 2025, Day 17: Introduction to Nonlinear Dynamics
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-17-introduction-to-nonlinear-dynamics.html
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

## Day 17 - Nonlinear Dynamics

### R&ouml;ssler Attractor

![bg right width:600px](../images/notes/week7/roessler.png)

$$\dot{x} = -y - z$$
$$\dot{y} = x + ay$$
$$\dot{z} = b + z(x - c)$$

**There are no crossings of the path shown in this picture**
---

## Announcements

* Midterm 1 is due Feb 27th (late on March 1st)
* **Friday's class:** Midterm 1 discussion and support session. Bring your questions.
---

# Seminars this week

## MONDAY, February 23, 2026    
  
Condensed Matter Physics Seminar, 4:10p.m., BPS 1400 & Zoom 
Speaker: Ilija Zeljkovic, Boston College
Title: Atomic-scale imaging of symmetry-broken electronic states in kagome superconductors
Zoom Link: https://msu.zoom.us/j/93613644939
Password: CMP
 
---

## TUESDAY, February 24, 2026    
  
High Energy Physics Seminar, 1:30p.m., BPS 1400 & Zoom 
Speaker: Daniel Adamiak/Artemiy Filippov, MSU
Title: Investing the phenomenon of double descent in cross-validation
*For the Zoom link – Please contact Joey Huston, Sophie Berkman and/or Brenda Wenzlick
 
---

## WEDNESDAY, February 25, 2026    
 
Astronomy Seminar, 1:30 p.m., BPS 1400 & Zoom 
Speaker: Juliette Becker, University of Wisconsin-Madison
Title: TBA
Zoom Link: https://msu.zoom.us/j/93334479606?pwd=OtIXPWhRPBfzYu53sl3trSJlaBYI7C.1
Passcode:  825824

---

## WEDNESDAY, February 25, 2026    
 
FRIB Nuclear Science Seminar, 3:30 p.m., FRIB 1300 & Zoom
Speaker: Jordan Stomps, Oak Ridge National Laboratory
Title: Data Science and Engineering for Nuclear Nonproliferation
Zoom Link: https://msu.zoom.us/j/93742845358?pwd=vlen3rlRdk8NHBSOxVIM1Aj2cP144m.1
Passcode: 416741
 
---

## THURSDAY, February 26, 2026    
 
Colloquium, Seminar, 3:30 p.m., BPS 1415 & Zoom
Refreshments at 3:00 BPS in BPS 1400
Speaker:  Dylan Yost, Colorado State
Title: Precision tests of quantum electrodynamics through hydrogen spectroscopy and vacuum birefringence
Zoom Link: https://msu.zoom.us/j/94951062663
Password: 2002
*For more information and scheduling a time to meet with the speaker, please see the calendar: https://pa.msu.edu/news-events-seminars/colloquium-schedule.aspx
 
---

## FRIDAY, February 27, 2026    
 
QuIC, Seminar, 12:40 p.m., BPS 1300 & Zoom 
Speaker: Kevin Sung, IBM
Title: Enhancing Chemistry on Quantum Computers with Fermionic Linear Optical Simulation
*For the full schedule, please see: https://sites.google.com/msu.edu/quic-seminar/ or for more information, please reach out to Ryan LaRosa directly

---

## FRIDAY, February 27, 2026    

IReNA Online Seminar, 2:00 pm, Zoom
Light refreshments at 1:50pm in 2025 Nuclear Conference Room - FRIB
Hosted by: Aldana Grichener (University of Arizona & Observatory)
Speaker: Shivani Shah, North Carolina State University
Title: Actinide Abundances, Variation, and Evolution in Metal-Poor Stars
Zoom Link: https://msu.zoom.us/j/827950260
Password: CENAM

---

## Reminders: Conservative Forces

- The curl of a conservative force is zero

$$\nabla \times \vec{F}_{cons} = 0$$

- Work done by a conservative force is path-independent

$$\underbrace{\int_{\vec{r}_1}^{\vec{r}_2} \vec{F}_{cons} \cdot d\vec{r}}_{\textrm{path\,a}} = \underbrace{\int_{\vec{r}_1}^{\vec{r}_2} \vec{F}_{cons} \cdot d\vec{r}}_{\textrm{path\,b}}$$

- Work done by a conservative force around a closed path is zero

$$\oint \vec{F}_{cons} \cdot d\vec{r} = 0$$

---

## Reminders: Conservative Forces

- The work done by a conservative force is equal to the negative of the change in potential energy

$$W = -\Delta U$$

- A conservative force can be expressed as the gradient of a scalar function

$$\vec{F}_{cons} = -\nabla U$$

---

## Reminders: Equilibrium (aka Critical or Fixed) Points

We found equilibrium points by setting the derivative of the potential energy to zero:

$$\frac{dU}{dx} = 0$$

We then determined if these points were stable or unstable by looking at the second derivative of the potential energy:

$$\frac{d^2U}{dx^2} > 0 \quad \textrm{stable}$$
$$\frac{d^2U}{dx^2} < 0 \quad \textrm{unstable}$$

---

## Relationship to Differential Equations

By setting $\frac{dU}{dx} = 0$, we are finding the equilibrium points where the force is zero,

$$-\frac{dU}{dx} = F_{x} = 0$$


If we consider the typical form of a differential equation, we can see that we are seeking the points where the differential equation is zero,

$$m\ddot{x} = F(x) \qquad m\ddot{x} = 0$$

This approach is a powerful way to understand the behavior of a system. And we can do so geometrically!

---

## Clicker Question 17-1

Let $\dot{x}=\sin{x}$. Set up the integral that could be used to solve for $t(x)$.

1. $\int \frac{dx}{\sin{x}}$
2. $\int \frac{dx}{\cos{x}}$
3. $\int \frac{dx}{\tan{x}}$
4. $\int \frac{dx}{\cot{x}}$
5. ???

---

## Clicker Question 17-2

We can integrate this with $x(0)=x_0$ to find $t(x)$:

$$t(x) = \ln\left(|\csc{x} - \cot{x}|\right) - \ln\left(|\csc{x_0} + \cot{x_0}|\right)$$

Find $x(t)$? 🤢🤢🤢

Instead find the equilibrium points ($x^*$) of the system. $n$ is an integer.

1. $x^*=0$
2. $x^*=0, \pm\pi$
3. $x^*=\pm\pi/2$
4. $x^*=n\frac{\pi}{2}$
5. $x^*=n\pi$

---

## Clicker Question 17-3a

Sketch the differential equation $\dot{x} = \sin{x}$ in the phase space $x$ vs. $\dot{x}$.

1. Note where the plot crosses the $x$-axis. These are the critical/equilibrium points, $x^*$. Identify the critical points.
2. By definition, $\dot{x} > 0$ is a "flow to the right" and $\dot{x} < 0$ is a "flow to the left". Sketch the direction of the flow - this should only appear in the $x$-axis.

**Click when you and your table are done.**

---
## Clicker Question 17-3b

Sketch the differential equation $\dot{x} = \sin{x}$ in the phase space $x$ vs. $\dot{x}$.

3. Look at the flow directions and the critical points. What can you say about the stability of the critical points? We use closed circles for stable points and open circles for unstable points. Add these to your plot.

**Click when you and your table are done.**

---

## Phase Space Diagram for $\dot{x} = \sin{x}$

![width:1000px](../images/notes/week7/1st-order-ode-ex-1.png)

---

## Clicker Question 17-4a

Consider now the differential equation $\dot{x} = x^3 - x$. To find $t(x)$, we can integrate:

$$t(x) = \int_{x_0}^{x} \frac{dx'}{x'^3 - x'}$$

That yields the following solution (🤢🤢🤢):

$$t(x) = \left(\dfrac{1}{2}\ln(1-x^2)-\ln(x)\right)-\left(\dfrac{1}{2}\ln(1-x_0^2)-\ln(x_0)\right)$$

1. Find the equilibrium points ($x^*$) of the system.
2. Sketch the differential equation $\dot{x} = x^3 - x$ in the phase space $x$ vs. $\dot{x}$.

**Click when you and your table are done.**

---

## Clicker Question 17-4b

Consider now the differential equation $\dot{x} = x^3 - x$. To find $t(x)$, we can integrate:

$$t(x) = \int_{x_0}^{x} \frac{dx'}{x'^3 - x'}$$

That yields the following solution (🤢🤢🤢):

$$t(x) = \left(\dfrac{1}{2}\ln(1-x^2)-\ln(x)\right)-\left(\dfrac{1}{2}\ln(1-x_0^2)-\ln(x_0)\right)$$

3. What can you say about the stability of the critical points? Add these to your plot.

**Click when you and your table are done.**

---

## Phase Space Diagram for $\dot{x} = x^3 - x$

![width:1000px](../images/notes/week7/1st-order-ode-ex-2.png)


---

## The Harmonic Oscillator Gets a Bad Rap

The SHO is a linear system. It's boring. It's predictable. It's stable. But it can help us understand nonlinear 2nd order ODEs and thus more complex systems.

Consider the physical pendulum. The equation of motion is

$$mL^2\ddot{\theta} = -mgL\sin{\theta}$$

Or more simply:

$$\ddot{\theta} = -\frac{g}{L}\sin{\theta}$$

In the case of small angles, $\sin{\theta} \approx \theta$, and we have a linear system. 

$$\ddot{\theta} = -\frac{g}{L}\theta$$

---

## Examples of SHOs

- The spring-mass system $\ddot{x} = -\omega^2 x$
- The simple pendulum $\ddot{\theta} = -\frac{g}{L}\theta$
- The LC circuit $\ddot{q} = -\frac{1}{LC}q$
- Water in a u-tube $\ddot{h} = -\frac{2g\rho A}{M}h$
- A jump rope $\ddot{u} = \frac{T}{\lambda}\left(\frac{n\pi}{d}\right)^2 u$

**Any system with a local minimum in the potential energy can ber modeled as an SHO.**