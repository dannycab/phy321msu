---
marp: true
theme: king
paginate: true

title: Day 03 - Computing Setup
description: Slides for PHY 321 Spring 2025, Day 03: Computing Setup
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, computing, ai, policy
url: https://dannycaballero.info/phy321msu/slides/day-03-computing-setup.html

---

# PHY 321 - Day 03

Skim *The Manifesto for Teaching and Learning in a Time of Generative AI*

![QR Code for Paper](./images/ai_paper.png)

<https://openpraxis.org/articles/10.55982/openpraxis.16.4.777>

---

![bg 100%](./images/strawberry-ollama.png)

---

# Announcements

* Homework 1 is due next Friday
* Help sessions will start next week
* No class on Monday (Labor Day)
* Complete the [student information poll](forms.office.com/r/LWEDtfkcg9) by today, please

---

# Student Information Poll

![QR Code](./images/sis_link.png)

**Fill out now 😻**

---

# Office Hours Poll

![QR Code](./images/office_hours_poll.png)

**Fill out now 😻**

---

# Generative AI

*Generative AI* is a type of artificial intelligence that can generate new data from existing data.

* It is an **extractive** technology that has mined a vast data set.
* It is a **probabilistic** technology that uses statistical models to generate new data.
* It is **not** a **creative** technology that can generate new ideas, concepts, or products.
* It is **not** a **truthful** technology that can generate new data that is intrinsically true.

**The "Grow At Any Cost" approach to generative AI is destroying communities, violating federal and international laws, upending climate progress, and consolidating power in the hands of a few.** 

---

# Generative AI Energy Consumption

![bg right:20%](./images/a100.png)

* The max power of a single A100 chip is 400W.
* Assume the compute needed to perform a simple generation task takes roughly 1s.

**How much energy would you use to complete a single homework assignment?**

**If every physics/astro undergrad used generative AI for their assignments in a week, how much energy would we use?**

**If everyone on campus uses generative AI in a week, how much energy is used?**


---

# Generative AI Water Consumption

![bg right:20%](./images/a100.png)

It takes about 9 liters of water per kWh (1 kWh = $3.6\times10^6$ J) to evaporate the heat from a GPU server.

**How much water is used if everyone on campus uses GenAI in a week?**

**How many homes could be serviced with that much water usage?**

---

# And yet,

* Generative AI can be used productively.
* Generative AI can support accessibility.
* Generative AI can support creativity.
* Generative AI can support learning.

The complexity and tension of these issues are why we need to develop a policy together.

**We will all live with the consequences of Generative AI, but y'all will for longer, so this policy must be yours.**

---


# Creating a Generative Artificial Intelligence Policy

We define **productivity** as the ability to use Generative AI to deepen your understanding of Classical Mechanics.

## Take five minutes to answer the following for yourself:

1. What are ways that you think that AI can be used productively in our classroom?
2. What are ways that you think that AI can be used unproductively in our classroom?
3. What do you think are acceptable uses of AI in our classroom?
4. What do you think are unacceptable uses of AI in our classroom?
5. How should we document the use of AI in our classroom?
6. Once we define a policy, how should we collectively enforce it?

---

# Creating a Generative Artificial Intelligence Policy

We define **productivity** as the ability to use Generative AI to deepen your understanding of Classical Mechanics.

## Share your ideas are your table. Develop a consensus on the following:

1. What do y'all think are acceptable uses of AI in our classroom?
2. What do y'all think are unacceptable uses of AI in our classroom?
3. How should we document the use of AI in our classroom?
4. Once we define a policy, how should we collectively enforce it?

Add your answers to the form at the following link: [https://forms.office.com/r/Bsh6ugKQ9Y](https://forms.office.com/r/Bsh6ugKQ9Y)

---

# Getting started with VS Code

- Download VS Code from <https://code.visualstudio.com/>
- Install it and then let's download a notebook 
- Open the notebook in VS Code

---

# Homework 1 Exercise 3

* 3a (2pt) Show (using the fact that multiplication of reals is distributive) that $\boldsymbol{a}\cdot(\boldsymbol{b}+\boldsymbol{c})=\boldsymbol{a}\cdot\boldsymbol{b}+\boldsymbol{a}\cdot\boldsymbol{c}$.

---

# Homework 1 Exercise 3

* 3b (3pt) Use this result to argue that the small amount of work $dW$ done over a distance $d\mathbf{r}$ only results from $F_{\parallel}$ the force component along the instantaneous velocity $\mathbf{v}$ and not $F_{\perp}$, the component perpendicular to it. What about the full integral of the work $W = \int_P dW$ where $P$ is some path? From which force does the work get done by, $F_{\parallel}$, $F_{\perp}$, both, neither?

---

# Homework 1 Exercise 3

* 3c (2pt) Show that (using product rule for differentiating reals)  $\frac{d}{dt}(\boldsymbol{a}\cdot\boldsymbol{b})=\boldsymbol{a}\cdot\frac{d\boldsymbol{b}}{dt}+\boldsymbol{b}\cdot\frac{d\boldsymbol{a}}{dt}$

---

# Homework 1 Exercise 3

* 3d (3pt) Use this to demonstrate that the time rate of change for the kinetic energy, $dK/dt$ for a circular orbiting object is zero. Start from definition of kinetic energy that uses the dot product: $K = 1/2 m \mathbf{v} \cdot \mathbf{v}.$ **It might help to draw a sketch of the velocity, force, and acceleration vectors.** 