# part 1
(lcm := __import__("math").lcm) and (inp := open("d").read().split("\n")) and (Y := len(inp)) and (X := len(inp[0])) and (Z := lcm(Y - 2, X - 2)) and (L := {(i + j * 1j, {">": 1, "v": 1j, "<": -1, "^": -1j}[v])for j, l in enumerate(inp, -1)for i, v in enumerate(l, -1)if "#" != v != "."}) and (is_inside := lambda pos: (0 < pos.real < X - 1 and 0 < pos.imag < Y - 1) or pos == 1 or pos == X - 2 + (Y - 1) * 1j) and (blizzard_pos := lambda pos, d, n: (pos := pos + n * d) and pos.real % (X - 2) + (pos.imag % (Y - 2)) * 1j) and (While := (lambda cond, cmd, state:(lambda f, *a :f(f, *a))((lambda While, cond, cmd, state: (((cmd(state) and False) or While(While, cond, cmd, state)) if cond(state) else False)), cond, cmd, state))) and (bfs := lambda start, end, steps:(lambda res = [-1],visited = set(),queue = [start],moves = [[0]],k = [0],S = [0]:While(lambda s: s,lambda s: ((moves.append(s[:]) or moves.pop(0) and False or s.clear() or S.append({blizzard_pos(pos, d, steps[0]) + 1 + 1j for pos, d in L}) or S.pop(0) and False) or any(((visited.add((p, steps[0] % Z)) or ((res.append(steps[0]) or res.pop(0) and False or s.clear() or k.pop()) if p == end else ((s.append(p) or  s.extend([p + dx + dy * 1j for dx in (-1, 0, 1)for dy in (-1, 0, 1)if (dx == 0) != (dy == 0) and is_inside(p + dx + dy * 1j)])) if p not in S[0] else False))) if not((p, steps[0] % Z) in visited) else False) if k else False for p in moves[0]) or steps.insert(0, steps.pop() + 1)),queue) or res[0])()) and print(bfs(1, X - 2 + (Y - 1) * 1j, [0]))
# part 2
(lcm := __import__("math").lcm) and (inp := open("d").read().split("\n")) and (Y := len(inp)) and (X := len(inp[0])) and (Z := lcm(Y - 2, X - 2)) and (L := {(i + j * 1j, {">": 1, "v": 1j, "<": -1, "^": -1j}[v])for j, l in enumerate(inp, -1)for i, v in enumerate(l, -1)if "#" != v != "."}) and (is_inside := lambda pos: (0 < pos.real < X - 1 and 0 < pos.imag < Y - 1) or pos == 1 or pos == X - 2 + (Y - 1) * 1j) and (blizzard_pos := lambda pos, d, n: (pos := pos + n * d) and pos.real % (X - 2) + (pos.imag % (Y - 2)) * 1j) and (While := (lambda cond, cmd, state:(lambda f, *a :f(f, *a))((lambda While, cond, cmd, state: (((cmd(state) and False) or While(While, cond, cmd, state)) if cond(state) else False)), cond, cmd, state))) and (bfs := lambda start, end, steps:(lambda res = [-1],visited = set(),queue = [start],moves = [[0]],k = [0],S = [0]:While(lambda s: s,lambda s: ((moves.append(s[:]) or moves.pop(0) and False or s.clear() or S.append({blizzard_pos(pos, d, steps[0]) + 1 + 1j for pos, d in L}) or S.pop(0) and False) or any(((visited.add((p, steps[0] % Z)) or ((res.append(steps[0]) or res.pop(0) and False or s.clear() or k.pop()) if p == end else ((s.append(p) or  s.extend([p + dx + dy * 1j for dx in (-1, 0, 1)for dy in (-1, 0, 1)if (dx == 0) != (dy == 0) and is_inside(p + dx + dy * 1j)])) if p not in S[0] else False))) if not((p, steps[0] % Z) in visited) else False) if k else False for p in moves[0]) or steps.insert(0, steps.pop() + 1)),queue) or res[0])()) and print(bfs(1, X - 2 + (Y - 1) * 1j, [bfs(X - 2 + (Y - 1) * 1j, 1, [bfs(1, X - 2 + (Y - 1) * 1j, [0])])]))
