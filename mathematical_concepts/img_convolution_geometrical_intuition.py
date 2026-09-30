"""
CONVOLUTION: 
THE "FIXED FILTER SLIDING OVER THE IMAGE" VIEW

We can mathematically think of convolution as:

Keep a fixed filter/window, move it over different
positions of the image, multiply corresponding values,
and sum the products.

This is especially intuitive in image processing.


1. THE USUAL IMAGE-PROCESSING INTERPRETATION
f = image
h = filter/kernel

We write: g(x) = Σ f(m) h(x-m)

Geometrically:

        IMAGE f
┌───────────────────────────────┐
│                               │
│     image values              │
│                               │
└───────────────────────────────┘
            ↑
        FILTER h

The filter moves across the image.

---
2. BUT CONVOLUTION IS COMMUTATIVE

Convolution has the property:

    f * h = h * f

Therefore:

    Σ f(m) h(x-m)

is equivalent to:

    Σ h(m) f(x-m)

So we can instead think:

    h = image
    f = filter

and write: g(x) = Σ h(m) f(x-m)

Now your interpretation becomes:

    f = fixed filter
    h = image

    x = position of the filter on the image
    m = position within the filter/image values
    being multiplied

---
3. SIMPLE 1-D EXAMPLE

Suppose the filter is:

f = [1  1  1]

and the image/signal is:

h = [10  20  30  40  50  60]

Put the filter over the first three values:

[10  20  30] 40  50  60

Multiply corresponding values:
1(10) + 1(20) + 1(30) = 60

---
4. SLIDE THE FILTER

Move the same filter 
one position to the right:

10 [20  30  40] 50  60

Now: 1(20) + 1(30) + 1(40) = 90
Move it again:

10  20 [30  40  50] 60

Now: 1(30) + 1(40) + 1(50) = 120

So the output is being constructed as:

60, 90, 120, ...


5. WHAT DOES x MEAN?
---
x tells us WHERE the filter currently is.

For example:

x = position 1

    [1  1  1]
        ↓  ↓  ↓
    10 20 30

x = position 2

        [1  1  1]
        ↓  ↓  ↓
    10 20 30 40

x = position 3

            [1  1  1]
            ↓  ↓  ↓
    10 20 30 40 50

Therefore:

changing x
    =
moving/sliding the filter

---
6. WHAT DOES m MEAN?

For a particular x,
m identifies the individual values
that are being multiplied.

For example, at one particular x:
g(x) = Σ h(m) f(x-m)
The summation over m means:
"Take all the corresponding values,
multiply them, and add the results."


7. 2-D IMAGE VERSION
---
Now imagine a 3x3 blurring filter:

f =
1/9  1/9  1/9
1/9  1/9  1/9
1/9  1/9  1/9


and an image:

10   10   10   10   10
10   10   10   10   10
10   10  100  100   10
10   10  100  100   10
10   10   10   10   10

Place the filter over one part of the image:

[10   10   10]
[10  100  100]
[10  100  100]

Multiply corresponding values:

1/9(10)    1/9(10)    1/9(10)
1/9(10)    1/9(100)   1/9(100)
1/9(10)    1/9(100)   1/9(100)


Then add:

output =
    (10 + 10 + 10
    +10 + 100 + 100
    +10 + 100 + 100) / 9

= 450 / 9

= 50


That 50 becomes one pixel in the output image.

---
8. THEN MOVE TO THE NEXT POSITION

Move the 3x3 filter one pixel to the right.
Take the new 3x3 region of the image.
Multiply corresponding values.
Add them.
That gives the next output pixel.
Then move again.
So:

position x1 -> calculate output pixel 1
position x2 -> calculate output pixel 2
position x3 -> calculate output pixel 3
...

---
9. convolution is commutative

Because convolution is commutative:

f * h = h * f

we can write 

g(x) = Σ f(m) h(x-m)
as 
g(x) = Σ h(m) f(x-m)

To visualize:
    g(x) = Σ f(m) h(x-m)
    h(m)     = image values
    f(x-m)   = filter positioned at x

or 
    g(x) = Σ h(m) f(x-m)
    h(m)     = filter values
    f(x-m)   = image positioned at x
    
    [  FILTER  ]
         ↓
    ───────────────────────
          IMAGE
    ───────────────────────


        [  FILTER  ]
             ↓
    ───────────────────────
            IMAGE
    ───────────────────────
    
---
10. IMPORTANT: THE FLIPPING ISSUE

For convolution, 
mathematically there is a flip.
For: f(x-m)
the filter is effectively 
reversed before the sliding.

However, for a symmetric blurring filter:

1  1  1
1  1  1
1  1  1

flipping it produces 
exactly the same filter:

1  1  1
1  1  1
1  1  1

Therefore you don't notice the flip.

This is why the usual image-processing picture:
"Take a square filter and slide it over the image"

works perfectly intuitively for a blurring filter.


---
11. Summary

There are two equivalent ways of
thinking about the convolution: f * h = h * f

sliding past f means:

At each position x, 
put the filter over the
corresponding part of the image, 
multiply matching
values, and add them.
Then move the filter to the next x.

That is the geometric meaning of "sliding past f."

"""