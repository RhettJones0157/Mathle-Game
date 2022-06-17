print("This is Mathle. It's like Wordle for math. Try to guess the math equation!")
print("Yellow: In the equation, but in the wrong spot.")
print("Green: In the equation, and in the right spot.")
print("Unhighlighted: Not in the equation.")
print()
import random
import itertools
gamecode = []
repeatgenerator = True


#randomly generate a 8-character equation
#have user input an equation
#hihglight certain characters
#rpeeat until win
#gamecode = 8-charcater code user is trying to guess
#numba1 operator numba2 = answer

#operator, two numbers are chosen
while repeatgenerator == True:
  operatorlist = ['+', '-', '*', '/']
  operator = random.randint(0, 3)
  operat = operatorlist[operator]
  if operat == '/':
    numba1 = random.randint(100, 500)
  if operat == '-':
    numba1 = random.randint(50, 100)
  if operat == '+':
    numba1 = random.randint(1, 50)
  if operat == '*':
    numba1 = random.randint(1, 15)
  numba2 = random.randint(1, 50)
  
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

    gamecodefinal = list(itertools.chain(*gamecode))
    
    print(gamecodefinal)
    


#









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
