# Final Project (Due Dec 8)

Your final project synthesizes physics, computation, and scientific communication. It provides an opportunity to explore a physical problem of your choice using computational methods and to present your findings in a clear, engaging manner. And we hope that you will work on something you find genuinely interesting!

It is worth **30%** of your course grade and has three graded components:

1. **Computational Essay – 60%**
2. **In-Class Presentation – 25%**
3. **Peer Review – 15%**

You may work **solo**, in **pairs**, or in **groups of three/four**. Expectations scale with group size. All members receive the same grade unless arranged with the instructor. **Check with Danny on scale if unsure.**

---

## Project Components

### 1. Computational Essay (60%)

Submit as a Jupyter Notebook. It should:

- Pose a clear, compelling research question about a physical system.
- Provide background and motivation.
- Apply appropriate computational modeling, simulation, or analysis.
- Integrate code, figures, and explanatory narrative.
- Reflect on limitations, implications, and possible extensions.

Your audience is physics students/instructors unfamiliar with your specific topic. Aim for clarity, organization, and engagement. A person should be able to read and understand your essay without running the code; the code should enhance understanding and the visualizations should be clear and relevant. There are numerous examples available on [the University of Oslo Computational Essay Repository](https://uio-ccse.github.io/computational-essay-showroom/intro.html).

**Due:** Monday, **December 8th**.

### 2. Presentation (25%)

Presented during the final week: **Dec 1, 3, or 5** (time slots will be assigned randomly).

Requirements:

- Length: **8-12 minutes** (depending on group size) + 3-5 minutes for Q&A
- State research question and motivation
- Summarize physics principles, computational methods, and key findings
- Use visuals (plots, animations, brief code excerpts); do not present the computational essay verbatim
- Make slides that present your work clearly and concisely
- Be accessible and invite discussion

It is expected that each group member presents a portion of the talk. Practice to ensure smooth delivery within the time limit.

### 3. Peer Review (15%)

To support a collaborative and reflective learning environment, you will complete a peer review form for each presentation you attend (at least two per class). These reviews are not about grading your classmates, but about offering thoughtful feedback and engaging with their ideas. Your reviews will be assessed for thoughtfulness and completeness, not for judgment of content.

**They will be shared anonymously with the presenters to help them improve.**

You are required to complete the following form for each presentation you attend. Opens on Dec 1st:

👉 <https://forms.cloud.microsoft/r/DF9MdrBJhf>

The form asks you to reflect on the physics, computation, and communication in each presentation. It includes questions about what you learned, what you found interesting, and what feedback you would offer to the presenters.

---


## 🧮 **Computational Essay Rubric (60% of Final Project Grade)**

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
How well you explain the physical system you’re studying, including relevant theory, assumptions, and how your model connects to real-world physics.

- **Strong (3.5-4.0):**  
  You clearly define the physical system (e.g., a double pendulum), explain the governing equations (e.g., Newton’s laws or energy conservation), and connect your model to real-world behavior. You discuss assumptions (e.g., frictionless pivot, small-angle approximation) and justify them.

- **Middling (2.5-3.0):**  
  You describe the system and mention some physics concepts, but the explanation is incomplete or contains minor inaccuracies. For example, you simulate a spring-mass system but don’t explain why Hooke’s Law applies or what the parameters mean.

- **Weaker (1.0–2.0):**  
  The physical system is vaguely described or misunderstood. There’s little to no explanation of the physics, or the explanation is incorrect. For example, you simulate a projectile but don’t mention gravity or forces.

---

#### **2. Computational Implementation (30%)**
**Definition:**  
How well your code models the system. This includes correctness, clarity, structure, and whether the computational method is appropriate.

- **Strong (3.5-4.0):**  
  Your code is clean, modular, and well-commented. You use appropriate numerical methods (e.g., `solve_ivp` for ODEs), and your results are reproducible. You include error handling or parameter exploration.

- **Middling (2.5-3.0):**  
  Your code runs and produces reasonable results, but it’s messy or hard to follow. You may use a less appropriate method (e.g., Euler’s method for stiff equations) or lack comments and structure.

- **Weaker (1.0–2.0):**  
  Your code is copied from class without modification, doesn’t run properly, or doesn’t match your problem. There’s little evidence you understand what the code is doing.

---

#### **3. Writing & Communication (20%)**
**Definition:**  
How clearly and effectively you communicate your ideas in the notebook. This includes structure, use of markdown, and visuals.

- **Strong (3.5-4.0):**  
  Your notebook reads like a story: it introduces the problem, explains each step, and uses labeled plots and diagrams to support your points. Markdown cells are used to explain code and results. You cite sources where appropriate.

- **Middling (2.5-3.0):**  
  Your notebook has some structure and explanations, but it’s inconsistent. Some plots are unlabeled or unexplained. The writing may be unclear in places. Few citations are provided.

- **Weaker (1.0–2.0):**  
  The notebook is mostly code with little explanation. It’s hard to follow, and visuals (if present) are not labeled or interpreted. No citations are provided.

---

#### **4. Reflection & Discussion (10%)**
**Definition:**  
How well you reflect on your results, discuss limitations, and suggest future directions.

- **Strong (3.5-4.0):**  
  You discuss what your model shows, what it doesn’t capture, and how it could be improved. You might compare your results to real data or suggest next steps.

- **Middling (2.5-3.0):**  
  You mention some limitations or future work, but the discussion is brief or superficial.

- **Weaker (1.0–2.0):**  
  You restate your results without reflection. There’s no discussion of limitations or next steps.

---

## 🎤 **Presentation Rubric (25% of Final Project Grade)**

| Criteria | Weight | 4.0 | 3.5 | 3.0 | 2.5 | 2.0 | 1.0 | 0.0 |
|----------|--------|-----|-----|-----|-----|-----|-----|-----|
| **Clarity of Research Question & Motivation** | 25% | Clear, compelling, and well-motivated; audience understands why it matters. | Mostly clear and relevant; minor gaps in motivation. | Adequate explanation; motivation somewhat vague. | Vague or underdeveloped question or motivation. | Unclear or confusing. | Minimal effort. | Missing. |
| **Explanation of Physics & Computation** | 25% | Physics and computation clearly explained; audience can follow reasoning. | Mostly clear; minor confusion or gaps. | Basic explanation; some confusion or missing links. | Incomplete or unclear explanation. | Major confusion or errors. | Minimal explanation. | Missing. |
| **Use of Visuals** | 25% | Visuals are clear, relevant, and enhance understanding. | Mostly effective visuals; minor issues. | Visuals present but not always helpful. | Visuals unclear or poorly integrated. | Visuals confusing or irrelevant. | Visuals present but not explained. | Missing. |
| **Delivery & Engagement** | 25% | Confident, well-paced, engaging; encourages discussion. | Mostly clear and engaging; minor pacing issues. | Adequate delivery; limited engagement. | Uneven or hard to follow. | Difficult to understand or disengaged. | Minimal effort. | Missing. |

---

### 🎤 Presentation – Rubric Component Definitions with Examples

#### **1. Clarity of Research Question & Motivation (25%)**
**Definition:**  
How clearly you state what you’re studying and why it matters.

- **Strong (3.5-4.0):**  
  “We’re modeling the spread of a forest fire using a cellular automaton. We chose this because it connects physics, computation, and environmental science, and we wanted to understand how wind and dryness affect fire behavior.”

- **Middling (2.5-3.0):**  
  “We’re simulating a forest fire. We thought it would be interesting.” (Some clarity, but lacks depth or motivation.)

- **Weaker (1.0–2.0):**  
  “We did a simulation. It’s about fire.” (Unclear or unmotivated.)

---

#### **2. Explanation of Physics & Computation (25%)**
**Definition:**  
How well you explain the physics and computational methods used in your project.

- **Strong (3.5-4.0):**  
  You explain the physical principles (e.g., conservation of energy), describe your equations, and walk through your computational method (e.g., how you used numerical integration).

- **Middling (2.5-3.0):**  
  You mention the physics and code but don’t explain how they connect. For example, “We used Python to simulate the motion” without explaining the equations or method.

- **Weaker (1.0–2.0):**  
  You show results but don’t explain how you got them. The audience is left guessing what the code or physics is doing.

---

#### **3. Use of Visuals (25%)**
**Definition:**  
How effectively you use visuals (plots, animations, code snippets) to support your explanation.

- **Strong (3.5-4.0):**  
  You use clear, labeled plots and animations that help the audience understand your results. You explain what each visual shows.

- **Middling (2.5-3.0):**  
  You include visuals, but they’re not well-labeled or explained. Some are helpful, others are confusing.

- **Weaker (1.0–2.0):**  
  Visuals are missing, unreadable, or not discussed. For example, showing a plot without saying what it means.

---

#### **4. Delivery & Engagement (25%)**
**Definition:**  
How well you communicate your ideas verbally and engage your audience.

- **Strong (3.5-4.0):**  
  You speak clearly and confidently, make eye contact, and guide the audience through your slides. You respond thoughtfully to questions.

- **Middling (2.5-3.0):**  
  You read from notes or slides, speak too quickly or quietly, or seem unsure. You answer questions briefly.

- **Weaker (1.0–2.0):**  
  You struggle to explain your work, don’t engage the audience, or don’t respond to questions.

---

## Timeline & Checkpoints

| Date | Milestone |
|------|-----------|
| Oct 31 | HW 7: First project update |
| Nov 14 | Midterm Project 2: Second update |
| Nov 21 | HW 8: Third update |
| Nov 24 & 26 | In-class work week |
| Dec 1, 3, 5 | Presentations |
| Dec 8 | Computational essay due |



