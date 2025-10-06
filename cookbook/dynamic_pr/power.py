# Dynamic programming (DP) is used when:
# A problem has overlapping subproblems (the same computation occurs multiple times).
# You store results of subproblems (memoization or tabulation) to avoid recomputation.

memo = {}
def power_dp(base, exp):
    if exp in memo:
        return memo[exp]
    if exp == 1:
        result = base
    else:
        first_exp = exp // 2
        second_exp = exp - first_exp
        result = power_dp(base, first_exp) * power_dp(base, second_exp)
    memo[exp] = result
    return result


