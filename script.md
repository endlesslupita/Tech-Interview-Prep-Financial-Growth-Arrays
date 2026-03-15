# Interview Script: Financial Growth Arrays

## INTRO

"Hi, I'm going to walk through my solution to the Financial Growth Arrays problem. I'll cover my clarifying questions, naive solution, optimized solution, complexity analysis, and test cases."

---

## CLARIFYING QUESTIONS

"Before coding, I'd want to ask a few clarifying questions:

- Is the input array always sorted in non-decreasing order? *(Yes, per the problem statement.)*
- Can the array be empty? *(I'll handle that as an edge case.)*
- Can it contain zeros? *(Yes — I tested for that.)*
- Should I sort the output, or can I assume squaring a sorted array produces a nearly-sortable result? *(The two-pointer approach handles this without a separate sort.)*"

---

## NAIVE SOLUTION

"I'll start with a naive approach. Since the input is sorted, the largest absolute values are at either end — one pointer at the front, one at the back. I compare absolute values, pop the larger one, square it, and append to a stack. After the loop, I reverse the stack to get ascending order.

Here's the issue: `pop(0)` in Python removes the first element and shifts every remaining element down by one. That's O(n) per call, and I call it up to n times — making this **O(n²) time, O(n) space**."

---

## DIAGRAM

*(Scroll to the README diagram)*

"Here's a visual of the optimized approach using `[-3, -1, 4, 7]`. I have a `left` pointer at index 0, a `right` pointer at the last index, and a `fill` pointer also starting at the last index of the output array.

Each step I compare absolute values at left and right, square the larger one, place it at `fill`, move `fill` left, and advance whichever pointer I took from. This fills the output from largest to smallest — no reverse needed."

---

## OPTIMIZED SOLUTION

"The optimized version eliminates `pop(0)` entirely. Instead of removing elements, I use index pointers and pre-allocate the output list with `[0] * n`. Direct index assignment is O(1). The loop runs exactly n times. This gives us **O(n) time, O(n) space** — the space is the same because we still need the output array."

---

## TEST CASES

*(Run pytest)*

"I have 12 tests — 6 for the naive solution, 6 for the optimized. Three normal cases cover mixed negatives and positives, all positives, and a longer mixed array. Three edge cases cover all negatives, an empty list, and a single zero. All 12 pass."

---

## CLOSING

"To summarize: the naive solution is O(n²) time due to `pop(0)` shifting. The optimized two-pointer solution is O(n) time by using direct index access and filling from the back. Both are O(n) space for the output array. The trade-off is added code complexity, but it's a significant performance gain for large inputs."
