# Building a Molecular Dynamics code

In this project, you will learn the basics of a simulation technique
called molecular dynamics (MD).

Molecular dynamics is based on the assumption that even atoms move
according to the laws of Newton, given the correct model for
interactions. The goal of this project is to model a gas of argon atoms,
where the atoms interact according to the famous Lennard-Jones
potential,
$$U(r) = 4\varepsilon\qty(\qty(\frac{\sigma}{r})^{12} - \qty(\frac{\sigma}{r})^6), \label{eq:lj}$$
where $r$ is the distance between two atoms,
$r=\norm{\vec{r}_i-\vec{r}_j}$. $\sigma$ and $\varepsilon$ are
parameters which determine which chemical compound is modelled. This
potential is a good approximation for noble gases.

## Understanding the potential {#subsec:understanding}

1.  Plot the potential as a function of $r$ with $\varepsilon=1$ and
    $\sigma=1$, for example for $r \in \qty[0.9,3]$.

2.  The behaviour of $U(r)$ is vastly different for $r < \sigma$ and
    $r > \sigma$. Which term in the
    potential, [\[eq:lj\]](#eq:lj){reference-type="ref+page"
    reference="eq:lj"}, dominates in each case and what is the effect?

3.  Find and characterise the equilibrium points of the potential.

4.  Describe qualitatively the motion of two atoms which start at rest
    separated by a distance of $\num{1.5}\sigma$. What if they start
    with a separation of $\num{0.95}\sigma$? (Hint: use the graph of the
    potential.)

5.  Describe the shape of the potential close to the stable equilibrium
    point. Can you think of other force(s) with the same behaviour?

## Forces and equations of motion

1.  Find the force on atom $i$ at position $\vec{r}_i$ from atom $j$ at
    position $\vec{r}_j$.

2.  Show that the equation of motion for atom $i$ is
    $$\dv[2]{\vec{r}_i}{t} = \frac{24\varepsilon}{m} \sum_{j \neq i} \qty(2\qty(\frac{\sigma}{\norm{\vec{r}_i-\vec{r}_j}})^{12}-\qty(\frac{\sigma}{\norm{\vec{r}_i-\vec{r}_j}})^6)\frac{\vec{r}_i-\vec{r}_j}{\norm{\vec{r}_i-\vec{r}_j}^2}.$$

## Units

Numerical accuracy is reduced when computing with values which are many
orders of magnitude apart. This is often an issue in physics, and
molecular dynamics is no exception. For example, the mass of argon is
smaller than $10^{-25}\ \si{\kg}$, while typical length scales are on
the order of nanometres, $10^{-9}\ \si{\m}$.

The remedy is to change units so that most quantities are close to $1$.
From [\[eq:lj\]](#eq:lj){reference-type="ref+page" reference="eq:lj"} it
is clear that $\sigma$ and $\varepsilon$ are the typical scales for
length and energy.

1.  Introduce the scaled coordinates $\vec{r}_i\,'=\vec{r}_i/\sigma$ and
    show that the equation of motion can be rewritten in terms of these
    coordinates as
    $$\dv[2]{\vec{r}_i\,'}{{t'}} = 24 \sum_{j \neq i} \qty(2\norm{\vec{r}_i\,'-\vec{r}_j\,'}^{-12}-\norm{\vec{r}_i\,'-\vec{r}_j\,'}^{-6})\frac{\vec{r}_i\,'-\vec{r}_j\,'}{\norm{\vec{r}_i\,'-\vec{r}_j\,'}^2},\label{eq:undim}$$
    where $t'=t/\tau$ for a suitable choice of $\tau$.

2.  What is the characteristic time scale $\tau$, and what is its value
    for argon, which has $\sigma=\SI{3.405}{\angstrom}$
    ($\SI{1}{\angstrom}=\SI{1e-10}{\m}$),
    $m = \SI{39.95}{\atomicmassunit}$
    ($\SI{1}{\atomicmassunit} = \SI{1.66e-27}{\kg}$) and
    $\varepsilon=\SI{1.0318e-2}{\eV}$
    ($\SI{1}{\eV}=\SI{1.602e-19}{\J}$)?

