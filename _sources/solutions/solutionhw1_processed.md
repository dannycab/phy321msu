# Solution Homework 1
**Spring 2025**

## Exercise 1 (15 pt), math reminder, properties of exponential function

The first exercise is meant to remind ourselves about properties of the exponential function and imaginary numbers. This is highly relevant later in this course when we start analyzing oscillatory motion and some wave mechanics. 

As physicists we should thus feel comfortable with expressions that include $\exp{(\imath 2\pi f t)}$. Here $t$ could be interpreted as time and $f$ as a frequency. We know that $\imath = \sqrt(-1)$ is the imaginary unit number.

* 1a (4pt): Perform Taylor expansions in powers of $2\pi f t$ of the functions $\cos{(2\pi f t)}$ and $\sin{(2\pi f t)}$.

\end{solution}{admonition} Solution
:class: hint

$$
\cos{(2 \pi f t)} = \sum_{n=0}^{\infty}\left(-1\right)^n \frac{(2 \pi f t)^{2n}}{(2n)!}=1-\frac{(2 \pi f t)^{2}}{2!}+\frac{(2 \pi f t)^{4}}{4!}-\dots,
$$

and

$$
\sin{(2 \pi f t)} = \sum_{n=0}^{\infty}\left(-1\right)^n \frac{(2 \pi f t)^{2n+1}}{(2n+1)!}=2 \pi f t-\frac{(2 \pi f t)^{3}}{3!}+\frac{(2 \pi f t)^{5}}{5!}-\dots,
$$
\end{solution}


* 1b (3pt): Perform a Taylor expansion of $\exp{(i2\pi f t)}$.

\begin{solution}
:class: hint
$$
\exp{(\imath 2 \pi f t)} = \sum_{n=0}^{\infty}\frac{(\imath 2 \pi f t)^{n}}{(n)!}=1+ 2 \pi f t+\frac{(\imath 2 \pi f t)^{2}}{2!}+\frac{(\imath 2 \pi f t)^{3}}{3!}+\frac{(\imath 2 \pi f t)^{4}}{4!}+\frac{(\imath 2 \pi f t)^{5}}{5!}+\dots.
$$
\end{solution}

* 1c (2pt): Using parts (a) and (b) here, show that $\exp{(\imath2\pi f t)}=\cos{(2\pi f t)}+\imath\sin{(2\pi f t)}$.

\begin{solution}
:class: hint
Using $\imath^2=-1$ we can rewrite the last results as

$$\exp{(\imath 2 \pi f t)} = \sum_{n=0}^{\infty}\frac{(\imath 2 \pi f t)^{n}}{(n)!}=1+\imath 2 \pi f t-\frac{(2 \pi f t)^{2}}{2!}-\imath\frac{(2 \pi f t)^{3}}{3!}+\frac{(2 \pi f t)^{4}}{4!}+\imath\frac{(2 \pi f t)^{5}}{5!}-\dots $$
$$\exp{(\imath 2 \pi f t)} = \left(1-\frac{(2 \pi f t)^{2}}{2!}+\frac{(2 \pi f t)^{4}}{4!}-\dots\right)+\imath\left(2 \pi f t-\frac{(2 \pi f t)^{3}}{3!}+\frac{(2 \pi f t)^{5}}{5!}-\dots\right)$$
$$ \exp{(\imath 2 \pi f t)} = \cos{(2 \pi f t)}+\imath\sin{(2 \pi f t)}$$
\end{solution}

* 1d (2pt): Show that $\ln{(-1)} = \imath \pi$.

\begin{solution}
:class: hint
Let $2 \pi f t = \pi$, we get

$$
\exp{(\imath\pi)}=\cos{(\pi)}+\imath\sin{(\pi)}=-1.
$$
\end{solution}

* 1e (4pt): Develop another novel mathematical relationship based on the properties you've discovered in this problem. Explain how your result connects to any of the results parts a-d.

\begin{solution}
:class: hint
Answers can vary.
\end{solution}

## Exercise 2 (15 pt), Vector algebra

As we have quickly realized, forces and motion in three dimensions are best described using vectors. Here we perform some elementary vector algebra that we wil need to have as tacit knowledge for the rest of the course. These operations are not typicay taken with specific numbers, but rather with vectors in general. When we need to, we use the notation $\boldsymbol{a}=(a_x,a_y,a_z)$ for vectors in three dimensions. To get us started the first two questions below include numerical values, but the third question expects you to use the general notation.

* 2a (4pt) One of the many uses of the scalar product is to find the angle between two given vectors. Find the angle between the vectors $\boldsymbol{a}=(1,3,9)$ and $\boldsymbol{b}=(9,3,1)$ by evaluating their scalar product.

\begin{solution}
:class: hint

One of the many uses of the scalar product is to find the angle between two given vectors. Find the angle between the vectors $\boldsymbol{a}=(1,3,9)$ and $\boldsymbol{b}=(9,3,1)$ by evaluating their scalar product. The vector product is given by:

