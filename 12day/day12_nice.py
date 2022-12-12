# part 1
(lambda imp,
  input=list(map(list, open("d").read().split("\n"))),
  posI=[0, 0],
  posG=[0, 0],
  bfs=lambda start, neighbors:(
        lambda
        range={tuple(start): 0},
        tmp=[start], 
        visited={tuple(start)},
        queue=[start],
        While=(
            lambda cond, cmd, state
            :(lambda f, *a :f(f, *a))(
            (lambda While, cond, cmd, state: (((cmd(state) and False) or While(While, cond, cmd, state)) if cond(state) else False)), 
              cond, 
              cmd, 
              state
            )
            )
        : While(
            (lambda s: len(s) > 0), 
            lambda s: tmp.insert(0, s.pop(0)) or (tmp.pop() and False) or 
            any(
              s.append(i) or visited.add(tuple(i)) or range.update({tuple(i): range[tuple(tmp[0])] + 1})
              for i in neighbors[tuple(tmp[0])] if tuple(i) not in visited
            ),
            queue
            ) or range
      )():
  any(
    any(
        posI.insert(0, i) or 
        posI.pop(1) or 
        posI.insert(1, j) or 
        posI.pop(2) or 
        input[i].insert(j, "a") or 
        input[i].pop(j + 1) and False
        if input[i][j] == "S" 
        else 
        posG.insert(0, i) or 
        posG.pop(1) or 
        posG.insert(1, j) or 
        posG.pop(2) or
        input[i].insert(j, "z") or 
        input[i].pop(j + 1) and False
        if input[i][j] == "E" 
        else False
        for j in range(len(input[0]))
    ) for i in range(len(input))
  ) or
  (lambda 
    neighbors={},
    get_neighbors=lambda i, j: [(i + x, j + y) for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)] if 0 <= i + x < len(input) and 0 <= j + y < len(input[0]) and ord(input[i][j]) >= ord(input[i + x][j + y]) - 1]
    :
    any(
      any(
        neighbors.update({(i, j): get_neighbors(i, j)})
          for j in range(len(input[0]))
      ) for i in range(len(input))
    ) or
    print(bfs(posI, neighbors)[tuple(posG)])    
  )()
)(__import__("sys").setrecursionlimit(1000000))
# part 2
(lambda imp,
  input=list(map(list, open("d").read().split("\n"))),
  posI=[0, 0],
  posG=[0, 0],
  bfs=lambda start, neighbors:(
        lambda
        range={tuple(start): 0},
        tmp=[start], 
        visited={tuple(start)},
        queue=[start],
        While=(
            lambda cond, cmd, state
            :(lambda f, *a :f(f, *a))(
            (lambda While, cond, cmd, state: (((cmd(state) and False) or While(While, cond, cmd, state)) if cond(state) else False)), 
              cond, 
              cmd, 
              state
            )
            )
        : While(
            (lambda s: len(s) > 0), 
            lambda s: tmp.insert(0, s.pop(0)) or (tmp.pop() and False) or 
            any(
              s.append(i) or visited.add(tuple(i)) or range.update({tuple(i): range[tuple(tmp[0])] + 1})
              for i in neighbors[tuple(tmp[0])] if tuple(i) not in visited
            ),
            queue
            ) or range
      )():
  any(
    any(
        posI.insert(0, i) or 
        posI.pop(1) or 
        posI.insert(1, j) or 
        posI.pop(2) or 
        input[i].insert(j, "a") or 
        input[i].pop(j + 1) and False
        if input[i][j] == "S" 
        else 
        posG.insert(0, i) or 
        posG.pop(1) or 
        posG.insert(1, j) or 
        posG.pop(2) or
        input[i].insert(j, "z") or 
        input[i].pop(j + 1) and False
        if input[i][j] == "E" 
        else False
        for j in range(len(input[0]))
    ) for i in range(len(input))
  ) or
  (lambda 
    m = [len(input) * len(input[0])],
    neighbors={},
    get_neighbors=lambda i, j: [(i + x, j + y) for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)] if 0 <= i + x < len(input) and 0 <= j + y < len(input[0]) and ord(input[i][j]) >= ord(input[i + x][j + y]) - 1]
    :
    any(
      any(
        neighbors.update({(i, j): get_neighbors(i, j)})
          for j in range(len(input[0]))
      ) for i in range(len(input))
    ) or
    any(
      any(
        m.append(min(m[-1], bfs((i, j), neighbors.copy()).get(tuple(posG), m[0])))
        for j in range(len(input[0])) if input[i][j] == "a"
      )for i in range(len(input))
    )  or print(m[-1])
  )()
)(__import__("sys").setrecursionlimit(1000000))
