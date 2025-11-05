---
marp: true
theme: graph_paper
paginate: true

title: Day 30 - Euler-Lagrange Equation
description: Slides for PHY 321 Fall 2025, Day 30: Euler-Lagrange Equation
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, Euler-Lagrange Equation, action principle, Lagrangian mechanics
url: https://dannycaballero.info/phy321msu/slides/day-30-calculus-of-variations.html
---

# Day 30 - Euler-Lagrange Equation

![width:1000px](./images/day-01/Slide1.png)


---

# Seminars this Week 
 
## WEDNESDAY, November 5, 2025
 
                                    
Astronomy Seminar, 1:30 pm, 1400 BPS, In Person and Zoom, Host~ 
Speaker: Nick Konidaris, Carnegie Observatories
Title: The Sephira Project: Astronomical Imaging with Third-Order Intensity Correlations

---

# Seminars this Week 
 
## WEDNESDAY, November 5, 2025
 
FRIB Nuclear Science Seminar, 3:30pm., FRIB 1300 Auditorium and online via Zoom 
Speaker: Assistant Professor Xing Wu of The Facility for Rare Isotope Beams (FRIB)                                                      
Title: Towards Quantum Control and Sensing of 227ThO Molecules and Other Radioactive Molecules for Nuclear Schiff Moment Search
Please click the link below to join the webinar:
Join Zoom Meeting: https://msu.zoom.us/j/91861947571?pwd=IlUS6RkYdHibaosm4aznsYsctbaMrU.1
Meeting ID: 939 4416 7137
Passcode: 026775
 
---

# Seminars this Week 
 
 
 
## THURSDAY, November 6, 2025
 
Colloquium, 3:30 pm, 1415 BPS, in person and zoom.  Host ~ Jay Strader/Laura Chomiuk
Refreshments and social half-hour in BPS 1400 starting at 3 pm
Speaker: Nick Konidaris, Carnegie Observations
Title: SDSS Local Volume Mapper instrument and Early Science Results
 
---

# Seminars this Week 
 
## FRIDAY, November 7, 2025     
                                                 
                          
IReNA Online Seminar, 9:00am, In Person and Zoom, FRIB 2025 Nuclear Conference Room, Light refreshments will be served at 1:50pm. 
Hosted by: Sota Kimura (University of Tsukuba)
Speaker Tomoshi Takeda, Hiroshima University, Japan
Title: A New Approach to X-ray Astronomy: Development and Observational Results of the CubeSat Observatory NinjaSat

---

# Seminars this Week 
 
## FRIDAY, November 7, 2025  
 
Special HEP Seminar
High Energy Physics Seminar, 1:00 pm, 1400 BPS, Host~ Joey Huston 
Speaker: Eric Bachmann, Technische Universität Dresden
Title: Evidence for longitudinal polarization in same-sign WW scattering with the ATLAS detector            
Organized by: Joey Huston, Sophie Berkman and Brenda Wenzlick

---

# Seminars this Week 
 
## FRIDAY, November 7, 2025 
 
QuIC Seminar, 12:30pm, -1:30pm, 1300 BPS, Virtual only today  
Speaker: Philip Crowley, MSU
Title:  Quantum dynamics for quantum sensing
Full Scheule is at: https://sites.google.com/msu.edu/quic-seminar/
For more information, reach out to Ryan LaRose

---

# Reminders

We proposed a solution to the line problem that involved an error term $\eta(x)$, which is a small perturbation to the true path $y(x)$. This leads to a perturbed function:

$$Y(x) = y(x) + \alpha \eta(x)$$

where $\alpha$ is a small parameter.

We proposed that there's a functional $f(Y,Y',x)$ that depends on a function $Y(x)$, its derivative $Y'(x)$, and the independent variable $x$ such that:

$$\int_{s_1}^{s_2} f(Y,Y',x) \, dx > \int_{s_1}^{s_2} f(y,y',x) \, dx$$

---

# Reminders

By taking the derivative of the functional with respect to $\alpha$, we can find the condition for which the functional is stationary (i.e., a minimum or maximum).

$$\frac{d}{d\alpha} \int_{s_1}^{s_2} f(Y,Y',x) \, dx \bigg|_{\alpha=0} = 0$$

This (with a lot of math) led us to the following expression:

$$\int_{s_1}^{s_2} \eta(x) \left[\dfrac{\partial f}{\partial y} - \dfrac{d}{dx}\left(\dfrac{\partial f}{\partial y'}\right)\right] \, dx = 0$$

---


# Clicker Question 30-1

We completed this derivation with the following mathematical statement:

$$\int_{s_1}^{s_2} \eta(x) \left[\dfrac{\partial f}{\partial y} - \dfrac{d}{dx}\left(\dfrac{\partial f}{\partial y'}\right)\right] \, dx = 0$$

where $\eta(x)$ is an arbitrary function. What does this imply about the term in square brackets?

1. The term in square brackets must be a pure function of $x$.
2. The term in square brackets must be a pure function of $y$.
2. The term in square brackets must be a pure function of $y'$.
3. The term in square brackets must be zero.
4. The term in square brackets must be a non-zero constant.

---

# Clicker Question 30-2

Returning to the line problem,

$$l = \int_{x_1}^{x_2} \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx$$

here, $f(y,y',x) = \sqrt{1 + (y')^2}$, where $y' = \frac{dy}{dx}$.

Apply the Euler-Lagrange equation to find the expression for the function $f(y,y',x)$ in this case. Write your result to find the expression for the term in square brackets:

$$\dfrac{d}{dx}\left[?\right] = 0$$

**Click when you have an answer!**

---

# Clicker Question 30-3

With,

$$y' = \pm\sqrt{\dfrac{c^2}{1 + c^2}}$$

where $c$ is a constant, the solution expresses a straight line.

1. True and I can prove it!
2. True, but I'm not sure how to prove it.
3. False, I think this is incorrect.
4. I don't know.

---

# Clicker Question 30-4

We derived the time that it takes to run from a point on the shore to a point in the water, $T$:

$$T = \dfrac{1}{v_1} \left(x_1^2 + (y-y_1)^2\right)^{1/2}+\dfrac{1}{v_2} \left(x_2^2 + (y_2-y)^2\right)^{1/2}$$

To find the minimal time, what derivative should we take?

1. $\dfrac{dT}{dx}$
2. $\dfrac{dT}{dy}$
3. $\dfrac{dT}{dt}$
4. Something else?

---

# Clicker Question 30-5

For the brachistochrone problem, the ball moves purely under the influence of gravity. Consider that the ball has moved a vertical distance $\Delta y$ from rest. What is the speed of the ball at this point?

1. $v = gt$
2. $v = 2 g\Delta y$
3. $v = \sqrt{2g\Delta y}$
4. I'm not sure, but $<\sqrt{2g\Delta y}$
5. Something else?