# [Two-atom simulations]{.underline}

## Implementation

1.  Write a function which
    solves [\[eq:undim\]](#eq:undim){reference-type="ref+page"
    reference="eq:undim"} for two atoms and finds the positions and
    velocities of the atoms as a function of time. Implement three
    different integration methods: Euler, Euler-Cromer and
    Velocity-Verlet
    (see [\[app:verlet\]](#app:verlet){reference-type="ref+page"
    reference="app:verlet"} for a description of the latter).

## Motion {#subsec:2motion}

1.  Simulate the motion of two atoms which start at rest separated by a
    distance of $\num{1.5}\sigma$. Use $\Delta t'=\num{0.01}$, simulate
    until $t'=5$ and integrate with the Euler-Cromer method.

2.  Plot the distance between the atoms as a function of time.

3.  How does the motion fit with your expectations
    from [\[subsec:understanding\]](#subsec:understanding){reference-type="ref+page"
    reference="subsec:understanding"}?

4.  Repeat the previous tasks, but now with an initial separation of
    $\num{0.95}\sigma$. Explain your results.

## Energy

1.  Plot the kinetic, potential and total energy as a function of time
    for the two cases in the previous section.

2.  Theoretically speaking, should the total energy be conserved? Why,
    or why not? What about momentum?

3.  Does your program fulfil this? If not, what could be the cause?

4.  Simulate the same system as
    in [\[subsec:2motion\]](#subsec:2motion){reference-type="ref+page"
    reference="subsec:2motion"} with the Euler, Euler-Cromer and
    Velocity Verlet algorithms, and compare graphs of the total energy
    as a function of time.

5.  Find the largest time step that keeps stable motion and conserves
    energy for all three methods (small fluctuations in energy are
    allowed as long as they are periodic and don't increase/decrease
    with time). Discuss your results.

6.  Link your experimentation to a brief discussion of the pros and cons
    of the three methods, both physically and computationally.

The Velocity-Verlet method should be used for the rest of the project.

## Visualisation

1.  Extend your implementation such that it writes to an `xyz`-file at
    each timestep (see [\[app:xyz\]](#app:xyz){reference-type="ref+page"
    reference="app:xyz"}).

2.  Visualise the results of your simulations using Ovito
    (see [\[app:ovito\]](#app:ovito){reference-type="ref+page"
    reference="app:ovito"}).

# [Large systems]{.underline}

## Implementation

1.  Implement a solver
    of [\[eq:undim\]](#eq:undim){reference-type="ref+page"
    reference="eq:undim"} for $N$ atoms, given initial positions and
    velocities.

2.  Use Newton's third law to reduce the number of force calculations.

As you will experience, it takes a lot longer to simulate $N$ atoms than
two --- in fact the time increases as $N^2$. One very simple way to
reduce simulation times is to look at the expression (or plot) of $U(r)$
and see that it goes very rapidly towards zero as $r$ increases. This
means that atoms far apart interact weakly, and the forces between them
can be ignored.

1.  Extend your implementation such that atoms more than $3\sigma$ apart
    do not interact.

This effectively sets the potential energy $U(r)$ to be $0$ for
$r\geq 3\sigma$. Since $U(3\sigma)$ is not exactly equal to $0$, the
potential energy becomes discontinuous, which breaks energy
conservation. The solution is to use a shifted potential, i.e. adding a
constant such that $U(3\sigma)$ is exactly zero.

1.  Plot the shifted potential and the corresponding force to verify
    your implementation of the cut-off.

2.  Does the shift of the potential described above impact the force
    calculations?

## Verification

1.  Reproduce your results for the 2-atom model from the previous
    section to verify your implementation.

2.  Simulate the motion of four atoms starting at rest from the
    positions $[1,0,0]$, $[0,1,0]$, $[-1,0,0]$ and $[0,-1,0]$.

