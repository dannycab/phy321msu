---
marp: true
theme: graph_paper
paginate: true

title: Day 04 - Mathematical Preliminaries
description: Slides for PHY 321 Spring 2025, Day 04: Mathematical Preliminaries
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-04-vector-reminders.html
---

# Day 04 - Mathematical Preliminaries

![bg right:60%](./images/vector.jpeg)

---

# Announcements

* Homework 1 is due this Friday
* Homework 2 is posted now
* Help sessions start this week
    * DC today at 4pm; Friday at 3pm (1248 BPS)
* Elisha (ULA) will join us Friday; additional help hours soon
    * Complete [poll for additional help hours](https://crab.fit/elisha-ula-office-hours-scheduling-351733)

---

# Seminars this week (Tuesday and Wednesday)

TUESDAY, January 21, 2025

* **High Energy Physics Theory Seminar**
    * 11:00am, FRIB 1200 lab; Speaker: **Alexei Bazavov**, MSU-CMSE/PA
    * Title: *Lattice QCD: From classical computation to quantum simulation*
           
WEDNESDAY, January 22, 2025    
                                     
* **Astronomy Seminar**
    * 1:30 pm, 1400 BPS; Speaker: **Allyson Bieryla**, CfA | Harvard & Smithsonian
    * Title:  *Exoplanets and Solar Eclipses for Research and Community Engagement*

---

# Seminars this week (Wednesday, cont.)   

* **PER Seminar**
    * 3:00 pm., BPS 1400; Speaker: **Justin Gambrell**, Assistant Professor, Department of Computational Mathematics, Science, and Engineering, Michigan State University - **MSU PA ALUMNUS**
    * Title: *Computational Thinking Assessment for Introductory Physics: Design, Implementation, and Future Directions*

* **FRIB Nuclear Science Seminar**
    * 3:30pm., FRIB 1300 Auditorium; Speaker: Calem Hoffman of Argonne National Laboratory
    * Title:  The Influence of Near-Threshold States on Nuclear Observables

---

# Goals for this week

## Be able to answer the following questions.

* What are the essential physics models for single particles?
* How do we setup problems in classical mechanics?
* What mathematics do we need to get started?
* How do we solve the equations of motion?

---

# AI Policy Update

## Acceptable use cases proposed by y'all: 

* All uses are OK
* Brainstorming, getting ideas, finding information
* Asking for help, clarifying concepts, elaborating on ideas
* Outlining, structuring, and editing writing
* Fixing errors, debugging code, checking solutions

---

# AI Policy Update

## Unacceptable use cases proposed by y'all: 

* No use is OK
* Asking directly for answers and solutions
* Using AI to complete the entire assignment
* Using AI to write papers or reports
* Turning in work that is not your own

---

# AI Policy Update

## Ways of documenting AI use proposed by y'all:
* Summarizing the use of AI and how it helped
* Documenting the use of AI in the assignment
* Providing prompts, responses, and outcomes
* Detailed documentation including screenshots and date/time of use

---

# AI Policy Update

## Ways of collectively enforcing our policy:

* It is not possible.
* Honor system; hold old your friends accountable
* Collective policy helps us all; encourage honesty and integrity
* Report violations to Danny
* Fail the assignment if you violate the policy
* Fail the course if you violate the policy

---

## Ranked Choice Vote on our AI Policy

* **Proposal 1: We adopt a policy that does not allow AI use at all.**
    * Violation results in a failing grade on assignment. 
    * Repeated violations result in failing the course.
* **Proposal 2: We adopt a policy that allows AI use for brainstorming, help, and editing.** 
    * AI cannot be used for direct answers or completion of assignments. 
    * We expect documentation of AI use, but it can be informal. 
    * Violations are discussed with Danny; the first violation requires a redo of the assignment, and repeated violations result in a failing grade.
---

## Ranked Choice Vote on our AI Policy

* **Proposal 3: We adopt a policy that allows AI for use in nearly any way.**
    * We require detailed documentation of use; this means screenshots, prompts, responses, and outcomes.
    * Violations are discussed with Danny; the first violation requires a redo of the assignment, and repeated violations result in a failing grade.
* **Proposal 4: We adopt a policy that allows AI for use in any way with no documentation required.**
    * Violations of the policy are limited to sharing answers or solutions with others.

Vote here: [https://forms.office.com/r/PwfNQYJ2Rm](https://forms.office.com/r/PwfNQYJ2Rm)

---

# Reminders from Day 03

* In a Newtonian world, we start from a vector description of motion
* Differential equations are mathematical models that describe the motion of particles
* We can use different methods to solve these differential equations

--- 

# Clicker Question 4-1

Consider the generic position vector $\vec{R}$ for a particle in 2D space. Which of the following describes the direction of the vector in plane polar coordinates ($r$, $\phi$)?

1. $\hat{R}$
2. $\hat{r}$
3. $\hat{\phi}$
4. Some combination of $\hat{r}$ and $\hat{\phi}$
5. I'm not sure.

---

# Group Discussion 4-1

We found the following expression for the equation of motion of a falling ball subject to air resistance:

$$m \ddot{y} = +mg - b \dot{y} - c \dot{y}^2$$

What are the units of the constants $b$ and $c$?

<!-- ---

# Group Discussion 4-2

Consider the generic position vector $\vec{R}$ for a particle in 2D space. Find the velocity vector $\vec{V}$ for the particle in Cartesian coordinates ($x$, $y$).

## What happens in plane polar coordinates? 

$$\vec{R} = r \hat{r} + \phi \hat{\phi}$$

Note: 

$$\hat{r} = \cos(\phi) \hat{x} + \sin(\phi) \hat{y}$$

$$\hat{\phi} = -\sin(\phi) \hat{x} + \cos(\phi) \hat{y}$$ -->

