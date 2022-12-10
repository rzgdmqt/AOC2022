# part1
# print(max(map(lambda l: sum(map(int, l)), (map(lambda o: o.split("\n"), open("d").read().split("\n\n"))))))
# part2
# print(sum(sorted(map(lambda l: sum(map(int, l)), (map(lambda o: o.split("\n"), open("d").read().split("\n\n")))))[-3:]))
# part1 + part2
print((lambda x = sorted(map(lambda l: sum(map(int, l)), (map(lambda o: o.split("\n"), open("d").read().split("\n\n")))))[-3:] : (x[-1], sum(x)))())