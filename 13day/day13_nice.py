# part 1
(
    lambda input=open("d").read().split("\n\n"), compare=lambda i, j: (
        lambda f, *a: f(f, *a)
    )(
        (
            lambda aux, l1, l2: (
                (
                    True
                    if l1[0] < l2[0]
                    else (False if l2[0] < l1[0] else aux(aux, l1[1:], l2[1:]))
                )
                if isinstance(l1[0], int) and isinstance(l2[0], int)
                else (
                    (
                        aux(aux, l1[1:], l2[1:])
                        if aux(aux, l1[0], l2[0]) == "empty"
                        else aux(aux, l1[0], l2[0])
                    )
                    if isinstance(l1[0], list) and isinstance(l2[0], list)
                    else (
                        (
                            aux(aux, l1[1:], l2[1:])
                            if aux(aux, [l1[0]], l2[0]) == "empty"
                            else aux(aux, [l1[0]], l2[0])
                        )
                        if isinstance(l1[0], int) and isinstance(l2[0], list)
                        else (
                            aux(aux, l1[1:], l2[1:])
                            if aux(aux, l1[0], [l2[0]]) == "empty"
                            else aux(aux, l1[0], [l2[0]])
                        )
                    )
                )
            )
            if l1 and l2
            else (
                True if len(l1) < len(l2) else (False if len(l2) < len(l1) else "empty")
            )
        ),
        i,
        j,
    ),: print(
        sum(
            [
                k + 1
                for k, inp in enumerate(input)
                if compare(
                    eval(inp.strip().split("\n")[0]), eval(inp.strip().split("\n")[1])
                )
            ]
        )
    )
)()
# part 2
(
    lambda input=list(
        map(eval, open("d").read().replace("\n\n", "\n").split("\n"))
    ), compare=lambda i, j: (lambda f, *a: f(f, *a))(
        (
            lambda aux, l1, l2: (
                (
                    True
                    if l1[0] < l2[0]
                    else (False if l2[0] < l1[0] else aux(aux, l1[1:], l2[1:]))
                )
                if isinstance(l1[0], int) and isinstance(l2[0], int)
                else (
                    (
                        aux(aux, l1[1:], l2[1:])
                        if aux(aux, l1[0], l2[0]) == "empty"
                        else aux(aux, l1[0], l2[0])
                    )
                    if isinstance(l1[0], list) and isinstance(l2[0], list)
                    else (
                        (
                            aux(aux, l1[1:], l2[1:])
                            if aux(aux, [l1[0]], l2[0]) == "empty"
                            else aux(aux, [l1[0]], l2[0])
                        )
                        if isinstance(l1[0], int) and isinstance(l2[0], list)
                        else (
                            aux(aux, l1[1:], l2[1:])
                            if aux(aux, l1[0], [l2[0]]) == "empty"
                            else aux(aux, l1[0], [l2[0]])
                        )
                    )
                )
            )
            if l1 and l2
            else (
                True if len(l1) < len(l2) else (False if len(l2) < len(l1) else "empty")
            )
        ),
        i,
        j,
    ),: (
        input.extend([[[2]], [[6]]])
    )
    or (
        lambda l=[], m=[input[0]]: any(
            m.insert(0, input[0])
            or (m.pop() and False)
            or any(
                m.insert(0, i) or (m.pop() and False) for i in input if compare(i, m[0])
            )
            or (l.append(m[0]) or input.remove(m[0]))
            for _ in range(len(input))
        )
        or print((l.index([[2]]) + 1) * (l.index([[6]]) + 1))
    )()
)()
