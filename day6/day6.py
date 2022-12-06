# part 1
print((lambda input: [i for i in range(4, len(input)) if len(set(input[i-4:i]))==4])(open("d").read())[0])
# part 2
print((lambda input: [i for i in range(14, len(input)) if len(set(input[i-14:i]))==14])(open("d").read())[0])