# Chaos in the driven nonlinear pendulum

The angular equation of motion of the pendulum is given by Newton's
equation and with no external force it reads:

$$
ml\frac{d^2\theta}{dt^2}+mgsin(\theta)=0,
$$(eqn_eom)

with an angular velocity
and acceleration given by 

$$
v=l\frac{d\theta}{dt},
$$(eqn_vel)

and

$$
a=l\frac{d^2\theta}{dt^2}.
$$(eqn_accel)


We do however expect that the motion will gradually come to an end due a
viscous drag torque acting on the pendulum. In the presence of the drag,
the above equation becomes:

$$
ml\frac{d^2\theta}{dt^2}+\nu\frac{d\theta}{dt}+mgsin(\theta)=0,
$$(eqn_eom_drag)
 
where $\nu$ is now a positive constant parameterizing
the viscosity of the medium in question. In order to maintain the motion
against viscosity, it is necessary to add some external driving force.
We choose here a periodic driving force. The last equation becomes then

$$
ml\frac{d^2\theta}{dt^2}+\nu\frac{d\theta}{dt}  +mgsin(\theta)=Asin(\omega t),
$$(eqn_eom_driven)
 
with $A$ and $\omega$ two constants representing the
amplitude and the angular frequency respectively. The latter is called
the driving frequency.

1.  Rewrite Eqs. {eq}`eqn_eom_drag` and {eq}`eqn_eom_driven` as dimensionless equations. That is,
    scale the equations.

2.  Write then a code which solves Eq. {eq}`eqn_eom_drag` using
    the Euler-Cromer method and fourth-order Runge Kutta method. Perform
    calculations for at least ten periods with $N=100$, $N=1000$ and
    $N=10000$ mesh points and values of $\nu = 1$, $\nu = 5$ and
    $\nu =10$. Set $l=1.0$ m, $g=1$ m/s$^2$ and $m=1$ kg. Choose as
    initial conditions $\theta(0) = 0.2$ (radians) and $v(0) = 0$
    (radians/s). Make plots of $\theta$ (in radians) as function of time
    and phase space plots of $\theta$ versus the velocity $v$. Check the
    stability of your results as functions of time and number of mesh
    points. Which case corresponds to damped, underdamped and overdamped
    oscillatory motion? Comment your results.

3.  Now we switch to Eq. {eq}`eqn_eom_driven` for the rest of the
    project. Add an external driving force and set $l=g=1$, $m=1$,
    $\nu = 1/2$ and $\omega = 2/3$. Choose as initial conditions
    $\theta(0) = 0.2$ and $v(0) = 0$ and $A=0.5$ and $A=1.2$. Make plots
    of $\theta$ (in radians) as function of time for at least 300
    periods and phase space plots of $\theta$ versus the velocity $v$.
    Choose an appropriate time step. Comment and explain the results for
    the different values of $A$.

4.  Keep now the constants from the previous exercise fixed but set now
    $A=1.35$, $A=1.44$ and $A=1.465$. Plot $\theta$ (in radians) as
    function of time for at least 300 periods for these values of $A$
    and comment your results.

5.  We want to analyse further these results by making phase space plots
    of $\theta$ versus the velocity $v$ using only the points where we
    have $\omega t=2n\pi$ where $n$ is an integer. These are normally
    called the drive periods. This is an example of what is called a
    Poincare section and is a very useful way to plot and analyze the
    behavior of a dynamical system. Comment your results.
