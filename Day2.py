#------------------------------------------------------------------------------#
name = "Day2.in"
file = open(name, "r")

input = []
for line in file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  input.append(line_list)

file.close()

#--------------------------------------------------------------------------------#

def day2(input):
    D = 0       # depth
    H = 0       # hotizontal
    for l in input:
        if l[0] == "forward":
            H += int(l[1])
        elif l[0] == "down":
            D += int(l[1])
        elif l[0] == "up":
            D -= int(l[1])
        else:
            print("Error")
            break
    return D * H

print("Solution Day 2 Part 1:  {}".format(day2(input)))


def day2_2(input):
    D = 0       # depth
    H = 0       # hotizontal
    A = 0       # aim
    for l in input:
        if l[0] == "forward":
            H += int(l[1])
            D += int(l[1]) * A 
        elif l[0] == "down":
            A += int(l[1])
        elif l[0] == "up":
            A -= int(l[1])
        else:
            print("Error")
            break
    return D * H
print("Solution Day 2 Part 2:  {}".format(day2_2(input)))
