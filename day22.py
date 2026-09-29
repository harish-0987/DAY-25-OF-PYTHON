# =============================================================================
# DAY 22: PATTERN PRINTING & LOGIC BUILDING IN PYTHON
# Author: Harish
# Repository: DAY-22-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

"""
DAY 22: MASTERING PATTERN PROBLEMS IN PYTHON
---------------------------------------------
Pattern printing is a classic and essential domain in computer science that
builds deep mental models for:
  1. Nested Loops (Outer loop = Rows, Inner loop(s) = Columns / Spaces / Symbols)
  2. Index Arithmetic & Coordinate Mapping (i, j, n relations)
  3. Spatial Reasoning & Symmetrical Decomposition
  4. Algorithmic Optimization & String Construction

General 4-Step Formula to Solve ANY Pattern:
  Step 1: Identify Total Rows -> Outer loop runs from i = 0 to n-1 (or 1 to n).
  Step 2: Identify Leading Spaces -> Inner loop 1 prints whitespace based on i.
  Step 3: Identify Characters / Stars / Numbers -> Inner loop 2 prints values.
  Step 4: Identify Symmetry / End Condition -> Handle palindromes or mirror halves.
"""


def print_header(title: str) -> None:
    """Utility function to print cleanly formatted pattern titles."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


# =============================================================================
# CATEGORY 1: BASIC STAR PATTERNS
# =============================================================================

def pattern_square_star(n: int = 5) -> None:
    """
    1. Solid Square of Stars
    Rows: n, Cols: n
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    """
    print_header("1. Solid Square Pattern")
    for i in range(n):
        print("* " * n)


def pattern_right_triangle(n: int = 5) -> None:
    """
    2. Right-Angled Triangle (Left Aligned)
    Row i has (i + 1) stars
    *
    * *
    * * *
    * * * *
    * * * * *
    """
    print_header("2. Right-Angled Triangle (Left Aligned)")
    for i in range(1, n + 1):
        print("* " * i)


def pattern_inverted_right_triangle(n: int = 5) -> None:
    """
    3. Inverted Right-Angled Triangle
    Row i has (n - i) stars
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    print_header("3. Inverted Right-Angled Triangle")
    for i in range(n, 0, -1):
        print("* " * i)


def pattern_mirrored_right_triangle(n: int = 5) -> None:
    """
    4. Mirrored Right-Angled Triangle (Right Aligned)
    Row i has (n - i) spaces and i stars
            *
          * *
        * * *
      * * * *
    * * * * *
    """
    print_header("4. Mirrored Right-Angled Triangle (Right Aligned)")
    for i in range(1, n + 1):
        spaces = "  " * (n - i)
        stars = "* " * i
        print(spaces + stars)


def pattern_inverted_mirrored_triangle(n: int = 5) -> None:
    """
    5. Inverted Mirrored Right Triangle
    Row i has i spaces and (n - i) stars
    * * * * *
      * * * *
        * * *
          * *
            *
    """
    print_header("5. Inverted Mirrored Right Triangle")
    for i in range(n):
        spaces = "  " * i
        stars = "* " * (n - i)
        print(spaces + stars)


# =============================================================================
# CATEGORY 2: PYRAMIDS, DIAMONDS & SYMMETRIC PATTERNS
# =============================================================================

def pattern_full_pyramid(n: int = 5) -> None:
    """
    6. Equilateral / Full Star Pyramid
    Spaces: (n - i), Stars: (2*i - 1)
        *
       ***
      *****
     *******
    *********
    """
    print_header("6. Full Star Pyramid")
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


def pattern_inverted_pyramid(n: int = 5) -> None:
    """
    7. Inverted Full Star Pyramid
    Spaces: i, Stars: 2*(n - i) - 1
    *********
     *******
      *****
       ***
        *
    """
    print_header("7. Inverted Star Pyramid")
    for i in range(n, 0, -1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


def pattern_diamond(n: int = 5) -> None:
    """
    8. Solid Diamond Pattern
    Combination of Full Pyramid + Inverted Pyramid
        *
       ***
      *****
     *******
    *********
     *******
      *****
       ***
        *
    """
    print_header("8. Solid Diamond Pattern")
    # Top half (including center row)
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Bottom half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))


