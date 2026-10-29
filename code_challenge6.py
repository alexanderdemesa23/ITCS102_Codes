size = int(input("input size -->"))
z = 0
for x in range(size):
  if z != size:
    for y in range(x + 1):
      if z != size:
        z += 1
        print(z, end = "\t")
      elif z == size:
        print("", end = "\t")
    print("\n")
