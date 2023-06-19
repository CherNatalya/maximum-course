num = int(input())
List = []
i = 0
for n in range(num):
    List.append(int(input()))
    List = list(map(int, List))
for q in range(1, num):
    if List[q] > List[q - 1]:
        i += 1
print(i)
