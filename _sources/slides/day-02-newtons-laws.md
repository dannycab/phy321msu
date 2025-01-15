---
marp: true
theme: gaia
_class: lead
paginate: true
---

# Day 02 - Newton's Laws

$$\mathbf{F}_{net} = m \mathbf{a}$$

![bg right:40%](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Portrait_of_Sir_Isaac_Newton%2C_1689_%28brightened%29.jpg/850px-Portrait_of_Sir_Isaac_Newton%2C_1689_%28brightened%29.jpg)

---

## Announcements

* Homework 1 is due next Friday
* Help sessions will start next week
* Friday's class will include AI policy discussion
    * We will work Problem 1 together and start discussing Problem 6

---

## Goals for this week

### Be able to answer the following questions.

* What is Classical Mechanics?
* How can we formulate it?
* What are the essential physics models for single particles?
* What mathematics do we need to get started?

---

<br/>
<br/>

# Take 2 min to write down what comes to mind when asked:
<br>

# What is "Classical" Physics?

---

## Classical Mechanics

### Modeling large, slow-moving objects

Newton's Laws are but one of a number of formulations:
* Lagrangian Mechanics
* Hamiltonian Mechanics
* Dynamical Systems Theory
* ...

![bg right 100%](https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Modernphysicsfields.svg/640px-Modernphysicsfields.svg.png)

--- 

### Classical Mechanics is still very relevant

Tiny Limbs and Long Bodies: Coordinating Lizard Locomotion
[Research Lab](https://research.gatech.edu/tiny-limbs-and-long-bodies-coordinating-lizard-locomotion) & [Link to Video](https://www.youtube.com/watch?v=Qme07fA3Fj4)


[![Tiny Limbs and Long Bodies: Coordinating Lizard Locomotion](https://img.youtube.com/vi/Qme07fA3Fj4/0.jpg)](https://www.youtube.com/watch?v=Qme07fA3Fj4)

---

## Think-Pair-Share

We used a tilted coordinate system ($x-y$ plane) to analyze the motion of a block on an inclined plane. How can we check that we did the gravitational force decomposition correctly?

Recall:
* $F_{\text{gravity}},x = m g \sin(\theta)$
* $F_{\text{gravity}},y = m g \cos(\theta)$

Come up with at least two checks.

---

## Clicker Question 2-1

The formal definition of a Taylor series expansion around a point $a$ is:

$$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \ldots$$

This formula makes me feel:

1. Confident, I got this.
2. A little nervous, but I think I remember.
3. Uncomfortable, I don't remember this.
4. I have no idea what this is.

---

## Think-Pair-Share

We derived the following differential equation for the falling ball in one-dimension:

$$\frac{d^2 y}{dt^2} = -g - \frac{b}{m} \frac{dy}{dt} - \frac{c}{m} \left(\frac{dy}{dt}\right)^2$$

Let's assume the turbulent drag term is negligible. Is there an anti-derivative of the right-hand side of this equation? If so, what is it?

$$\frac{dv}{dt} = -g - \frac{b}{m}v$$

