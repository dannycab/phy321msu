---
marp: true
theme: graph_paper
paginate: true

title: Day 33 - Introduction to Lagrangian Dynamics
description: Slides for PHY 331 Spring 2025, Day 33: Introduction to Lagrangian Dynamics
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, Lagrangian dynamics, action principle, Lagrangian mechanics
url: https://dannycaballero.info/phy331msu/slides/day-33-introduction-to-lagrangian-dynamics.html
---

# Day 33 - Introduction to Lagrangian Dynamics

![bg right width:600px](../images/notes/week12/newton-scared.jpg)

---

# Announcements

* Feedback on Proposals are out; working on updates
* Any Project Questions? Email me! 
    * We can set up a meeting if needed.
* Scarlett is grading HW 5 and 6
* Friday: No Class (DC out of town)
    * **Monday**: Finish Euler-Lagrange Equation; Start Lagrangian Mechanics
    * **Wednesday:** Midterm 2 Help Session
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

# Final Project Rubric

* $P$, **Physics Content (40%)**: 
    - Clear explanation of the physical problem being addressed.
    - Appropriate use of computational methods to analyze the problem.
    - Correctness and accuracy of the results and conclusions drawn from the analysis.
* $C$, **Computational Implementation (30%)**:
    - Code is well-organized, readable, and follows best practices (e.g., comments, variable names).
    - The computational approach is appropriate for the problem and effectively implemented.
    - Code runs without errors and produces the expected output.

---

# Final Project Rubric

* $W$, **Writing and Presentation (20%)**:
    - The essay is well-structured with a logical flow of ideas.
    - Visualizations (if any) are clear, relevant, and enhance the understanding of the content.
    - Proper formatting and adherence to any specified guidelines (e.g., length, citation style).
* $R$, **Reflection and Discussion (10%)**:
    - Thoughtful reflection on the computational approach and its limitations.
    - Discussion of the implications of the results and how they relate to the original problem.
    - Consideration of potential future work or extensions to the analysis.

---

# Final Project Rubric

Each section of the rubric will be scored on a 4.0 scale.

| Criteria                        | Excellent (4.0) | Great (3.5) | Good (3.0) | Fair (2.5) | Poor (2.0) | Missing (0) |
|---------------------------------|------------------|-------------|------------|------------|------------|-------------|

Your grade will be computed based on the weighted average of the above criteria. Your final score (on a 100 scale) will be calculated as follows:

$$\text{Computational Essay Grade} = \dfrac{\left(0.4P + 0.3C + 0.2W + 0.1R\right)}{4}*100$$

Details? Under 'Resources' <https://dannycaballero.info/phy321msu/resources/computational-essay-rubric.html>


---

# Newton's Laws

We use Newton's laws of motion to describe the dynamics of a system:
1. **First Law**: An object at rest remains at rest, and an object in motion continues in motion with the same speed and in the same direction unless acted upon by a net external force.
2. **Second Law**: The acceleration of an object is directly proportional to the net force acting on it and inversely proportional to its mass. Mathematically, this is expressed as:
   $$ \vec{F} = m \vec{a} $$
3. **Third Law**: For every action, there is an equal and opposite reaction. This means that if object A exerts a force on object B, then object B exerts a force of equal magnitude and opposite direction on object A.

---

# Newton's Laws Expectations

* We can describe every interaction on a body using forces
* We can sum up all the forces vectorially in particular coordinate systems (Cartesian, polar, etc.)
* We can derive equations of motion for a system by applying Newton's second law

Sometimes, these expectations can be limiting, especially when dealing with complex systems or when forces are not easily identifiable. 

---

# Newton's Laws in Plane Polar Coordinates

In plane polar coordinates ($r,\phi$), we can express Newton's second law as follows:

$$
\vec{F} = m \vec{a} \implies
\vec{F} = m \left( \ddot{r} - r \dot{\phi}^2 \right) \hat{r} + m \left( r \ddot{\phi} + 2\dot{r}\dot{\phi} \right) \hat{\phi}
$$

where:
- $\ddot{r}$ is the radial acceleration,
- $\dot{\phi}$ is the angular velocity,
- $\ddot{\phi}$ is the angular acceleration,
- $\hat{r}$ and $\hat{\phi}$ are the unit vectors in the radial and angular directions, respectively.

**How?** And what new insights can we gain from this?

---

# Clicker Question 33-1

![bg right width:600px](../images/notes/week12/coordinate-system.png)

The appropriate definition of the $\hat{r}$ vector using Cartesian coordinates ($x,y$) is:

1. $\hat{r} = \left( \cos(\phi), \sin(\phi) \right)$
2. $\hat{r} = \left( \sin(\phi), \cos(\phi) \right)$
3. $\hat{r} = \left(-\sin(\phi), \cos(\phi) \right)$
4. $\hat{r} = \left( \cos(\phi), -\sin(\phi) \right)$
5. None of the above.

---

# Clicker Question 33-2

![bg right width:600px](../images/notes/week12/coordinate-system.png)

The appropriate definition of the $\hat{\phi}$ vector using Cartesian coordinates ($x,y$) is:

1. $\hat{r} = \left( \cos(\phi), \sin(\phi) \right)$
2. $\hat{r} = \left( \sin(\phi), \cos(\phi) \right)$
3. $\hat{r} = \left(-\sin(\phi), \cos(\phi) \right)$
4. $\hat{r} = \left( \cos(\phi), -\sin(\phi) \right)$
5. None of the above.