$$
\boldsymbol{a}\cdot\boldsymbol{b} = \vert \boldsymbol{a} \vert \vert \boldsymbol{b} \vert \cos{\theta_{ab}}.
$$

We have

$$
\boldsymbol{a}^T\boldsymbol{b} = 1(9) \boldsymbol{e}_1\cdot\boldsymbol{e}_1+ 3(3)\boldsymbol{e}_2\cdot\boldsymbol{e}_2+ 9(1)\boldsymbol{e}_3\cdot\boldsymbol{e}_3= 9+9+9=27,
$$

since $\boldsymbol{e}_i\cdot\boldsymbol{e}_i=1$ for our unit vectors, with $i=1,2,3$. Note also that the unit vectors are orthogonal, that is $\boldsymbol{e}_i \cdot \boldsymbol{e}_j=0$ if $i\ne j$.
The norm of $\vert \boldsymbol{a}\vert^2 = 1+9+81=91$. The norm of $\vert \boldsymbol{b}\vert^2 = 81+9+1=91$. This means we have:

$$
\boldsymbol{a}^T\boldsymbol{b} = 27 = 91 \cos{\theta_{ab}} = \vert \boldsymbol{a} \vert \vert \boldsymbol{b} \vert \cos{\theta_{ab}},
$$

leading to $\cos{\theta_{ab}}=27/91$ and $\theta_{ab}=1.2695 $ rad, with $1$ rad being equal to $180/pi$. Thus we have $\theta_{ab}=72.74$ degrees.

A small digression on linear algebra useful for python programming of vectors.
We define the vectors as one-dimensional arrays meaning that we write
$\boldsymbol{a}^T=\begin{bmatrix} 1 & 3 & 9\end{bmatrix}$ and  $\boldsymbol{b}^T=\begin{bmatrix} 9 & 3 & 1\end{bmatrix}$, where we use $T$ to indicate the transpose of a vector.

We would then write the dot product as:

$$
\boldsymbol{a}^T\boldsymbol{b}=\begin{bmatrix} 1 & 3 & 9\end{bmatrix}\begin{bmatrix} 9 \\ 3 \\ 1\end{bmatrix}=27.
$$
\end{solution}

In Python we would code this as


```python
# we import numpy and math functions
import numpy as np
from math import acos, sqrt, pi
# Define a
a =np.array([1,3,9])
# Define b 
b =np.array([9,3,1])
# to compute the dot products we use the dot function or the multiplication sign @
norm_a = sqrt(np.dot(a,a))  # we could write it as a.T @ a or just a @ a
# We will stick with the @ operator hereafter when we multiply vector or matrices
norm_b = sqrt(b.T @ b)
dot_ab = a.T @ b
theta_ab = acos(dot_ab/(norm_a*norm_b))
# convert to degrees
print(theta_ab*180/pi)
```

    72.7402973585292


* 2b (5pt) For a cube with sides of length 1, one vertex at the origin, and sides along the $x$, $y$, and $z$ axes, the vector of the body diagonal from the origin can be written $\boldsymbol{a}=(1, 1, 1)$ and the vector of the face diagonal in the $xy$ plane from the origin is $\boldsymbol{b}=(1,1,0)$. Find first the lengths of the body diagonal and the face diagonal. Use then part (2a) to find the angle between the body diagonal and the face diagonal. **Make sure to include a sketch of your cube, the relevant vectors, and the angle you find.**

\begin{solution}
:class: hint

For a cube with sides of length 1, one vertex at the origin, and sides along the $x$, $y$, and $z$ axes, the vector of the body diagonal from the origin can be written $\boldsymbol{a}=(1, 1, 1)$ and the vector of the face diagonal in the $xy$ plane from the origin is $\boldsymbol{b}=(1,1,0)$. Find first the lengths of the body diagonal and the face diagonal. Use then part (2a) to find the angle between the body diagonal and the face diagonal.

The length of the body diagonal $\vert\boldsymbol{b}\vert=\sqrt{3}$ and the length of the face diagonal is $\vert \boldsymbol{f}\vert = \sqrt{2}$. From this we find

$$
\boldsymbol{b}^T\boldsymbol{f}=2=\sqrt{2}\sqrt{3}\cos{\theta_{bf}},
$$
leading to $\cos{\theta_{bf}}=\sqrt{2}/\sqrt{3}$ and $\theta_{bf}=0.615$ rad or
$\theta_{bf}=35.3$ degrees.
\end{solution}

* 2c (6pt) Consider two arbitrary vectors in three dimensions, $\boldsymbol{a}=(a_x, a_y, a_z)$ and $\boldsymbol{b}=(b_x, b_y, b_z)$. Prove that the cross product $\boldsymbol{a} \times \boldsymbol{b}$ results in a vector that is perpendicular to both $\boldsymbol{a}$ and $\boldsymbol{b}$. Use the properties of the dot product and the cross product to support your proof. Include a diagram illustrating the vectors and their cross product.

