# Part 1
(lambda s = open("d").readlines(), u=set():any(any(any(u.add((i, *(list(map(int, l.split(",")))[k] + (i == k) * j for k in range(3))))for j in range(2)) for i in range(3)) for l in s) or print(2 * len(u) - 6 * len(s)))()

# Part 2
(lambda s=open("d").read().split("\n"):(lambda c={(*map(int,l.split(',')),) for l in s},neighbors=lambda x, y, z: {(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}:(lambda C = {z for x in c for y in neighbors(*x) for z in [y,*neighbors(*y)]}-c,:(lambda dfs=lambda visited, stack: (lambda f, *a: f(f, *a))(lambda aux, visited, stack: aux(aux, visited | stack, {y for x in stack for y in neighbors(*x) & C - visited}) + sum(len(neighbors(*x) & c) for x in stack) if stack else 0,visited,stack):print(dfs(set(), {min(C)})))())())() )()