"""
FREQUENCY VS ANGULAR (CIRCULAR) FREQUENCY

1) Frequency (f)

Symbol: f Unit: Hertz (Hz) = cycles per second Meaning: How many
complete cycles happen per second.

Example: If a signal repeats 10 times per second: f = 10 Hz

2) Angular (Circular) Frequency (ω)

Symbol: ω Unit: radians per second (rad/s) Meaning: How fast the phase
angle changes in radians per second.

Since one full cycle = 2π radians:

ω = 2πf f = ω / (2π)

Why Two Different Quantities?

In electronics & signal processing: sin(2πft)

In physics & differential equations: sin(ωt)

Using ω makes equations cleaner (no repeated 2π).

Relationship Between Cycles and Radians

One full cycle = 360° = 2π radians.

If: f = 5 Hz

Then: 5 cycles happen in 1 second Each cycle = 2π radians

So in one second, phase advances:

5 × 2π = 10π radians

This is radians per second — not total radians in general, but rate of
phase change.

Why Is This Important?

Because oscillations are rotations in disguise.

A sine wave: sin(ωt)

is the vertical projection of uniform circular motion.

Instead of asking: “How many cycles per second?”

Physicists ask: “How fast is the angle changing?”

That rate is angular frequency (ω).

When Is One Cycle = 2π?

One cycle equals 2π when we measure phase in radians.

This happens when: - Using sine/cosine - Using complex exponentials
e^(iθ) - Solving differential equations - Doing Fourier transforms -
Studying rotations - Physics oscillators

Because: sin(θ) = sin(θ + 2π)

So periodicity in radians is always 2π.

When Is One Cycle NOT 2π?

Only when measuring differently:

Degrees: One cycle = 360°

Time domain: One cycle = period T T = 1/f

Spatial waves: One cycle = wavelength λ

So “one cycle” depends on what variable you’re measuring.

Domain Comparison: Radians → 2π Degrees → 360° Time → T seconds Space →
λ meters

But in phase space, one cycle is always 2π.

Why Physicists Prefer ω

Harmonic oscillator equation:

d²x/dt² + ω²x = 0

If written with frequency:

d²x/dt² + (2πf)²x = 0

Using ω keeps equations simpler.

Deep Intuition

Think of oscillation as rotation.

Constant rotation speed → constant angular frequency. Sine wave =
projection of rotation.

So:

f = how many laps per second ω = how fast the angle is sweeping

Mathematically:

ω = dθ/dt

Oscillation = rotation in disguise.

"""