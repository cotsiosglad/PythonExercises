# A frog wants to cross a river, and the river is divided into N positions. The frog starts at position 0 and wants to reach position X.
# The frog can jump a distance of K positions forward at a time. The goal is to find the minimum time required for the frog to cross the river.

# Position 0 to position x
# Frog can jump distance of K positions forward at a time.


riverPos = float(input("The river is divided into N positions: "))
frogDest = float(input("The frog starts at position 0 and wants to reach position X: "))

if riverPos > frogDest:
    frogJump = input("The frog can jump a distance of K positions forward at a time: ")
    total = (float(frogDest) / float(frogJump))
    print("The frog will need total of jumps : " + str(total))
else:
    print("River Position has to be larger number than frog destination")