3.  Visualise the results in Ovito, describe and explain the motion.

4.  Plot the potential, kinetic and total energy as a function of time,
    and comment on the energy conservation.

5.  Repeat the above exercises with a small perturbation in the initial
    positions, such that the first atom starts at $[1,0.1,0]$.

## Initialisation

While we are interested in simulating liquid argon, which will not be in
an ordered structure, the simplest choice of initial positions is a
regular crystal structure. Our choice of structure is the face-centred
cubic lattice, as this is the crystal structure of solid argon.

The smallest repeating unit is called a unit cell, and each unit cell
contains four atoms. When creating a structure of $n\times n\times n$
unit cells, the atoms should be placed at

$$\begin{bmatrix}
            i & j & k \\
            i & 0.5+j & 0.5+k \\
            0.5+i & j & 0.5+k \\
            0.5+i & 0.5+j & k
        \end{bmatrix}\cdot d\qquad \qquad\qquad$$

![image](fig.pdf)

where $i$, $j$ and $k$ run from $0$ to $n-1$ and $d$ is the size of one
unit cell. One atom is placed at the bottom left corner of the unit
cell, and the other three at the centre of the three connected walls
(see drawing above). This structure will contain $4n^3$ atoms in total,
and the total size of the simulation box will be $(nd)^3=L^3$.

1.  Write a function which takes $n$ and $L$ (or $n$ and $d$) as
    arguments and returns the positions of $4n^3$ atoms on a
    face-centred cubic lattice.

2.  Verify your implementation by calling your function for $n=3$ and
    $L = 20$, writing the resulting positions to an `xyz`-file and
    looking at the result in Ovito. Your system should contain
    $4\cdot3^3=108$ atoms.

3.  Show that the unit cell size corresponding to the density
    $\rho=\SI{1.374}{\gram\per\cm\tothe3}$ is $d=1.7 \sigma$. This will
    be used in the remaining parts of the project.

## Many atoms, open boundary

1.  Simulate $256$ atoms starting from rest, and visualise the results.

2.  Plot the potential, kinetic and total energy as a function of time.
    What is the main difference from the energy graphs for two and four
    atoms?

## Boundary conditions

In the previous exercise, you probably observed that the atoms
immediately spread out into a large volume, possibly with some
continuing to infinity (and beyond). This is not the behaviour we want.
Ideally, we would like to model the bulk behaviour of argon by the use
of periodic boundary conditions, although it can be finicky to implement
this efficiently.

To simulate bulk behaviour properly, the atoms should not only be
constrained to move inside the box, but should also feel forces from
neighboring images (copies) of the same box. i.e. if an atom is close to
the right-facing wall, it should feel forces from atoms close to the
left-facing wall, as if the two walls were connected. To efficiently
calculate the shortest distance between atoms $i$ and $j$ across
boundaries, the following trick should be used

     dx = x[j] - x[i]
     dx = dx - round(dx/L)*L

where `L` is the size of the box, and `round` rounds up to the nearest
integer (see if you understand the logic behind this calculation!).
Periodic boundary conditions also mean that if an atom leave the box on
one side, it should reenter on the opppsite side.

If the implementation of periodic bounadry conditions proves to be too
diffucult or too slow, it's also possible to use *reflective* boundary
conditions. Although it doesn't simulate bulk behaviour the same way, it
still gives reasonable results for the quantities that we want to
measure for larger systems.

Having reflective boundary conditions simply means that atoms that would
otherwise leave the box, are turned around. Calculations of forces
across boundaries are also neglected in this case.

1.  Implement either periodic or reflective boundary conditions (or
    both) in your program.

2.  Run a simulation with $108$ atoms and verify visually that your
    implementation works. Give the atoms some initial velocities of your
    own choosing.

# [Science]{.underline}

By now, you will have a well-functioning (if not terribly efficient) set
of tools for running molecular dynamics simulations. It is now time to
apply these tools to real problems. The goal is to reproduce some of the
main results from the first article containing proper molecular dynamics
("landmark simulations" according to Wikipedia[^1]), written by A.
Rahman in 1964.

