(
    lambda 
        imp,
        While=(lambda cond, cmd, state: (lambda f, *a: f(f, *a))((lambda While, cond, cmd, state: (((cmd(state) and False)or While(While, cond, cmd, state))if cond(state)else False)),cond,cmd,state,)),
        put = lambda l, i, e: l.insert(i, e) or (l.pop(i + 1) and False),
        jetdir = {"<": -1, ">": 1},
        rocks = __import__("itertools").cycle((((0, 0), (1, 0), (2, 0), (3, 0)),((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),((0, 0), (0, 1), (0, 2), (0, 3)),((0, 0), (1, 0), (0, 1), (1, 1)),)),
        jets = __import__("itertools").cycle(open("d").read().strip()):
        (
            lambda 
                translatex=lambda rock, dx: any(put(rock[i], 0, rock[i][0] + dx) for i in range(len(rock))),
                translatey=lambda rock, dy: any(put(rock[i], 1, rock[i][1] + dy) for i in range(len(rock))),
                checkwalls=lambda rock, dx: all((0 <= p[0]+dx <= 6) for p in rock),
                checkblock=lambda rock, G, dx, dy: all(not((x+dx, y+dy) in G) for x, y in rock),
                prune=lambda G, top: any(G.remove(p) for p in [p for p in G if p[1] < top - 100])
                :
                (
                    lambda
                        target=[999999999999],
                        G = [set([(x, 0) for x in range(7)])],
                        top = [0],
                        idx = [-1],
                        tracker = [__import__("collections").defaultdict(list)],
                        initial = [None],
                        divisor = [None],
                        amount = [None],
                        rock = [-1],
                        dir = [-1],
                        tgtidx = [-1],
                        b = [True],
                        modulus=[0],
                        state=[1, 1]: 
                        While(
                            lambda s: s[0],
                            lambda s:(
                                put(s, 1, 3) or 
                                (idx.append(idx[0] + 1) or idx.pop(0) and False) or 
                                (rock.append([[x+2, y+top[0]+4] for x, y in next(rocks)]) or rock.pop(0) and False) or 
                                While(
                                    lambda s: s[1],
                                    lambda s: dir.append(jetdir[next(jets)]) or dir.pop(0) and False or
                                    (translatex(rock[0], dir[0]) if checkwalls(rock[0], dir[0]) and checkblock(rock[0], G[0], dir[0], 0) else False) or
                                    (put(s, 1, 0) if not checkblock(rock[0], G[0], 0, -1) else translatey(rock[0], -1)),
                                    state
                                ) or 
                                G[0].update([(x, y) for x, y in rock[0]]) or
                                (top.append(max([p[1] for p in rock[0]] + [top[0]])) or top.pop(0) and False) or
                                prune(G[0], top[0]) or 
                                (print("part1", top[0]) if idx[0] == 2021 else False) or # part 1
                                ((
                                    modulus.append(top[0] - (initial[0] + ((idx[0] // divisor[0]) - 1) * amount[0])) or modulus.pop(0) and False or
                                    print("part2", initial[0] + ((target[0] // divisor[0]) - 1) * amount[0] + modulus[0]) or  # part 2
                                    put(s, 0, 0)
                                ) if idx[0] == tgtidx[0] else False) or
                                (
                                    ( 
                                        (tracker[0].update({idx[0]: [(top[0], top[0])]}) if idx[0] != 0 else False) or 
                                        any((
                                            tracker[0][i].append((top[0], top[0]-tracker[0][i][-1][0])) or
                                            ((
                                                divisor.append(i) or divisor.pop(0) and False or
                                                initial.append(tracker[0][i][0][0]) or initial.pop(0) and False or
                                                amount.append(tracker[0][i][-1][-1]) or amount.pop(0) and False or
                                                tgtidx.append(idx[0] + (target[0] % divisor[0])) or tgtidx.pop(0) and False or
                                                tracker.append(__import__("collections").defaultdict(list)) or tracker.pop(0) and False or
                                                b.append(False) or b.pop(0) and False
                                            ) if len(tracker[0][i]) > 3 and tracker[0][i][-1][1] == tracker[0][i][-2][1] == tracker[0][i][-3][1] == tracker[0][i][-4][1] 
                                            else (tracker[0].pop(i) and False 
                                                if len(tracker[0][i]) > 3 and tracker[0][i][-1][1] != tracker[0][i][-2][1] 
                                                else False))) if b[0] else False
                                            for i in [i for i in tracker[0] if idx[0] % i == 0]
                                        )
                                    ) if divisor[0] is None else False
                                )

                            ),
                            state
                        )
                )()
        )()
)(__import__("sys").setrecursionlimit(1000000))

