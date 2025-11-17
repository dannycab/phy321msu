---
marp: true
theme: graph_paper
paginate: true

title: Day 35 - Lagrangian Examples
description: Slides for PHY 321 Spring 2025, Day 35: Lagrangian Examples
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, Lagrangian, examples
url: https://dannycaballero.info/phy321msu/slides/day-35-lagrangian-examples.html

---

# Day 35 - Lagrangian Examples

![bg right width:500px](../images/notes/week13/lagrange-pooh.jpeg)

---

# Announcements

* Last "Class" Week
* Homework 8 due Friday, Nov 21st (late after Nov 26th)
* Next Week: Project Work and Discussion
* Last Week: Presentations
* Final Project Due Dec 8th (no later than 11:59 pm)
* **No Final Exam**

---

# Complete Google Form

## By November 21st

Reporting your group members for the final project and a short summary of your project idea for sharing with the class.

<https://forms.gle/iPKR9EDAaHW3GirN7>

![bg left width:350px](../images/notes/week13/group_form_qr.png)

---

## Reminders

We used the Lagrangian formalism to derive the equations of motion for a plane pendulum. We chose the $x$ and $y$ coordinates.

$$T(\dot{x}, \dot{y}) = \dfrac{1}{2} m (\dot{x}^2 + \dot{y}^2) \quad V(y) = mgy$$

$$\mathcal{L} = T - V = \dfrac{1}{2} m (\dot{x}^2 + \dot{y}^2) - mgy$$

This gave us the following derivatives for the Lagrangian:

$$\frac{\partial \mathcal{L}}{\partial x} = 0 \quad \frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{x}} \right) = \frac{d}{dt} \left( m\dot{x} \right) = 0$$
$$\frac{\partial \mathcal{L}}{\partial y} = -mg \quad \frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{y}} \right) = -m\ddot{y}$$

---

# We made a mistake by not including the constraint

We made a mistake by not including the constraint $x^2 + y^2 = L^2$ in our Lagrangian.

We can change variables to $r$ and $\phi$.
$$x = r \cos(\phi) \quad y = r \sin(\phi)$$

$$T(\dot{x}, \dot{y}) = \dfrac{1}{2} m (\dot{x}^2 + \dot{y}^2) = \dfrac{1}{2} m \left( r^2 \dot{\phi}^2 + 2r\dot{r}\dot{\phi} + \dot{r}^2 \right) = T(r, \dot{r}, \phi, \dot{\phi})$$
$$V(y) = mgy = mg r \sin(\phi) = V(r, \phi)$$

Now we include the constraint $r = L$, so that $\dot{r} = 0$.

$$T(\phi, \dot{\phi}) = \dfrac{1}{2} m L^2 \dot{\phi}^2 \quad V(\phi) = mgL \cos(\phi)$$

$$\mathcal{L} = \dfrac{1}{2} m L^2 \dot{\phi}^2 - mgL \cos(\phi)$$

---

# Clicker Question 35-1

With $\mathcal{L} = \dfrac{1}{2} m L^2 \dot{\phi}^2 - mgL \cos(\phi)$, we can find the equations of motion. 

$$\dfrac{\partial \mathcal{L}}{\partial \phi} - \dfrac{d}{dt} \left( \dfrac{\partial \mathcal{L}}{\partial \dot{\phi}} \right) = 0$$

Which of the following equations of motion is correct?

1. $\ddot{\phi} = -\frac{g}{L} \sin(\phi)$
2. $\ddot{\phi} = -\frac{g}{L} \cos(\phi)$
3. $\ddot{\phi} = -\sqrt{\frac{g}{L} \sin(\phi)}$
4. $\ddot{\phi} = -\sqrt{\frac{g}{L} \cos(\phi)}$
5. None of these

---

# Clicker Question 35-2

For the Atwood's machine, $M$ is connected to $m$ by a string of length $l$. Each mass has a length of string extended as measured from the center of the pulley ($R$) of $y_1$ and $y_2$, respectively. The string wraps around half the pulley. 

Which of the following represents the equation of constraint for the system?

1. $y_1 + y_2 = l - R \phi$
2. $y_1 - y_2 = l + R \phi$
3. $y_1 + y_2 = l - \pi R$
4. $y_1 - y_2 = l + \pi R$
5. None of these

**Take the time derivative of the constraint equation.** What do you notice?

---

# Clicker Question 35-3

With a Lagrangian of the form $\mathcal{L} = \frac{1}{2}(M+m)\dot{y}^2_1 - (M-m)gy_1$, we can find the **generalized forces** and **generalized momenta**.

$$F_{y_1} = \frac{\partial \mathcal{L}}{\partial y_1} = -\frac{\partial V}{\partial y_1} \quad p_{y_1} = \frac{\partial \mathcal{L}}{\partial \dot{y}_1} = \frac{\partial T}{\partial \dot{y}_1}$$

What are $F_{y_1}$ and $p_{y_1}$ for the Atwood's machine?

1. $F_{y_1} = -mg$ and $p_{y_1} = m\dot{y}_1$
2. $F_{y_1} = -Mgy_1$ and $p_{y_1} = M\dot{y}_1$
3. $F_{y_1} = -(M-m)g$ and $p_{y_1} = (M+m)\dot{y}_1$
4. $F_{y_1} = -(M+m)g$ and $p_{y_1} = (M-m)\dot{y}_1$
5. None of these

---

# Clicker Question 35-4

Now, we allow the pulley (mass, $M_p$) to rotate. The Lagrangian is given by:
$$\mathcal{L} = \frac{1}{2}(M+m)\dot{y}_1^2 + \frac{1}{2}I\dot{\phi}^2 - (M-m)gy_1$$

Where $I$ is the moment of inertia of the pulley. What is the moment of inertia of the pulley?

1. $I = \frac{1}{2}M_pR^2$
2. $I = \frac{1}{3}M_pR^2$
3. $I = M_pR^2$
4. $I = \frac{1}{4}M_pR^2$
5. None of these

---

# Clicker Question 35-5

The rope moves without slipping on the pulley. A rotation of $R d\phi$ corresponds to a displacement of $dy_1$ for the first mass, $M$. What is the **new** equation of constraint for the system?

1. $y_1 + y_2 = l - R \phi$
2. $dy_1 = R d\phi$
3. $y_1 = R\phi$
4. $\dot{y}_1 = R \dot{\phi}$
5. More than one of these
