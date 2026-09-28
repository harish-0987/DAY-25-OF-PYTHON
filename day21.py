# =============================================================================
# DAY 21: FILE HANDLING IN PYTHON (BASIC LEVEL)
# Author: Harish
# Repository: DAY-21-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

# =============================================================================
# INTRODUCTION TO FILE HANDLING:
# =============================================================================
# In computer programming, data stored in variables is temporary and gets lost
# as soon as the program terminates (stored in RAM/Volatile Memory).
#
# File handling allows Python to store data permanently on disk (Non-Volatile
# Storage). It is a fundamental building block for data persistence, logging,
# configuration management, and data processing.
#
# THE FILE LIFECYCLE:
# 1. OPEN   : Open the file stream using open() and specify the mode.
# 2. OPERATE: Read from, write to, or append data to the file.
# 3. CLOSE  : Always close the file to free up system resources.
#
# COMMON FILE MODES:
# - 'r' : Read mode (Default). Opens file for reading; raises FileNotFoundError if absent.
# - 'w' : Write mode. Creates a new file or overwrites/truncates existing content.
# - 'a' : Append mode. Appends new data to the end of the file without erasing past data.
# - 'x' : Exclusive creation mode. Creates file, fails with FileExistsError if already exists.
# - 't' : Text mode (Default). Handles strings and automatically decodes characters.
# - 'b' : Binary mode. Handles raw bytes (images, audio, PDFs, etc.).
# - '+' : Read and Write mode (e.g., 'r+', 'w+', 'a+').
#
# BEST PRACTICE:
# Always prefer using the 'with' statement (Context Manager).
# It guarantees that files are automatically and cleanly closed, even if an
# unexpected error or exception occurs during file processing.
# =============================================================================

import os


def print_section(title: str) -> None:
    """Utility function to print cleanly formatted section headers."""
    print("\n" + "=" * 75)
    print(f"  {title}")
    print("=" * 75)


