---
marp: true
theme: graph_paper
paginate: true

title: Day 18 - Introduction to Nonlinear Dynamics
description: Slides for PHY 321 Fall 2025, Day 18: Introduction to Nonlinear Dynamics
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

* Midterm 1 is due Oct 10th

---

# Seminars this week

## MONDAY, October 6, 2025             
 
 
Condensed Matter Seminar 4:10 pm,1400 BPS, In Person and Zoom, Host ~ Tyler Cocker
Speaker: Edoardo Baldini, University Texas - Austin
Title: Nonlinear Coupled Magnonics
Zoom Link: https://msu.zoom.us/j/93613644939
Meeting ID: 936 1364 4939
Password: CMP
 
---
 
# Seminars this week

## WEDNESDAY, October 8, 2025    
 
FRIB Nuclear Science Seminar, 11:00am., FRIB room 1300 and online via Zoom.
Speaker: Dr. Yuhu Zhai of Princeton Plasma Physics Laboratory 
Title: Innovation in superconducting magnet technologies: R&D Gaps and opportunities to mature HTS for fusion and other applications
Join Zoom: https://msu.zoom.us/j/96657965451?pwd=Isaf23sK5agzaao0Kwaei7AaWHkc4W.1
Meeting ID: 966 5796 5451
Passcode: 479842
 
---
 
# Seminars this week

## WEDNESDAY, October 8, 2025  
                                   
Astronomy Seminar, 1:30 pm, 1400 BPS, In Person and Zoom, Host~ 
Speaker: Kyle Kremer, UC San Diego
Title: Globular Clusters: Astronomical factories of gravitational-wave and
electromagnetic transients
Zoom Link: https://msu.zoom.us/j/94228252584?pwd=zNJdjCNAabNkppOcg5FlAv01ihzLwl.1
Meeting ID: 942 2825 2584
Passcode: 541987
 
 
---
 
# Seminars this week

## THURSDAY, October 9, 2025
 
Colloquium, 3:30 pm, 1415 BPS, in person and zoom.  Host ~ Xing Wu
Refreshments and social half-hour in BPS 1400 starting at 3 pm
Speaker: Benjamin Jones, University of Texas at Arlington
Title: Single Barium Ion Identification Technologies for Background-Free Neutrinoless DoubleBeta Decay searches -
Zoom Link: https://msu.zoom.us/j/94951062663
Password: 2002  Or complete link:  https://msu.zoom.us/j/94951062663?pwd=c48uM25P9UsRVuR74rkOioOWgpoxgC.1
 
---
 
# Seminars this week

## FRIDAY, October 10, 2025 
 
QuIC Seminar, 12:30pm, -1:30pm, 1300 BPS, Zoom only 
Speaker: Daniel Nino, Xanadu
Title: Quantum Computational Chemistry (With Pennylane)
Full Scheule is at: https://sites.google.com/msu.edu/quic-seminar/
For more information, reach out to Ryan LaRose
 

---
 
# Seminars this week

## FRIDAY, October 10, 2025 

FRIB IReNA Online Seminar, 2:00pm., Eastern Time.
Hosted By: Hosted by: Borbala Cseh (Konkoly Observatory)
Speaker: Artemis Spyrou, MSU
Title: Neutron-capture reaction constraints for astrophysical processes Please see website for full abstract.
Please click the link below to join the webinar:
Join Zoom: https://msu.zoom.us/j/827950260
Meeting ID:
Passcode: JINA

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

# Reminders: Equilibrium (aka Critical or Fixed) Points

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