\begin{solution}
:class: hint

The cross product of two vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ is defined as:

$$
\boldsymbol{a} \times \boldsymbol{b} = \begin{vmatrix}
\boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\
a_x & a_y & a_z \\
b_x & b_y & b_z
\end{vmatrix},
$$

where $\boldsymbol{i}$, $\boldsymbol{j}$, and $\boldsymbol{k}$ are the unit vectors in the x, y, and z directions, respectively.

Using the determinant formula for the cross product, we have:

$$
\boldsymbol{a} \times \boldsymbol{b} = (a_y b_z - a_z b_y)\boldsymbol{i} - (a_x b_z - a_z b_x)\boldsymbol{j} + (a_x b_y - a_y b_x)\boldsymbol{k}.
$$

Let $\boldsymbol{c} = \boldsymbol{a} \times \boldsymbol{b}$, so $\boldsymbol{c} = (c_x, c_y, c_z)$, where:

$$
c_x = a_y b_z - a_z b_y, \\
c_y = a_z b_x - a_x b_z, \\
c_z = a_x b_y - a_y b_x.
$$

To prove that $\boldsymbol{c}$ is perpendicular to $\boldsymbol{a}$ and $\boldsymbol{b}$, we need to show that their dot products are zero:

$$
\boldsymbol{a} \cdot \boldsymbol{c} = a_x c_x + a_y c_y + a_z c_z.
$$

Substitute the components of $\boldsymbol{c}$:

$$
\boldsymbol{a} \cdot \boldsymbol{c} = a_x (a_y b_z - a_z b_y) + a_y (a_z b_x - a_x b_z) + a_z (a_x b_y - a_y b_x).
$$

Expanding and simplifying, we find that all terms cancel out:

$$
\boldsymbol{a} \cdot \boldsymbol{c} = a_x a_y b_z - a_x a_z b_y + a_y a_z b_x - a_y a_x b_z + a_z a_x b_y - a_z a_y b_x = 0.
$$

The proof is identical for $\boldsymbol{b} \cdot \boldsymbol{c}$.
\end{solution}

## Exercise 3 (10 pt), More vector mathematics

* 3a (5pt) Show (using the fact that multiplication of reals is distributive)
that $\boldsymbol{a}(\boldsymbol{b}+\boldsymbol{c})=\boldsymbol{a}\boldsymbol{b}+\boldsymbol{a}\boldsymbol{c}$.

\begin{solution}
:class: hint

Writing out the equations and keeping in mind that the norm of unit vectors is one, we have

$$
\boldsymbol{a}\cdot(\boldsymbol{b}+\boldsymbol{c})= a_1(b_1+c_1)+a_2(b_2+c_2)+a_3(b_3+c_3)\\
= (a_1b_1+a_1c_1)+(a_2b_2+a_2c_2)+(a_3b_3+a_3c_3)\\
= (a_1b_1+a_2b_2+a_3b_3)+(a_1c_1+a_2c_2+a_3c_3)\\
= \boldsymbol{a}\cdot\boldsymbol{b}+\boldsymbol{a}\cdot\boldsymbol{c}.
$$
\end{solution}

* 3b (5pt) Show that (using product rule for differentiating reals) $\frac{d}{dt}(\boldsymbol{a}\boldsymbol{b})=\boldsymbol{a}\frac{d\boldsymbol{b}}{dt}+\boldsymbol{b}\frac{d\boldsymbol{a}}{dt}$.

\begin{solution}
:class: hint
$$
\frac{d}{dt}(\boldsymbol{a}\cdot\boldsymbol{b})= \frac{d}{dt}(a_1b_1+a_2b_2+a_3b_3)\\
= \left(a_1\frac{db_1}{dt}+\frac{da_1}{dt}b_1\right)+\left(a_2\frac{db_2}{dt}+\frac{da_2}{dt}b_2\right)+\left(a_3\frac{db_3}{dt}+\frac{da_3}{dt}b_3\right)\\
= \left(a_1\frac{db_1}{dt}+a_2\frac{db_2}{dt}+a_3\frac{db_3}{dt}\right)+\left(\frac{da_1}{dt}b_1+\frac{da_2}{dt}b_2+\frac{da_3}{dt}b_3\right)\\
= \boldsymbol{a}\cdot\frac{d\boldsymbol{b}}{dt}+\frac{d\boldsymbol{a}}{dt}\cdot\boldsymbol{b}.
$$
\end{solution}

## Exercise 4 (10 pt), Algebra of cross products

* 4a (5pt) Show that the cross products are distributive
$\boldsymbol{a}\times(\boldsymbol{b}+\boldsymbol{c})=\boldsymbol{a}\times\boldsymbol{b}+\boldsymbol{a}\times\boldsymbol{c}$.

\begin{solution}
:class: hint

