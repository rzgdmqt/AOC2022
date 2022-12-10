import os

for dr in os.listdir("."):
  if dr.endswith("day"):
    a = dr.split("day")[0]
    if len(a) == 1:
      os.rename(dr, f"0{a}day")
    else:
      os.rename(dr, f"{a}day")