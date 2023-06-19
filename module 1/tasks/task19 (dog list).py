List = list(input())
Max = List.index(max(List))
Min = List.index(min(List))
List[Min], List[Max] = List[Max], List[Min]
print(List)
