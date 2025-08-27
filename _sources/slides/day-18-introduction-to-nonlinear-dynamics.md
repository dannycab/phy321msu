---
marp: true
theme: graph_paper
paginate: true

title: Day 18 - Introduction to Nonlinear Dynamics
description: Slides for PHY 321 Spring 2025, Day 18: Introduction to Nonlinear Dynamics
author: Prof. Danny Caballero <caball18@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-18-introduction-to-nonlinear-dynamics.html
---

# Day 18 - Introduction to Nonlinear Dynamics

## R&ouml;ssler Attractor

![bg right width:600px](../images/notes/week7/roessler.png)

$$\dot{x} = -y - z$$
$$\dot{y} = x + ay$$
$$\dot{z} = b + z(x - c)$$

## There are no crossings of the path shown in this picture
---

# Announcements

* Midterm 1 is due Feb 28th
* Homework 5 is now posted; due Mar 14th

---

# 6pm Today (SPS/Astro Club)

![width:800px](../images/notes/week6/resisting.png)

---

# Seminars this week

## MONDAY, February 24, 2025  
* High Energy Physics Seminar, 2:00-3:00pm, 1400 BPS, **Ben Assi**, University of Cincinnati, *Precision QCD and EFT for Next-Generation collider Studies*
* Condensed Matter Seminar 4:10 pm, 1400 BPS, **Ben Pingault**, Argonne National Lab, *Interfacing spins with mechanical vibrations*

## WEDNESDAY, February 26, 2025    

* Astronomy Seminar, 1:30 pm, 1400 BPS, **Lieke von Son**, CCA, Flatiron Institution, *Beyond the first waves: where we stand in understanding binary neutron star and black hole formation channels*
 
---
# Seminars this week


## THURSDAY, February 27, 2025
 
* High Energy Physics Seminar, 2:00 – 3:00 pm, 1400 BPS, **Matthew Lim**, University of Sussex
Title, *Precision at Scale: Towards Automated NNLO Event Generation*

## FRIDAY,  February 28, 2025 

* FRIB IReNA Online Seminar, 2:30pm., **Soham Chakraborty**, TRIUMF, *TACTIC: a detector for unclear astrophysics*, Zoom ONLY: <https://msu.zoom.us/j/827950260> Passcode: JINA

---

# Reminders: Conservative Forces

- The curl of a conservative force is zero

$$\nabla \times \vec{F}_{cons} = 0$$

- Work done by a conservative force is path-independent

$$\underbrace{\int_{\vec{r}_1}^{\vec{r}_2} \vec{F}_{cons} \cdot d\vec{r}}_{\textrm{path\,a}} = \underbrace{\int_{\vec{r}_1}^{\vec{r}_2} \vec{F}_{cons} \cdot d\vec{r}}_{\textrm{path\,b}}$$

- Work done by a conservative force around a closed path is zero

$$\oint \vec{F}_{cons} \cdot d\vec{r} = 0$$

---

# Reminders: Conservative Forces

- The work done by a conservative force is equal to the negative of the change in potential energy

$$W = -\Delta U$$

- A conservative force can be expressed as the gradient of a scalar function

$$\vec{F}_{cons} = -\nabla U$$

---

# Reminders: Critical Points

We found equilibrium points by setting the derivative of the potential energy to zero:

$$\frac{dU}{dx} = 0$$

We then determined if these points were stable or unstable by looking at the second derivative of the potential energy:

$$\frac{d^2U}{dx^2} > 0 \quad \textrm{stable}$$
$$\frac{d^2U}{dx^2} < 0 \quad \textrm{unstable}$$

---

# Relationship to Differential Equations

By setting $\frac{dU}{dx} = 0$, we are finding the equilibrium points where the force is zero,

$$-\frac{dU}{dx} = F_{x} = 0$$


If we consider the typical form of a differential equation,

$$m\ddot{x} = F(x)$$

We can see that we are seeking the points where the differential equation is zero,

$$m\ddot{x} = 0$$

This approach is a powerful way to understand the behavior of a system. And we can do so geometrically!

---

# Clicker Question 18-1

Let $\dot{x}=\sin{x}$. Set up the integral that could be used to solve for $t(x)$.

1. $\int \frac{dx}{\sin{x}}$
2. $\int \frac{dx}{\cos{x}}$
3. $\int \frac{dx}{\tan{x}}$
4. $\int \frac{dx}{\cot{x}}$
5. ???

---

# Clicker Question 18-2

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

# Clicker Question 18-3

Sketch the differential equation $\dot{x} = \sin{x}$ in the phase space $x$ vs. $\dot{x}$.

1. Note where the plot crosses the $x$-axis. These are the critical/equilibrium points, $x^*$. Identify the critical points.
2. By definition, $\dot{x} > 0$ is a "flow to the right" and $\dot{x} < 0$ is a "flow to the left". Sketch the direction of the flow - this should only appear in the $x$-axis.
3. Look at the flow directions and the critical points. What can you say about the stability of the critical points? We use closed circles for stable points and open circles for unstable points. Add these to your plot.

## Click when you and your table are done.

---

# Phase Space Diagram for $\dot{x} = \sin{x}$

![width:1000px](../images/notes/week7/1st-order-ode-ex-1.png)

---

# Clicker Question 18-4

Consider now the differential equation $\dot{x} = x^3 - x$. To find $t(x)$, we can integrate:

$$t(x) = \int_{x_0}^{x} \frac{dx'}{x'^3 - x'}$$

That yields the following solution (🤢🤢🤢):

$$t(x) = \left(\dfrac{1}{2}\ln(1-x^2)-\ln(x)\right)-\left(\dfrac{1}{2}\ln(1-x_0^2)-\ln(x_0)\right)$$

1. Find the equilibrium points ($x^*$) of the system.
2. Sketch the differential equation $\dot{x} = x^3 - x$ in the phase space $x$ vs. $\dot{x}$.
3. What can you say about the stability of the critical points? Add these to your plot.

## Click when you and your table are done.

---

# Phase Space Diagram for $\dot{x} = x^3 - x$

![width:1000px](../images/notes/week7/1st-order-ode-ex-2.png)


---

# The Harmonic Oscillator Gets a Bad Rap

The SHO is a linear system. It's boring. It's predictable. It's stable. But it can help us understand nonlinear 2nd order ODEs and thus more complex systems.

Consider the physical pendulum. The equation of motion is

$$mL^2\ddot{\theta} = -mgL\sin{\theta}$$

Or more simply:

$$\ddot{\theta} = -\frac{g}{L}\sin{\theta}$$

In the case of small angles, $\sin{\theta} \approx \theta$, and we have a linear system. 

$$\ddot{\theta} = -\frac{g}{L}\theta$$

---

# Examples of SHOs

- The spring-mass system $\ddot{x} = -\omega^2 x$
- The simple pendulum $\ddot{\theta} = -\frac{g}{L}\theta$
- The LC circuit $\ddot{q} = -\frac{1}{LC}q$
- Water in a u-tube $\ddot{h} = -\frac{2g\rho A}{M}h$
- A jump rope $\ddot{u} = \frac{T}{\lambda}\left(\frac{n\pi}{d}\right)^2 u$

## Any system with a local minimum in the potential energy can ber modeled as an SHO.