Section 4b) and 4c) (marked with \*) describes two different ways to
find the *diffusion constant*. You may choose to do only one of the
them, but we'll encourage you to do both. It's worth noting however that
a functioning implementation of periodic boundary conditions is needed
for section 4c.

## Temperature

#### Measurement:

Temperature is one of the most important concepts in thermodynamics, and
you will learn much more about it in FYS2160. As you may have learnt
already, temperature measures the vibrations of atoms. This is
formalised through the equipartition theorem, which for a monoatomic gas
such as argon states that $$\ev{K} = \tfrac{3}{2}k_\mathrm{B}T,$$ where
$\ev{K}$ is the average kinetic energy, $T$ is the temperature and
$k_\mathrm{B}$ is Boltzmann's constant. In a molecular dynamics
simulation, the temperature can be calculated by using the equipartition
theorem "backwards", i.e.
$$T = \frac{2\ev{K}}{3k_\mathrm{B}} = \frac{\ev{mv^2}}{3k_\mathrm{B}} = \frac{m}{3k_\mathrm{B}N}\sum_i v_i^2.$$
The sum runs over all atoms.

#### Units:

Note that since we are using reduced coordinates such as
$\vec{r}\,'=\vec{r}/\sigma$ and $t'=t/\tau$, a direct calculation from
the equation above gives a reduced temperature $T'=T/T_0$, where
$T_0 = \varepsilon/k_\mathrm{B}=\SI{119.7}{\kelvin}$. In reduced units,
the temperature expression is simplified to
$$T' = \frac{1}{3N}\sum_i v_i'^2.$$

1.  Extend your implementation with the calculation of temperature.

#### Initialisation of velocities:

Velocities in a gas are usually distributed according to a normal
distribution, i.e. a Gaussian function, as you can see in figure 1
of [@Rahman_1964]. In order to initialise a system with a given
temperature, each component of the velocity of each atom should be
randomly chosen from a normal distribution with mean zero and standard
deviation $\sqrt{kT/m}$. The following `numpy` command achieves this in
reduced units:

    v0 = np.random.normal(0, sqrt(T), size=(N,3))

1.  Run a simulation with $108$ atoms and an initial temperature of
    $\SI{300}{\kelvin}$. Plot the temperature as a function of time.

2.  Find an initial temperature that makes the equilibrium temperature
    approximately equal to the $\SI{94.4}{\kelvin}$ used
    in [@Rahman_1964]. Plot the temperature as a function of time.

## \*Velocity autocorrelation and diffusion coefficient

The velocity autocorrelation, denoted $A(t)$, is a measure of how
similar the distribution of velocities is to the initial distribution.
It is shown in figure 4 of [@Rahman_1964]. $A(t=0)=1$, since the
velocity distribution at $t=0$ *is* the initial distribution, while
$A(t)$ decreases rapidly for $t>0$ as the atoms collide with each other
and the velocities become less and less similar to the initial
distribution.

Mathematically, the velocity autocorrelation is defined as
$$A(t) = \ev{\frac{\vec{v}(t)\cdot\vec{v}(0)}{\vec{v}(0)\cdot\vec{v}(0)}}
         = \frac{1}{N} \sum_i \frac{\vec{v}_i(t)\cdot\vec{v}_i(0)}{\vec{v}_i(0)\cdot\vec{v}_i(0)},\label{eq:vacf}$$
where the sum runs over all atoms.

1.  Add the calculation of the velocity autocorrelation to your
    implementation.

2.  Run a simulation with e.g. $256$ atoms (more if you can), and plot
    the velocity autocorrelation as a function of time. Compare with
    figure 4 of [@Rahman_1964].

One cause of deviations is that the initial configuration of positions
and velocities ($\vec{v}_i(0)$
in [\[eq:vacf\]](#eq:vacf){reference-type="ref+page"
reference="eq:vacf"}) should be an equilibrium distribution.

