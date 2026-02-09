---
marp: true
theme: graph_paper
paginate: true

title: Day 12 - Conservation of Energy
description: Slides for PHY 321 Spring 2026, Day 12: Conservation of Energy
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-12-conservation-of-energy.html
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

## Day 12 - Conservation of Energy

![bg right width:600px](../images/notes/week5/conservation-of-energy.png)

We observe that energy is conserved everywhere we look!

$$\Delta E_{system} = W + Q$$



---

## Announcements

* **Homework 4 is posted** (due Friday; late after Sunday)
* **First midterm is coming up** (assigned Monday, 16 Feb)
    * One exercise will ask you to get started on your final project planning. 
    * *Who are you gonna work with? What are you interested in studying?* Start thinking about this!
* **There will be no class/office hours on Friday** 
    * Observance plans are posted on Spartans Together: <https://spartanstogether.msu.edu/plans-feb-13-2026>
* **Need help this week?** Make an appointment with Danny: <https://cal.com/dannycaballero/phy-321>

------

## Reminder of our Midterm Procedures

* The take-home midterms will be open for almost two weeks; you can often start some exercises early as they cover older material.
* They are meant to be challenging, but we will provide you with the resources and support you need to complete them.
* There is no homework due during the period in which the midterm is assigned.
* In contrast to homework assignments, DC will not work any exercises directly

You may work closely together with me, Mihir, and your classmates, but you and your partner must write up your own solutions.

---

## Seminars this week


### WEDNESDAY, February 11, 2026    
 
Astronomy Seminar, 1:30 p.m., BPS 1400 & Zoom 
Speaker: Evan Kirby, Notre Dame
Title: TBA
Zoom Link: https://msu.zoom.us/j/93334479606?pwd=OtIXPWhRPBfzYu53sl3trSJlaBYI7C.1
Passcode:  825824

---

## Seminars this week


### WEDNESDAY, February 11, 2026   
 
FRIB Nuclear Science Seminar, 3:30 p.m., FRIB 1300 & Zoom
Speaker: Kyle Godbey, FRIB
Title: What’s Driving the New Era of Discovery in Nuclear Science?
Zoom Link: https://msu.zoom.us/j/99975564296?pwd=e3puzoZ4Yu7m6CiCf7SWiaKjvxgCwu.1
Passcode: 569117
 
---

## Seminars this week

### FRIDAY, February 13, 2026    
 
IReNA Online Seminar, 2:00 pm, Zoom
Light refreshments at 1:50pm in 2025 Nuclear Conference Room - FRIB
Hosted by: Artemis Tsantiri (University of Regina, Canada)
Speaker: Thanassis Psaltis, Saint Mary’s University - Canada
Title: Nuclear physics constraints on the γ-ray signatures of core-collapse supernovae
Zoom Link: https://msu.zoom.us/j/827950260
Password: CENAM

---


## This Week's Goals

* Remind ourselves of the concept of energy and energy conservation
* Apply the conservation of energy to a variety of systems
* Develop the mathematical tools to analyze energy conservation in more complex systems
* Connect our new understanding of energy conservation to our previous work on forces and motion

---

## Clicker Question 12-1

Which of the following are true about a point particle? (Use 1/A - True, 2/B - False)

12-1a. A point particle has no size. 
12-1b. A point particle can have no mass.
12-1c. A point particle can have no charge.
12-1d. A point particle can have no internal energy.

---

## Clicker Question 12-2

Einstein's proposed total energy for a particle of mass $m$ moving at speed $v$ is given by $E = \gamma m c^2$, where $\gamma = 1/\sqrt{1 - v^2/c^2}$.  We take the limit as $v/c \to 0$ to find the total energy of a particle at rest. Which terms below appear in the Taylor expansion of $\gamma$ in powers of $v/c$?

| a | b | c | d |
|---|---|---|---|
| $1$ | $v/c$ | $(v/c)^2$ | $(v/c)^3$ |

1.) a only 2.) a and b 3.) a and c

4.) b and d 5.) all terms


---

## Clicker Question 12-3

Which of the following are statements of the conservation of energy?

1. The total energy of a system is constant.
2. $\Delta E_{system} = 0$
3. $\Delta E_{system} = W + Q$
4. $\frac{dE_{system}}{dt} = 0$
5. All of the above

---

## Conservation of Energy

**General Principle**: Energy is conserved in every process.

$$\Delta E_{sys} = W + Q$$

**Isolated System**: No work or heat is exchanged with the surroundings.

$$\Delta E_{sys} = 0$$

**Point Particle**: A model that allows us to ignore the internal structure of an object.

$$\Delta K =  W_{\text{ext}}$$


---

## The Potential Energy Function (SHO, $F_{s} = -kx$)

$$\Delta K = W_{s}$$

$$\dfrac{1}{2} m v_f^2 - \dfrac{1}{2} m v_i^2 = \int_{x_i}^{x_f} F_s dx = - \int_{x_i}^{x_f} kx dx$$

$$\dfrac{1}{2} m v_f^2 - \dfrac{1}{2} m v_i^2 = - \dfrac{1}{2} k x_f^2 + \dfrac{1}{2} k x_i^2$$

$$\dfrac{1}{2} m v_f^2 + \dfrac{1}{2} k x_f^2 = \dfrac{1}{2} m v_i^2 + \dfrac{1}{2} k x_i^2$$

$$K_f + U_{s,f} = K_i + U_{s,i}$$

$$U_s = \dfrac{1}{2} k x^2$$

---

## Clicker Question 12-5

The gravitation force near the Earth's surface is given by $\vec{F} = -mg\hat{z}$. What is the potential energy function for this force? Choose $+\hat{z}$ to be up.

1. $U = -mgz$
2. $U = mgz$
3. $U = -mgz + U_0$
4. $U = mgz + U_0$
5. None of the above

---

## Clicker Question 12-6

A model for a lattice chain acting on a electron is given by $F(x) = - F_0 \sin\left(\dfrac{2\pi x}{b}\right)$. What is the potential energy function for this force?

1. $U = -F_0 \cos\left(\dfrac{2\pi x}{b}\right)$
2. $U = F_0 \cos\left(\dfrac{2\pi x}{b}\right)$
3. $U = -\dfrac{F_0 b}{2\pi} \cos\left(\dfrac{2\pi x}{b}\right)$
4. $U = \dfrac{F_0 b}{2\pi} \cos\left(\dfrac{2\pi x}{b}\right)$
5. None of the above

---

## Clicker Question 12-7

I say "Stokes' Theorem" and you say...

![Gravedigger bg left ](../images/notes/week5/gravedigger.png)

1. HELL YEAH BROTHER 🤘
2. I'm not sure what that is 🤷
3. DEAR GOD WHY?!?! 😭

---

## Clicker Question 12-8

The curl of a vector field is given by $\nabla \times \vec{F}$. If the curl of a vector field is zero, what can we say about the vector field?

1. It is a conservative force
2. It is a non-conservative force
3. It is a constant force
4. It is a force that does no work

--- 

## Clicker Question 12-9

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

## Clicker Question 12-10

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

## Clicker Question 12-11

Consider a vector field with zero curl: $\nabla \times \vec{F} = 0$. Which of the following statements is true?

1. The field is conservative
2. $\int \nabla \times \vec{F} \cdot d\vec{A} = 0$
3. $\oint \vec{F} \cdot d\vec{r} \neq 0$
4. $\vec{F}$ is the gradient of some scalar function, e.g., $\vec{F} = - \nabla U$
5. Some combination of the above