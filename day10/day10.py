# part 1
(lambda input=open("d").read().split("\n"),cycle=[0],data={"sum": 0, "value":1}: (lambda:any(cycle.append(0) or (cycle.append(int(row.split(" ")[1])) if row.startswith("addx") else False)for row in input) or any((data.update({"sum": data["sum"] + i * data["value"]}) if (i - 20) % 40 == 0 else False) or data.update({"value": data["value"] + n}) for i, n in enumerate(cycle)) or print(data["sum"]))())()
# part 2
(lambda input=open("d").read().split("\n"),cycle=[0],data={"value":1},crt=[" "]*240: (lambda:any(cycle.append(0) or (cycle.append(int(row.split(" ")[1])) if row.startswith("addx") else False)for row in input) or any((crt.insert(i - 1, "█") or crt.pop(i) and False if data["value"] - 1 <= (i - 1) % 40 <= data["value"] + 1 else False) or data.update({"value": data["value"] + n}) for i, n in enumerate(cycle)) or any(print("".join(crt[i * 40:i*40 + 40]))for i in range(6)))())()
