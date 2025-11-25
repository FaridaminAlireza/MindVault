"""
Example — k-rank SVD for Image Compression

Overview
  - We show how to compress a grayscale image using a truncated (rank-k) SVD.
  - The idea: compute A = U Σ V^T, keep only the largest k singular values/vectors,
    form A_k = U_k Σ_k V_k^T. A_k is the best rank-k approximation to A (Eckart–Young theorem).
  - This reduces storage from m×n to k*(m + n + 1) numbers (approx), and often
    preserves perceptually important features.

Example setup (small grayscale image)
  - Suppose we have a small 6×6 grayscale image matrix A 
  (pixel intensities 0–255). For clarity we show a toy matrix:
      A = [
        [52, 55, 61, 66, 70, 61],
        [63, 59, 55, 90, 109, 85],
        [62, 59, 68, 113, 144, 104],
        [63, 58, 71, 122, 154, 106],
        [67, 61, 68, 104, 126, 88],
        [68, 65, 60, 70, 77, 68]
      ]
  - (This is small enough to think about but large enough to show low-rank structure.)

Step 1 — Compute SVD of A
  - Compute A = U Σ V^T.
    - U is 6×6 orthogonal (columns = left singular vectors).
    - Σ is 6×6 diagonal with singular values σ1 ≥ σ2 ≥ ... ≥ σ6 ≥ 0.
    - V is 6×6 orthogonal (columns = right singular vectors).
  - In practice, use a numeric library (numpy.linalg.svd, LAPACK, MATLAB, etc.).
    Do not form A^T A explicitly if precision matters.

Step 2 — Inspect singular values
  - Look at the diagonal of Σ: σ1, σ2, σ3, ...
  - Often the first few σ_i are large and the rest decay rapidly
    (image has redundancy).
  - Example (schematic only): Σ_diagonal ≈ [400, 80, 20, 5, 1, 0.5]
    - Here σ1 is dominant; σ2 still significant; remaining are small.

Step 3 — Choose k
  - Choose k according to:
      - Desired compression ratio/storage budget; or
      - Energy threshold: keep the smallest k such that
            (σ1^2 + ... + σk^2) / (σ1^2 + ... + σr^2) ≥ τ
        for some τ (e.g., τ = 0.90 or 0.95).
  - Example: with the schematic singular values above,
      - σ1^2 = 160000, σ2^2 = 6400, σ3^2 = 400, σ4^2 = 25, ...
      - Total energy ≈ 167000. To capture 95% energy you might
        need k = 2 (160000+6400 = 166400 ≈ 99.6%).

Step 4 — Form truncated matrices U_k, Σ_k, V_k
  - U_k: first k columns of U (size 6×k).
  - Σ_k: top-left k×k block of Σ (diagonal with σ1..σk).
  - V_k: first k columns of V (size 6×k).
  - Then A_k = U_k Σ_k V_k^T (size 6×6), rank ≤ k.

Step 5 — Reconstruct approximation A_k and visualize
  - For k = 1:
      - A_1 = σ1 * u1 * v1^T  (outer product). This captures
        the dominant structure (global contrast, main gradient).
  - For k = 2:
      - A_2 = σ1 u1 v1^T + σ2 u2 v2^T. This adds finer structure/texture.
  - Compare A and A_k visually: often A_2 or A_5 looks almost as good as
    A for many natural images.

Step 6 — Compute approximation error (quantitative)
  - Frobenius norm error:
      ||A - A_k||_F = sqrt(σ_{k+1}^2 + σ_{k+2}^2 + ... + σ_r^2)
    (this follows from orthogonality and Eckart–Young).
  - Relative error (energy retained):
      energy_retained = (σ1^2 + ... + σk^2) / (σ1^2 + ... + σr^2).
  - Example using schematic singular values and k=2:
      - residual_energy = σ3^2 + σ4^2 + ... ≈ 400 + 25 + 1 + 0.25 = 426.25
      - ||A - A_2||_F = sqrt(426.25) ≈ 20.64
      - energy_retained ≈ (160000 + 6400) / 167000 ≈ 0.996

Step 7 — Storage and compression ratio
  - Store A exactly: m×n numbers = 36 numbers (here).
  - Store A_k via SVD factors: U_k (6×k), Σ_k (k numbers), V_k (6×k) 
  → total ≈ k*(6+6) + k = k*(12) + k? More precisely: (m*k) + k + (n*k) = k*(m + n + 1).
    - For m=n=6 and k=2: storage ≈ 2*(6+6+1) = 26 numbers (vs 36 original) → ~28% reduction.
    - For large images (m,n big) and small k, the savings are huge.

Step 8 — Practical considerations for real images
  - Color images:
      - Apply SVD separately to each color channel (R, G, B) or 
      convert to YCbCr and compress luminance more aggressively.
  - Quantization:
      - After forming A_k, you may quantize pixel values to integers 0–255.
  - Memory vs quality tradeoff:
      - Lower k → higher compression, more blurring;
        higher k → better fidelity, larger size.
  - Computing only top-k singular values:
      - For large images, use truncated or randomized SVD algorithms
        to compute only the largest k singular values/vectors efficiently.

Pseudo-code (numpy-style)
  # A is an m x n float matrix (grayscale)
  U, s, VT = svd(A, full_matrices=False)          # s is vector of singular values
  k = choose_k_based_on_energy(s, tau=0.95)       # choose k
  U_k = U[:, :k]                                  # m x k
  S_k = diag(s[:k])                               # k x k
  V_kT = VT[:k, :]                                # k x n
  A_k = U_k @ S_k @ V_kT                          # reconstructed image

Worked-small numeric intuition (rank-1)
  - Let u1 be the first left singular vector (column vector), v1 the first right singular vector.
  - A_1 = σ1 u1 v1^T: each row of A_1 is a scalar multiple of v1^T (so rows are all linearly dependent).
  - For an image, this means A_1 captures a single dominant pattern (e.g., a smooth gradient or average background).

Visual intuition
  - The right singular vectors v_i (rows of V^T) capture horizontal patterns across columns.
  - The left singular vectors u_i capture vertical patterns across rows.
  - Singular value σ_i scales the contribution of pattern pair (u_i, v_i).
  - Truncation removes small-scale patterns/noise (those scaled by small σ_i).

Closing notes
  - Rank-k SVD gives the best approximation in both spectral and Frobenius norms.
  - Use energy thresholding (retain 90–99% energy) or eye-based tuning for images.
  - For big images, use libraries that implement fast truncated SVD (randomized SVD, ARPACK-based methods).

"""