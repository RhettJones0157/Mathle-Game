print("\033[0;37;40mThis is Mathle. It's like Wordle for math. Try to guess the math equation!\n")
print("\033[0;37;40mYellow: In the equation, but in the wrong spot.\n")
print("\033[0;37;40mGreen: In the equation, and in the right spot.\n")
print("\033[0;37;40mUnhighlighted: Not in the equation.\n")
print()
import random
import itertools
gamecode = []
repeatgenerator = True

while repeatgenerator == True:
  operatorlist = ['+', '-', '*', '/']
  operator = random.randint(0, 3)
  operat = operatorlist[operator]
  numba2 = random.randint(1, 20)
  if operat == '/':
    numba1 = random.randint(100, 500)
    numba2 = random.randint(50, 100)
  if operat == '-':
    numba1 = random.randint(30, 100)
  if operat == '+':
    numba1 = random.randint(9, 50)
  if operat == '*':
    numba1 = random.randint(15, 50)
  
  gamecode.append(str(numba1))
  gamecode.append(operat)
  gamecode.append(str(numba2))
  gamecodestring = ''.join(gamecode)
  gamecodestring.split()
  answer = eval(gamecodestring)
    
  if len(str(numba1)) + len(str(numba2)) + len(str(answer)) != 6:
    repeatgenerator = True
    gamecode = []
    
  else:  
    repeatgenerator = False
    gamecode = []
    number1 = [int(a) for a in str(numba1)]
    number2 = [int(b) for b in str(numba2)]
    answera = [int(c) for c in str(answer)]
    
    gamecode.append(number1)
    gamecode.append(operat)
    gamecode.append(number2)
    gamecode.append('=')
    gamecode.append(answera)

    wordle = list(itertools.chain(*gamecode))
    for i in range(8):
      wordle[i-1] = str(wordle[i-1])
    
    print()
    print()
    print()
    print()

color = '\033[37m'
def guess(place, t, u, v, w, x, y, z):
  if theirs[place] == wordle[place]:
    color = '\033[32m'
  elif theirs[place] == wordle[t] or theirs[place] == wordle[u] or theirs[place] == wordle[v] or theirs[place] == wordle[w] or theirs[place] == wordle[x] or theirs[place] == wordle[y] or theirs[place] == wordle[z]:
    color = '\033[33m'
  else:
    color = '\033[37m'
  return color
for i in range(999):
  print()
  guessword = input("\033[0;37;40mEnter math equation:\n")
  theirs = list(guessword)
  if len(theirs) != 8:
    print("\033[0;37;40mEquation incorrect length.\n")
  else:
    a = guess(0, 1, 2, 3, 4, 5, 6, 7)
    b = guess(1, 0, 2, 3, 4, 5, 6, 7)    
    c = guess(2, 0, 1, 3, 4, 5, 6, 7)
    d = guess(3, 0, 1, 2, 4, 5, 6, 7)
    e = guess(4, 0, 1, 2, 3, 5, 6, 7)
    f = guess(5, 0, 1, 2, 3, 4, 6, 7)
    g = guess(6, 0, 1, 2, 3, 4, 5, 7)
    h = guess(7, 0, 1, 2, 3, 4, 5, 6)
    print(a + theirs[0] + b + theirs[1] + c + theirs[2] + d + theirs[3] + e + theirs[4] + f + theirs[5] + g + theirs[6] + h + theirs[7])
    if theirs == wordle:
        print("You won!")
        break

#have user input an equation
#hihglight certain characters
#rpeeat until win
#gamecode = 8-charcater code user is trying to guess
#numba1 operator numba2 = answer









'''
f = '\033[37m'
def guess(place, w, x, y, z):
    if theirs[place] == wordle[w] or theirs[place] == wordle[x] or theirs[place] == wordle[y] or theirs[place] == wordle[z]:
        color = '\033[33m'
    elif theirs[place] == wordle[place]:
        color = '\033[32m'
    else:
        color = '\033[37m'
    return color
for i in range(6):
  guessword = input("Enter word: ")
  theirs = list(guessword)
  if len(theirs) < 5:
    print("Word not long enough.")
  else:
    a = guess(0, 1, 2, 3, 4)
    b = guess(1, 0, 2, 3, 4)    
    c = guess(2, 0, 1, 3, 4)
    d = guess(3, 0, 1, 2, 4)
    e = guess(4, 0, 1, 2, 3)
    print(a + theirs[0] + b + theirs[1] + c + theirs[2] + d + theirs[3] + e + theirs[4] + f)
    if theirs == wordle:
        print("You won!")
        break
'''
