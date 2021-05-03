import copy
import sys

# initial: Initial Board (2D Array)
# horiz_constraints: Horizontal Constraints (2D Array)
# vert_constraints: Vertical Constraints (2D Array)
# variables: All variables are strings in form "xij" (List)
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
        num = int(self.initial[row][col])

        # Removes value at i,j from its neighbors domains (AllDiff)
        # Column neighbors
        for c in range(0, 6, 1):
            var = "x" + str(row) + str(c)
            if num in self.domains[var]:
                self.domains[var].remove(int(num))

        # Row neighbors
        for r in range(0, 6, 1):
            var = "x" + str(r) + str(col)
            if num in self.domains[var]:
                self.domains[var].remove(int(num))

        # Removes values > or < from right neighbor
        if col < 5:
            neighbor_var = "x" + str(row) + str(col + 1)
            if self.horiz_constraints[row][col] == ">":
                self.domains[neighbor_var] = [x for x in self.domains[neighbor_var] if x < num]
            elif self.horiz_constraints[row][col] == "<":
                self.domains[neighbor_var] = [x for x in self.domains[neighbor_var] if x > num]

        # Removes values ^ or v from bottom neighbor
        if row < 5:
            neighbor_var = "x" + str(row + 1) + str(col)
            if self.vert_constraints[row][col] == "v":
                self.domains[neighbor_var] = [x for x in self.domains[neighbor_var] if x < num]
            elif self.vert_constraints[row][col] == "^":
                self.domains[neighbor_var] = [x for x in self.domains[neighbor_var] if x > num]


    # Updates domains of neighbors for initial values
    def forwardCheck(self):
        for i in range(0, 6, 1):
            for j in range(0, 6, 1):
                if self.initial[i][j] != "0":
                    self.updateNeighborDomains(i, j)


    # MRV used for selecting next variable to work on
    def minimumRemainingValuesHueristic(self, vars):
        min = 7
        min_remaining = []

        # Determine min size of remaining domains
        for var in vars:
            if len(self.domains[var]) < min:
                min = len(self.domains[var])

        # Obtain domains with min size
        for var in vars:
            if len(self.domains[var]) == min:
                min_remaining.append(var)

        #return the smallest domain

        return min_remaining




    # Degree Heuristic used for selecting next variable to work on



    # Determines if the given board is consistent with constraints
    def isConsistent(self, var, assignment):

        diff = False
        horiz_const = False
        vert_const = False

        row = int(var[1])
        col = int(var[2])



        diff = allDiff(row, col, assignment)
        horiz_const = self.checkHorizontalConstraint(var, assignment)[0]
        vert_const = self.checkVerticalConstraint(var, assignment)[0]

        return diff and horiz_const and vert_const

    # Determines if var satisfies horizontal constraints
    def checkHorizontalConstraint(self, var, assignment):
        row = int(var[1])
        col = int(var[2])

        val = int(assignment[row][col])

        valid_right = True
        valid_left = True

        horizontal_constrains = 0

        # Check if there is a inequality to the right
        if col < 5:
            neighbor_val = int(assignment[row][col + 1])
            if neighbor_val == 0:
                valid_right = True
            elif self.horiz_constraints[row][col] == ">" and val < neighbor_val:
                valid_right = False
                horizontal_constrains+=1
            elif self.horiz_constraints[row][col] == "<" and val > neighbor_val:
                valid_right = False
                horizontal_constrains+=1

        # Check if there is a inequality to the left
        if col > 0:
            neighbor_val = int(assignment[row][col - 1])
            if neighbor_val == 0:
                valid_left = True
            elif self.horiz_constraints[row][col - 1] == ">" and val > neighbor_val:
                valid_left = False
                horizontal_constrains+=1
            elif self.horiz_constraints[row][col - 1] == "<" and val < neighbor_val:
                valid_left = False
                horizontal_constrains+=1

        return (valid_left and valid_right, horizontal_constrains)


    # Determines if var satisfies vertical constraints
    def checkVerticalConstraint(self, var, assignment):
        row = int(var[1])
        col = int(var[2])

        val = int(assignment[row][col])

        vertical_contstrains = 0

        valid_top = True
        valid_bottom = True

        # Check if there is a inequality to the bottom
        if row < 5:
            neighbor_val = int(assignment[row + 1][col])
            if neighbor_val == 0:
                valid_bottom = True
            elif self.vert_constraints[row][col] == "v" and val < neighbor_val:
                valid_bottom = False
                vertical_contstrains += 1
            elif self.vert_constraints[row][col] == "^" and val > neighbor_val:
                valid_bottom = False
                vertical_contstrains += 1

        # Check if there is a inequality to the top
        if row > 0:
            neighbor_val = int(assignment[row - 1][col])
            if neighbor_val == 0:
                valid_top = True
            elif self.vert_constraints[row - 1][col] == "v" and val > neighbor_val:
                valid_top = False
                vertical_contstrains += 1
            elif self.vert_constraints[row - 1][col] == "^" and val < neighbor_val:
                valid_top = False
                vertical_contstrains += 1

        return (valid_bottom and valid_top,vertical_contstrains)

