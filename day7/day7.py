# part 1
(lambda input, dict={}, current=["/"]:(lambda f=[(any(dict.update({"/".join(current[0].split("/")[:i]): dict.get("/".join(current[0].split("/")[:i]), 0) + int(cmd.split(" ")[0])}) for i in range(len(current[0].split("/")))) if cmd[0].isdigit() else (current.append("/".join(current[0].split("/")[:-2]) + "/") or (current.pop(-2) and False)) if  cmd.startswith("$ cd ..")else (current.append("/") or (current.pop(-2) and False)) if cmd == "$ cd /" else (current.append(current[0] + cmd.split(" ")[-1] + "/") or (current.pop(-2) and False)) if cmd.startswith("$ cd ")else ...) for cmd in input]: print(sum(v for _, v in dict.items() if v <= 100000)))())(open("d").read().split("\n"))
# part 2
(lambda input, dict={}, current=["/"]:(lambda f=[(any(dict.update({"/".join(current[0].split("/")[:i]): dict.get("/".join(current[0].split("/")[:i]), 0) + int(cmd.split(" ")[0])}) for i in range(len(current[0].split("/")))) if cmd[0].isdigit() else (current.append("/".join(current[0].split("/")[:-2]) + "/") or (current.pop(-2) and False)) if  cmd.startswith("$ cd ..")else (current.append("/") or (current.pop(-2) and False)) if cmd == "$ cd /" else (current.append(current[0] + cmd.split(" ")[-1] + "/") or (current.pop(-2) and False)) if cmd.startswith("$ cd ")else ...) for cmd in input]: print(min([v for _, v in sorted(list(dict.items()), key=lambda x: x[1]) if v > 30000000 - (70000000 - dict[""] // 2)])))())(open("d").read().split("\n"))