To prove the distributive property of the cross product for vectors in three-dimensional space, we need to show that for any vectors $\boldsymbol{a}$, $\boldsymbol{b}$, and $\boldsymbol{c}$, the following holds:

$$ \boldsymbol{a}\times(\boldsymbol{b}+\boldsymbol{c})=\boldsymbol{a}\times\boldsymbol{b}+\boldsymbol{a}\times\boldsymbol{c}. $$

Let's denote $\boldsymbol{a} = (a_x, a_y, a_z)$, $\boldsymbol{b} = (b_x, b_y, b_z)$, and $\boldsymbol{c} = (c_x, c_y, c_z)$.

The vector sum $\boldsymbol{b}+\boldsymbol{c}$ is given by:

$$ \boldsymbol{b}+\boldsymbol{c} = (b_x + c_x, b_y + c_y, b_z + c_z). $$

Now, we compute the cross product of $\boldsymbol{a}$ with this sum:

$$
\boldsymbol{a}\times(\boldsymbol{b}+\boldsymbol{c}) = \begin{vmatrix}
\boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\
a_x & a_y & a_z \\
b_x + c_x & b_y + c_y & b_z + c_z
\end{vmatrix},
$$

which yields:

$$
\boldsymbol{a}\times(\boldsymbol{b}+\boldsymbol{c}) = (a_y(b_z + c_z) - a_z(b_y + c_y))\boldsymbol{i} - (a_x(b_z + c_z) - a_z(b_x + c_x))\boldsymbol{j} + (a_x(b_y + c_y) - a_y(b_x + c_x))\boldsymbol{k}.
$$

Expanding this, we get:

$$
\boldsymbol{a}\times(\boldsymbol{b}+\boldsymbol{c}) = (a_y b_z + a_y c_z - a_z b_y - a_z c_y)\boldsymbol{i} - (a_x b_z + a_x c_z - a_z b_x - a_z c_x)\boldsymbol{j} + (a_x b_y + a_x c_y - a_y b_x - a_y c_x)\boldsymbol{k}.
$$

Next, we compute the cross products $\boldsymbol{a}\times\boldsymbol{b}$ and $\boldsymbol{a}\times\boldsymbol{c}$ separately:

$$
\boldsymbol{a}\times\boldsymbol{b} = \begin{vmatrix}
\boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\
a_x & a_y & a_z \\
b_x & b_y & b_z
\end{vmatrix}
= (a_y b_z - a_z b_y)\boldsymbol{i} - (a_x b_z - a_z b_x)\boldsymbol{j} + (a_x b_y - a_y b_x)\boldsymbol{k},
$$

and

$$
\boldsymbol{a}\times\boldsymbol{c} = \begin{vmatrix}
\boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\
a_x & a_y & a_z \\
c_x & c_y & c_z
\end{vmatrix}
= (a_y c_z - a_z c_y)\boldsymbol{i} - (a_x c_z - a_z c_x)\boldsymbol{j} + (a_x c_y - a_y c_x)\boldsymbol{k}.
$$

Now, we add the two cross products:

$$
(\boldsymbol{a}\times\boldsymbol{b}) + (\boldsymbol{a}\times\boldsymbol{c}) = [(a_y b_z - a_z b_y) + (a_y c_z - a_z c_y)]\boldsymbol{i} - [(a_x b_z - a_z b_x) + (a_x c_z - a_z c_x)]\boldsymbol{j} + [(a_x b_y - a_y b_x) + (a_x c_y - a_y c_x)]\boldsymbol{k}.
$$

Simplifying, we get:

$$
(\boldsymbol{a}\times\boldsymbol{b}) + (\boldsymbol{a}\times\boldsymbol{c}) = (a_y b_z + a_y c_z - a_z b_y - a_z c_y)\boldsymbol{i} - (a_x b_z + a_x c_z - a_z b_x - a_z c_x)\boldsymbol{j} + (a_x b_y + a_x c_y - a_y b_x - a_y c_x)\boldsymbol{k}.
$$

Comparing the expanded form of $\boldsymbol{a}\times(\boldsymbol{b}+\boldsymbol{c})$ with the sum $(\boldsymbol{a}\times\boldsymbol{b}) + (\boldsymbol{a}\times\boldsymbol{c})$, we can see that they are identical:

$$
\boldsymbol{a}\times(\boldsymbol{b}+\boldsymbol{c}) = (\boldsymbol{a}\times\boldsymbol{b}) + (\boldsymbol{a}\times\boldsymbol{c}).
$$
\end{solution}

* *4b (5pt) Show that $\frac{d}{dt}(\boldsymbol{a}\times\boldsymbol{b})=\boldsymbol{a}\times\frac{d\boldsymbol{b}}{dt}+\boldsymbol{b}\times\frac{d\boldsymbol{a}}{dt}$. Be careful with the order of factors.

\begin{solution}
:class: hint

