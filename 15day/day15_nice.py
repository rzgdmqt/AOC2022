# part 1
(
    lambda S=[], B=[]: (
        lambda _=list(
            map(
                lambda o: S.append(
                    list(map(lambda p: int(p[2 : len(p) - 1]), o.split(" ")[2:4]))
                )
                or B.append(
                    list(
                        map(
                            lambda p: int(p[2 : len(p) - (1 if p[-1] == "," else 0)]),
                            o.split(" ")[8:10],
                        )
                    )
                ),
                open("d").read().strip().split("\n"),
            )
        ), input=list(
            map(
                lambda o: list(map(lambda p: int(p[2 : len(p) - 1]), o.split(" ")[2:4]))
                + list(
                    map(
                        lambda p: int(p[2 : len(p) - (1 if p[-1] == "," else 0)]),
                        o.split(" ")[8:10],
                    )
                ),
                open("d").read().strip().split("\n"),
            )
        )[
            :-1
        ], Y=2000000: (
            lambda x_min=min(min(input, key=lambda x: min(x[::2]))[::2]), x_max=max(
                max(input, key=lambda x: max(x[::2]))[::2]
            ), distance=lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2), points=[]: (
                lambda contains=lambda x1, y1, S1, S2, d: distance(
                    x1, y1, S1, S2
                ) <= d, max_distance=max(
                    [distance(x1, y1, x2, y2) for x1, y1, x2, y2 in input]
                ): (
                    lambda contained_in_any=lambda x, y, circles: any(
                        contains(x, y, x1, y1, distance(x1, y1, x2, y2))
                        for x1, y1, x2, y2 in circles
                    ): any(
                        points.append(1)
                        for x in range(x_min - max_distance, x_max + max_distance)
                        if contained_in_any(x, Y, input)
                        and [x, Y] not in S
                        and [x, Y] not in B
                    )
                )()
                or print(len(points))
            )()
        )()
    )()
)()
# part 2
(
    lambda input=list(
        map(
            lambda o: list(map(lambda p: int(p[2 : len(p) - 1]), o.split(" ")[2:4]))
            + list(
                map(
                    lambda p: int(p[2 : len(p) - (1 if p[-1] == "," else 0)]),
                    o.split(" ")[8:10],
                )
            ),
            open("d").read().strip().split("\n"),
        )
    ),: (
        lambda distance=lambda x1, y1, x2, y2: abs(x1 - x2) + abs(
            y1 - y2
        ), sum_pair=lambda l1, l2: (l1[0] + l2[0], l1[1] + l2[1]),: (
            lambda contains=lambda x1, y1, S1, S2, d: distance(x1, y1, S1, S2) <= d,: (
                lambda result=[], tmp=[1], contained_in_any=lambda x, y, circles: any(
                    contains(x, y, x1, y1, distance(x1, y1, x2, y2))
                    for x1, y1, x2, y2 in circles
                ), get_border=lambda s1, s2, b1, b2: [
                    (s1 - distance(s1, s2, b1, b2) - 1, s2, 1, 1),
                    (s1, s2 + distance(s1, s2, b1, b2) + 1, 1, -1),
                    (s1 + distance(s1, s2, b1, b2) + 1, s2, -1, -1),
                    (s1, s2 - distance(s1, s2, b1, b2) - 1, -1, 1),
                ]: any(
                    any(
                        any(
                            tmp.append(sum_pair((s_x, s_y), (k * s1, k * s2)))
                            or (tmp.pop(0) and False)
                            or (
                                (result.append(tmp[-1]) or True)
                                if not contained_in_any(*tmp[-1], input)
                                and 0 <= tmp[-1][0] <= 4000000
                                and 0 <= tmp[-1][1] <= 4000000
                                else False
                            )
                            for k in range(
                                s_x - get_border(s1, s2, b1, b2)[(i + 1) % 4][0] + 1
                            )
                        )
                        for i, (s_x, s_y, s1, s2) in enumerate(
                            get_border(s1, s2, b1, b2)
                        )
                    )
                    for s1, s2, b1, b2 in input
                )
                and print(result[-1][0] * 4000000 + result[-1][1])
            )()
        )()
    )()
)()
