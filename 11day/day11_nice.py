# part1
(lambda 
  input=list(map(lambda o: list(map(lambda p: p.strip(), o)), map(lambda o: o.split("\n"), open("d").read().split("\n\n")))),
  op={"+": lambda x, y: x + y, "*": lambda x, y: x * y}
  : (lambda 
      inspected={f"m{i}":0 for i in range(len(input))},
      monkeys={f"m{i}": [int(j.replace(",", "")) for j in m[1].split(" ")[2:]] for i, m in enumerate(input)},
      monkey_change=
        {
          f"m{i}": 
            (lambda p, q: (lambda x: p(x, int(q) if q.isdigit() else x)))(op[m[2].split(" ")[-2]], m[2].split(" ")[-1])  for i, m in enumerate(input)
        },
      monkey_test = {f"m{i}" : (lambda p: lambda x : x % p == 0)(int(m[3].split(" ")[-1])) for i, m in enumerate(input)},
      monkey_throw = {f"m{i}" : ("m" + m[-2].split(" ")[-1], "m" + m[-1].split(" ")[-1]) for i, m in enumerate(input)},
      : (lambda throw= lambda n, m1, m2: (monkeys[m1].pop(0) and False) or monkeys[m2].append(n)
        :any(
          any(
            any(
              (throw(monkey_change[f"m{i}"](j) // 3, f"m{i}",monkey_throw[f"m{i}"][0])
              if monkey_test[f"m{i}"](monkey_change[f"m{i}"](j) // 3)
              else throw(monkey_change[f"m{i}"](j) // 3, f"m{i}",monkey_throw[f"m{i}"][1])) or
              inspected.update({f"m{i}" : inspected[f"m{i}"] + 1})
              for j in monkeys[f"m{i}"][:]
            )
            for i in range(len(input))
          ) for _ in range(20)
        ) or print(sorted(inspected.values())[-1] * sorted(inspected.values())[-2])
      )()
  )()
)()
# part 2
(lambda 
  input=list(map(lambda o: list(map(lambda p: p.strip(), o)), map(lambda o: o.split("\n"), open("d").read().split("\n\n")))),
  op={"+": lambda x, y: x + y, "*": lambda x, y: x * y},
  n = {"n": 1}
  : (lambda 
      inspected={f"m{i}":0 for i in range(len(input))},
      monkeys={f"m{i}": [int(j.replace(",", "")) for j in m[1].split(" ")[2:]] for i, m in enumerate(input)},
      monkey_change=
        {
          f"m{i}": 
            (lambda p, q: (lambda x: p(x, int(q) if q.isdigit() else x)))(op[m[2].split(" ")[-2]], m[2].split(" ")[-1])  for i, m in enumerate(input)
        },
      monkey_test = {f"m{i}" : (lambda p: lambda x : x % p == 0)(n.update({"n": n["n"] * int(m[3].split(" ")[-1])}) or int(m[3].split(" ")[-1])) for i, m in enumerate(input)},
      monkey_throw = {f"m{i}" : ("m" + m[-2].split(" ")[-1], "m" + m[-1].split(" ")[-1]) for i, m in enumerate(input)},
      : (lambda throw= lambda n, m1, m2: (monkeys[m1].pop(0) and False) or monkeys[m2].append(n)
        :any(
          any(
            any(
              (throw(monkey_change[f"m{i}"](j) % n["n"], f"m{i}",monkey_throw[f"m{i}"][0])
              if monkey_test[f"m{i}"](monkey_change[f"m{i}"](j) % n["n"])
              else throw(monkey_change[f"m{i}"](j) % n["n"], f"m{i}",monkey_throw[f"m{i}"][1])) or
              inspected.update({f"m{i}" : inspected[f"m{i}"] + 1})
              for j in monkeys[f"m{i}"][:]
            )
            for i in range(len(input))
          ) for _ in range(10000)
        ) or print(sorted(inspected.values())[-1] * sorted(inspected.values())[-2])
      )()
  )()
)()