To show that the time derivative of the cross product of two vectors $\boldsymbol{a}$ and $\boldsymbol{b}$ equals the cross product of the first vector and the time derivative of the second vector plus the time derivative of the first vector cross the second vector, we can use the properties of derivatives and the cross product.

Given two time-dependent vectors $\boldsymbol{a}(t) = (a_x(t), a_y(t), a_z(t))$ and $\boldsymbol{b}(t) = (b_x(t), b_y(t), b_z(t))$, we want to prove that:

$$ \frac{d}{dt}(\boldsymbol{a}(t) \times \boldsymbol{b}(t)) = \boldsymbol{a}(t) \times \frac{d\boldsymbol{b}(t)}{dt} + \frac{d\boldsymbol{a}(t)}{dt} \times \boldsymbol{b}(t). $$

The cross product $\boldsymbol{a}(t) \times \boldsymbol{b}(t)$ is given by:

$$ \boldsymbol{a}(t) \times \boldsymbol{b}(t) = (a_y(t) b_z(t) - a_z(t) b_y(t), a_z(t) b_x(t) - a_x(t) b_z(t), a_x(t) b_y(t) - a_y(t) b_x(t)). $$

Now, take the time derivative of the cross product component-wise:

$$ \frac{d}{dt}(\boldsymbol{a}(t) \times \boldsymbol{b}(t)) = \left(\frac{d}{dt}(a_y(t) b_z(t) - a_z(t) b_y(t)), \frac{d}{dt}(a_z(t) b_x(t) - a_x(t) b_z(t)), \frac{d}{dt}(a_x(t) b_y(t) - a_y(t) b_x(t))\right). $$

Applying the product rule to each component, we get:

$$ \frac{d}{dt}(\boldsymbol{a}(t) \times \boldsymbol{b}(t)) = \left(a_y(t) \frac{db_z(t)}{dt} + \frac{da_y(t)}{dt} b_z(t) - a_z(t) \frac{db_y(t)}{dt} - \frac{da_z(t)}{dt} b_y(t), \right. $$
$$ \left. a_z(t) \frac{db_x(t)}{dt} + \frac{da_z(t)}{dt} b_x(t) - a_x(t) \frac{db_z(t)}{dt} - \frac{da_x(t)}{dt} b_z(t), \right. $$
$$ \left. a_x(t) \frac{db_y(t)}{dt} + \frac{da_x(t)}{dt} b_y(t) - a_y(t) \frac{db_x(t)}{dt} - \frac{da_y(t)}{dt} b_x(t) \right). $$

Now, we rearrange the terms to separate the contributions from $\boldsymbol{a}(t)$ and the derivatives of $\boldsymbol{b}(t)$, and vice versa:

$$ \frac{d}{dt}(\boldsymbol{a}(t) \times \boldsymbol{b}(t)) = \left(a_y(t) \frac{db_z(t)}{dt} - a_z(t) \frac{db_y(t)}{dt}, a_z(t) \frac{db_x(t)}{dt} - a_x(t) \frac{db_z(t)}{dt}, a_x(t) \frac{db_y(t)}{dt} - a_y(t) \frac{db_x(t)}{dt}\right) $$
$$ + \left(\frac{da_y(t)}{dt} b_z(t) - \frac{da_z(t)}{dt} b_y(t), \frac{da_z(t)}{dt} b_x(t) - \frac{da_x(t)}{dt} b_z(t), \frac{da_x(t)}{dt} b_y(t) - \frac{da_y(t)}{dt} b_x(t)\right). $$


The first set of terms corresponds to $\boldsymbol{a}(t)$ crossed with the time derivative of $\boldsymbol{b}(t)$, and the second set of terms corresponds to the time derivative of $\boldsymbol{a}(t)$ crossed with $\boldsymbol{b}(t)$:

$$ \boldsymbol{a}(t) \times \frac{d\boldsymbol{b}(t)}{dt} = \left(a_y(t) \frac{db_z(t)}{dt} - a_z(t) \frac{db_y(t)}{dt}, a_z(t) \frac{db_x(t)}{dt} - a_x(t) \frac{db_z(t)}{dt}, a_x(t) \frac{db_y(t)}{dt} - a_y(t) \frac{db_x(t)}{dt}\right), $$

$$ \frac{d\boldsymbol{a}(t)}{dt} \times \boldsymbol{b}(t) = \left(\frac{da_y(t)}{dt} b_z(t) - \frac{da_z(t)}{dt} b_y(t), \frac{da_z(t)}{dt} b_x(t) - \frac{da_x(t)}{dt} b_z(t), \frac{da_x(t)}{dt} b_y(t) - \frac{da_y(t)}{dt} b_x(t)\right). $$


Combining these two cross products, we obtain the original expression:

$$ \frac{d}{dt}(\boldsymbol{a}(t) \times \boldsymbol{b}(t)) = \boldsymbol{a}(t) \times \frac{d\boldsymbol{b}(t)}{dt} + \frac{d\boldsymbol{a}(t)}{dt} \times \boldsymbol{b}(t). $$

