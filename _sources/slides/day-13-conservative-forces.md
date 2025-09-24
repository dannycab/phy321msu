---
marp: true
theme: graph_paper
paginate: true

title: Day 13 - Conservative Forces
description: Slides for PHY 321 Fall 2025, Day 13: Conservative Forces
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, energy, conservative forces, work,
url: https://dannycaballero.info/phy321msu/slides/day-13-conservative-forces.html
---

# Day 13 - Conservative Forces

![Conservative Forces bg right 100%](../images/notes/week5/conservative-forces.png)

$$\vec{F} = - \nabla U$$
$$U = - \int \vec{F} \cdot d\vec{r}$$
$$\nabla \times \vec{F} = 0$$


---

# Announcements

* HW 4 is due Friday
  * **Friday's Class:** We will work HW 4 Exercise 4 together + Q&A
  * Friday Office Hours (14:00-16:00; 1248 BPS)
* Midterm 1 is available now
  * We will talk about it Monday (come with questions)
  * There will be no office hours on Oct 3rd (DC traveling)

---


# Seminars this week 
 
## WEDNESDAY, September 24, 2025   
 
Astronomy Seminar, 1:30 pm, 1400 BPS, In Person and Zoom, Host~ 
Speaker: Kosuke Namekata, NAOJ
Title:
Zoom Link: https://msu.zoom.us/j/887295421?pwd=N1NFb0tVU29JL2FFSkk0cStpanR3UT09
Meeting ID: 887-295-421
Passcode: 002454

---

# Seminars this week 
 
## THURSDAY, September 25, 2025 (Promotion Talk!)
 
Colloquium, 3:30 pm, 1415 BPS, in person and zoom.  Host ~  
Refreshments and social half-hour in BPS 1400 starting at 3 pm
Speaker: Wolfgang Kerzendorf, MSU - (PTRC)
Title: Calibrating Stellar Explosions as Probes of the Evolving Universe 
Background: 
For more information and to schedule time with the speaker, see the colloquium calendar at https://pa.msu.edu/news-events-seminars/colloquium-schedule.aspx
Zoom Link: https://msu.zoom.us/j/94951062663
Password: 2002  Or complete link:  https://msu.zoom.us/j/94951062663?pwd=c48uM25P9UsRVuR74rkOioOWgpoxgC.1
 
---

# Seminars this week 
 
## FRIDAY, September 26, 2025 
 
QuIC Seminar, 12:30pm, -1:30pm, 1300 BPS, In Person  
Speaker: Alexei Bazavov, MSU
Title: Efficient State Preparation for the Schwinger Model
Full Scheule is at: https://sites.google.com/msu.edu/quic-seminar/
For more information, reach out to Ryan LaRose
 
---

# Seminars this week 
 
## FRIDAY, September 26, 2025 

IReNA Online Seminar, 2:00 pm, In Person and Zoom, FRIB 2025 Nuclear Conference Room, Light refreshments will be served at 1:50pm. 
Hosted by: Steffen Turkat (TU Dresden, Germany)
Speaker:  Dominik Koll, HZDR, Germany
Title: The search for freshly synthesized radionuclides from stellar explosions on Earth
Zoom Link: https://msu.zoom.us/j/827950260
Password: JINA

---


# This Week's Goals

* Remind ourselves of the concept of energy and energy conservation
* Apply the conservation of energy to a variety of systems
* Develop the mathematical tools to analyze energy conservation in more complex systems
* Connect our new understanding of energy conservation to our previous work on forces and motion

---

# Reminders

* Energy is conserved in every process; our choice of system determines how we account for energy.
* Closed, isolated systems are often the simplest to analyze.
* A point particle is a model that allows us to ignore the internal structure of an object.
* The Work-Energy Theorem is just a statement of the conservation of energy for a point particle.

---

# Conservation of Energy

**General Principle**: Energy is conserved in every process.

$$\Delta E_{sys} = W + Q$$

**Isolated System**: No work or heat is exchanged with the surroundings.

