# Testing simple loops in Python

def forward(i):
    print("forward(" + str(i) + ")")

for i in range(9):
    forward(i)
print("after loop")

print()
print()

for i in range(10,-10,-1):
    forward(i)