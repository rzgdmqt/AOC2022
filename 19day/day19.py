# part 1
(lambda imp = __import__("sys").setrecursionlimit(100000000), find_best = lambda ore_r, clay_r, obs_r, geode_r, end, While=(lambda cond, cmd, state: (lambda f, *a: f(f, *a))((lambda While, cond, cmd, state: (((cmd(state) and False)or While(While, cond, cmd, state))if cond(state)else False)),cond,cmd,state,)): ( ( lambda  max_ore = max(x["o"] for x in [ore_r, clay_r, obs_r, geode_r]), max_clay = max(x["c"] if "c" in x else 0 for x in [ore_r, clay_r, obs_r, geode_r]), max_obsidian = max(x["ob"] if "ob" in x else 0 for x in [ore_r, clay_r, obs_r, geode_r]), queue = [[0, 0, 0, 0, 0, ore_r["a"], clay_r["a"], obs_r["a"], geode_r["a"]]], best = set(), flags = [[0, 0, 0, 0]], q = [0]: (While( lambda s: len(queue), lambda s: ( q.append(max(queue)) or (q.pop(0) and False) or (queue.pop(queue.index(q[0])) and False) or (( best.add(q[0][4]) or flags.append([0, 0, 0, 0]) or (flags.pop(0) and False) or  any((best.add(q[0][4]) or  ( ((queue.append([t + 1, q[0][1] - o + q[0][5], q[0][2] + q[0][6], q[0][3] + q[0][7], q[0][4] + q[0][8], q[0][5] + 1, q[0][6], q[0][7], q[0][8]]) or flags[0].insert(0, 1) or (flags[0].pop(1) and False)) if not flags[0][0] and q[0][1] >= (o := ore_r["o"]) and q[0][5] < max_ore else False) or((queue.append([t + 1, q[0][1] - o + q[0][5], q[0][2] + q[0][6], q[0][3] + q[0][7], q[0][4] + q[0][8], q[0][5], q[0][6] + 1, q[0][7], q[0][8]]) or flags[0].insert(1, 1) or (flags[0].pop(2) and False)) if not flags[0][1] and q[0][1] >= (o := clay_r["o"]) and q[0][6] < max_clay else False) or((queue.append([t + 1, q[0][1] - o + q[0][5], q[0][2] - c + q[0][6], q[0][3] + q[0][7], q[0][4] + q[0][8], q[0][5], q[0][6], q[0][7] + 1, q[0][8]]) or flags[0].insert(2, 1) or (flags[0].pop(3) and False)) if not flags[0][2] and q[0][1] >= (o := obs_r["o"]) and q[0][2] >= (c := obs_r["c"]) and q[0][7] < max_obsidian else False) or((queue.append([t + 1, q[0][1] - o + q[0][5], q[0][2] + q[0][6], q[0][3] - ob + q[0][7], q[0][4] + q[0][8], q[0][5], q[0][6], q[0][7], q[0][8] + 1]) or flags[0].insert(3, 1) or (flags[0].pop(4) and False)) if not flags[0][3] and q[0][1] >= (o := geode_r["o"]) and q[0][3] >= (ob := geode_r["ob"]) else False) ) or q[0].insert(1, q[0][1] + q[0][5]) or (q[0].pop(2) and False) or  q[0].insert(2, q[0][2] + q[0][6]) or (q[0].pop(3) and False) or  q[0].insert(3, q[0][3] + q[0][7]) or (q[0].pop(4) and False) or  q[0].insert(4, q[0][4] + q[0][8]) or (q[0].pop(5) and False)) for t in range(q[0][0], end) ) ) if not(q[0][0] > end - 3 and q[0][4] + (q[0][8] * (end - q[0][0])) + (min([geode_r["ob"] // (q[0][7] or 1), geode_r["o"] // (q[0][5] or 1)]) * ((end - q[0][0]) // 2)) < max(best or [0])) else False) ), queue) or max(best)) )()), input = open("d").read().replace(":", " :").split("\n"): ( lambda  data = {(z := [int(i) for i in vr.split(" ") if i.isdigit()])[0] : [{"a" : 1, "o" : z[1]}, {"a" : 0, "o" : z[2]}, {"a" : 0, "o" : z[3], "c" : z[4]}, {"a" : 0, "o" : z[5], "ob" : z[6]}] for vr in input}, p = [0]: any( p.append(p[0] + blueprint * find_best({**ore_r}, {**clay_r}, {**obs_r}, {**geode_r}, 24)) or (p.pop(0) and False) for blueprint, (ore_r, clay_r, obs_r, geode_r) in data.items() ) or print(p[0]) )())()
# part 2
(lambda imp = __import__("sys").setrecursionlimit(100000000), find_best = lambda ore_r, clay_r, obs_r, geode_r, end, While=(lambda cond, cmd, state: (lambda f, *a: f(f, *a))((lambda While, cond, cmd, state: (((cmd(state) and False)or While(While, cond, cmd, state))if cond(state)else False)),cond,cmd,state,)): ( ( lambda  max_ore = max(x["o"] for x in [ore_r, clay_r, obs_r, geode_r]), max_clay = max(x["c"] if "c" in x else 0 for x in [ore_r, clay_r, obs_r, geode_r]), max_obsidian = max(x["ob"] if "ob" in x else 0 for x in [ore_r, clay_r, obs_r, geode_r]), queue = [[0, 0, 0, 0, 0, ore_r["a"], clay_r["a"], obs_r["a"], geode_r["a"]]], best = set(), flags = [[0, 0, 0, 0]], q = [0]: (While( lambda s: len(queue), lambda s: ( q.append(max(queue)) or (q.pop(0) and False) or (queue.pop(queue.index(q[0])) and False) or (( best.add(q[0][4]) or flags.append([0, 0, 0, 0]) or (flags.pop(0) and False) or  any((best.add(q[0][4]) or  ( ((queue.append([t + 1, q[0][1] - o + q[0][5], q[0][2] + q[0][6], q[0][3] + q[0][7], q[0][4] + q[0][8], q[0][5] + 1, q[0][6], q[0][7], q[0][8]]) or flags[0].insert(0, 1) or (flags[0].pop(1) and False)) if not flags[0][0] and q[0][1] >= (o := ore_r["o"]) and q[0][5] < max_ore else False) or((queue.append([t + 1, q[0][1] - o + q[0][5], q[0][2] + q[0][6], q[0][3] + q[0][7], q[0][4] + q[0][8], q[0][5], q[0][6] + 1, q[0][7], q[0][8]]) or flags[0].insert(1, 1) or (flags[0].pop(2) and False)) if not flags[0][1] and q[0][1] >= (o := clay_r["o"]) and q[0][6] < max_clay else False) or((queue.append([t + 1, q[0][1] - o + q[0][5], q[0][2] - c + q[0][6], q[0][3] + q[0][7], q[0][4] + q[0][8], q[0][5], q[0][6], q[0][7] + 1, q[0][8]]) or flags[0].insert(2, 1) or (flags[0].pop(3) and False)) if not flags[0][2] and q[0][1] >= (o := obs_r["o"]) and q[0][2] >= (c := obs_r["c"]) and q[0][7] < max_obsidian else False) or((queue.append([t + 1, q[0][1] - o + q[0][5], q[0][2] + q[0][6], q[0][3] - ob + q[0][7], q[0][4] + q[0][8], q[0][5], q[0][6], q[0][7], q[0][8] + 1]) or flags[0].insert(3, 1) or (flags[0].pop(4) and False)) if not flags[0][3] and q[0][1] >= (o := geode_r["o"]) and q[0][3] >= (ob := geode_r["ob"]) else False) ) or q[0].insert(1, q[0][1] + q[0][5]) or (q[0].pop(2) and False) or  q[0].insert(2, q[0][2] + q[0][6]) or (q[0].pop(3) and False) or  q[0].insert(3, q[0][3] + q[0][7]) or (q[0].pop(4) and False) or  q[0].insert(4, q[0][4] + q[0][8]) or (q[0].pop(5) and False)) for t in range(q[0][0], end) ) ) if not(q[0][0] > end - 3 and q[0][4] + (q[0][8] * (end - q[0][0])) + (min([geode_r["ob"] // (q[0][7] or 1), geode_r["o"] // (q[0][5] or 1)]) * ((end - q[0][0]) // 2)) < max(best or [0])) else False) ), queue) or max(best)) )()), input = open("d").read().replace(":", " :").split("\n"): ( lambda  data = {(z := [int(i) for i in vr.split(" ") if i.isdigit()])[0] : [{"a" : 1, "o" : z[1]}, {"a" : 0, "o" : z[2]}, {"a" : 0, "o" : z[3], "c" : z[4]}, {"a" : 0, "o" : z[5], "ob" : z[6]}] for vr in input}, p = [1]: any( p.append(p[0] * find_best({**ore_r}, {**clay_r}, {**obs_r}, {**geode_r}, 32)) or (p.pop(0) and False) for blueprint, (ore_r, clay_r, obs_r, geode_r) in data.items() if blueprint < 4 ) or print(p[0]) )())()