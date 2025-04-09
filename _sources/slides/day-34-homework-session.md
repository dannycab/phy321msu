---
marp: true
theme: graph_paper
paginate: true

title: Day 34 - Homework Session
description: Slides for PHY 321 Spring 2025, Day 34: Homework Session
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, motion, oscillations, resonance
url: https://dannycaballero.info/phy321msu/slides/day-34-homework-session.html
---

# Day 34 - Homework Session

![bg right width:600px](../images/notes/week3/quack.png)

---

# Announcements

* Feedback on Proposals are out; working on updates
* Any Project Questions? Email me! 
    * We can set up a meeting if needed.
* Friday: No Class (DC out of town); no office hours
* Homework 8 is posted 
* Rubric for Final Project is posted

---

# Seminars This Week

## WEDNESDAY, April 9, 2025    
 
                                     
* **Astronomy Seminar**, 1:30 pm, 1400 BPS, *Bertram Bitsch, University College Cork*      
Title: Planetary Dynamics
 
* **FRIB Nuclear Science Seminar**, 3:30pm., FRIB 1300 Auditorium, *Dr. Suzanne Lapi of University of Alabama at Birmingham*, Title: Development of new 

---

# Seminars This Week

## THURSDAY, April 10, 2025
 
* **Colloquium**, 3:30 pm, 1415 BPS, *Grant Tremblay, Harvard Smithsonian Astrophysical Observatory*, Title: Our fading age of discovery:  Why it's happening, and why we can't give up
 
## FRIDAY, April 11, 2025 
 
* **IReNA Online Seminar**, 2:00 pm, FRIB 2025 Nuclear Conference Room, *Marco La Cognata, INFN LNS, Italy*, Title: Nuclear reactions for Astrophysics and the opportunity of indirect methods

---

# Stand Up for Higher Education

* Graduate Employee Union
* Union of Nontenure Track Faculty
* Union of Tenure System Faculty

**Thursday, April 17th at 3pm**

**Please make time to show up!**

[www.dayofactionforhighered.org](https://www.dayofactionforhighered.org)

![bg right width:500px](../images/notes/week12/standup.png)

---

## Reminders

We used the Lagrangian formalism to derive the equations of motion for a plane pendulum. We chose the $x$ and $y$ coordinates.

$$T(\dot{x}, \dot{y}) = \dfrac{1}{2} m (\dot{x}^2 + \dot{y}^2) \quad V(y) = mgy$$

$$\mathcal{L} = T - V = \dfrac{1}{2} m (\dot{x}^2 + \dot{y}^2) - mgy$$

This gave us the following derivatives for the Lagrangian:

$$\frac{\partial \mathcal{L}}{\partial x} = 0 \quad \frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{x}} \right) = \frac{d}{dt} \left( m\dot{x} \right) = 0$$
$$\frac{\partial \mathcal{L}}{\partial y} = -mg \quad \frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{y}} \right) = -m\ddot{y}$$

---

# Clicker Question 34-1

For this plane pendulum, the mathematical statement

$$\frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{x}} \right) = \frac{d}{dt} \left( m\dot{x} \right) = 0$$

is equivalent to what statement? Is it true?

1. Conservation of energy. True.
2. Conservation of energy. False.
3. Conservation of linear momentum. True.
4. Conservation of linear momentum. False.

---

# Clicker Question 34-2

For this plane pendulum, the mathematical statement

$$\frac{\partial \mathcal{L}}{\partial y} - \frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{y}} \right) = -mg -m\ddot{y} = 0$$

$$g = - \ddot{y}$$
is equivalent to what statement? Is it true?

1. The pendulum oscillates. True.
2. The pendulum oscillates. False.
3. The pendulum is in free fall. True.
4. The pendulum is in free fall. False.
5. Something else.

---

# We made a mistake by not including the constraint

We made a mistake by not including the constraint $x^2 + y^2 = L^2$ in our Lagrangian.

We can change variables to $r$ and $\phi$.
$$x = r \cos(\phi) \quad y = r \sin(\phi)$$

$$T(\dot{x}, \dot{y}) = \dfrac{1}{2} m (\dot{x}^2 + \dot{y}^2) = \dfrac{1}{2} m \left( r^2 \dot{\phi}^2 + 2r\dot{r}\dot{\phi} + \dot{r}^2 \right) = T(r, \dot{r}, \phi, \dot{\phi})$$
$$V(y) = mgy = mg r \sin(\phi) = V(r, \phi)$$

Now we include the constraint $r = L$, so that $\dot{r} = 0$.

$$T(\phi, \dot{\phi}) = \dfrac{1}{2} m L^2 \dot{\phi}^2 \quad V(\phi) = mgL \sin(\phi)$$

$$\mathcal{L} = \dfrac{1}{2} m L^2 \dot{\phi}^2 - mgL \sin(\phi)$$

---

# Clicker Question 34-3

For the plane pendulum, we changed the Lagrangian from Cartesian coordinates to plane polar coordinates. In Cartesian, we found the Lagrangian depended on $y,\dot{x},\dot{y}$. In polar, it only depended on $\phi$ and $\dot{\phi}$.

$$\mathcal{L}(x,y,\dot{y}) \longrightarrow \mathcal{L}(\phi, \dot{\phi})$$

What does that tell you about the dimensions of the system? The system is:

1. in 3D space, so it's 3D.
2. described by two spatial dimensions ($x,y$), so it's 2D.
3. described by one spatial dimension ($\phi$), so it's 1D.