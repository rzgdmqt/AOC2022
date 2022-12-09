# part 1
(lambda 
  # we define constants
  input=open("d").read().split("\n"), 
  moves={"R": [0, 1], "L":[0, -1], "U":[-1, 0], "D":[1, 0]},
  now_t = [0, 0],
  now_h = [0, 0],
  # we define fome functions
  put=lambda l, i, n: l.insert(i, n) or (l.pop(i + 1) and False),
  sgn = lambda x: -1 if x < 0 else 1
  : (
    lambda 
    # some more constants and functions
    been,
    rows=list(map(lambda o: (o.split(" ")[0], int(o.split(" ")[1])), input)),
    sum_pair_no_return=lambda l1, l2: put(l1, 0, l1[0] + l2[0]) or put(l1, 1, l1[1] + l2[1]),
    diff_pair = lambda l1, l2: [l1[0] - l2[0], l1[1] - l2[1]],
    normalize_pair = lambda p: [sgn(p[0]) * p[0] // p[0] if p[0] != 0 else 0, sgn(p[1]) * p[1] // p[1] if p[1] != 0 else 0],
    : (
      any(
        (any(
          sum_pair_no_return(now_h, moves[m]) or 
          (sum_pair_no_return(now_t, normalize_pair(diff_pair(now_h, now_t))) if abs(max(diff_pair(now_h, now_t), key=abs)) > 1 else False) or
          been.add(tuple(now_t))
            for _ in range(l)
        )) for m, l in rows
      ) or print(len(been))
    )
  )({(0, 0)})
)()

# part 2
(lambda 
  input, 
  put=lambda l, i, n: l.insert(i, n) or (l.pop(i + 1) and False),
  moves={"R": [0, 1], "L":[0, -1], "U":[-1, 0], "D":[1, 0]},
  now_rope = [[0, 0] for _ in range(10)],
  sgn = lambda x: -1 if x < 0 else 1
  : (
    lambda 
    been,
    sum_pair_no_return=lambda l1, l2: put(l1, 0, l1[0] + l2[0]) or put(l1, 1, l1[1] + l2[1]),
    diff_pair = lambda l1, l2: [l1[0] - l2[0], l1[1] - l2[1]],
    normalize_pair = lambda p: [sgn(p[0]) * p[0] // p[0] if p[0] != 0 else 0, sgn(p[1]) * p[1] // p[1] if p[1] != 0 else 0],
    rows=list(map(lambda o: (o.split(" ")[0], int(o.split(" ")[1])), input)),
    : (
      any(
        (any(
          sum_pair_no_return(now_rope[0], moves[m]) or
          any( 
              sum_pair_no_return(now_rope[i], normalize_pair(diff_pair(now_rope[i-1], now_rope[i]))) 
              or been.add(tuple(now_rope[-1]))
                for i in range(1,10) if abs(max(diff_pair(now_rope[i-1], now_rope[i]), key=abs)) > 1
          )
            for _ in range(l)
        )) for m, l in rows
      ) or print(len(been))
    )
  )({(0, 0)})
  )(open("d").read().split("\n"))