def pattern_half_diamond(n: int = 5) -> None:
    """
    9. Half Diamond (Sideways Pyramid)
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    print_header("9. Half Diamond Pattern")
    for i in range(1, 2 * n):
        stars = i if i <= n else (2 * n - i)
        print("* " * stars)


def pattern_hourglass(n: int = 5) -> None:
    """
    10. Hourglass Pattern
    Inverted Pyramid followed by Full Pyramid
    *********
     *******
      *****
       ***
        *
       ***
      *****
     *******
    *********
    """
    print_header("10. Hourglass Pattern")
    # Upper inverted pyramid
    for i in range(n, 1, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Lower upright pyramid
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))


def pattern_butterfly(n: int = 5) -> None:
    """
    11. Butterfly Pattern
    Row i has i stars, 2*(n - i) spaces, and i stars
    *                 *
    * *             * *
    * * *         * * *
    * * * *     * * * *
    * * * * * * * * * *
    * * * *     * * * *
    * * *         * * *
    * *             * *
    *                 *
    """
    print_header("11. Butterfly Pattern")
    # Upper half
    for i in range(1, n + 1):
        stars = "* " * i
        spaces = "  " * (2 * (n - i))
        print(stars + spaces + stars)
    # Lower half
    for i in range(n - 1, 0, -1):
        stars = "* " * i
        spaces = "  " * (2 * (n - i))
        print(stars + spaces + stars)


# =============================================================================
# CATEGORY 3: NUMBER & BINARY PATTERNS
# =============================================================================

def pattern_same_number_triangle(n: int = 5) -> None:
    """
    12. Same Number Triangle
    Row i repeats digit i (i times)
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
    """
    print_header("12. Same Number Triangle")
    for i in range(1, n + 1):
        row = " ".join(str(i) for _ in range(i))
        print(row)


def pattern_increasing_number_triangle(n: int = 5) -> None:
    """
    13. Increasing Number Triangle
    Row i prints 1 up to i
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    """
    print_header("13. Increasing Number Triangle")
    for i in range(1, n + 1):
        row = " ".join(str(col) for col in range(1, i + 1))
        print(row)


def pattern_inverted_number_triangle(n: int = 5) -> None:
    """
    14. Inverted Increasing Number Triangle
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1
    """
    print_header("14. Inverted Increasing Number Triangle")
    for i in range(n, 0, -1):
        row = " ".join(str(col) for col in range(1, i + 1))
        print(row)


def pattern_floyds_triangle(n: int = 5) -> None:
    """
    15. Floyd's Triangle
    Consecutive integers starting from 1
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
    """
    print_header("15. Floyd's Triangle")
    current = 1
    for i in range(1, n + 1):
        row_vals = []
        for _ in range(i):
            row_vals.append(str(current))
            current += 1
        print(" ".join(row_vals))


def pattern_binary_triangle(n: int = 5) -> None:
    """
    16. Binary Alternating (0-1) Triangle
    If (row + col) is even -> 1, else 0
    1
    0 1
    1 0 1
    0 1 0 1
    1 0 1 0 1
    """
    print_header("16. Binary Alternating Triangle (0-1)")
    for i in range(1, n + 1):
        row = []
        start = 1 if i % 2 != 0 else 0
        for j in range(i):
            row.append(str(start))
            start = 1 - start
        print(" ".join(row))


def pattern_palindromic_number_pyramid(n: int = 5) -> None:
    """
    17. Palindromic Number Pyramid
    Ascends from 1 to i, then descends back to 1
        1
       121
      12321
     1234321
    123454321
    """
    print_header("17. Palindromic Number Pyramid")
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        ascending = "".join(str(x) for x in range(1, i + 1))
        descending = "".join(str(x) for x in range(i - 1, 0, -1))
        print(spaces + ascending + descending)


def pattern_number_crown(n: int = 5) -> None:
    """
    18. Number Crown / Valley Pattern
    Left number list + Middle spaces + Right reversed number list
    1                 1
    1 2             2 1
    1 2 3         3 2 1
    1 2 3 4     4 3 2 1
    1 2 3 4 5 5 4 3 2 1
    """
    print_header("18. Number Crown Pattern")
    for i in range(1, n + 1):
        left = " ".join(str(x) for x in range(1, i + 1))
        right = " ".join(str(x) for x in range(i, 0, -1))
        spaces = "  " * (2 * (n - i))
        if spaces:
            print(left + "  " + spaces[:-2] + right)
        else:
            print(left + " " + right)


# =============================================================================
# CATEGORY 4: CHARACTER & ALPHABET PATTERNS
# =============================================================================

def pattern_increasing_alphabet_triangle(n: int = 5) -> None:
    """
    19. Increasing Alphabet Triangle
    A
    A B
    A B C
    A B C D
    A B C D E
    """
    print_header("19. Increasing Alphabet Triangle")
    for i in range(1, n + 1):
        row = " ".join(chr(65 + j) for j in range(i))
        print(row)


def pattern_same_alphabet_triangle(n: int = 5) -> None:
    """
    20. Same Alphabet Triangle
    A
    B B
    C C C
    D D D D
    E E E E E
    """
    print_header("20. Same Alphabet Triangle")
    for i in range(n):
        char = chr(65 + i)
        print((char + " ") * (i + 1))


def pattern_inverted_alphabet_triangle(n: int = 5) -> None:
    """
    21. Inverted Alphabet Triangle
    A B C D E
    A B C D
    A B C
    A B
    A
    """
    print_header("21. Inverted Alphabet Triangle")
    for i in range(n, 0, -1):
        row = " ".join(chr(65 + j) for j in range(i))
        print(row)


def pattern_alphabet_palindrome_pyramid(n: int = 5) -> None:
    """
    22. Alphabet Palindromic Pyramid
        A
       ABA
      ABCBA
     ABCDCBA
    ABCDEDCBA
    """
    print_header("22. Alphabet Palindromic Pyramid")
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        asc = "".join(chr(65 + j) for j in range(i))
        desc = "".join(chr(65 + j) for j in range(i - 2, -1, -1))
        print(spaces + asc + desc)


def pattern_reverse_letter_triangle(n: int = 5) -> None:
    """
    23. Reverse Letter Triangle (Starting from n-th letter)
    E
    D E
    C D E
    B C D E
    A B C D E
    """
    print_header("23. Reverse Letter Triangle")
    for i in range(n):
        start_char = 65 + (n - 1 - i)
        row = " ".join(chr(start_char + j) for j in range(i + 1))
        print(row)


# =============================================================================
# CATEGORY 5: HOLLOW & BOUNDARY PATTERNS
# =============================================================================

def pattern_hollow_square(n: int = 5) -> None:
    """
    24. Hollow Square
    Boundary stars with hollow interior
    * * * * *
    *       *
    *       *
    *       *
    * * * * *
    """
    print_header("24. Hollow Square")
    for i in range(n):
        if i == 0 or i == n - 1:
            print("* " * n)
        else:
            print("* " + "  " * (n - 2) + "*")


def pattern_hollow_pyramid(n: int = 5) -> None:
    """
    25. Hollow Star Pyramid
        *
       * *
      *   *
     *     *
    *********
    """
    print_header("25. Hollow Pyramid")
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        if i == 1:
            print(spaces + "*")
        elif i == n:
            print("*" * (2 * n - 1))
        else:
            inner_spaces = " " * (2 * i - 3)
            print(spaces + "*" + inner_spaces + "*")


def pattern_hollow_diamond(n: int = 5) -> None:
    """
    26. Hollow Diamond Pattern
        *
       * *
      *   *
     *     *
      *   *
       * *
        *
    """
    print_header("26. Hollow Diamond")
    # Top half
    for i in range(1, n + 1):
        outer = " " * (n - i)
        if i == 1:
            print(outer + "*")
        else:
            inner = " " * (2 * i - 3)
            print(outer + "*" + inner + "*")
    # Bottom half
    for i in range(n - 1, 0, -1):
        outer = " " * (n - i)
        if i == 1:
            print(outer + "*")
        else:
            inner = " " * (2 * i - 3)
            print(outer + "*" + inner + "*")


# =============================================================================
# CATEGORY 6: ADVANCED MATHEMATICAL & MATRIX PATTERNS
# =============================================================================

def pattern_pascals_triangle(n: int = 5) -> None:
    """
    27. Pascal's Triangle
    Each number is the sum of the two directly above it: C(n, k)
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
    """
    print_header("27. Pascal's Triangle")
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    # Print centered
    for i, row in enumerate(triangle):
        leading_spaces = " " * (n - 1 - i)
        content = " ".join(str(x) for x in row)
        print(leading_spaces + content)


def pattern_concentric_number_matrix(n: int = 4) -> None:
    """
    28. Concentric Square Number Matrix (Classic FAANG Interview Pattern)
    Size: (2*n - 1) x (2*n - 1)
    Value at (i, j) = n - min(dist to 4 edges)
    4 4 4 4 4 4 4
    4 3 3 3 3 3 4
    4 3 2 2 2 3 4
    4 3 2 1 2 3 4
    4 3 2 2 2 3 4
    4 3 3 3 3 3 4
    4 4 4 4 4 4 4
    """
    print_header("28. Concentric Square Number Matrix (Interview Favorite)")
    size = 2 * n - 1
    for i in range(size):
        row = []
        for j in range(size):
            # Distance to the 4 edges
            top = i
            left = j
            bottom = size - 1 - i
            right = size - 1 - j
            min_dist = min(top, left, bottom, right)
            row.append(str(n - min_dist))
        print(" ".join(row))


# =============================================================================
# MAIN FUNCTION: EXECUTES ALL PATTERNS DEMONSTRATIVELY
# =============================================================================

def main() -> None:
    print("=" * 70)
    print(" DAY 22: PATTERN PRINTING & PROBLEM SOLVING IN PYTHON")
    print(" Author: Harish | Motto: 'Not here to be known, here to build.'")
    print(" Repository: https://github.com/harish-0987/DAY-22-OF-PYTHON")
    print("=" * 70)

    # 1. Basic Star Patterns
    pattern_square_star(5)
    pattern_right_triangle(5)
    pattern_inverted_right_triangle(5)
    pattern_mirrored_right_triangle(5)
    pattern_inverted_mirrored_triangle(5)

    # 2. Pyramids, Diamonds & Symmetrical
    pattern_full_pyramid(5)
    pattern_inverted_pyramid(5)
    pattern_diamond(5)
    pattern_half_diamond(5)
    pattern_hourglass(5)
    pattern_butterfly(5)

    # 3. Numbers & Binary Patterns
    pattern_same_number_triangle(5)
    pattern_increasing_number_triangle(5)
    pattern_inverted_number_triangle(5)
    pattern_floyds_triangle(5)
    pattern_binary_triangle(5)
    pattern_palindromic_number_pyramid(5)
    pattern_number_crown(5)

    # 4. Characters & Alphabets
    pattern_increasing_alphabet_triangle(5)
    pattern_same_alphabet_triangle(5)
    pattern_inverted_alphabet_triangle(5)
    pattern_alphabet_palindrome_pyramid(5)
    pattern_reverse_letter_triangle(5)

    # 5. Hollow & Boundary Patterns
    pattern_hollow_square(5)
    pattern_hollow_pyramid(5)
    pattern_hollow_diamond(5)

    # 6. Advanced Mathematical Patterns
    pattern_pascals_triangle(5)
    pattern_concentric_number_matrix(4)

    print("\n" + "=" * 70)
    print(" DAY 22 COMPLETE: All 28 Pattern Problems Executed Successfully!")
    print(" 'Not here to be known, here to build.'")
    print("=" * 70)


if __name__ == "__main__":
    main()
