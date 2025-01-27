---
marp: true
theme: graph_paper
paginate: true

title: Day 06 - Making Classical Models
description: Slides for PHY 321 Spring 2025, Day 06: Making Classical Models
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-06-making-classical-models.html

---

# Day 06 - Making Classical Models

![bg right:60%](../images/notes/week3/von_karman.png)

---

# Plane Polar Coordinates Warm-Up

We introduced plane polar coordinates ($r,\phi$). For any position vector, $\vec{R}$, we can write:

$$\vec{R} = \left|\vec{R}\right|\hat{r} = r\hat{r}$$

where $r$ is the magnitude of $\vec{R}$, and $\hat{r}$ is the radial unit vector.

Find $\dot{\vec{R}} = \frac{d\vec{R}}{dt}$. Get as far as you can. Our answer will be in terms of $\hat{r}$ and $\hat{\phi}$.

**Remember the chain rule and Cartesian unit vectors are fixed in space/time**

$\hat{r} = \cos(\phi)\hat{x} + \sin(\phi)\hat{y} \qquad \hat{\phi} = -\sin(\phi)\hat{x} + \cos(\phi)\hat{y}$
$\frac{d}{d\phi} \cos \phi = -\sin \phi \qquad \frac{d}{d\phi} \sin \phi = \cos \phi$

---

# Day 06 - Making Classical Models

![bg right:60%](../images/notes/week3/von_karman.png)

---

# Announcements

- Homework 2 is due Friday
- Video recordings have continued to fail.
- Updated office hours:

---

# Goals for Week 3

- Be able to answer the following questions.
    - What is Mathematical Modeling?
    - What is the process for analyzing these models?
- Be able to solve "Simple" Motion Problems with Newton's Laws.

---

# Modeling Video

[<img src="https://img.youtube.com/vi/dkTncoPqo5Y/maxresdefault.jpg" width="800" alt="Modeling Video" />](https://www.youtube.com/watch?v=dkTncoPqo5Y)

Source: <https://www.youtube.com/watch?v=dkTncoPqo5Y>

--- 

# What is your experience with modeling?

## Take 2-3 min to think about your prior physics classes
- What models have you used? What makes that a model?
- What made a that model good or not so good?
- What kinds of things could you do to make a better model?

---

# Vortex Shedding

- At higher Reynolds numbers, flow around objects becomes unstable.
- This instability can lead to the formation of vortices.
- This "shedding" of vortices can lead to vibrations and noise.

![bg right:60%](../images/notes/week3/von_karman.png)

---

# Model of vortex shedding behind a cylinder

- Controlling vortex shedding is important in many engineering applications.

![width:1000px](../images/notes/week3/vortex-shedding.png)
<!-- <img src="../images/notes/week3/vortex-shedding.png" width="100%"> -->

<p><small><i>Giosan, Ioan, and P. Eng. "<b>Vortex shedding induced loads on free standing structures</b>" Structural Vortex Shedding Response Estimation Methodology and Finite Element Simulation 42 (2013).</i></small></p>

---

# Renewables: Wind Turbines

## Thorntonbank Wind Farm 

### North Sea off the coast of Belgium

*Notice the cylindrical shape of the support structure.*

![bg right:40%](https://upload.wikimedia.org/wikipedia/commons/b/ba/Windmills_D1-D4_%28Thornton_Bank%29.jpg)



---

# Clicker Question 6-1

The SHO is a useful model: $m\ddot{x} = -kx$. 

Assume the **restoring force is anti-symmetric** about the equilibrium position, what is the next term model?

1. $\sim x^2$ 
2. $\sim x^3$
3. $\sim x^4$
4. $\sim x^5$

![bg right w:80%](../images/notes/week3/sho_horizontal.png)


---

# Clicker Question 6-2

Assuming a **linear model** for Air Resistance $\sim bv$, we obtained this EOM for a falling ball:

$$\ddot{y} = -g + \frac{b}{m}\dot{y}$$


What happens when $\ddot{y} = 0$?
1. The ball stops moving ($v = 0$).
2. The ball reaches a velocity of $mg/b$.
3. The ball reaches a terminal velocity.
4. I'm not sure.

---

# Clicker Question 6-3

For the system of **Linear Drag in 1D**, we found a solution for the velocity as a function of time, with $v = 0$ at $t = 0$.
$$v(t) = v_{term}\left(1-e^{-\dfrac{bt}{m}}\right)$$

where $v_{term} = \sqrt{\frac{mg}{b}}$. 

---

![bg right w:100%](../images/notes/week3/cq6-3.png)


# CQ 6-3

**Which sketch could be correct for the velocity of the ball?**

---

# Clicker Question 6-4

For the system of **Quadratic Drag in 1D**, we found a solution for the velocity as a function of time, with $v = 0$ at $t = 0$.

$$v(t) = v_{term}\tanh(gt/v_{term})$$

where $v_{term} = (mg/c)^{1/2}$. Do the units make sense? What are the units of $\left[gt/v_{term}\right]$? 
1. Yes, the units for $\left[gt/v_{term}\right]$ are $m/s$;both sides have the same units.
2. No, the units for $\left[gt/v_{term}\right]$ are m/s; each side has different units.
3. Yes, the units for $\left[gt/v_{term}\right]$ are unit-less; both sides have the same units.
4. No, the units for $\left[gt/v_{term}\right]$ are unit-less; each side has the different units.

---

# Clicker Question 6-5

For the system of **Quadratic Drag in 1D**, we found a solution for the velocity as a function of time, with $v = 0$ at $t = 0$.

$$v(t) = v_{term}\tanh(gt/v_{term})$$ 

where $v_{term} = \sqrt{mg/c}$. What happens when $t \rightarrow \infty$?

1. The object stops moving.
2. The object travels at a constant velocity.
3. The object travels at an increasing velocity.
4. The object travels at a decreasing velocity.
5. I'm not sure.








