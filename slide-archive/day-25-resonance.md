---
marp: true
theme: graph_paper
paginate: true

title: Day 25 - Resonance + Homework Session
description: Slides for PHY 321 Fall 2025, Day 25: Resonance
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, motion, oscillations, resonance
url: https://dannycaballero.info/phy321msu/slides/day-25-resonance.html
---

# Day 25 - Resonance + Homework Session

![width:800px](../images/notes/week9/tuning-fork.png)

---

# Reminders

We started to solve the forced harmonic oscillator equation:

$$\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = f(t)$$

We examined the case of a sinusoidal driving force:

$$\ddot{x} + 2 \beta \dot{x} + \omega_0^2 x = f_0 \cos(\omega t)$$

There's a complimentary case where the driving force is a sine wave:

$$\ddot{y} + 2 \beta \dot{y} + \omega_0^2 y = f_0 \sin(\omega t)$$

---

# Reminders

We combined the two equations into a complex equation using these identities:

$$z(t) = x(t) + i y(t)$$

$$e^{i \omega t} = \cos(\omega t) + i \sin(\omega t)$$

The resulting equation is:

$$\ddot{z} + 2 \beta \dot{z} + \omega_0^2 z = f_0 e^{i \omega t}$$

Notice that there's a homogeneous part ($z_h$) and a particular part ($z_p$).

$$\ddot{z}_h + 2 \beta \dot{z}_h + \omega_0^2 z_h = 0$$

---

# Reminders

The homogeneous part is the solution we've found before with the general solution:

$$z_h(t) = C_1 e^{rt} + C_2 e^{r^* t}$$

where $r = -\beta \pm i \sqrt{\omega_0^2 - \beta^2}$. In the case of a weakly damped oscillator ($\beta^2 < \omega_0^2$), we have:

$$z_h(t) = e^{-\beta t} \left( C_1 e^{-i \sqrt{\omega_0^2 - \beta^2} t} + C_2 e^{+i \sqrt{\omega_0^2 - \beta^2} t} \right)$$

These solutions die out as $t \to \infty$. They are called **transient solutions**.

---

# Solving the particular part

The particular part is the solution to the driven harmonic oscillator equation:

$$\ddot{z}_p + 2 \beta \dot{z}_p + \omega_0^2 z_p = f_0 e^{i \omega t}$$

Assume a sinusoidal solution (frequency, $\omega$) of the form:
$$z_p(t) = C e^{i \omega t}$$

where $C$ is a complex number. Then, we have:

$$-\omega^2 C e^{i \omega t} + 2 i \beta \omega C e^{i \omega t} + \omega_0^2 C e^{i \omega t} = f_0 e^{i \omega t}$$

$$\left(-\omega^2 + 2 i \beta \omega + \omega_0^2\right) C = f_0$$

---

# Amplitude of the particular solution

$$C =\dfrac{f_0}{\left(\omega_0^2-\omega^2 + 2 i \beta \omega\right)}$$

We want to convert this to polar form:

$$C = A e^{-i \delta}$$

where $A$ and $\delta$ are real numbers. We use the complex form to compute the magnitude of the amplitude:

$$A^2 = C \bar{C} = \dfrac{f_0^2}{\left(\omega_0^2-\omega^2 + 2 i \beta \omega \right)\left(\omega_0^2-\omega^2 - 2 i \beta \omega \right)}$$

$$A^2 = \dfrac{f_0^2}{(\omega_0^2 - \omega^2)^2 + 4 \beta^2 \omega^2}$$

---

# Clicker Question 24-5

We found that the square amplitude of the driven harmonic oscillator is:

$$A^2 = \dfrac{f_0^2}{(\omega_0^2 - \omega^2)^2 + 4 \beta^2 \omega^2}$$

When is the amplitude of the driven oscillator maximized?

1. When the driving frequency ($\omega$) is far from the natural frequency ($\omega_0$)
2. When the driving frequency ($\omega$) is close to the natural frequency ($\omega_0$)
3. When the damping ($2\beta$) is weak
4. When the damping ($2\beta$) is strong
5. Some combination of the above

---

# Finding the phase

With,

$$C =\dfrac{f_0}{\left(\omega_0^2-\omega^2 + 2 i \beta \omega \right)} = Ae^{-i\delta}$$

then we can compare the complex forms:

$$f_0 e^{i \delta} = A \left(\omega_0^2-\omega^2 + 2 i \beta \omega \right).$$

Both $f_0$ and $A$ are real numbers, so the phase $\delta$ is the same phase as the complex number:

$$\delta = \tan^{-1}\left(\dfrac{2 \beta \omega}{\omega_0^2 - \omega^2}\right)$$

---

# The Particular Solution

Let's return to the particular solution:

$$z_p(t) = C e^{i \omega t} = A e^{-i \delta} e^{i \omega t} = A e^{i(\omega t - \delta)}$$

$$z_p(t) = A \cos(\omega t - \delta) + i A \sin(\omega t - \delta)$$

So we get solutions to both driven oscillators:

$$x_p(t) = Re(z_p(t)) = A \cos(\omega t - \delta)$$

$$y_p(t) = Im(z_p(t)) = A \sin(\omega t - \delta)$$

