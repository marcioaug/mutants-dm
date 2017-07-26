i = "89 0100111111001100000001111011111101"

file = open("inputs.txt", "r")

inputs = []

for line in file.readlines():
    if line is not '\n':
        inputs.append(([int(x) for x in line.split(' ')[1] if x is not '\n']))

file = open("transform.py", "w")

file.writelines('data_set = [\n')

for line in inputs:
    file.writelines('    ' + str(line) + ',\n')

file.writelines(']\n')
