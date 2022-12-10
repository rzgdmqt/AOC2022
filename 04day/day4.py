# part 1
print((lambda:sum((int(i[0][0])<=int(i[1][0])and int(i[0][1])>=int(i[1][1]))or(int(i[0][0])>=int(i[1][0])and int(i[0][1])<=int(i[1][1]))for i in(map(lambda o:list(map(lambda p:p.split("-"),o)),map(lambda o:o.split(","),open("d").read().split("\n"))))))())
# part 2
print((lambda:sum(set(range(int(i[0][0]),int(i[0][1])+1))&set(range(int(i[1][0]),int(i[1][1])+1))!=set()for i in(map(lambda o:list(map(lambda p:p.split("-"),o)),map(lambda o:o.split(","),open("d").read().split("\n"))))))())