These are the **steady-state solutions**. 

They persist as $t \to \infty$ and oscillate at the driving frequency $\omega$.

---

# The Full Solution

$$x(t) = x_h(t) + x_p(t)$$

Here, $x_h(t)$ is the transient solution and $x_p(t)$ is the steady-state solution. 

For weakly damped oscillators, the transient solution can be written in the form:

$$x_h(t) = A_{tr}e^{-\beta t} \cos(\sqrt{\omega_0^2 - \beta^2} t + \delta_{tr})$$

where $A_{tr}$ and $\delta_{tr}$ are real numbers and are the amplitude and phase of the transient solution. Both are determined by the initial conditions.

$$x_p(t) = A \cos(\omega t - \delta)$$

where $A$ and $\delta$ are real numbers and are the amplitude and phase of the steady-state solution.

---

# The Full Solution

The transient plus the steady-state solution is the full solution:

$$x(t) = A_{tr}e^{-\beta t} \cos(\sqrt{\omega_0^2 - \beta^2} t + \delta_{tr}) + A \cos(\omega t - \delta)$$

As $t \to \infty$, the transient solution dies out and the steady-state solution persists.

$$x(t \to \infty) = A \cos(\omega t - \delta)$$

where 

$$A = \dfrac{f_0}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4 \beta^2 \omega^2}}$$
$$\delta = \tan^{-1}\left(\dfrac{2 \beta \omega}{\omega_0^2 - \omega^2}\right)$$

---

# Resonance

The amplitude of the steady-state solution is:

$$A^2 = \dfrac{f_0^2}{(\omega_0^2 - \omega^2)^2 + 4 \beta^2 \omega^2}$$

We change $\omega_0$ and observe how the amplitude changes.

![bg right width:600px](../images/notes/week9/resonance.png)

---

# Achieving resonance

The denominator of the equation controls the amplitude:

$$(\omega_0^2 - \omega^2)^2 + 4 \beta^2 \omega^2$$

**Case 1:** Tune $\omega_0$ to be close to $\omega$. *Car Radio tuning* 

With $\omega_0 = \omega$, the amplitude is:

$$A^2 = \dfrac{f_0^2}{4 \beta^2 \omega^2}$$

---

# Achieving resonance

The denominator of the equation controls the amplitude:

$$(\omega_0^2 - \omega^2)^2 + 4 \beta^2 \omega^2$$

**Case 2:** Tune $\omega$ to be close to $\omega_0$. *Pushing a swing* 

Find the $\omega$ that maximizes the amplitude by taking the derivative with respect to $\omega$:

$$\dfrac{d}{d\omega} \left((\omega_0^2 - \omega^2)^2 + 4 \beta^2 \omega^2\right) = 0$$

$$2(\omega_0^2 - \omega^2)(-2\omega) + 8 \beta^2 \omega = 0$$

$$4\omega(\omega^2 - \omega_0^2 + 2 \beta^2) = 0$$

$$\omega = 0 \qquad \omega = \sqrt{\omega_0^2 - 2 \beta^2}$$

---

# HW6 Exercise 2 Morse Potential as an SHO

If the potential has a local minimum, we can often find SHO approximation for that potential near the local minimum. 

The [Morse potential](https://en.wikipedia.org/wiki/Morse_potential) is a convenient model for the potential energy of a diatomic molecule. The potential is a radial one and thus one-dimensional. It is given by,

$$U(r) = A\left[ \left(e^{(R-r)/S}-1\right)^2-1\right]$$

where the distance between the centers of the two atoms is $r$, and the constants $A$, $R$, and $S$ are all positive. Here $S<<R$.

* 2a (2pt) Sketch (or plot) the potential as a function of $r$.

---

# HW6 Exercise 2 Morse Potential as an SHO


$$U(r) = A\left[ \left(e^{(R-r)/S}-1\right)^2-1\right]$$


* 2b (3pt) Find the equilibrium position of the potential, i.e. the position where the potential is at a minimum. We will call this $r_e$.
* 2c (3pt) Rewrite the potential in terms of the displacement from equilibrium, $r = r_e + x$. Expand the potential to second order in $x$.
* 2d (2pt) Find the effective spring constant, $k$, for the potential near the minimum. What is the frequency of small oscillations about the minimum?

---

# HW6 Exercise 4, Toy Potential

Consider a toy potential of the form,

$$U(r) = U_0\left(\dfrac{r}{R}+\lambda^2\frac{R}{r}\right)$$

where $U_0$, $R$, and $\lambda$ are all positive constants and the domain of the potential is $0<r<\infty$. 

* 4a (2pt) Sketch (or plot) the potential as a function of $r$.

---

# HW6 Exercise 4, Toy Potential

$$U(r) = U_0\left(\dfrac{r}{R}+\lambda^2\frac{R}{r}\right)$$

* 4b (3pt) Find the equilibrium position of the potential, i.e. the position where the potential is at a minimum. We will call this $r_e$.
* 4c (5pt) Rewrite the potential in terms of the displacement from equilibrium, $r = r_e + x$. Expand the potential to second order in $x$. What is the effective spring constant, $k$, for the potential near the minimum? What is the frequency of small oscillations about the minimum?