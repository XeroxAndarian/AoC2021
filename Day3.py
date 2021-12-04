#------------------------------------------------------------------------------#
name = "Day3.in"
file = open(name, "r")

input = []
for line in file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  input.append(line_list[0])

file.close()
# print(input)
#--------------------------------------------------------------------------------#

def day3(input):
    Gamma = ""
    Epsilon = ""
    for i in range(len(input[0])):
        zeros = 0
        ones = 0
        a = 0
        for j in range(len(input)):
            if int(input[j][i]) == 0:
                zeros += 1
            else:
                ones += 1
        if zeros < ones:
            a = 1

        Gamma += str(a)
        Epsilon += str(abs(1-a))

    Gamma_decimal = binary(Gamma)
    Epsilon_decimal = binary(Epsilon)
    
    return Gamma_decimal * Epsilon_decimal


def binary(string):
    n = 0
    for m in range(len(string)):
        n += int(string[-(m + 1)]) * 2**m
    return n

print("Solution Day 3 Part 1:  {}".format(day3(input)))


def day3_2(input):
    O2 = ""
    for i in range(len(input[0])):
        zeros = 0
        ones = 0
        a = 0
        for j in range(len(input)):
            if input[j][0:i] != O2:
                continue
            if int(input[j][i]) == 0:
                zeros += 1
            else:
                ones += 1
        if zeros + ones  == 1:
            if zeros < ones:
                a = 1
            else:
                a = 0
        elif zeros <= ones:
            a = 1
        O2 += str(a)

    CO2 = ""
    for i in range(len(input[0])):
        zeros = 0
        ones = 0
        a = 0
        for j in range(len(input)):
            if input[j][0:i] != CO2:
                continue
            if int(input[j][i]) == 0:
                zeros += 1
            else:
                ones += 1
        if zeros + ones  == 1:
            if zeros < ones:
                a = 0
            else:
                a = 1
        elif zeros <= ones:
            a = 1
        CO2 += str(abs(1-a))

    return binary(CO2) * binary(O2)

print("Solution Day 3 Part 2:  {}".format(day3_2(input)))