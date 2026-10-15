# Puzzle #008 — Second-Largest Number

**Type:** Solve  
**Difficulty:** Beginner  
**Skill:** Track two values

## Problem

Return the second-largest distinct number in a list. If there are fewer than two distinct numbers, return `None`.

## Rules

- Repeated copies of the largest number count as one distinct value.
- Do not use `sort()`, `sorted()`, `set()`, or `max()`.
- Negative numbers are allowed.

## Examples

Input: `[4, 8, 2, 8, 6, 4]`  
Output: `6`

Input: `[9, 3]`  
Output: `3`

Input: `[5, 5, 5]`  
Output: `None`

Input: `[-5, -2, -8]`  
Output: `-5`

## Edge cases

An empty list or a list with one distinct value returns `None`.

## First attempt

Try to solve it with basic language features before opening a solution.
