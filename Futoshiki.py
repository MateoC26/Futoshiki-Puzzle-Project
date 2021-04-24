import sys

# Checks if all values in a list are different (Except for 0)
def checkDiff(elems):
    for elem in elems:
        #Don't check for 0
        if(elem == "0"):
            continue

        # Returns False if a duplicate is found
        if elems.count(elem) > 1:
            return False

    # Returns true all elements are "0" or there isn't a duplicate
    return True

# AllDiff constraint for row and col
def allDiff(row, col, board):
    row_elems = []
    col_elems = []

    for c in range(0, 6, 1):
        row_elems.append(board[row][c])

    for r in range(0, 6, 1):
        col_elems.append(board[r][col])

    return checkDiff(row_elems) and checkDiff(col_elems)


# initial: Initial Board (2D Array)
# horiz_constraints: Horizontal Constraints (2D Array)
# vert_constraints: Vertical Constraints (2D Array)
# variables: All variables in form xij (List)
# domains: Domains for all variables (Dictionary)
class CSP:
    def __init__(self, initial, horiz_constraints, vert_constraints):
        self.initial = initial
        self.horiz_constraints = horiz_constraints
        self.vert_constraints = vert_constraints
        self.variables = []
        for i in range(0, 6, 1):
            for j in range(0, 6, 1):
                self.variables.append("x" + str(i) + str(j))
        self.domains = {}
        for var in self.variables:
            self.domains[var] = [1, 2, 3, 4, 5, 6]


    # Updates neighbors of variable at row,col
    # Used for forward checking
    def updateNeighborDomains(self, row, col):
        num = self.initial[row][col]

        # Removes value at i,j from its neighbors domains
        # Column neighbors
        for c in range(0, 6, 1):
            var = "x" + str(row) + str(c)
            if int(num) in self.domains[var]:
                self.domains[var].remove(int(num))

        # Row neighbors
        for r in range(0, 6, 1):
            var = "x" + str(r) + str(col)
            if int(num) in self.domains[var]:
                self.domains[var].remove(int(num))

        #STILL NEED TO UPDATE NEIGHBORS BASED ON VERTICAL AND HORIZONTAL CONSTRAINTS


    # Updates domains of neighbors for intial values
    def forwardCheck(self):
        for i in range(0, 6, 1):
            for j in range(0, 6, 1):
                if self.initial[i][j] != "0":
                    self.updateNeighborDomains(i, j)




#---------------------------------Main------------------------------
initial = []
horiz_ineq = []
vert_ineq = []

# Ask to initialize the file until found
#while True:
#    print("\nEnter the name of the input, ensuring that you type .txt afterwards.\n\nOutput will be written in SampleOutput.txt. Please check your directory. ")
#    file_name = input();
#    try:
#       input_file = open(file_name)
#       if input_file:
#           break
#    except IOError:
#        print ("There is no such a file, please try again")

input_file = open("SampleInput.txt")

input_str = input_file.read()

# Splits with each new line
split_input = input_str.split('\n')

# Clean the output file
#file = open("SampleOutput.txt","r+")
#file.truncate(0)
#file.close()

# Open output file for writing
#sys.stdout = open("SampleOutput.txt", "w")

switch = 0
curr_elem = ""

# Splits with each space
# Appends to initial if switch = False
# else appends to goal
for arr in split_input:
    if arr == '':
        switch += 1
        continue

    if switch == 0:
        initial.append(arr.split(" "))
    elif switch == 1:
        horiz_ineq.append(arr.split(" "))
    else:
        vert_ineq.append(arr.split(" "))

# Prints the initial state, horizontal and vertical inequalities
for row in range(0, 6, 1):
    for col in range(0, 6, 1):
        print(initial[row][col], end = " ")
    print()

print()

for row in range(0, 6, 1):
    for col in range(0, 5, 1):
        print(horiz_ineq[row][col], end = " ")
    print()

print()

for row in range(0, 5, 1):
    for col in range(0, 6, 1):
        print(vert_ineq[row][col], end = " ")
    print()

print()

# Solution for CSP initialized
solution = CSP(initial, horiz_ineq, vert_ineq)

# Apply forward checking before starting search
solution.forwardCheck()

input_file.close()
sys.stdout.close()


# TODO
# Finish updateDomains (need to update based on inequalities)
# Create backtracking algorithm
# Implement Select-Unassigned-Value
# Implement Minimum Remaining Value and Degree Heuristics (used in Select-Unassigned-Value)
# Clean up the file
# Create PDF