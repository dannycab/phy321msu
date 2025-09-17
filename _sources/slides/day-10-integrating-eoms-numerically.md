---
marp: true
theme: graph_paper
paginate: true

title: Day 10 - Integrating EOMs Numerically
description: Slides for PHY 321 Spring 2025, Day 10: Integrating EOMs Numerically
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion, numerical integration, euler
url: https://dannycaballero.info/phy321msu/slides/day-10-integrating-eoms-numerically.html
---

# Day 10 - Integrating EOMs Numerically

![bg right width:600px](../images/notes/week4/numerical_integration.png)


---

# Announcements

* HW 4 is posted; starting project work
* Midterm 1 is coming up (Assigned 29 Sep; Due 10 Oct)
- **REMINDER:** Office hours, for now (Mihir-MN; Danny-DC):
  - Tuesday 6-8pm (MN, Zoom)
  - Thursday 6-8pm (MN, Zoom)
  - Friday 2-4pm (DC, 1248 BPS)
- Zoom Link: <https://msu.zoom.us/j/96882248075> 
    - password: `phy321msu`
- **Friday's Class:** Homework 4 Exercise 3 + Q&A
---
 
# Seminars this week

## WEDNESDAY, September 17, 2025    
                                 
Astronomy Seminar, 1:30 pm, 1400 BPS, In Person and Zoom, Host~ 
Speaker: Matthew Murphy, Michigan State University
Title:
Zoom Link: https://msu.zoom.us/j/887295421?pwd=N1NFb0tVU29JL2FFSkk0cStpanR3UT09
Meeting ID: 887-295-421
Passcode: 002454
 
---
 
# Seminars this week

## WEDNESDAY, September 17, 2025 

FRIB Nuclear Science Seminar, 3:30pm., FRIB 1300 Auditorium and online via Zoom 
Speaker: Katie Yurkewicz of Argonne National Laboratory (**MSU ALUM**)
Title: From Nuclei to Narratives: Lessons Learned on the Journey from NSCL Student to Lab Communications Leader
Please see website for full abstract.
Please click the link below to join the webinar:
Join Zoom: https://msu.zoom.us/j/96657965451?pwd=Isaf23sK5agzaao0Kwaei7AaWHkc4W.1
Meeting ID: 966 5796 5451
Passcode: 479842
 
 
---
 
# Seminars this week

## FRIDAY, September 19, 2025 
 
QuIC Seminar, 12:30pm, -1:30pm, 1300 BPS, In Person  
Speaker: Jeremiah Rowland, Michigan State University
Title: Measurement Reduction Techniques for Measuring Hamiltonians
Full Scheule is at: https://sites.google.com/msu.edu/quic-seminar/
For more information, reach out to Ryan LaRose

**Reminder: email me your extra credit seminar write-ups**

---

# Goals for this week

![bg right width:600px](../images/notes/week4/numerical_integration.png)

* Establish a model for drag forces
* Develop an understanding of the process for modeling forces
* Produce equations of motion that can be investigated
* Start probing the behavior of these systems with math and computing

---

# Model-to-EOM Pipeline for Classical Mechanics

1. ✅ Develop conceptual description of the system; make justifiable assumptions
2. ✅ Using a framework of physics (i.e., Newton's Laws, Lagrangian Dynamics), develop a mathematical model of the system
3. ✅ Produce the equations of motion (EOM) by following the framework (i.e., ordinary differential equations)
4. 😵 **Solve for trajectories of the system** (e.g., $x(t)$, $v(t)$, $v(x)$)

## Most EOMs are nonlinear

## We need approximate methods to produce trajectories
---


# Clicker Question 10-1

We found that the equation of motion for the spring-mass system was:

$$\ddot{x} = -\dfrac{k}{m}x = -\omega^2 x$$

Your friends have proposed the following **general solutions**:

$$1.\;x(t) = A\cos(\omega t) \qquad 2.\;x(t) = B\sin(\omega t) \qquad 3.\;x(t) = A\cos(\omega t) + B\sin(\omega t) $$
$$ 4.\;x(t) = A\cos(\omega t + \phi) \qquad 5.\;x(t) = B\sin(\omega t + \phi) \qquad 6.\;x(t) = A\cos(\omega t + \phi) + B\sin(\omega t + \phi) $$

How many of them are correct? 
(1) Only one (2) Two (3) Three
(4) Four (5) All of them

---

# Clicker Question 10-2

To convert the second order ODE for a spring mass system,

$$\ddot{x} = -\dfrac{k}{m}x = -\omega^2 x$$

to two first order ODEs, we first introduce an equation for the velocity:

$$v = \dot{x}.$$ 

This is a first order ODE, and the first one we need. What is the other first order ODE?

---

# Clicker Question 10-2

For spring-mass system ($\ddot{x} = -\omega^2 x$), and using the first order ODE the defines velocity $v = \dot{x}$, which other first order ODE can be used with the velocity equation to represent the spring mass system?

1. $\dot{x} = -\omega^2 x$
2. $\dot{v} = -\omega^2 x$
3. $\ddot{x} = a$
4. $\dot{v} = a$
5. Something else

---

# Clicker Question 10-3

We derived the Euler step for constant acceleration:

$$v[i+1]=v[i]+a*\Delta t$$
$$x[i+1]=x[i]+v[i]*\Delta t$$

We can implement in Python for arrays `x` and `v` with: 

```python
v[i+1]=v[i]+a*deltat        # Constant Acceleration
x[i+1]=x[i]+v[i]*deltat     # Euler Step
```

How can we implement a non-constant acceleration?

---

# Clicker Question 10-3

How can we implement a non-constant acceleration?

```python
v[i+1]=v[i]+a*deltat        # Constant Acceleration
x[i+1]=x[i]+v[i]*deltat     # Euler Step
```

1. Add in `a[i]` to the first equation
2. Pre-compute the array `a` outside the loop 
3. Compute `a[i]` in the loop
4. Change `v[i]` to `v[i+1]`
5. More than one of these
