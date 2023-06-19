List = list(input())
print(sorted(List))
for num in range(1, len(List)):
    if List[num - 1] > List[num]:
        List[num - 1], List[num] = List[num], List[num - 1]
print(List)
