import sys
import backend

args = sys.argv
input_file = open(args[1], "r")
output_file = open(args[2], "w") 
numbers = []

print("Check the answer in output.txt")

for line in input_file:
    numbers = line.strip().split(' ')
    expression = backend.solving(numbers)
    output_file.write(str(expression) + "\n")

input_file.close
output_file.close