$$\Delta E_{sys} = 0$$

**Point Particle**: A model that allows us to ignore the internal structure of an object.

$$\Delta K =  W_{\text{ext}}$$


---

# The Potential Energy Function

## Simple Harmonic Oscillator ($F_{s} = -kx$)

$$\Delta K = W_{s}$$

$$\dfrac{1}{2} m v_f^2 - \dfrac{1}{2} m v_i^2 = \int_{x_i}^{x_f} F_s dx = - \int_{x_i}^{x_f} kx dx$$

$$\dfrac{1}{2} m v_f^2 - \dfrac{1}{2} m v_i^2 = - \dfrac{1}{2} k x_f^2 + \dfrac{1}{2} k x_i^2$$

$$\dfrac{1}{2} m v_f^2 + \dfrac{1}{2} k x_f^2 = \dfrac{1}{2} m v_i^2 + \dfrac{1}{2} k x_i^2$$

$$K_f + U_{s,f} = K_i + U_{s,i}$$

$$U_s = \dfrac{1}{2} k x^2$$

---

# Clicker Question 13-1

The gravitation force near the Earth's surface is given by $\vec{F} = -mg\hat{z}$. What is the potential energy function for this force? Choose $+\hat{z}$ to be up.

1. $U = -mgz$
2. $U = mgz$
3. $U = -mgz + U_0$
4. $U = mgz + U_0$
5. None of the above

---

# Clicker Question 13-2

A model for a lattice chain acting on a electron is given by $F(x) = - F_0 \sin\left(\dfrac{2\pi x}{b}\right)$. What is the potential energy function for this force?

1. $U = -F_0 \cos\left(\dfrac{2\pi x}{b}\right)$
2. $U = F_0 \cos\left(\dfrac{2\pi x}{b}\right)$
3. $U = -\dfrac{F_0 b}{2\pi} \cos\left(\dfrac{2\pi x}{b}\right)$
4. $U = \dfrac{F_0 b}{2\pi} \cos\left(\dfrac{2\pi x}{b}\right)$
5. None of the above

---

# Clicker Question 13-3

I say "Stokes' Theorem" and you say...

![Gravedigger bg left ](../images/notes/week5/gravedigger.png)

1. HELL YEAH BROTHER 🤘
2. I'm not sure what that is 🤷
3. DEAR GOD WHY?!?! 😭

---

# Clicker Question 13-4

The curl of a vector field is given by $\nabla \times \vec{F}$. If the curl of a vector field is zero, what can we say about the vector field?

1. It is a conservative force
2. It is a non-conservative force
3. It is a constant force
4. It is a force that does no work

--- 

# Clicker Question 13-5

Which of the following fields have no divergence?

<div style="display: flex; align-items: center; gap: 20px; max-width: 800px; margin: 0 auto; white-space: nowrap; height: 400px;">
  A. <img src="../images/notes/week5/cq_left_field.png" alt="A" width="400">
  B. <img src="../images/notes/week5/cq_right_field.png" alt="B" width="400">
</div>

1. A
2. B
3. Both A and B
4. Neither A nor B

---

# Clicker Question 13-5

Which of the following fields have no curl?

<div style="display: flex; align-items: center; gap: 20px; max-width: 800px; margin: 0 auto; white-space: nowrap; height: 400px;">
  A. <img src="../images/notes/week5/cq_left_field.png" alt="A" width="400">
  B. <img src="../images/notes/week5/cq_right_field.png" alt="B" width="400">
</div>

1. A
2. B
3. Both A and B
4. Neither A nor B

---

# Clicker Question 13-6

Consider a vector field with zero curl: $\nabla \times \vec{F} = 0$. Which of the following statements is true?

1. The field is conservative
2. $\int \nabla \times \vec{F} \cdot d\vec{A} = 0$
3. $\oint \vec{F} \cdot d\vec{r} \neq 0$
4. $\vec{F}$ is the gradient of some scalar function, e.g., $\vec{F} = - \nabla U$
5. Some combination of the above

