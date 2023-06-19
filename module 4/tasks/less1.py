string = input()
i = len(string) // 2
print(string[:i] == string[:len(string) - i - 1:-1])
