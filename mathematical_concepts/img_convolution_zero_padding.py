""" E
DFT CONVOLUTION: PERIODICITY, WRAP-AROUND, AND ZERO PADDING

1. THE MAIN IDEA

When we use the DFT to perform convolution, we calculate:

    DFT(f) * DFT(h)
             |
             v
          IDFT
             |
             v
       convolution

However, there is an important difference:

    DFT multiplication  ->  CIRCULAR CONVOLUTION

while usually we want:

    LINEAR CONVOLUTION


Why?

Because the DFT assumes that every input function is PERIODIC.

If the DFT length is N, it assumes:

    f[m + N] = f[m]

So the function repeats every N samples.


2. A SIMPLE EXAMPLE


Let:

    f = [1  1  1]

and:

    h = [1  1  1]


We first calculate their ordinary (linear) convolution.


3. LINEAR CONVOLUTION


Imagine h sliding across f.

The result is:

    f * h = [1  2  3  2  1]


You can see where these values come from:

    1
    1 + 1 = 2
    1 + 1 + 1 = 3
    1 + 1 = 2
    1 = 1


Therefore:

    LINEAR CONVOLUTION:

        [1  2  3  2  1]

The result has 5 samples.

Why 5?

    length(f) + length(h) - 1

    = 3 + 3 - 1

    = 5


4. NOW USE A 3-POINT DFT


Suppose we take a 3-point DFT because both functions
have length 3.

The DFT assumes:

    f = [1  1  1]

actually represents the periodic signal:

    ... [1  1  1] [1  1  1] [1  1  1] [1  1  1] ...


The same happens to h:

    ... [1  1  1] [1  1  1] [1  1  1] [1  1  1] ...


So the DFT does NOT think the signal ends after the
third sample.

It thinks it immediately starts again.


5. THIS CAUSES WRAP-AROUND


The linear convolution was:

    [1  2  3  2  1]

Think of its positions as:

       0   1   2   3   4
       -------------------
       1   2   3   2   1


But the 3-point DFT only has positions:

       0   1   2
       ---------
       1   2   3


What happens to the values at positions 3 and 4?

Because the DFT is periodic, they WRAP AROUND to the
beginning.


Position 3:

    value = 2

    3 modulo 3 = 0

so:

    position 3  ->  position 0


Position 4:

    value = 1

    4 modulo 3 = 1

so:

    position 4  ->  position 1


Therefore the values are combined like this:

    position 0:

        original:       1
        wrapped from 3: 2
                        ---
        total:          3


    position 1:

        original:       2
        wrapped from 4: 1
                        ---
        total:          3


    position 2:

        original:       3
        wrapped:        0
                        ---
        total:          3


Therefore:

    CIRCULAR CONVOLUTION:

        [3  3  3]


This is different from:

    LINEAR CONVOLUTION:

        [1  2  3  2  1]


6. VISUALIZING THE WRAP-AROUND


Linear result:

    [1  2  3  2  1]
     ^        ^
     |        |
     |        |
     |        +---- wraps to position 1
     |
     +------------- position 3 wraps to position 0


More explicitly:

    position:   0   1   2   3   4
                -------------------
    value:      1   2   3   2   1

                |       |   |
                |       |   +----> position 1
                |       |
                +----------- position 0


So:

    1 + 2 = 3

    2 + 1 = 3

    3     = 3


giving:

    [3  3  3]


This unwanted contribution is called:

    WRAP-AROUND


7. WHY DOES THE BOOK SAY "PERIODIC"?


The DFT assumes:

    f[m + N] = f[m]

For N = 3:

    f[m + 3] = f[m]

Therefore:

    f[0] = f[3] = f[6] = ...
    f[1] = f[4] = f[7] = ...
    f[2] = f[5] = f[8] = ...


So:

    [1 1 1]

is interpreted as:

    ... 1 1 1 | 1 1 1 | 1 1 1 | 1 1 1 ...


The DFT sees the signal as a circle rather than a finite
line.


8. THE SOLUTION: ZERO PADDING

If we want LINEAR convolution using the DFT, we need to
increase the DFT length.

For functions of lengths M and N:

    required DFT length >= M + N - 1


In our example:

    M = 3
    N = 3

so:

    M + N - 1 = 5


Therefore we zero-pad both functions to length 5:

    f = [1  1  1  0  0]

    h = [1  1  1  0  0]


Then use a 5-point DFT.


9. WHY DO THE ZEROS FIX THE PROBLEM?


The DFT now assumes a period of 5.

So:

    f = [1  1  1  0  0]

is interpreted as:

    ... [1 1 1 0 0] [1 1 1 0 0] [1 1 1 0 0] ...


Notice the zeros between the copies.

The convolution result is:

    [1  2  3  2  1]


It fits completely inside the 5 available positions.

There is therefore no unwanted nonzero value wrapping from
the end back to the beginning.


10. LINEAR VS CIRCULAR CONVOLUTION


WITHOUT ZERO PADDING:

    f = [1 1 1]
    h = [1 1 1]

    DFT length = 3

          DFT
           |
           v
    circular convolution
           |
           v

       [3 3 3]


WITH ZERO PADDING:

    f = [1 1 1 0 0]
    h = [1 1 1 0 0]

    DFT length = 5

          DFT
           |
           v
    circular convolution
           |
           v

       [1 2 3 2 1]

    which is exactly the desired
    linear convolution.


11. THE MOST IMPORTANT FORMULA


If:

    length(f) = M

    length(h) = N

then the length of their linear convolution is:

    M + N - 1


Therefore, to use the DFT to calculate linear convolution:

    choose DFT length L such that

        L >= M + N - 1


and zero-pad both signals to length L.


12. INTUITION


Think of the DFT as putting the signal on a CIRCLE.

Without zero padding:

             0
           /   \
         2       1
           \   /
            


If the convolution goes past the end:

    right side
         |
         v
         0
       /   \
     2       1
       \   /
        <---

it comes back to the beginning.

That is the WRAP-AROUND effect.


Zero padding makes the circle large enough that the complete
linear convolution fits inside it before wrapping can occur.


13. THE BOOK'S SENTENCE IN SIMPLE WORDS


Book:

"Using the DFT allows us to perform convolution in the
frequency domain, but the functions are treated as periodic,
with a period equal to the length of the functions."


Meaning:

    The DFT assumes the input repeats forever.

    Therefore DFT multiplication naturally produces
    circular convolution.

    Circular convolution can cause the end of the result
    to wrap around and add to the beginning.

    If we want ordinary linear convolution, we prevent
    this by zero-padding the inputs.

    For lengths M and N, use a DFT length of at least:

        M + N - 1


FINAL MEMORY PICTURE


    LINEAR CONVOLUTION:

    [1  2  3  2  1]
     ---------------->
       no wrapping


    CIRCULAR CONVOLUTION:

    [1  2  3]
     ^     |
     |_____|
       wrapping


    ZERO-PADDED DFT:

    [1  1  1  0  0]
     ----------------
       enough space
       for the result

    Result:

    [1  2  3  2  1]


The central idea is:

    DFT = periodic world

    zero padding = create enough space so that
                   periodic wrap-around does not
                   corrupt the linear convolution.
"""