This proves the required relationship and demonstrates that the time derivative of a cross product can be distributed across the cross product operation while maintaining the order of factors, which is crucial because the cross product is not commutative.
\end{solution}

## Exercise 5 (10 pt), Area of triangle and law of sines

The three vectors $\boldsymbol{a}$, $\boldsymbol{b}$, and $\boldsymbol{c}$ are the three sides of a triangle *ABC*. The angles $\alpha$, $\beta$, and $\gamma$ are the angles opposite the sides $\boldsymbol{a}$, $\boldsymbol{b}$, and $\boldsymbol{c}$, respectively. as shown below.

![triangle](../images/assignments/1.15-triangle.png)

*(Figure: A triangle with sides $\boldsymbol{a}$, $\boldsymbol{b}$, and $\boldsymbol{c}$ and angles $\alpha$, $\beta$, and $\gamma$; reproduced from JRT.)*

* 5a (5pt) Show that the area of the triangle can be given by any of these three equivalent expressions: $A=\frac{1}{2}|\boldsymbol{a}\times\boldsymbol{b}|=\frac{1}{2}|\boldsymbol{b}\times\boldsymbol{c}|=\frac{1}{2}|\boldsymbol{c}\times\boldsymbol{a}|$.

\begin{solution}
:class: hint

If we place the vertex $A$ at the origin and side $b$ along the $x$-axis, then the magnitude
of the cross product $\boldsymbol{b}\times \boldsymbol{c}$ gives,

$$
\vert \boldsymbol{b}\times \boldsymbol{c}\vert = \vert b_xc_y-b_yc_x\vert =\vert b_xc_y-0\dots c_x\vert =b_xc_y,
$$

which is nothing but the magnitude of the base multiplied with the magnitude of the height.
We recognize that $c_y$ is the height of the vertex $B$ above the $x$-axis. From this we get that the area is,

$$
\mathrm{area}=\frac{1}{2}(\mathrm{base})\cdot(\mathrm{height})=\frac{1}{2}\vert \boldsymbol{b}\times \boldsymbol{c}\vert,
$$

which we were supposed to show.
\end{solution}


