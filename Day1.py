#------------------------------------------------------------------------------#
name = "Day1.in"
file = open(name, "r")

input = []
for line in file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  input.append(int(line_list[0]))

file.close()
#--------------------------------------------------------------------------------#


def day1(input):
    counter = 0
    for i in range(len(input)):
        if (i + 1 == len(input)):
            break
        else:
            if (input[i+1] > input[i]):
                counter += 1
    return counter

print("Solution Day 1 Part 1:  {}".format(day1(input)))


seznam_trojic = []
for i in range(len(input)):
    if (i+2 == len(input)):
        break
    else:
        vsota = input[i] + input[i+1] + input[i+2]
        seznam_trojic.append(vsota)

print("Solution Day 1 Part 2:  {}".format(day1(seznam_trojic)))
