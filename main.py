print("Try to guess the math equation")
print("Yellow: In the equation, but in the wrong spot.")
print("Green: In the equation, and in the right spot.")
print("Unhighlighted: Not in the equation.")
import random



#randomly generate a 8-character equation
#have user input an equation
#hihglight certain characters
#rpeeat until win





#gamecode = 8-charcater code user is trying to guess
#numba1 operator numba2 = answer

gamecode = []
operatorlist = ['+', '-', '*', '/']
operator = random.randint(0, 3)
numba1 = random.randint(1, 50)
numba2 = random.randint(1, 50)
operator1 = operatorlist[operator]
gamecode.append(str(numba1))
gamecode.append(operator1)
gamecode.append(str(numba2))

gamecodestring = ''.join(gamecode)
answer = eval(gamecodestring)

#

gamecode.append('=')
gamecode.append(answer)
print(gamecode)








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