def main() -> None:
    print("=" * 75)
    print(" DAY 21: FILE HANDLING IN PYTHON (BASIC LEVEL)")
    print(" Author: Harish | Motto: 'Not here to be known, here to build.'")
    print("=" * 75)

    # File names used for the demonstrations
    sample_filename = "day21_sample.txt"
    log_filename = "day21_activity.log"

    # -------------------------------------------------------------------------
    # PART 1: WRITING TO A FILE ('w' MODE)
    # -------------------------------------------------------------------------
    print_section("PART 1: WRITING TO A FILE ('w' MODE)")
    print("Mode 'w' creates the file if it does not exist, or overwrites it if it does.\n")

    # Method 1: Using write() with explicit open() and close()
    file = open(sample_filename, "w", encoding="utf-8")
    file.write("Welcome to Python File Handling!\n")
    file.write("Line 1: Files allow permanent data storage.\n")
    file.close()
    print(f"[+] Successfully wrote initial lines to '{sample_filename}' using open() and close().")

    # Method 2: Using writelines() to write a list of strings
    additional_lines = [
        "Line 2: Python makes file operations intuitive and simple.\n",
        "Line 3: Always remember to handle resources responsibly.\n",
        "Line 4: 'w' mode overwrites, while 'a' mode preserves existing content.\n"
    ]
    file = open(sample_filename, "a", encoding="utf-8")
    file.writelines(additional_lines)
    file.close()
    print(f"[+] Appended multiple lines using writelines().")

    # -------------------------------------------------------------------------
    # PART 2: READING FROM A FILE ('r' MODE)
    # -------------------------------------------------------------------------
    print_section("PART 2: READING FROM A FILE ('r' MODE)")
    print("Python provides several ways to read file content based on your needs:\n")

    # Approach A: read() - Reads the whole content (or up to N characters)
    print("--- 1. Using file.read() [Whole file as a single string] ---")
    file = open(sample_filename, "r", encoding="utf-8")
    full_content = file.read()
    file.close()
    print(full_content)

    # Approach B: read(N) - Reads only the first N characters
    print("--- 2. Using file.read(25) [First 25 characters] ---")
    file = open(sample_filename, "r", encoding="utf-8")
    partial_content = file.read(25)
    file.close()
    print(f"'{partial_content}'...\n")

    # Approach C: readline() - Reads one line at a time
    print("--- 3. Using file.readline() [Line by Line] ---")
    file = open(sample_filename, "r", encoding="utf-8")
    first_line = file.readline().strip()
    second_line = file.readline().strip()
    file.close()
    print(f"First Line : {first_line}")
    print(f"Second Line: {second_line}\n")

    # Approach D: readlines() - Reads all lines into a Python List
    print("--- 4. Using file.readlines() [List of Strings] ---")
    file = open(sample_filename, "r", encoding="utf-8")
    lines_list = file.readlines()
    file.close()
    print(f"Number of lines: {len(lines_list)}")
    print(f"List output    : {[line.strip() for line in lines_list]}\n")

    # Approach E: Iterating over file object directly (Most memory-efficient for large files)
    print("--- 5. Iterating directly over the file object (Memory-Efficient) ---")
    file = open(sample_filename, "r", encoding="utf-8")
    for index, line in enumerate(file, start=1):
        print(f"  [{index}] {line.strip()}")
    file.close()

    # -------------------------------------------------------------------------
    # PART 3: APPENDING TO A FILE ('a' MODE)
    # -------------------------------------------------------------------------
    print_section("PART 3: APPENDING TO A FILE ('a' MODE)")
    print("Mode 'a' adds new content at the end of the file without deleting existing data.\n")

    file = open(log_filename, "w", encoding="utf-8")
    file.write("[INIT] Activity log started.\n")
    file.close()

    # Appending entries to the log file
    file = open(log_filename, "a", encoding="utf-8")
    file.write("[INFO] User 'Harish' logged into the system.\n")
    file.write("[INFO] Data processing completed successfully.\n")
    file.write("[INFO] Session saved to disk.\n")
    file.close()

    print(f"[+] Content appended to '{log_filename}'. Let's inspect it:")
    file = open(log_filename, "r", encoding="utf-8")
    print(file.read())
    file.close()

    # -------------------------------------------------------------------------
    # PART 4: THE 'with' STATEMENT (CONTEXT MANAGER - MODERN BEST PRACTICE)
    # -------------------------------------------------------------------------
    print_section("PART 4: THE 'with' STATEMENT (CONTEXT MANAGER)")
    print("Why use 'with open(...) as f:'?")
    print("- Automatically closes the file when the block exits.")
    print("- Even if an error or exception occurs inside, the file is guaranteed to close.")
    print("- Prevents memory leaks and file descriptor exhaustion.\n")

    with open(sample_filename, "a", encoding="utf-8") as f:
        f.write("Line 5: Written securely using Python's 'with' statement!\n")

    print("[+] Appended using 'with' block.")
    print(f"Is file closed outside the with block? -> {f.closed}")

    print("\nReading back with 'with' block:")
    with open(sample_filename, "r", encoding="utf-8") as f:
        for line in f:
            print(f"  > {line.strip()}")

    # -------------------------------------------------------------------------
    # PART 5: FILE POINTER POSITION (tell() AND seek())
    # -------------------------------------------------------------------------
    print_section("PART 5: FILE POINTER POSITION (tell() & seek())")
    print("- tell(): Returns the current position (byte offset) of the file pointer.")
    print("- seek(offset): Moves the file pointer to a specific location.\n")

    with open(sample_filename, "r", encoding="utf-8") as f:
        print(f"Initial pointer position : {f.tell()} (Start of file)")
        first_chunk = f.read(15)
        print(f"Read 15 characters       : '{first_chunk}'")
        print(f"Pointer position now     : {f.tell()}")

        # Reset pointer back to the beginning (0)
        f.seek(0)
        print(f"Pointer after seek(0)    : {f.tell()} (Reset to start)")
        re_read = f.read(15)
        print(f"Read 15 characters again : '{re_read}'")

    # -------------------------------------------------------------------------
    # PART 6: SAFE FILE HANDLING WITH try...except
    # -------------------------------------------------------------------------
    print_section("PART 6: SAFE FILE OPERATIONS WITH try...except")
    print("Protecting against FileNotFoundError and IOError when opening files:\n")

    non_existent_file = "non_existent_data.txt"

    try:
        print(f"Attempting to read '{non_existent_file}'...")
        with open(non_existent_file, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"[Caught Error] File '{non_existent_file}' does not exist! Gracefully handled.")
    except IOError as e:
        print(f"[Caught Error] I/O operation error: {e}")
    else:
        print("[Success] File read successfully without any errors.")
    finally:
        print("[Cleanup] Finished safe file access attempt.")

    # -------------------------------------------------------------------------
    # PART 7: PRACTICAL MINI-PROJECT - FILE CONTENT ANALYZER
    # -------------------------------------------------------------------------
    print_section("PART 7: PRACTICAL MINI-PROJECT: FILE CONTENT ANALYZER")
    print("A simple utility function to analyze file statistics:\n")

    def analyze_file(filepath: str) -> None:
        """Counts lines, words, and characters in a given file."""
        if not os.path.exists(filepath):
            print(f"Error: File '{filepath}' does not exist.")
            return

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        lines = content.splitlines()
        words = content.split()
        char_count = len(content)

        print(f"File Analysis for: '{filepath}'")
        print(f"  - Total Lines     : {len(lines)}")
        print(f"  - Total Words     : {len(words)}")
        print(f"  - Total Characters: {char_count}")

    analyze_file(sample_filename)

    # -------------------------------------------------------------------------
    # PART 8: CLEANUP OF DEMO FILES
    # -------------------------------------------------------------------------
    print_section("PART 8: ENVIRONMENT CLEANUP")
    # Clean up the sample files so the workspace remains clean
    for temp_file in [sample_filename, log_filename]:
        if os.path.exists(temp_file):
            os.remove(temp_file)
            print(f"[Cleanup] Removed temporary demo file: '{temp_file}'")

    print("\n" + "=" * 75)
    print(" DAY 21 COMPLETE: You have mastered the fundamentals of File Handling!")
    print(" Keep practicing and keep building!")
    print("=" * 75)


if __name__ == "__main__":
    main()
