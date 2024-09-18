# 8-Puzzle Solver (A* Algorithm)

This project implements the **A\* (A-star) search algorithm** to solve the 8-puzzle problem. The goal is to rearrange a given start state of the puzzle into a specified goal state by sliding tiles into the blank space. The solution is found using the A* algorithm with the **Manhattan Distance** heuristic.

## Problem Statement

The 8-puzzle problem consists of a 3x3 grid with eight numbered tiles and a blank space (denoted by `0`). The objective is to move the tiles to match a goal configuration, using as few moves as possible. The blank space can be moved up, down, left, or right to swap with adjacent tiles.

### Example Start and Goal States:

**Start State:**
1 2 3 4 0 6 7 5 8

**Goal State:**

The goal is to move the tiles in the start state to match the goal state by sliding tiles into the blank space.

## Features

- Implements A\* algorithm to find the optimal solution path.
- Uses **Manhattan Distance** as the heuristic to guide the search.
- Generates valid moves by swapping the blank space with its neighbors.
- Keeps track of visited states to avoid redundant computations.
- Returns the sequence of steps to solve the puzzle if a solution exists.

## How to Use

### Input:

The user provides the initial state of the puzzle as a 3x3 matrix through the console. For example, for the start state:

```bash
Enter row 1 of the start state (space-separated): 1 2 3
Enter row 2 of the start state (space-separated): 4 0 6
Enter row 3 of the start state (space-separated): 7 5 8