1.  Use the final positions and velocities from the previous simulation
    as initial positions and velocities for a new simulation, and
    calculate and plot the new velocity autocorrelation.

2.  If your plot is very noisy (and your program does not run for too
    long), redo the two above simulations multiple times and average the
    velocity autocorrelation.

The article also contains calculations of the diffusion coefficient $D$,
as shown in figure 3. Here, it is calculated as the slope of the mean
squared displacement as a function of time. This requires periodic
boundary conditions, which we have chosen to omit from this project.
Fortunately, the diffusion coefficient can also be obtained from the
velocity autocorrelation, via the Green-Kubo relation,

$$D = \frac{1}{3}\int_0^\infty A(t)\dd{t}.$$ While it is not possible to
integrate to $\infty$ in a molecular dynamics simulation, the rapid
decrease of $\abs{A(t)}$ ensures that a finite integral will give a good
approximation. Use your previous plot of $A(t)$ to determine a
reasonable upper bound.

1.  Estimate the diffusion coefficient from your previously calculated
    velocity autocorrelation. Compare with the result
    from [@Rahman_1964].

## \*Mean squared displacement and diffusion coefficient

A more intuituve and direct way to calculate the diffusion in the system
is via the *mean squared displacement*, defined as

$$\langle r^2(t) \rangle = \langle (\vec{r}(t) - \vec{r}(t_0))^2 \rangle = \frac{1}{N} \sum_{n=1}^N (\vec{r}_n(t) - \vec{r}_n(t_0)))^2.
 \label{eq:msd}$$

This measure tells us the average distance the atoms has traveled after
a time $t$ as compared to their positions at a reference time, $t_0$.
It's important that $t_0$ is set at a time where the system is already
at equilibrium.

**Important note: Periodic boundary conditions are required to calculate
the msd, as we need to keep track of where, and how many times the atoms
has crossed the boundaries.** This means counters for all atoms in all
three directions are needed.

1.  Add the calculation of the mean squared displacement to your
    implementation.

Through the theory of brownian motion, it can be shown that the mean
squared displement is linked to the diffusion constant $D$ by the
following relation (in three dimensions):

$$\langle r^2(t) \rangle = 6Dt \hspace{0.5 cm} \text{when } t \rightarrow \infty.$$

As with the velocity autocorrelation, the relation to the diffusion
constant implies a simulation of infinite time, but the rapid
convergence of the msd ensures a good approximation also in this case.

1.  Implement the calculation of the diffusion constant, and run a
    simulation for 864 atoms (fewer is also fine if the runtime is
    slow). How does your result compare to the one in [@Rahman_1964]?

2.  (Optional) If your program isn't too slow, calculate the diffusion
    constant as a function of temperature $D(T)$ for equilibrium
    temperatures in the range of $T = [50 K, 120K]$. Plot the result and
    describe what you see. Google the element of argon, and see if you
    find something that's supposed to happen in the given temperature
    range. Can you link this to your results?

## Radial distribution function

The radial distribution function $g(r)$ shown in figure 2
of [@Rahman_1964] describes the distribution of distances between an
atom and its neighbours. It is defined as the ratio of the density at a
distance $r$ from an atom and the average density, i.e.

$$g(r) = \frac{V}{N} \frac{n(r)}{4\pi r^2\Delta r},\label{eq:rdf}$$
where $V$ is the total volume, $N$ the total number of particles and
$n(r)$ the average number of particles at a distance between $r$ and
$r+\Delta r$. $g(r)$ should be calculated for all atoms and then
averaged. An example implementation is given below. The output should be
averaged over many timesteps for a smooth result. Note that while $g(r)$
should approach $1$ when $r\to\infty$ in bulk, the finite system size
causes $g(r)$ to decay for large $r$.

1.  Run a simulation with as many atoms for as long as you can.
    Calculate the radial distribution function $g(r)$, plot the result
    and compare with figure 2 of [@Rahman_1964].

``` {.python linerange="rdfstart-rdfend"}
```

# Appendix {#appendix .unnumbered}

