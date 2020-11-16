from workplace import task1
import sys

#  dont touch this stuff 

numtasks = 1
testcases = {}

for i in range(1, numtasks+1):
  print("---------- task" + str(i) + " ----------")
  testcases["t{0}t".format(i)] = open(("task" + str(i) + "test.py"), "r").read()
  testcases["t{0}a".format(i)] = task1("Paul Shim", 5)

  print(len(testcases["t{0}t".format(i)]))
  print(len(testcases["t{0}a".format(i)]))

  if testcases["t{0}t".format(i)] == testcases["t{0}a".format(i)]:
    print("Success")
  else:
    print("You failed.")
