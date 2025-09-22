---
marp: true
theme: graph_paper
paginate: true

title: Day 12 - Conservation of Energy
description: Slides for PHY 321 Fall 2025, Day 12: Conservation of Energy
author: Prof. Danny Caballero <caball14@msu.edu>
keywords: classical mechanics, models, modeling, differential equations, motion
url: https://dannycaballero.info/phy321msu/slides/day-12-conservation-of-energy.html
---

# Day 12 - Conservation of Energy

![bg right width:600px](../images/notes/week5/conservation-of-energy.png)

$$\Delta E_{system} = W + Q$$

---

# Announcements

* HW 4 is due Friday
* Midterm 1 will be available next Monday
    * Four exercises (3 physics; 1 project work)
    * You may work together; and ask any questions
    * DC will not work exercises from Midterm
## Move Mihir's office hours? 
1. Yes
2. No
3. Maybe?

---

# Reminder of our Midterm Procedures

* The take-home midterms will be open for almost two weeks; you can often start some exercises early as they cover older material.
* They are meant to be challenging, but we will provide you with the resources and support you need to complete them.
* There is no homework due during the period in which the midterm is assigned.
* In contrast to homework assignments, DC will not work any exercises directly

You may work closely together with me, Mihir, and your classmates, but you and your partner must write up your own solutions.

---

# Seminars this week

## MONDAY, September 22, 2025             
  
Condensed Matter Seminar 4:10 pm,1400 BPS, In Person and Zoom, Host ~ Philip Crowley
Speaker: Dean Lee, Michigan State University
Title: Algorithms for nuclear many-body systems
Zoom Link: https://msu.zoom.us/j/93613644939
Meeting ID: 936 1364 4939
Password: CMP
 
---

# Seminars this week 
 
## WEDNESDAY, September 24, 2025    
 
                                    
FRIB Nuclear Science Seminar, 11:00am., online via Zoom,  (Zoom Only)
Speaker: Hongwei Zhao of IMPCAS
Title: High intensity heavy-ion accelerator facility and key technology R&D
Please see website for full abstract.
Please click the link below to join the webinar:
Join Zoom: https://msu.zoom.us/j/96657965451?pwd=Isaf23sK5agzaao0Kwaei7AaWHkc4W.1
Meeting ID: 966 5796 5451
Passcode: 479842

---

# Seminars this week 
 
## WEDNESDAY, September 24, 2025   
 
Astronomy Seminar, 1:30 pm, 1400 BPS, In Person and Zoom, Host~ 
Speaker: Kosuke Namekata, NAOJ
Title:
Zoom Link: https://msu.zoom.us/j/887295421?pwd=N1NFb0tVU29JL2FFSkk0cStpanR3UT09
Meeting ID: 887-295-421
Passcode: 002454

---

# Seminars this week 
 
## THURSDAY, September 25, 2025 (Promotion Talk!)
 
Colloquium, 3:30 pm, 1415 BPS, in person and zoom.  Host ~  
Refreshments and social half-hour in BPS 1400 starting at 3 pm
Speaker: Wolfgang Kerzendorf, MSU - (PTRC)
Title: Calibrating Stellar Explosions as Probes of the Evolving Universe 
Background: 
For more information and to schedule time with the speaker, see the colloquium calendar at https://pa.msu.edu/news-events-seminars/colloquium-schedule.aspx
Zoom Link: https://msu.zoom.us/j/94951062663
Password: 2002  Or complete link:  https://msu.zoom.us/j/94951062663?pwd=c48uM25P9UsRVuR74rkOioOWgpoxgC.1
 
---

# Seminars this week 
 
## FRIDAY, September 26, 2025 
 
QuIC Seminar, 12:30pm, -1:30pm, 1300 BPS, In Person  
Speaker: Alexei Bazavov, MSU
Title: Efficient State Preparation for the Schwinger Model
Full Scheule is at: https://sites.google.com/msu.edu/quic-seminar/
For more information, reach out to Ryan LaRose
 
---

# Seminars this week 
 
## FRIDAY, September 26, 2025 

IReNA Online Seminar, 2:00 pm, In Person and Zoom, FRIB 2025 Nuclear Conference Room, Light refreshments will be served at 1:50pm. 
Hosted by: Steffen Turkat (TU Dresden, Germany)
Speaker:  Dominik Koll, HZDR, Germany
Title: The search for freshly synthesized radionuclides from stellar explosions on Earth
Zoom Link: https://msu.zoom.us/j/827950260
Password: JINA

---


# This Week's Goals

* Remind ourselves of the concept of energy and energy conservation
* Apply the conservation of energy to a variety of systems
* Develop the mathematical tools to analyze energy conservation in more complex systems
* Connect our new understanding of energy conservation to our previous work on forces and motion

---

# Clicker Question 12-1

Which of the following are true about a point particle? (Use 1/A - True, 2/B - False)

12-1a. A point particle has no size. 
12-1b. A point particle can have no mass.
12-1c. A point particle can have no charge.
12-1d. A point particle can have no internal energy.

---

# Clicker Question 12-2

Einstein's proposed total energy for a particle of mass $m$ moving at speed $v$ is given by $E = \gamma m c^2$, where $\gamma = 1/\sqrt{1 - v^2/c^2}$.  We take the limit as $v/c \to 0$ to find the total energy of a particle at rest. Which terms below appear in the Taylor expansion of $\gamma$ in powers of $v/c$?

| a | b | c | d |
|---|---|---|---|
| $1$ | $v/c$ | $(v/c)^2$ | $(v/c)^3$ |

1.) a only 2.) a and b 3.) a and c

4.) b and d 5.) all terms


---

# Clicker Question 12-3

Which of the following are statements of the conservation of energy?

1. The total energy of a system is constant.
2. $\Delta E_{system} = 0$
3. $\Delta E_{system} = W + Q$
4. $\frac{dE_{system}}{dt} = 0$
5. All of the above