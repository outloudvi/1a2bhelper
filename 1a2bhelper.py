curComb = [] # All possibilities
curTest = [] # All tests


class Global:
  pass

# Test if the number  (target) fulfills the rule:
#  (a)A (b)B for the number (orig)
def TestOK(orig, a, b, target):
  origList = []
  targList = []
  for i in orig:
    if i not in origList:
      origList.append(i)
  for i in target:
    if i not in targList:
      targList.append(i)
  tgapb = 0 # Total A+B
  for i in origList:
    if i in targList:
      tgapb += 1
  tga = 0   # Total A
  for i in range(len(orig)):
    if orig[i] == target[i]:
      tga += 1
  if tga == a and tgapb == a + b:
    return True
  else:
    return False

# Info
def ShowInfo():
  print("""
1A2B Solver.
""")

# Check if a number qualifies to be a number of 1A2B
def uniq(strnum):
  nl = []
  for i in strnum:
    if i in nl:
      return False
    nl.append(i)
  return True


def AskForLength():
  while 1:
    x = int(input("Number length: "))
    if 1 <= x and x <= 10:
      return x
    else:
      print("Invalid.")


def leftpad(t, l):
  while len(t) < l:
    t = '0' + t
  return t


def main():
  global curComb, curTest
  r = Global()
  ShowInfo()
  r.len = AskForLength()
  for i in range(0, 10**r.len): # Need optimizing
    ti = leftpad(str(i), r.len)
    if uniq(ti):
      curComb.append(ti)
  print('Generated. %s possibilities.' % len(curComb))
  while 1:
    if len(curComb) == 1:
      print("The only value: %s" % curComb[0])
    x = str(input('> '))
    arg = x.split(' ')
    argLen = len(arg)
    if argLen == 1:
      if arg[0] == 's': # Show all possibilities
        print('\n'.join(curComb))
      if arg[0] in curComb:
        print("Likely.")
        continue
      else:
        print("Unreasonable.")
    elif argLen == 3:
      curTest.append(arg)
      argZen = []
      for i in curComb:
        if TestOK(arg[0], int(arg[1]), int(arg[2]), i) == True:
          argZen.append(i)
      curComb = argZen
      print("Now %s left." % (len(curComb)))
    else:
      print("Unrecognized.")

if __name__ == "__main__":
    main()
