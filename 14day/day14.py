# part 1
(lambda imp, input=list( map(lambda o: list(map(lambda p: list(map(int, p.split(","))), o.split(" -> "))),  open("d").read().strip().split("\n") )),diff=(lambda p1, p2: [p2[0] - p1[0], p2[1] - p1[1]]),set_false=lambda i, j, c: c[i].insert(j, False) or (c[i].pop(j + 1) and False): (lambda  column_min=min(min(input, key=min))[0], column_max=max(max(input, key=max))[0], rows_max=max(map(lambda x: x[1],(map(lambda x: max(x, key=lambda x: x[1]), input[:])))), sandunits=[]: (lambda  cave=[[True for _ in range(column_max - column_min + 1)] for _ in range(rows_max + 1)]: any( any( any( set_false(vr[index][1], j, cave) for j in range(min(vr[index][0], vr[index + 1][0])-column_min, max(vr[index][0], vr[index + 1][0])-column_min + 1) ) if diff(vr[index], vr[index + 1])[1] == 0 else any( set_false(i, vr[index][0]-column_min, cave) for i in range(min(vr[index][1], vr[index + 1][1]), max(vr[index][1], vr[index + 1][1]) + 1) ) for index in range(len(vr) - 1) ) for vr in input ) or (lambda progress=( lambda i, j:  (lambda f, *a : f(f, *a))( (lambda aux, i, j :  ("inf" if (i >= rows_max or j > column_max - column_min or j < 0) else (aux(aux, i + 1, j) if cave[i + 1][j] else (aux(aux, i + 1, j - 1) if cave[i + 1][j - 1] else (aux(aux, i + 1, j + 1)) if cave[i + 1][j + 1] else set_false(i, j, cave)))) ), i, j )), While = ( lambda cond, cmd, state :( lambda f, *a :f(f, *a) )( (lambda While, cond, cmd, state: (((cmd(state) and False) or While(While, cond, cmd, state)) if cond(state) else False)),  cond,  cmd,  state ) ):  While( lambda s: progress(0, 500 - column_min) != "inf", lambda s: sandunits.append(1), cave ))() or  print(len(sandunits)) )() )())(__import__("sys").setrecursionlimit(1000000))
# part 2
(lambda imp, input=list( map(lambda o: list(map(lambda p: list(map(int, p.split(","))), o.split(" -> "))),  open("d").read().strip().split("\n") )),diff=(lambda p1, p2: [p2[0] - p1[0], p2[1] - p1[1]]),set_false=lambda i, j, c: c[i].insert(j, False) or (c[i].pop(j + 1) and False): (lambda column_min=min(min(input, key=min))[0], column_max=max(max(input, key=max))[0], rows_max=max(map(lambda x: x[1],(map(lambda x: max(x, key=lambda x: x[1]), input[:])))) + 2, sandunits=[]: ( lambda _=input.append([[column_min - rows_max, rows_max], [column_max + rows_max, rows_max]]), column_min=min(min(input, key=min))[0], column_max=max(max(input, key=max))[0],:(lambda  cave=[[True for _ in range(column_max - column_min + 1)] for _ in range(rows_max + 1)]: any( any( any( set_false(vr[index][1], j, cave) for j in range(min(vr[index][0], vr[index + 1][0])-column_min, max(vr[index][0], vr[index + 1][0])-column_min + 1) ) if diff(vr[index], vr[index + 1])[1] == 0 else any( set_false(i, vr[index][0]-column_min, cave) for i in range(min(vr[index][1], vr[index + 1][1]), max(vr[index][1], vr[index + 1][1]) + 1) ) for index in range(len(vr) - 1) ) for vr in input ) or (lambda progress=( lambda i, j:  (lambda f, *a : f(f, *a))( (lambda aux, i, j :  ("inf" if (i >= rows_max or j > column_max - column_min or j < 0) else (aux(aux, i + 1, j) if cave[i + 1][j] else (aux(aux, i + 1, j - 1) if cave[i + 1][j - 1] else (aux(aux, i + 1, j + 1)) if cave[i + 1][j + 1] else ("inf" if i == 0 else set_false(i, j, cave))))) ), i, j )), While = ( lambda cond, cmd, state :( lambda f, *a :f(f, *a) )( (lambda While, cond, cmd, state: (((cmd(state) and False) or While(While, cond, cmd, state)) if cond(state) else False)),  cond,  cmd,  state ) ):  While( lambda s: progress(0, 500 - column_min) != "inf", lambda s: sandunits.append(1), cave ))() or  print(len(sandunits) + 1) )() )() )())(__import__("sys").setrecursionlimit(1000000))