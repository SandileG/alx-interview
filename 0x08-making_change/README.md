# Coin Change Problem: README

The "Change comes from within" project focuses on solving the *coin change problem*, a classic challenge in algorithm design. This README will explain the problem, different approaches to solving it, and how to implement a solution efficiently.

---

## Problem Description

Given:
- A list of coin denominations (e.g., `[1, 2, 5]`).
- A target amount (e.g., `11`).

The task is to determine the **minimum number of coins** required to make the target amount. If it’s not possible to achieve the amount using the given denominations, the function should return `-1`.

---

## Approaches to Solve the Problem

### 1. **Greedy Algorithm**
A greedy algorithm attempts to solve the problem by:
1. Selecting the largest coin denomination that does not exceed the target amount.
2. Subtracting the value of that coin from the target amount.
3. Repeating until the target amount is zero.

#### Example:
- Denominations: `[1, 2, 5]`
- Target: `11`

Steps:
1. Choose `5` → Remaining amount: `6`.
2. Choose `5` again → Remaining amount: `1`.
3. Choose `1` → Remaining amount: `0`.

Result: 3 coins (`[5, 5, 1]`).

**Limitations**:  
The greedy algorithm does not always yield the optimal solution. For example, with denominations `[1, 3, 4]` and a target `6`, the greedy algorithm may choose `[4, 1, 1]` (3 coins) instead of `[3, 3]` (2 coins).

---

### 2. **Dynamic Programming Approach**
Dynamic programming (DP) provides an optimal solution by breaking the problem into smaller subproblems. The key idea is to compute the minimum coins required for every amount from `0` to the target amount.

#### Steps:
1. Create an array `dp` of size `(target + 1)` initialized to `float('inf')` (representing an unreachable state), except `dp[0] = 0` (no coins needed for amount `0`).
2. For each coin in the list of denominations:
   - For each amount `x` from the coin's value to `target`:
     - Update `dp[x]` using the formula:  
       `dp[x] = min(dp[x], dp[x - coin] + 1)`
3. Return `dp[target]`. If `dp[target]` is still `float('inf')`, return `-1`.

#### Example:
- Denominations: `[1, 3, 4]`
- Target: `6`

| Amount | `dp` Array Updates |
|--------|---------------------|
| `0`    | `0`                |
| `1`    | `1` (using `1`)    |
| `2`    | `2` (using `1, 1`) |
| `3`    | `1` (using `3`)    |
| `4`    | `1` (using `4`)    |
| `5`    | `2` (using `4, 1`) |
| `6`    | `2` (using `3, 3`) |

Result: 2 coins (`[3, 3]`).

#### Complexity:
- **Time Complexity**: `O(n * target)` where `n` is the number of denominations.
- **Space Complexity**: `O(target)` for the `dp` array.

---

### 3. **Comparison of Approaches**

| Approach       | Pros                              | Cons                                         |
|----------------|-----------------------------------|---------------------------------------------|
| Greedy         | Simple and fast for some cases.  | May fail to find the optimal solution.      |
| Dynamic Prog.  | Guarantees optimal solution.     | Higher computational cost compared to greedy.|

---

## Implementation in Python

### Greedy Algorithm
```python
def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if amount == 0:
            break
        count += amount // coin
        amount %= coin
    return count if amount == 0 else -1
```

### Dynamic Programming
```python
def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins for amount 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
```

---

## Steps to Solve the Problem

1. **Understand Input and Output**:
   - Input: List of denominations and the target amount.
   - Output: Minimum number of coins or `-1`.

2. **Decide the Algorithm**:
   - Use the **greedy approach** for simple cases (e.g., when denominations include `1` or follow a pattern like `[1, 2, 4]`).
   - Use **dynamic programming** for complex cases.

3. **Write Tests**:
   Test the solution with edge cases:
   - Target amount = `0` (should return `0`).
   - No denominations (should return `-1`).
   - Denominations cannot form the target (should return `-1`).

4. **Optimize**:
   - Analyze performance with large inputs.
   - Refactor code for clarity and efficiency.

---

## Example Usage
```python
coins = [1, 2, 5]
amount = 11

# Greedy Algorithm
print(coin_change_greedy(coins, amount))  # Output: 3

# Dynamic Programming
print(coin_change_dp(coins, amount))  # Output: 3
```

---

## Summary
The coin change problem demonstrates the importance of choosing the right algorithm based on problem constraints. While the greedy approach is faster and simpler, dynamic programming guarantees correctness for all cases. By practicing both approaches, you will gain a deeper understanding of algorithm design and optimization.
