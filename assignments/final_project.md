# Final Project (Due May 1st; Video Due April 27th)

Your final project synthesizes physics, computation, and scientific communication. It provides an opportunity to explore a physical problem of your choice using computational methods and to present your findings in a clear, engaging manner. And we hope that you will work on something you find genuinely interesting!

It is worth **30%** of your course grade and has two graded components:

1. **Computational Essay – 70%**
2. **Video Presentation – 30%**

You may work **solo**, in **pairs**, or in **groups of three**. Expectations scale with group size. All members receive the same grade unless arranged with the instructor. **Check with Danny on scale if unsure.**

---

## Project Components

### 1. Computational Essay (70%)

Submit as a Jupyter Notebook. It should:

- Pose a clear, compelling research question about a physical system.
- Provide background and motivation.
- Apply appropriate computational modeling, simulation, or analysis.
- Integrate code, figures, and explanatory narrative.
- Reflect on limitations, implications, and possible extensions.

Your audience is physics students/instructors unfamiliar with your specific topic. Aim for clarity, organization, and engagement. A person should be able to read and understand your essay without running the code; the code should enhance understanding and the visualizations should be clear and relevant. There are numerous examples available on [the University of Oslo Computational Essay Repository](https://uio-ccse.github.io/computational-essay-showroom/intro.html).

**Due:** Thursday, **May 1st at 11:59pm**. *You may turn this in earlier with your presentation.* Submit as a single zip file on D2L. Please make sure you include:
- Your Jupyter Notebook (.ipynb)
- Any data files needed to run your code
- A README with instructions for running your notebook (e.g., required libraries, how to run the code, etc.)
- And any other supporting materials (e.g., animations, videos, etc.) that I might need to view your project as you intended.

### 2. Video Presentation (30%)

Record and submit a video presentation of your project.

**Format:**
- Length: **8-12 minutes** (depending on group size; 8 minutes for solo, 10 for pairs, 12 for groups of three)
- All group members should present a portion of the video. If one member genuinely cannot participate, the rest of the group must agree to this, and the presenter(s) must explicitly acknowledge that member's contributions in the video.
- **Submit by sharing a link to your video** — either [MSU Mediaspace](https://mediaspace.msu.edu/) (*preferred*) or YouTube (unlisted). Send your link to Danny by the deadline using the D2L assignment submission form.

**Requirements:**
- State your research question and motivation
- Summarize the physics principles, computational methods, and key findings
- Use visuals (plots, animations, brief code excerpts) — do not read the computational essay verbatim
- Speak or communicate your ideas as clearly as possible; practice to ensure smooth delivery within the time limit

**Due:** Monday, **April 27th at 11:59pm**.

Danny will share a playlist of all project videos with the class after the deadline.

---

## Meet with Danny Before You Submit

Danny will be out of town during the last week of class (April 20–24). To make up for that lost instructional time and to make sure you are set up to do well on the final project, **he is offering individual or group appointments the week of April 14–17 (DC will be in ET) and April 20-24 (DC will be in CET, +6hrs)**.

These meetings are a chance to:
- Get final feedback on your project direction and progress
- Ask any remaining questions about the rubric or expectations
- Make sure you feel confident going into the submission

**Appointments are optional but encouraged.** Students who attend will receive participation credit equivalent to one week of in-class clicker points.

👉 **Schedule your appointment here:** 
- **April 14–17 (DC in ET; 10am-4pm ET)**: 
  - <https://cal.com/dannycaballero/phy-321-final-project-check-in-april-13-17>
- **April 20–24 (DC in CET; 10am-9pm CET, 4am-3pm ET)**: 
  - <https://cal.com/dannycaballero/phy-321-final-project-check-in-april-20-24>

Meetings will be held over Zoom. You will receive a link when you book.

---

## 🧮 Computational Essay Rubric (70% of Final Project Grade)

| Criteria | Weight | 4.0 | 3.5 | 3.0 | 2.5 | 2.0 | 1.0 | 0.0 |
|---------|--------|-----|-----|-----|-----|-----|-----|-----|
| **Physics Content** | 40% | Clear, accurate, and complete explanation of the physical system; strong connection between model and physics; insightful conclusions. | Mostly clear and accurate; minor gaps in explanation or interpretation. | Adequate explanation; some inaccuracies or missing depth. | Basic explanation; lacks clarity or depth; some errors. | Incomplete or inaccurate explanation; weak connection to physics. | Minimal effort; major errors or confusion. | Missing or irrelevant. |
| **Computational Implementation** | 30% | Code is clean, well-structured, commented; correct and efficient implementation; results reproducible. | Mostly clean and functional code; minor inefficiencies or unclear sections. | Code runs but has some issues; organization or clarity lacking. | Code runs with difficulty; poor structure or unclear logic. | Code has major issues or errors; unclear purpose. | Code mostly non-functional or copied without understanding. | Missing. |
| **Writing & Communication** | 20% | Clear, logical structure; excellent use of visuals; writing is polished and engaging. | Mostly clear and organized; visuals support content; minor writing issues. | Adequate structure; visuals present but not always effective; writing is uneven. | Disorganized or hard to follow; visuals unclear or missing; writing needs work. | Poorly written or structured; visuals unhelpful or absent. | Very difficult to follow; minimal effort. | Missing. |
| **Reflection & Discussion** | 10% | Deep reflection on limitations, implications, and future work; thoughtful insights. | Good reflection with some insight; future work mentioned. | Basic reflection; limited insight or depth. | Minimal reflection; vague or generic. | Very limited or off-topic. | Present but superficial. | Missing. |

---

### 🧮 Computational Essay – Rubric Component Definitions with Examples

#### **1. Physics Content (40%)**
**Definition:**  
How well you explain the physical system you're studying, including relevant theory, assumptions, and how your model connects to real-world physics.

- **Strong (3.5-4.0):**  
  You clearly define the physical system (e.g., a double pendulum), explain the governing equations (e.g., Newton's laws or energy conservation), and connect your model to real-world behavior. You discuss assumptions (e.g., frictionless pivot, small-angle approximation) and justify them.

- **Middling (2.5-3.0):**  
  You describe the system and mention some physics concepts, but the explanation is incomplete or contains minor inaccuracies. For example, you simulate a spring-mass system but don't explain why Hooke's Law applies or what the parameters mean.

- **Weaker (1.0–2.0):**  
  The physical system is vaguely described or misunderstood. There's little to no explanation of the physics, or the explanation is incorrect. For example, you simulate a projectile but don't mention gravity or forces.

---

#### **2. Computational Implementation (30%)**
**Definition:**  
How well your code models the system. This includes correctness, clarity, structure, and whether the computational method is appropriate.

- **Strong (3.5-4.0):**  
  Your code is clean, modular, and well-commented. You use appropriate numerical methods (e.g., `solve_ivp` for ODEs), and your results are reproducible. You include error handling or parameter exploration.

- **Middling (2.5-3.0):**  
  Your code runs and produces reasonable results, but it's messy or hard to follow. You may use a less appropriate method (e.g., Euler's method for stiff equations) or lack comments and structure.

- **Weaker (1.0–2.0):**  
  Your code is copied from class without modification, doesn't run properly, or doesn't match your problem. There's little evidence you understand what the code is doing.

---

#### **3. Writing & Communication (20%)**
**Definition:**  
How clearly and effectively you communicate your ideas in the notebook. This includes structure, use of markdown, and visuals.

- **Strong (3.5-4.0):**  
  Your notebook reads like a story: it introduces the problem, explains each step, and uses labeled plots and diagrams to support your points. Markdown cells are used to explain code and results. You cite sources where appropriate.

- **Middling (2.5-3.0):**  
  Your notebook has some structure and explanations, but it's inconsistent. Some plots are unlabeled or unexplained. The writing may be unclear in places. Few citations are provided.

- **Weaker (1.0–2.0):**  
  The notebook is mostly code with little explanation. It's hard to follow, and visuals (if present) are not labeled or interpreted. No citations are provided.

---

#### **4. Reflection & Discussion (10%)**
**Definition:**  
How well you reflect on your results, discuss limitations, and suggest future directions.

- **Strong (3.5-4.0):**  
  You discuss what your model shows, what it doesn't capture, and how it could be improved. You might compare your results to real data or suggest next steps.

- **Middling (2.5-3.0):**  
  You mention some limitations or future work, but the discussion is brief or superficial.

- **Weaker (1.0–2.0):**  
  You restate your results without reflection. There's no discussion of limitations or next steps.

---

## 🎤 Video Presentation Rubric (30% of Final Project Grade)

| Criteria | Weight | 4.0 | 3.5 | 3.0 | 2.5 | 2.0 | 1.0 | 0.0 |
|----------|--------|-----|-----|-----|-----|-----|-----|-----|
| **Clarity of Research Question & Motivation** | 25% | Clear, compelling, and well-motivated; audience understands why it matters. | Mostly clear and relevant; minor gaps in motivation. | Adequate explanation; motivation somewhat vague. | Vague or underdeveloped question or motivation. | Unclear or confusing. | Minimal effort. | Missing. |
| **Explanation of Physics & Computation** | 25% | Physics and computation clearly explained; audience can follow reasoning. | Mostly clear; minor confusion or gaps. | Basic explanation; some confusion or missing links. | Incomplete or unclear explanation. | Major confusion or errors. | Minimal explanation. | Missing. |
| **Use of Visuals** | 25% | Visuals are clear, relevant, and enhance understanding; each is explained on screen. | Mostly effective visuals; minor issues. | Visuals present but not always helpful or explained. | Visuals unclear or poorly integrated. | Visuals confusing or irrelevant. | Visuals present but not explained. | Missing. |
| **Delivery & Clarity** | 25% | Speaks or communicates clearly; does not read verbatim from slides; presentation flows naturally within time limit. | Mostly clear and well-paced; minor issues. | Adequate delivery; occasionally reads from slides or pacing is uneven. | Often reads from slides or difficult to follow. | Hard to understand; disengaged delivery. | Minimal effort. | Missing. |

---

### 🎤 Video Presentation – Rubric Component Definitions with Examples

#### **1. Clarity of Research Question & Motivation (25%)**
**Definition:**  
How clearly you state what you're studying and why it matters.

- **Strong (3.5-4.0):**  
  "We're modeling the spread of a forest fire using a cellular automaton. We chose this because it connects physics, computation, and environmental science, and we wanted to understand how wind and dryness affect fire behavior."

- **Middling (2.5-3.0):**  
  "We're simulating a forest fire. We thought it would be interesting." (Some clarity, but lacks depth or motivation.)

- **Weaker (1.0–2.0):**  
  "We did a simulation. It's about fire." (Unclear or unmotivated.)

---

#### **2. Explanation of Physics & Computation (25%)**
**Definition:**  
How well you explain the physics and computational methods used in your project.

- **Strong (3.5-4.0):**  
  You explain the physical principles (e.g., conservation of energy), describe your equations, and walk through your computational method (e.g., how you formulate the problem with numerical integration and used numerical integration).

- **Middling (2.5-3.0):**  
  You mention the physics and code but don't explain how they connect. For example, "We used Python to simulate the motion" without explaining the equations or method.

- **Weaker (1.0–2.0):**  
  You show results but don't explain how you got them. The audience is left guessing what the code or physics is doing.

---

#### **3. Use of Visuals (25%)**
**Definition:**  
How effectively you use visuals (plots, animations, code snippets) to support your explanation.

- **Strong (3.5-4.0):**  
  You use clear, labeled plots and animations that help the audience understand your results. You explain what each visual shows while it is on screen.

- **Middling (2.5-3.0):**  
  You include visuals, but they're not well-labeled or explained on screen. Some are helpful, others are confusing.

- **Weaker (1.0–2.0):**  
  Visuals are missing, unreadable, or not discussed. For example, showing a plot without saying what it means.

---

#### **4. Delivery & Clarity (25%)**
**Definition:**  
How clearly and naturally you communicate your ideas in the video. This doesn't require your speech to be perfect, but it should be understandable and engaging. In fact, you need not speak if you can creatively communicate your ideas through visuals, text, or other means in the video. The key is that your ideas are communicated clearly and effectively.

- **Strong (3.5-4.0):**  
  You speak or communicate clearly and at a measured pace, guide the audience through your slides without reading them verbatim, and the presentation flows naturally within the time limit.

- **Middling (2.5-3.0):**  
  You occasionally read from notes or slides, speak too quickly or quietly in places, or the pacing is uneven. The presentation is followable but not polished.

- **Weaker (1.0–2.0):**  
  You read directly from slides or notes throughout, speak in a way that is hard to follow, or the video is significantly over or under the time limit.

---

## Timeline & Checkpoints

| Date | Milestone |
|------|-----------|
| 27 Feb | Midterm Project 1: First project update |
| 10 Apr | Midterm Project 2: Second project update |
| 13–17 Apr | **Schedule your appointment with Danny** — <https://cal.com/dannycaballero/phy-321-final-project-check-in-april-13-17> |
| 20–24 Apr | Final project prep week (No Class -Danny out of town; meetings via Zoom) - **Schedule your appointment with Danny** — <https://cal.com/dannycaballero/phy-321-final-project-check-in-april-20-24> |
| **27 Apr** | **Video Presentation Due at 11:59pm** — send link to video using D2L form |
| **1 May** | **Computational Essay Due at 11:59pm** — submit zip file on D2L (can be submitted at the same time as presentation) |