---

# Clicker Question 33-3

We need to take the derivative of $\hat{r}$ with respect to time. Why should we do this in Cartesian coordinates?

1. The Cartesian coordinates are easier to work with for derivatives.
2. The derivative of $\hat{r}$ in Cartesian coordinates are zero.
3. The unit vector $\hat{r}$ is location dependent.
4. The Cartesian unit vectors do not change with time.
5. Something else?

---

# Summary of Results

With $\vec{r} = r \hat{r}$,

$$\vec{v} = \dot{\vec{r}} = \dot{r} \hat{r} + r \dot{\phi} \hat{\phi}$$

$$\vec{a} = \dot{\vec{v}} = \ddot{r} \hat{r} + \dot{r} \dot{\phi} \hat{\phi} + r \ddot{\phi} \hat{\phi} + r \dot{\phi}^2 \hat{r}$$

This allows us to express Newton's second law in polar coordinates as:

$$
\vec{F} = m \left( \ddot{r} - r \dot{\phi}^2 \right) \hat{r} + m \left( r \ddot{\phi} + 2\dot{r}\dot{\phi} \right) \hat{\phi}
$$

Or

$$F_r = m \left( \ddot{r} - r \dot{\phi}^2 \right) \quad \text{and} \quad F_\phi = m \left( r \ddot{\phi} + 2\dot{r}\dot{\phi} \right)$$


---

# Euler-Lagrange Equation

We found that certain kinds of optimization problems involving functionals could be solved using the **Euler-Lagrange equation**. This equation provides a powerful method to derive the equations of motion for a system based on an action principle.

The Euler-Lagrange equation is given by:

$$
\frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right) - \frac{\partial f}{\partial y} = 0
$$

where $f(y, y', x)$ is a **functional** that depends on the dependent variable $y$, its derivative $y' = \frac{dy}{dx}$, and the independent variable $x$.

---

# The Action Integral

The action integral is central to Lagrangian dynamics. The action $S$ is defined as the integral of a **functional** $L(q,\dot{q},t)$ over time:

$$
S = \int_{t_1}^{t_2} \mathcal{L}(q, \dot{q}, t) \, dt
$$

where:
- $q$ represents the **generalized coordinates** of the system,
- $\dot{q}$ represents the **generalized velocities** (time derivatives of $q$),
- $t$ represents time.

**Hamilton's Principle:** The path the system takes **minimizes (or extremizes) the action $S$**. 

---

# The Lagrangian

The Lagrangian $\mathcal{L}$ is a function that summarizes the dynamics of the system. It is typically defined as:

$$
\mathcal{L}(q, \dot{q}, t) = T - V
$$

where:
- $T$ is the **kinetic energy** of the system (depends on **gen. vel.**, $\dot{q}$),
- $V$ is the **potential energy** of the system (depends on **gen. pos.**, $q$).

The equation of motion is recovered by applying the Euler-Lagrange equation to the Lagrangian (minimizing the action integral).

$$
\frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{q}}\right) - \frac{\partial \mathcal{L}}{\partial q} = 0
$$

---

# Clicker Question 33-4

For a 1D SHO, the kintetic and potential energy are given by:

$$
T = \frac{1}{2} m \dot{x}^2 \quad \text{and} \quad V = \frac{1}{2} k x^2
$$

What are the derivatives of the Lagrangian $\mathcal{L} = T - V$ with respect to $x$ and $\dot{x}$?

1. $\frac{\partial \mathcal{L}}{\partial x} = kx$ and $\frac{\partial \mathcal{L}}{\partial \dot{x}} = m\dot{x}$
2. $\frac{\partial \mathcal{L}}{\partial x} = -kx$ and $\frac{\partial \mathcal{L}}{\partial \dot{x}} = m\dot{x}$
3. $\frac{\partial \mathcal{L}}{\partial x} = kx$ and $\frac{\partial \mathcal{L}}{\partial \dot{x}} = -m\dot{x}$
4. $\frac{\partial \mathcal{L}}{\partial x} = -kx$ and $\frac{\partial \mathcal{L}}{\partial \dot{x}} = -m\dot{x}$
5. None of the above.

---

# Clicker Question 33-5

For the plane pendulum, with $\mathcal{L}(x, \dot{x}, y, \dot{y}, t) = \frac{1}{2} m \left( \dot{x}^2 + \dot{y}^2 \right) - mgy$

We found:

$$\frac{d}{dt}\left(m\dot{x}\right) = 0 \qquad \text{and} \quad \ddot{y} = - g$$

Does that seem right?

1. Yes, it's fine.
2. Maybe, but I'm not sure I can tell you why.
3. No, I know this is wrong, but I'm not sure why.
4. No, this is definitely wrong and I can prove it!

---

# Clicker Question 33-6

For the plane pendulum, we changed the Lagrangian from Cartesian coordinates to plane polar coordinates. In Cartesian, we found the Lagrangian depended on $y,\dot{x},\dot{y}$. In polar, it only depended on $\phi$ and $\dot{\phi}$.

$$\mathcal{L}(x,y,\dot{y}) \longrightarrow \mathcal{L}(\phi, \dot{\phi})$$

What does that tell you about the dimensions of the system? The system is:

1. in 3D space, so it's 3D.
2. described by two spatial dimensions ($x,y$), so it's 2D.
3. described by one spatial dimension ($\phi$), so it's 1D.