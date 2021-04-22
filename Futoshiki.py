import sys

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
file = open("SampleOutput.txt","r+")
file.truncate(0)
file.close()

# Open output file for writing
sys.stdout = open("SampleOutput.txt", "w")

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

input_file.close()
sys.stdout.close()