## Data file format {#app:xyz}

The `xyz`-format is a semi-standard format for storing data from
molecular dynamics simulations. Each time step is stored in the
following format, and there are no blank lines between timesteps:

-   A line containing the number of atoms (an integer).

-   An ignored line (this line is usually written as a header for the
    subsequent columns).

-   One line for each atom, containing the atom type and the $x$-, $y$-
    and $z$-coordinates.

For two atoms simulated over three timesteps, where `xij` represents the
$x$-coordinate of atom $j$ at timestep $i$, the file would look like
this:

    [language=]
        2
        type  x   y   z     <--- This line is a read as a comment, and therefore ignored.
        Ar   x11 y11 z11
        Ar   x12 y12 z12
        2
        type  x   y   z
        Ar   x21 y21 z21
        Ar   x22 y22 z22
        2
        type  x   y   z
        Ar   x31 y31 z31
        Ar   x32 y32 z32

## Visualisation {#app:ovito}

Files written in the `xyz`-format can be read using the Ovito
visualisation tool. It can be downloaded and installed from
<https://ovito.org/index.php/download>.

When the installation has finished, simply open Ovito, click "File"
$\to$ "Load File" and choose your `xyz`-file. Edit the column mapping in
the dialogue if necessary. When the atoms have appeared on your screen,
check the box named "File contains time series" on the right-hand side,
press and watch your atoms move around!

## Velocity-Verlet {#app:verlet}

The Velocity-Verlet integration scheme is based on a second-order Taylor
polynomial. With $\vec{r}_i(t)$ denoting the position of atom $i$ at a
time $t$, the second-order Taylor expansions of position and velocity
can be written as $$\begin{aligned}
{2}
    \vec{r}_i(t+\Delta t) &\approx \vec{r}_i(t) + \vec{v}_i(t)\Delta t + \tfrac{1}{2}\vec{a}_i(t)\Delta t^2\\
    \vec{v}_i(t+\Delta t) &\approx \vec{v}_i(t) + \vec{a}_i(t)\Delta t + \tfrac{1}{2}\vec{a}_i'(t)\Delta t^2.
\end{aligned}$$ There is no explicit expression for $\vec{a}'(t)$. It
can, however, be approximated using our old friend
$$\vec{a}\,'(t)\approx\frac{\vec{a}(t+\Delta t)-\vec{a}(t)}{\Delta t}.$$
Since the acceleration is independent of the velocity, the newly updated
position, $\vec{r}(t+\Delta t)$, is sufficient to calculate
$\vec{a}(t+h)$. Inserting this into the expression for
$\vec{v}(t+\Delta t)$, we get $$\begin{aligned}
{2}
    \vec{v}_i(t+\Delta t) &\approx \vec{v}_i(t) + \vec{a}_i(t)\Delta t + \tfrac{1}{2}\qty(\vec{a}_i(t+\Delta t)-\vec{a}_i(t))\Delta t\\
    &= \vec{v}_i(t) + \tfrac{1}{2}\qty(\vec{a}_i(t)+\vec{a}_i(t+\Delta t))\Delta t.
\end{aligned}$$ The discretised algorithm then becomes $$\begin{aligned}
{2}
    \vec{r}_{i,j+1} &\approx \vec{r}_{i,j} + \vec{v}_{i,j}\Delta t + \tfrac{1}{2}\vec{a}_{i,j}\Delta t^2\\
    \vec{v}_{i,j+1} &\approx \vec{v}_{i,j} + \tfrac{1}{2}\qty(\vec{a}_{i,j} + \vec{a}_{i,j+1})\Delta t,
\end{aligned}$$ where $\vec{r}_{i,j}$ is the position of atom $i$ at
timestep $j$. In your implementation, you should avoid having to
calculate the acceleration more than once per timestep.

::: thebibliography
99 Rahman, Aneesur, Physical Review **136**, A405 (1964).
:::

[^1]: <https://en.wikipedia.org/wiki/Molecular_dynamics#History>
