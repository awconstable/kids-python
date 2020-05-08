#print even numbers
print("Even Numbers")
for i in range(20):
    if((i % 2) == 0):
        print(i)

#print odd numbers
print("Odd Numbers")
for i in range(20):
    if((i % 2) == 1):
        print(i)

# tile puzzle
def has_path_right():
    return True

def turn_right():
    print("turn right")

def forward():
    print("forward")

for i in range(9):
    if(has_path_right()):
        turn_right()
    forward()


