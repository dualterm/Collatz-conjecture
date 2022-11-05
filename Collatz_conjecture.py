import sys
sys.setrecursionlimit(100000)

prenumber = 0
def loop():
  global prenumber
  prenumber = prenumber + 1
  number = prenumber
  count = 0

  with open("data.txt", "a") as file:
    file.write(str(prenumber))
    file.write("---")
  while number != 1:
    if number % 2 != 0:
      number = number * 3 + 1
      count = count + 1
    if number % 2 == 0:
      number = number / 2
      count = count + 1
  with open("data.txt", "a") as file:
    file.write(str(count))
    file.write("\n")
  if prenumber == 20000:
    exit()
  return loop()
loop()
