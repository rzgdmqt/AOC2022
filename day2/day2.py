# part 1 - one way
print((lambda w={"X" : "A", "Y": "B", "Z": "C"}, p=["A","B","C"]: sum(map(lambda r: p.index(r[1]) + 1 + (6 if p[(p.index(r[1]) - 1) % 3] == r[0] else 3 if r[1] == r[0] else 0), map(lambda o: [o[0], w[o[1]]], map(lambda o: o.split(), open("day2/d.txt").read().split("\n"))))))())
#part 1 - or another
print((lambda w={'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}: sum(map(lambda o : w[o], open("day2/d.txt").read().split("\n"))))())
# part 2 - I'm gonna get you
print((lambda p={"X" : 0, "Y": 3, "Z": 6}, r=["A","B","C"]: sum(map(lambda o: p[o[1]] +  r.index(o[0]) + 1, map(lambda o: [r[(r.index(o[0]) + (1 if o[1] == "Z" else 2 if o[1] == "X" else 0)) % 3], o[1]], map(lambda o: o.split(), open("day2/d.txt").read().split("\n"))))))())