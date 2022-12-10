# part 1
print((lambda p=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":sum(map(lambda o:sum([p.index(i)for i in o]),map(lambda o:set(o[:len(o)//2])&set(o[len(o)//2:]),open("d").read().split("\n")))))())
# part 2
print((lambda r:(lambda p=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":sum(map(lambda o:p.index(list(set(o[0])&set(o[1])&set(o[2]))[0]),([r[i:i+3]for i in range(0,len(r)-2,3)]))))())(open("d").read().split("\n")))
