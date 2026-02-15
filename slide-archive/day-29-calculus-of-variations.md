---
marp: true
theme: graph_paper
paginate: true

title: Day 29 - Calculus of Variations
description: Slides for PHY 321 Fall 2025, Day 29: Calculus of Variations
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, differential equations, calculus of variations, action principle, Lagrangian mechanics
url: https://dannycaballero.info/phy321msu/slides/day-29-calculus-of-variations.html
---

# Day 29 - Calculus of Variations

![bg right width:600px](../images/notes/week11/soap_bubble.png)

---

# Announcements

* Midterm 2 is posted (Due 14 November 2025 at 11:59 pm)
* **Office Hours this week:** Midterm 2 Help

---

# Seminars this Week

## MONDAY, November 3, 2025

Condensed Matter Seminar 4:10 pm,1400 BPS, In Person and Zoom, Host ~ Philip Crowley
Speaker:   Chaitanya Murthy, University of Rochester                                                                  
Title:  A modified interferometer to measure anyonic braiding statistics
Zoom Link: https://msu.zoom.us/j/93613644939
Meeting ID: 936 1364 4939
Password: CMP
 
 
---

# Seminars this Week
 
 
## TUESDAY, November 4, 2025
 
High Energy Physics Seminar, 1:30 pm, 1400 BPS, Host~ Joshua Isaacson  
Speaker: Mareen Hoppe, Technische Universität Dresden
Title: Simulating polarization effects in Monte-Carlo event generators           
Organized by: Joey Huston, Sophie Berkman and Brenda Wenzlick
 
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

# Calculus of Variations

Variational calculus is a mathematical method to find functions that optimize a certain quantity. We will use variational calculus to derive the **Euler-Lagrange equations** for a set of **generalized coordinates** (i.e., $q,\dot{q}$). This is fundamental to Lagrangian mechanics.

$$L(q, \dot{q}, t) = T(\dot{q}) - U({q})$$

$$S = \int_{t_1}^{t_2} L(q, \dot{q}, t) \, dt \qquad \delta S = 0 $$

$$ \dfrac{d}{dt} \left( \dfrac{\partial L}{\partial \dot{q}} \right) - \dfrac{\partial L}{\partial q} = 0 $$



---

# Clicker Question 30-1

The generic segment, $ds$, of a curve in 2D Cartesian coordinates is given by 

$$ds = \sqrt{(dx)^2 + (dy)^2}$$

The integral of $ds$ from $s_1$ to $s_2$ gives the length of the curve, $l$. What is the correct expression for $l$?

1. $l = \int_{s_1}^{s_2} ds$
2. $l = \int_{s_1}^{s_2} \sqrt{(dx)^2 + (dy)^2}$
3. $l = \int_{s_1}^{s_2} \sqrt{1 + (dy/dx)^2} \, dx$
4. $l = \int_{s_1}^{s_2} \sqrt{(dx/dy)^2 + 1} \, dy$
5. More than one of the above

---

# Clicker Question 30-2

I can explain why:

$$\int_{s_1}^{s_2} f((Y(x), Y'(x), x) \, dx > \int_{s_1}^{s_2} f((y(x), y'(x), x) \, dx$$

where $Y(x) = y(x) + \alpha \eta(x)$, the true path plus an error term.

1. Yes, I can explain why
2. I think I can explain why
3. I'm having trouble seeing why
4. I don't think I can explain why

---

# Clicker Question 30-3

For the function $Y(x) = y(x) + \alpha \eta(x)$, where $y(x)$ is the true path, $\eta(x)$ is a small error term, and $\alpha$ is a small parameter, what is the derivative of $Y(x)$ with respect to $\alpha$?

$$\frac{dY}{d\alpha} = ?$$

1. $y(x)$
2. $\eta(x)$
3. $\eta'(x)$
4. $\alpha \eta(x)$
5. $y'(x) + \alpha \eta'(x)$

---

# Clicker Question 30-4

For the function $Y'(x) = y'(x) + \alpha \eta'(x)$, what is the derivative of $Y'(x)$ with respect to $\alpha$?

$$\frac{dY'}{d\alpha} = ?$$

1. $y'(x)$
2. $\eta'(x)$
3. $\eta''(x)$
4. $\alpha \eta'(x)$
5. $y''(x) + \alpha \eta''(x)$

---

# Clicker Question 30-5

The "surface term" that we computed for $\int_{s_1}^{s_2} \eta'(x) \frac{df}{dy'} dx$ is:

$$\left[\eta(x)\dfrac{df}{dy'}\right]_{x_1}^{x_2}=0$$

I can explain why this surface term is equal to zero:

1. Yes, I can explain why
2. I think I can explain why
3. I'm having trouble seeing why
4. I don't think I can explain why
5. I don't know what a surface term is

---

# Clicker Question 30-6

We completed this derivation with the following mathematical statement:

$$\int_{s_1}^{s_2} \eta(x) \left[\dfrac{\partial f}{\partial y} - \dfrac{d}{dx}\left(\dfrac{\partial f}{\partial y'}\right)\right] = 0$$

where $\eta(x)$ is an arbitrary function. What does this imply about the term in square brackets?

1. The term in square brackets must be a pure function of $x$.
2. The term in square brackets must be a pure function of $y$.
2. The term in square brackets must be a pure function of $y'$.
3. The term in square brackets must be zero.
4. The term in square brackets must be a non-zero constant.