def degreeHeuristic(vars,board,csp):

    max_vars = []

    global_max = 0

    for var in vars:
        max = getDegree(var, board,csp)
        if global_max < max:
            global_max = max

    for var in vars:
        if global_max == getDegree(var, board,csp):
            max_vars.append(var)


    return max_vars


def getDegree(var, board,csp):

    degree = 0

    col = int(var[2])
    row = int(var[1])

    for c in range(0, 6, 1):
        if board[row][c] == '0':
            degree += 1

    for c in range(0, 6, 1):
        if board[row][c] == '0':
            degree += 1

    vertical_constrains = csp.checkVerticalConstraint(var,board)[1]
    horizontal_constrains = csp.checkHorizontalConstraint(var,board)[1]

    return degree+vertical_constrains+horizontal_constrains

# Checks if all values in a list are different (Except for 0)

def checkDiff(elems):
    for elem in elems:
        #Don't check for 0
        if(elem == "0"):
            continue

        # Returns False if a duplicate is found
        if elems.count(elem) > 1:
            return False

    # Returns true if all elements are "0" or there isn't a duplicate
    return True


# AllDiff constraint for a row and col
def allDiff(row, col, board):
    row_elems = []
    col_elems = []

    for c in range(0, 6, 1):
        row_elems.append(board[row][c])

    for r in range(0, 6, 1):
        col_elems.append(board[r][col])

    return checkDiff(row_elems) and checkDiff(col_elems)


# Chooses a variable to work on next
# Uses MRV and Degree Heuristics
def selectUnassignedVariable(csp, assignment):
    vars = []

    for i in range(0, 6, 1):
        for j in range(0, 6, 1):
            if assignment[i][j] == "0":
                vars.append("x" + str(i) + str(j))

    vars = csp.minimumRemainingValuesHueristic(vars)

    #In case of a tie between the min domain use degreeHeuristic:

    if len(vars) > 1 :
        vars = degreeHeuristic(vars,assignment,csp)
        #vars = vars[0:3]
    return vars[-1]


# Determines if the board is complete
def isComplete(assignment):
    for i in range(0, 6, 1):
        for j in range(0, 6, 1):
            if assignment[i][j] == "0":
                return False
    return True


#Backtracking Search
def backTrackingSearch(csp):
    initial_copy = copy.deepcopy(csp.initial)
    return backtrack(csp, initial_copy)


#Recursive move of backtracking search
def backtrack(csp, assignment):
    if isComplete(assignment):
        return assignment

    var = selectUnassignedVariable(csp, assignment)
    #print("New var chosen:" + var)
    #print("Domain is " + str(csp.domains[var]))
    row = int(var[1])
    col = int(var[2])


    for value in csp.domains[var]:
        #print("Value chosen is : " + str(value))
        assignment[row][col] = str(value)
        #for r in range(0, 6, 1):
            #for c in range(0, 6, 1):
               # print(assignment[r][c], end=" ")
           # print()

        #print("Am I consistent? " + str(csp.isConsistent(var, assignment)))
        if csp.isConsistent(var, assignment):

            #print()
            result = backtrack(csp, assignment)
            if result != None:
                return result

        #print("Row and col are: " + str(row) + " , " + str(col))
        assignment[row][col] = "0"

        #print()

    return None


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

input_file = open("Input1.txt")

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

# Prints the initial state, horizontal and vertical inequalities NOT NEEDED IN OUTPUT
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
problem = CSP(initial, horiz_ineq, vert_ineq)

# Apply forward checking before starting search
problem.forwardCheck()

#for var in problem.variables:
#   print(var + ":")
#   print(problem.domains[var])

solution = backTrackingSearch(problem)

# Print solution
for row in range(0, 6, 1):
    for col in range(0, 6, 1):
        print(solution[row][col], end = " ")
    print()

input_file.close()
sys.stdout.close()


# TODO
# Implement Degree Heuristic (used in Select-Unassigned-Value)
# Clean up the code for performance and readability
# Add comments
# Create PDF