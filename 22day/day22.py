# # part 1
(lambda np=__import__("numpy"), imp=__import__("sys").setrecursionlimit(1000000) ,inp= open("d").read().split("\n\n"), While=( lambda cond, cmd, state :(lambda f, *a :f(f, *a))( (lambda While, cond, cmd, state: (((cmd(state) and False) or While(While, cond, cmd, state)) if cond(state) else False)),cond,cmd,state ) ):  ( lambda  grid = np.array(list(map(lambda o: np.array(list(o) + [" "] * (150 - len(o))), inp[0].split("\n")))), instructions = inp[1] + "E", dirs = {0: np.array([0, 1]), 1: np.array([1, 0]), 2: np.array([0, -1]), 3: np.array([-1, 0])},  jump=[""],  pos=[np.array([0, 0])], dir=[0], i = [0] : (lambda move = lambda pos, dir, l:  (lambda  last_good=[pos[-1]], p=[]: While( lambda s: s[-1] and grid[*((p.append((pos[-1] + dirs[dir]) % np.array(grid.shape))) or p[-1])] != "#", lambda s: ((s.append(s[-1] - 1)) or last_good.append(p[-1]) if grid[*p[-1]] == "." else False) or (pos.append(p[-1])), [l] ) or (last_good[-1] if grid[*pos[-1]] == " " else pos[-1]) )(): While( lambda s: s[-1] < len(instructions), lambda s:  (j := instructions[s[-1]]) and  (pos.append(move([pos[-1]], dir[-1], int(jump[-1]))) or  dir.append((dir[-1] + (1 if j == "R" else - 1 if j == "L" else 0)) % 4) or  jump.append("")  if j in "LRE" else jump.append(jump[-1] + j)) or s.append(s[-1] + 1), i ) or print(np.sum(pos[-1] * np.array([1000, 4]) + np.array([1000, 4])) + dir[-1]) )())())()
# part 2
(lambda imp=__import__("sys").setrecursionlimit(1000000), data = (open("d").read() + "E").split("\n\n"),get_region = lambda r, c: [(i+1, r-rr*50, c-cc*50) for i,(rr,cc) in enumerate([(0,1),(0,2),(1,1),(2,1),(2,0),(3,0)]) if rr*50<=r<(rr+1)*50 and cc*50<=c<(cc+1)*50][0],new_coords = lambda r, c, d, nd: (lambda a = {0: c, 1: r, 2: 50 - 1 - c, 3:50-1-r}: (lambda b = {0: (50-1,a[d]), 1: (a[d],0), 2: (0,50-1-a[d]), 3:(50-1-a[d],50-1)}: b[nd])())():(lambda inp = list(map(lambda o: list(o) + [" "] * (150 - len(o)), data[0].split("\n"))),get_dest = lambda r, c, d: (lambda reg_rr_rc = get_region(r,c):(lambda new_region_nd = {(4,0):(3,0), (4,1):(2,3), (4,2):(6,3), (4,3):(5,3),(1,0):(6,1), (1,1):(2,1), (1,2):(3,2), (1,3):(5,1),(3,0):(1,0), (3,1):(2,0), (3,2):(4,2), (3,3):(5,2),(6,0):(5,0), (6,1):(4,0), (6,2):(2,2), (6,3):(1,2),(2,0):(6,0), (2,1):(4,3), (2,2):(3,3), (2,3):(1,3),(5,0):(3,1), (5,1):(4,1), (5,2):(6,2), (5,3):(1,1)}[(reg_rr_rc[0],d)]:(lambda nr_nc = new_coords(reg_rr_rc[1],reg_rr_rc[2],d,new_region_nd[1]): (lambda nr_nc=([(0,1),(0,2),(1,1),(2,1),(2,0),(3,0)][new_region_nd[0]-1][0]*50+nr_nc[0],[(0,1),(0,2),(1,1),(2,1),(2,0),(3,0)][new_region_nd[0]-1][1]*50+nr_nc[1]): (*nr_nc,new_region_nd[1]))())())())(),While=( lambda cond, cmd, state :(lambda f, *a :f(f, *a))( (lambda While, cond, cmd, state: (((cmd(state) and False) or While(While, cond, cmd, state)) if cond(state) else False)),cond,cmd,state ) ): (lambda r_c_d_i_n = [0, 50, 1, 0, 0],rr_cc = [0, 0],nr_nc_nd = [0, 0, 0],k = [],tmp = []:While(lambda s: r_c_d_i_n[3] < len(data[1]),lambda s: (k.append(0) or ((r_c_d_i_n.insert(4, r_c_d_i_n.pop(4)* 10 + int(data[1][r_c_d_i_n[3]]))) if data[1][r_c_d_i_n[3]].isdigit() else (any(((((rr_cc.insert(0, (r_c_d_i_n[0]+[(-1,0),(0,1),(1,0),(0,-1)][r_c_d_i_n[2]][0])%200)) or rr_cc.pop(1) and False or(rr_cc.insert(1, (r_c_d_i_n[1]+[(-1,0),(0,1),(1,0),(0,-1)][r_c_d_i_n[2]][1])%150)) or rr_cc.pop(2) and False) or((tmp.append(get_dest(r_c_d_i_n[0],r_c_d_i_n[1],r_c_d_i_n[2])) or(nr_nc_nd.insert(0, tmp[-1][0]) or nr_nc_nd.pop(1) and False) or(nr_nc_nd.insert(1, tmp[-1][1]) or nr_nc_nd.pop(2) and False) or(nr_nc_nd.insert(2, tmp[-1][2]) or nr_nc_nd.pop(3) and False)) or (((r_c_d_i_n.insert(0, nr_nc_nd[0]) or r_c_d_i_n.pop(1) and False) or(r_c_d_i_n.insert(1, nr_nc_nd[1]) or r_c_d_i_n.pop(2) and False) or(r_c_d_i_n.insert(2, nr_nc_nd[2]) or r_c_d_i_n.pop(3) and False)) if inp[nr_nc_nd[0]][nr_nc_nd[1]]!='#' else False) if inp[rr_cc[0]][rr_cc[1]]==' ' else (k.pop() if inp[rr_cc[0]][rr_cc[1]]=='#' else ((r_c_d_i_n.insert(0, rr_cc[0]) or r_c_d_i_n.pop(1) and False) or(r_c_d_i_n.insert(1, rr_cc[1]) or r_c_d_i_n.pop(2) and False))))) if k else False)for _ in range(r_c_d_i_n[4])) or (((turn := data[1][r_c_d_i_n[3]]) and((r_c_d_i_n.insert(2, (r_c_d_i_n.pop(2)+(3 if turn=="L" else 1 if turn=="R" else 0))%4)) or(r_c_d_i_n.insert(4, 0) or r_c_d_i_n.pop(5) and False))) if r_c_d_i_n[3]!=len(data[1]) else False)))) or (r_c_d_i_n.insert(3, r_c_d_i_n.pop(3) + 1)),[]) or print(((r_c_d_i_n[0]+1)*1000 + (r_c_d_i_n[1]+1)*4 + {0:3,1:0,2:1,3:2}[r_c_d_i_n[2]])))())())()
