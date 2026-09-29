# Day 22: Pattern Problems & Logic Building in Python 🌟📐

> **Motto**: *"Not here to be known, here to build."*  
> **Author**: Harish  
> **Repository**: [DAY-22-OF-PYTHON](https://github.com/harish-0987/DAY-22-OF-PYTHON)

Welcome to **Day 22 of Python**! Today's focus is on **Mastering Pattern Problems & Logic Building** in Python.

Pattern printing is one of the most foundational and frequently tested problem-solving domains in software engineering, technical coding rounds, and competitive programming. Beyond visual printing, it develops your intuition for **nested loops**, **coordinate geometry in 2D space**, **arithmetic progressions**, and **symmetrical problem decomposition**.

---

## 📌 Table of Contents

1. [Overview & Learning Objectives](#-overview--learning-objectives)
2. [The Universal 4-Step Pattern Formula](#-the-universal-4-step-pattern-formula)
3. [Pattern Categories & Implementations](#-pattern-categories--implementations)
   - [Category 1: Basic Star Patterns](#category-1-basic-star-patterns)
   - [Category 2: Pyramids, Diamonds & Symmetrical Patterns](#category-2-pyramids-diamonds--symmetrical-patterns)
   - [Category 3: Number & Binary Patterns](#category-3-number--binary-patterns)
   - [Category 4: Character & Alphabet Patterns](#category-4-character--alphabet-patterns)
   - [Category 5: Hollow & Boundary Patterns](#category-5-hollow--boundary-patterns)
   - [Category 6: Advanced Matrix & Mathematical Patterns](#category-6-advanced-matrix--mathematical-patterns)
4. [Master Formula Reference Sheet](#-master-formula-reference-sheet)
5. [Complexity Analysis](#-complexity-analysis)
6. [Top Interview Tips for Pattern Problems](#-top-interview-tips-for-pattern-problems)
7. [How to Run the Code](#-how-to-run-the-code)
8. [Summary & Takeaways](#-summary--takeaways)

---

## 🎯 Overview & Learning Objectives

By completing Day 22, you will understand:
- How to systematically break down any visual grid into mathematical relations between row index `i` and column index `j`.
- How to calculate leading whitespace and trailing symmetric elements cleanly.
- How to manipulate ASCII characters (`ord()` and `chr()`) for dynamic letter patterns.
- How to generate mathematical structures like **Pascal's Triangle** and **Concentric Distance Matrix** ($2n - 1 \times 2n - 1$).
- How to write clean, modular, and reusable Python functions.

---

## 💡 The Universal 4-Step Pattern Formula

Every 2D pattern can be decoded using this exact 4-step framework:

```
┌───────────────────────────────────────────────────────────────┐
│ STEP 1: OUTER LOOP (Rows)                                     │
│ How many total lines are there? range(n) or range(1, n+1)     │
└───────────────────────────────┬───────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│ STEP 2: INNER LOOP 1 (Leading Spaces)                         │
│ Is the pattern right-aligned or centered? Compute space count │
└───────────────────────────────┬───────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│ STEP 3: INNER LOOP 2 (Characters / Stars / Numbers)           │
│ What is printed on row i? Count = f(i), Value = g(i, j)       │
└───────────────────────────────┬───────────────────────────────┘
                                │
                                ▼
┌───────────────────────────────────────────────────────────────┐
│ STEP 4: SYMMETRY / MIRRORING (If applicable)                  │
│ For diamonds & butterflies: split into top half & bottom half │
└───────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Pattern Categories & Implementations

### Category 1: Basic Star Patterns

#### 1. Solid Square
```
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```
- **Formula**: $n$ rows, each row has $n$ stars.
- **Code snippet**:
  ```python
  for i in range(n):
      print("* " * n)
  ```

#### 2. Right-Angled Triangle (Left Aligned)
```
*
* *
* * *
* * * *
* * * * *
```
- **Formula**: Row $i$ ($1$-indexed) prints $i$ stars.
- **Code snippet**:
  ```python
  for i in range(1, n + 1):
      print("* " * i)
  ```

#### 3. Inverted Right-Angled Triangle
```
* * * * *
* * * *
* * *
* *
*
```
- **Formula**: Row $i$ starts from $n$ stars and decrements down to $1$.
- **Code snippet**:
  ```python
  for i in range(n, 0, -1):
      print("* " * i)
  ```

#### 4. Mirrored Right-Angled Triangle (Right Aligned)
```
        *
      * *
    * * *
  * * * *
* * * * *
```
- **Formula**: Leading spaces = $2 \times (n - i)$, Stars = $i$.

#### 5. Inverted Mirrored Right Triangle
```
* * * * *
  * * * *
    * * *
      * *
        *
```
- **Formula**: Leading spaces = $2 \times i$, Stars = $n - i$.

---

### Category 2: Pyramids, Diamonds & Symmetrical Patterns

#### 6. Full Star Pyramid
```
    *
   ***
  *****
 *******
*********
```
- **Formula**: Spaces = $n - i$, Stars = $2i - 1$.
- **Code snippet**:
  ```python
  for i in range(1, n + 1):
      print(" " * (n - i) + "*" * (2 * i - 1))
  ```

#### 7. Inverted Star Pyramid
```
*********
 *******
  *****
   ***
    *
```
- **Formula**: Spaces = $n - i$, Stars = $2i - 1$ where $i$ counts down from $n$ to $1$.

#### 8. Solid Diamond
```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```
- **Formula**: Top upright pyramid ($1 \dots n$) + Bottom inverted pyramid ($n-1 \dots 1$).

#### 9. Half Diamond (Sideways Pyramid)
```
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
```
- **Formula**: Total rows = $2n - 1$. For row $i$, `stars = i if i <= n else 2*n - i`.

#### 10. Hourglass Pattern
```
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
```

#### 11. Butterfly Pattern
```
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
```
- **Formula**: Left stars = $i$, Middle spaces = $2 \times (n - i)$, Right stars = $i$. Mirror for bottom half.

---

### Category 3: Number & Binary Patterns

#### 12. Same Number Triangle
```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

#### 13. Increasing Number Triangle
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

#### 14. Floyd's Triangle
```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```
- **Logic**: Maintain a running accumulator counter `current = 1`, incrementing on each printed cell.

#### 15. Binary Alternating (0-1) Triangle
```
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
```
- **Formula**: If `(row + col) % 2 == 0` print `1`, else `0`. Or flip state with `start = 1 - start`.

#### 16. Palindromic Number Pyramid
```
    1
   121
  12321
 1234321
123454321
```
- **Formula**: Ascending numbers from $1$ to $i$, then descending from $i-1$ down to $1$.

#### 17. Number Crown / Valley Pattern
```
1                 1
1 2             2 1
1 2 3         3 2 1
1 2 3 4     4 3 2 1
1 2 3 4 5 5 4 3 2 1
```
- **Formula**: Left numbers $1 \dots i$, middle spaces $2 \times (n - i)$, right numbers $i \dots 1$.

---

### Category 4: Character & Alphabet Patterns

Using `chr(65 + index)` where `65` is ASCII for `'A'`.

#### 18. Increasing Alphabet Triangle
```
A
A B
A B C
A B C D
A B C D E
```

#### 19. Same Alphabet Triangle
```
A
B B
C C C
D D D D
E E E E E
```

#### 20. Alphabet Palindromic Pyramid
```
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
```

#### 21. Reverse Letter Triangle
```
E
D E
C D E
B C D E
A B C D E
```
- **Formula**: Start char on row $i$ is `65 + (n - 1 - i)`.

---

### Category 5: Hollow & Boundary Patterns

In hollow patterns, stars are printed **only on boundaries**:
- First row / Last row
- First column / Last column
- Inner cells contain whitespace.

#### 22. Hollow Square
```
* * * * *
*       *
*       *
*       *
* * * * *
```

#### 23. Hollow Pyramid
```
    *
   * *
  *   *
 *     *
*********
```
- **Formula**: Row $1$ has $1$ star; Row $n$ is filled with stars; Middle rows have $1$ star, $(2i - 3)$ spaces, and $1$ star.

#### 24. Hollow Diamond
```
    *
   * *
  *   *
 *     *
  *   *
   * *
    *
```

---

### Category 6: Advanced Matrix & Mathematical Patterns

#### 25. Pascal's Triangle
```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```
- **Formula**: Every element is $C(n, k) = \frac{n!}{k!(n-k)!}$ or computed additively via `row[j] = prev[j-1] + prev[j]`.

#### 26. Concentric Square Number Matrix (FAANG Interview Classic)
For $n = 4$, matrix size is $(2n - 1) \times (2n - 1) = 7 \times 7$:
```
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
```
- **Core Formula**:
  $$\text{value}(i, j) = n - \min(\text{top}, \text{left}, \text{bottom}, \text{right})$$
  Where:
  - $\text{top} = i$
  - $\text{left} = j$
  - $\text{bottom} = (2n - 2) - i$
  - $\text{right} = (2n - 2) - j$

---

## 📊 Master Formula Reference Sheet

| Pattern Type | Rows | Leading Spaces | Symbols / Elements | Key Formula |
| :--- | :---: | :---: | :---: | :--- |
| **Right Triangle** | $n$ | $0$ | $i$ stars | `* * i` |
| **Inverted Triangle** | $n$ | $0$ | $n - i + 1$ stars | `* * (n - i)` |
| **Full Pyramid** | $n$ | $n - i$ | $2i - 1$ stars | `" "*(n-i) + "*"*(2*i-1)` |
| **Diamond** | $2n - 1$ | $|n - i|$ | $2(n - |n - i|) - 1$ | Combined Upright + Inverted |
| **Floyd's Triangle** | $n$ | $0$ | $i$ numbers | `current += 1` |
| **Binary Triangle** | $n$ | $0$ | $i$ bits | `(i + j) % 2` or `1 - state` |
| **Palindromic Pyramid** | $n$ | $n - i$ | $1 \to i \to 1$ | Ascending + Descending loops |
| **Hollow Pyramid** | $n$ | $n - i$ | Boundary stars | Inner spaces $= 2i - 3$ |
| **Concentric Square** | $2n - 1$ | $0$ | $(2n - 1)$ per row | $n - \min(\text{distances})$ |

---

## ⚡ Complexity Analysis

- **Time Complexity**:
  - Most 2D patterns iterate over $n$ rows and up to $O(n)$ columns per row.
  - Overall Time Complexity: $\mathcal{O}(n^2)$
  - Concentric Matrix: $\mathcal{O}((2n)^2) = \mathcal{O}(n^2)$
- **Space Complexity**:
  - If printed line-by-line: $\mathcal{O}(1)$ auxiliary space (excluding string output buffers).
  - If stored in memory (Pascal triangle / grid): $\mathcal{O}(n^2)$ space.

---

## 💡 Top Interview Tips for Pattern Problems

1. **Draw a Grid**: Always sketch an index table on paper showing row index $i$ against column index $j$.
2. **Tabulate Relationships**: Create columns for:
   - Row $i$
   - Number of leading spaces
   - Number of symbols/digits
   - Value of symbols
3. **Spot Linearity**: Notice if the counts form an Arithmetic Progression (e.g., $1, 3, 5, 7 \implies 2i - 1$).
4. **Leverage String Multiplication**: In Python, `" " * k` and `"* " * k` make pattern printing significantly cleaner than nested manual loops.
5. **Handle Symmetries Separately**: Don't try to solve complex diamonds or butterflies in a single convoluted loop—split them into top and bottom halves.

---

## 💻 How to Run the Code

Run the master script directly using Python:

```bash
python day22.py
```

All 28 pattern problems across all categories will run sequentially with clean headers and visual outputs in your terminal!

---

## 🚀 Summary & Takeaways

- You now possess an intuitive mental blueprint to decompose and code any 2D pattern question.
- Mastered loop bounds, space calculations, ASCII character conversions, palindromes, and 2D distance transforms.
- Built a reusable reference implementation for technical interview preparation.

*"Not here to be known, here to build."*
