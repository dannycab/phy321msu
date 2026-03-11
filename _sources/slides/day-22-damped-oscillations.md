---
marp: true
theme: graph_paper
paginate: true

title: Day 22 - Damped Oscillations
description: Slides for PHY 321 Spring 2026, Day 21: Oscillations
author: Prof. Danny Caballero <caball20@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, oscillations
url: https://dannycaballero.info/phy321msu/slides/day-22-damped-oscillations.html
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


# Day 22 - Damped Oscillations

![bg right width:600px](../images/notes/week9/car_shock.png)

Shock absorbers are a type of damped oscillator. 

They must be tuned to the weight of the car and the type of driving.

---

## Announcements

* Homework 5 is due on today (late on Sunday)
  * Anyone may request an extension for HW5 up to one week, no questions asked. Just email me.
* Homework 6 is due the following Friday (late on Sunday)
  * Again, anyone may request an extension for HW6 up to one week, no questions asked. Just email me.
* Class next Monday, maybe? 

---


## Reminders

We are solving the harmonic oscillator equation:
$$\ddot{x} + \omega_0^2 x = 0$$

We have general solutions of the form:

$$x(t) = A\cos(\omega_0 t + \delta)$$
$$x(t) = A\sin(\omega_0 t + \delta)$$
$$x(t) = A\cos(\omega_0 t) + B\sin(\omega_0 t)$$

We seek complex solutions of the form:

$$x(t) = Ae^{(i\omega_0 t + \delta)}$$

---

## Reminders

We denote a complex number in "Cartesian form" as:

$$z = x + iy$$

Here, $x$ is the real part and $y$ is the imaginary part; both are real numbers.

$$Re(z) = x \qquad Im(z) = y$$

The complex conjugate of $z$ is:

$$z^* = \bar{z} = x - iy$$

---

## Reminders

We can also write a complex number in "polar form" as:

$$z = Ae^{i\delta}$$

where $A$ is the magnitude of the complex number and $\delta$ is the phase. Both are real numbers.

$$A = |z| = \sqrt{x^2 + y^2} \qquad \delta = \tan^{-1}\left(\frac{y}{x}\right)$$

The complex conjugate of $z$ is:
$$z^* = \bar{z} = Ae^{-i\delta}$$

---

## Reminders

The product of a complex number and its complex conjugate is:

$$z\bar{z} = (x + iy)(x - iy) = x^2 + y^2 = A^2$$

The sum of a complex number and its complex conjugate is:

$$z + \bar{z} = (x + iy) + (x - iy) = 2x = 2Re(z)$$

The difference of a complex number and its complex conjugate is:

$$z - \bar{z} = (x + iy) - (x - iy) = 2iy = 2iIm(z)$$

---

## Clicker Question 22-1

A complex number $z$ is plotted in the complex plane such that $z$ lies in the second quadrant.

![bg right width:600px](../images/notes/week9/plane2.png)

Where does the complex conjugate $z^*$ lie?
1. In the first quadrant.
2. In the second quadrant.
3. In the third quadrant.
4. In the fourth quadrant.


---

# Visualizing the Complex Solution

We constructed a solution of the form:

$$Ae^{i(\omega t-\delta)}$$

We can plot it in the complex plane and see the real and imaginary parts, and how they change in time.

---

## Visualizing the Complex Solution

We can plot the solution on the complex plane. For this, $\delta = \pi/4$, and the amplitude is $A=1$.

The solution rotates counterclockwise in the complex plane, following the rainbow from violet to red.

![bg right width:500px](../images/notes/week9/complex_plane.png)

---

## Projecting the Real Solution

The real part is just the projection of the complex solution onto the real axis. Just how far along the real axis is the solution at any given time. 

That looks like a time trace, but not quite, it's the real projection. The colors scheme is the same as before.

![bg right width:500px](../images/notes/week9/real_part.png)


---

## The Time Trace of the Solution

We just flip the axes to produce the time trace that you are used to seeing. The color scheme is the same as before.

![bg right width:500px](../images/notes/week9/time_trace.png)

---

## Table Activity 22-2

We constructed a solution for the weakly damped harmonic oscillator:

$$x(t) = e^{-\beta t} \left(C_1e^{i\omega_1 t} + C_2e^{-i\omega_1 t}\right)$$

where $\omega_1 = \sqrt{\omega_0^2 - \beta^2}$.

* What is the physical meaning of $\beta$? 
* Sketch this solution, you can choose parameters, or just roughly sketch it.
* What happens to the amplitude of the solution as time goes on?
* Can you describe the mathematical "envelope" of the solution?
* What is the physical meaning of this envelope?

**Click when you and your table are done.**

---

## Exercise 3

The apparatus below is a massless wheel of radius $R$ that is mounted to a frictionless axle. A small, dense piece of clay with mass $M$ is glued to edge of the wheel as shown. Another mass $m$ hangs from a massless string that is wrapped around the wheel. We can assume the string is inextensible and does not slip, and the system is in a uniform gravitational field.

![bg width:500px right](../images/assignments/5.4-apparatus.png)

---

## Exercise 3

We can show that this complicated system is still one-dimensional (at least in space) and then we can see the effects of parameters like $m/M$.

* In terms of the rotation angle $\phi$ of the wheel, write down the total potential energy $U(\phi)$ of the system of both masses. Take note of any constraints that you use to write this as a 1D problem. When working this kind of problem, every object-Earth pair has gravitational potential energy and we must have the same zero of potential energy for every pair.

---

## Exercise 3

* Use this potential energy to find  values of $m$ and $M$ for which there are "fixed points", "critical points", or what we sometimes call "equilibrium points". The language we use comes from different fields, but the concept is the same. What is the condition for the existence of any critical points?

* Describe the fixed points, determine their stability, and explain why they make sense in terms of the expected motion.

---

## Exercise 3

* Plot the potential energy for two different values of $m/M$ and explain the differences in the potential energy graphs. Consider cases when you observe very different motion. Think about an initial condition where the mass $m$ is at rest and the wheel is at rest. What happens when you release the mass $m$ for your two cases?

* Determine the value of $m/M$ for which the system begins to exhibit oscillations (if released from $\phi=0$). 