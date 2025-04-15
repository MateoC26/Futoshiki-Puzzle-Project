# Futoshiki Puzzle AI Project
Using Minimum Remaining Value and Degree heursitics and Backtracking search to provide a solution to a Futoshiki puzzle (https://en.wikipedia.org/wiki/Futoshiki) given the Initial state of the board and vertical/horizontal constraits.

Input Format:
n : Initial State - i x i Grid
h : Horizontal Constraints (< or >) - i x i - 1 Grid
x : Vertical Constraints (v or ^) - i - 1 x i Grid

n n n n n n
n n n n n n
n n n n n n
n n n n n n
n n n n n n
n n n n n n

0 0 h 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 h 0
0 h 0 0 h
h 0 0 0 0

x 0 0 0 0 0
0 0 0 0 0 0
0 0 0 x 0 0
0 0 0 0 0 x
x 0 0 0 0 0

Instructions to run:
1. Install python on your console with “Brew” or “pip” on your root directory as such: “Brew install python”
2. Download the entire folder as it is. Then navigate to the directory “15PuzzleAIProject” as such: “cd 15PuzzleAIProject”.
3. Run “python Futoshiki.py”.
4. Please create an empty .txt file in the same directory as the root called “SampleOutput.txt”.
5. You will be prompted to enter an input file name, until a match is found. Press enter once you have written it down in the console. Note: only files in the root of the project directory will be found, otherwise you must include the relative path to this directory. Example “Input1.txt”.
6. The generated output will be written down in“SampleOutput.txt”. Note: this file gets re-written every time the algorithm is run with a new input. If you want to keep a record of the output, make a copy of “SampleOutput.txt” before re-running the code.
7. The input files “Input1.txt”, “Input2.txt”, “Input3.txt”, have been included in the directory for your convenience. 