* 5b (5pt) 5b (5pt) Use the equality of the three expressions for the area of the triangle to show that $\frac{\sin{\alpha}}{a}=\frac{\sin{\beta}}{b}=\frac{\sin{\gamma}}{c}$, which is known as the [Law of Sines](https://en.wikipedia.org/wiki/Law_of_sines).

```{admonition} SOLUTION
:class: hint

From part 5a, using the formula for the magnitude of the cross product we have,

$$
\mathrm{area}=\frac{1}{2}ab\sin{\gamma}=\frac{1}{2}bc\sin{\alpha}=\frac{1}{2}ca\sin{\beta},
$$

which leads to,

$$
\frac{abc}{2\mathrm{area}}=    \frac{c}{\sin{\gamma}}=\frac{a}{\sin{\alpha}}=\frac{b}{\sin{\beta}}.
$$


## Exercise 6 (40pt), Numerical elements, getting started with some simple data

Our first numerical attempt will involve reading data from file or
just setting up two vectors, one for position and one for time. Our data are from 
[Usain Bolt's world record 100m during the olympic games in Beijing in
2008](https://www.youtube.com/watch?v=93dC0o2aHto). The data show the time used in units of 10m (see below). Before we however
venture into this, we need to repeat some basic Python syntax with an
emphasis on

* basic Python syntax for arrays

* define and operate on vectors and matrices in Python

* create plots for motion in 1D space

For more information, see the [introductory slides](https://mhjensen.github.io/Physics321/doc/pub/week3/html/week3.html).
Here are some of the basic packages we will be using this week


```python
import numpy as np 
import matplotlib.pyplot as plt
%matplotlib inline
```


    notebook controller is DISPOSED. 


    View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details.


The first exercise here deals with simply getting familiar with vectors and matrices.

We will be working with vectors and matrices to get you familiar with them

1. Initalize two three-dimensional $xyz$ vectors in the below cell using np.array([x,y,z]). Vectors are represented through arrays in python

2. V1 should have x1=1, y1 =2, and z1=3. 

3. Vector 2 should have x2=4, y2=5,  and z2=6. 

4. Print both vectors to make sure your code is working properly.


```python
V1 = np.array([1,2,3])
V2 = np.array([4,5,6])
print("V1: ", V1)
print("V2: ", V2)
```

    V1:  [1 2 3]
    V2:  [4 5 6]



    notebook controller is DISPOSED. 


    View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details.


If this is not too familiar, here's a useful link for creating vectors in python <https://docs.scipy.org/doc/numpy-1.13.0/user/basics.creation.html>. Alternatively, look up the [introductory slides](https://mhjensen.github.io/Physics321/doc/pub/Introduction/html/Introduction.html).

Now lets do some basic mathematics with vectors.

Compute and print the following, and double check with hand calculations:

* 6a (2pt)  Calculate $\boldsymbol{V}_1-\boldsymbol{V}_2$.

* 6b (2pt)  Calculate $\boldsymbol{V}_2-\boldsymbol{V}_1$.

* 6c (2pt) Calculate the dot product $\boldsymbol{V}_1\boldsymbol{V}_2$.

* 6d (2pt) Calculate the cross product $\boldsymbol{V}_1\times\boldsymbol{V}_2$.

Here is some useful explanation on numpy array operations if you feel a bit confused by what is happening, see <https://www.pluralsight.com/guides/overview-basic-numpy-operations>

### 6a-6d, solutions

The following code prints the first two exercises


```python
print(V1-V2)
print(V2-V1)
```

    [-3 -3 -3]
    [3 3 3]



    notebook controller is DISPOSED. 


    View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details.


For the dot product of V1 and V2 below we can use the **dot** function of **numpy** as follows


```python
print(V1.dot(V2))
```

    32



    notebook controller is DISPOSED. 


    View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details.


Alternatively, and this is the way it is normally written in Python now, we have


```python
print(V1 @ V2)
```

    32



    notebook controller is DISPOSED. 


    View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details.


A personal remark: I am not too fond of this notation!

As a small challenge try to write your own function for the **dot** product of two vectors.

Matrices can be created in a similar fashion in python.  In this
language we can work with them through the package numpy (which we
have already imported)


```python
M1 = np.matrix([[1,2,3],
             [4,5,6],
             [7,8,9]])
M2 = np.matrix([[1,2],
             [3,4],
             [5,6]])
M3 = np.matrix([[9,8,7],
             [4,5,6],
             [7,6,9]])
```


    notebook controller is DISPOSED. 


    View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details.


Matrices can be added in the same way vectors are added in python as shown here


```python
print("M1+M3: ", M1+M3)
```

    M1+M3:  [[10 10 10]
     [ 8 10 12]
     [14 14 18]]



    notebook controller is DISPOSED. 


    View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details.


What happens if we try to do $M1+M2$?

That's enough vectors and matrices for now. Let's move on to some physics problems! Yes, the actual subject we are studying for. 

We can opt for two different ways of handling the data. The data is listed in the table here and represents the total time Usain Bolt used in steps of  10 meters of distance. The label $i$ is just a counter and we start from zero since Python arrays are by default set from zero. The variable $t$ is time in seconds and $x$ is the position in meters.

<table class="dotable" border="1">
<thead>
<tr><th align="center"> i  </th> <th align="center"> 0  </th> <th align="center"> 1  </th> <th align="center"> 2  </th> <th align="center"> 3  </th> <th align="center"> 4  </th> <th align="center"> 5  </th> <th align="center"> 6  </th> <th align="center"> 7  </th> <th align="center"> 8  </th> <th align="center"> 9  </th> </tr>
</thead>
<tbody>
<tr><td align="center">   x[m]    </td> <td align="center">   10      </td> <td align="center">   20      </td> <td align="center">   30      </td> <td align="center">   40      </td> <td align="center">   50      </td> <td align="center">   60      </td> <td align="center">   70      </td> <td align="center">   80      </td> <td align="center">   90      </td> <td align="center">   100     </td> </tr>
<tr><td align="center">   t[s]    </td> <td align="center">   1.85    </td> <td align="center">   2.87    </td> <td align="center">   3.78    </td> <td align="center">   4.65    </td> <td align="center">   5.50    </td> <td align="center">   6.32    </td> <td align="center">   7.14    </td> <td align="center">   7.96    </td> <td align="center">   8.79    </td> <td align="center">   9.69    </td> </tr>
</tbody>
</table>

### 6e-6f (6pt)+(6pt), solution

You can here make a file with the above data and read them in and set
up two vectors, one for time and one for position. Alternatively, you
can just set up these two vectors directly and define two vectors in
your Python code.
**Note** we add by hand the initial conditions with position and time set to zero!

The following example code may help here. It plots the solution as well.


```python
# we just initialize time and position
x = np.array([0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0])
t = np.array([0.0,1.85, 2.87, 3.78, 4.65, 5.50, 6.32, 7.14, 7.96, 8.79, 9.69])
plt.plot(t,x, color='black')
plt.xlabel("Time t[s]")
plt.ylabel("Position x[m]")
plt.title("Usain Bolt's world record run")
plt.show()
```


    
![png](solutionhw1_files/solutionhw1_32_0.png)
    



    notebook controller is DISPOSED. 


    View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details.


### 6g (10pt), solution

Compute thereafter the mean velocity for every interval $i$ and the total velocity (from $i=0$ to the given interval $i$) for each interval and plot these two quantities as function of time. Comment your results.


```python
# Now we can compute the mean velocity using our data
# We define first an array Vaverage
n = np.size(t)
Vaverage = np.zeros(n)
TotalVaverage = np.zeros(n)
for i in range(1,n):
    Vaverage[i] = (x[i]-x[i-1])/(t[i]-t[i-1])
    TotalVaverage[i] = (x[i]-x[0])/(t[i]-t[0])
```


    notebook controller is DISPOSED. 


    View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details.


### 6h (10pt), solution

Finally, compute and print and plot the mean velocities, total average velocity, acceleration for each interval and the total acceleration.


```python
# Now we can compute the mean acceleration using our data
# inport pandas first
import pandas as pd
# We define first an array Aaverage
n = np.size(t)
Aaverage = np.zeros(n)
Aaverage[0] = 0
TotalAaverage = np.zeros(n)
for i in range(1,n):
    Aaverage[i] = (Vaverage[i]-Vaverage[i-1])/(t[i]-t[i-1])
    TotalAaverage[i] = (Vaverage[i]-Vaverage[0])/(t[i]-t[0])
data = {'t[s]': t,
        'x[m]': x,
        'v[m/s]': Vaverage,
	'Totvaver[m/s]': TotalVaverage,
        'a[m/s^2]': Aaverage,
	'TotAaver[m/s]': TotalAaverage
        }
NewData = pd.DataFrame(data)
display(NewData[0:n])
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>t[s]</th>
      <th>x[m]</th>
      <th>v[m/s]</th>
      <th>Totvaver[m/s]</th>
      <th>a[m/s^2]</th>
      <th>TotAaver[m/s]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.85</td>
      <td>10.0</td>
      <td>5.405405</td>
      <td>5.405405</td>
      <td>2.921841e+00</td>
      <td>2.921841</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.87</td>
      <td>20.0</td>
      <td>9.803922</td>
      <td>6.968641</td>
      <td>4.312271e+00</td>
      <td>3.416001</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.78</td>
      <td>30.0</td>
      <td>10.989011</td>
      <td>7.936508</td>
      <td>1.302296e+00</td>
      <td>2.907146</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.65</td>
      <td>40.0</td>
      <td>11.494253</td>
      <td>8.602151</td>
      <td>5.807378e-01</td>
      <td>2.471882</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.50</td>
      <td>50.0</td>
      <td>11.764706</td>
      <td>9.090909</td>
      <td>3.181800e-01</td>
      <td>2.139037</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6.32</td>
      <td>60.0</td>
      <td>12.195122</td>
      <td>9.493671</td>
      <td>5.248976e-01</td>
      <td>1.929608</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7.14</td>
      <td>70.0</td>
      <td>12.195122</td>
      <td>9.803922</td>
      <td>1.516402e-14</td>
      <td>1.708000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>7.96</td>
      <td>80.0</td>
      <td>12.195122</td>
      <td>10.050251</td>
      <td>-1.516402e-14</td>
      <td>1.532050</td>
    </tr>
    <tr>
      <th>9</th>
      <td>8.79</td>
      <td>90.0</td>
      <td>12.048193</td>
      <td>10.238908</td>
      <td>-1.770231e-01</td>
      <td>1.370670</td>
    </tr>
    <tr>
      <th>10</th>
      <td>9.69</td>
      <td>100.0</td>
      <td>11.111111</td>
      <td>10.319917</td>
      <td>-1.041202e+00</td>
      <td>1.146657</td>
    </tr>
  </tbody>
</table>
</div>



    notebook controller is DISPOSED. 


    View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details.


We see clearly from this table that the average velocity increases
till approximately 60m. Then it is constant for another 20 meters
before it starts to decrease. The average acceleration increases till
he has reached the first 20 meters, then it starts decreasing. After 80
meters we see clearly that he starts to slow down since the acceleration
becomes negative.

After 100 $m$ we note also that the total average velocity is
approximately 10.32 $m/s$ and the total average acceleration is
decreasing from its peak around 20 $m$.

We can also graph the estimates of his instantaneous velocity and acceleration (average between intervals) as functions of time.


```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Plot the velocity as function of time
ax1.plot(t, Vaverage, color='black')
ax1.set_xlabel("Time t[s]")
ax1.set_ylabel("Velocity v[$m/s$]")
ax1.set_title("Velocity vs Time")
ax1.grid()

# Plot the acceleration as function of time
ax2.plot(t, Aaverage, color='blue')
ax2.set_xlabel("Time t[s]")
ax2.set_ylabel("Acceleration a[$m/s^2$]")
ax2.set_title("Acceleration vs Time")
ax2.grid()

plt.tight_layout()
plt.show()
```


    
![png](solutionhw1_files/solutionhw1_38_0.png)
    



    notebook controller is DISPOSED. 


    View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details.




The interesting question is how quickly Usain Bolt
could have run if he had not slowed down during the last 20 meters. Can you find this
based on the present analysis, that is the above table? Assume he kept
a constant velocity like the one he had from 60m to 80m. How fast
could he have run if he had kept the same velocity till he reached
100m?
