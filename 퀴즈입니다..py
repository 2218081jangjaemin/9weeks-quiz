import random

height = int(input("크리스마스 트리의 높이를 설정하세요: "))

print(" " * (height - 1) + "☆")

for i in range(height):
    for j in range(height - i):
        print(" ", end="")
    for k in range(i * 2 + 1):
        print(random.choice(["*", "●"]), end="")
    print()

print(" " * (height - 1) + "||")
