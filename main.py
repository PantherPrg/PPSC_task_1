from workplace import lunchPunishment
import sys

#  dont touch this stuff 

numtasks = 3
variables = {}
testcases = [["Paul Shim", 5], ["Joshua Almario", 20], ["John Adams", 25]]
perfect = True

for i in range(1, numtasks+1):
  print("---------- test" + str(i) + " ----------")
  variables["t{0}t".format(i)] = open(("task" + str(i) + "test.py"), "r").read()
  variables["t{0}a".format(i)] = lunchPunishment(testcases[i-1][0], int(testcases[i-1][1]))

  if variables["t{0}t".format(i)] == variables["t{0}a".format(i)]:
    print("|         Success         |")
  else:
    print("|       You failed.       |")
    perfect = False

print("---------------------------")

if perfect == True:
  print("\nCongratulations! You successfully completed PPSC_task_1")
