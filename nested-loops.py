
def forward(i):
    print("forward() - [" + str(i) + "]")

def turn_left(i):
    print("turn_left()- [" + str(i) + "]")

# Initial loop test
for i in range(9):
    for j in range(9):
        print("(" + str(i) + ", " + str(j) + ")")

# U-turn puzzle
for i in range(3):
    for j in range(6):
        forward(j)
    turn_left(i)