numbers_contain_3 = []
count = 0
for n in range(1, 10001):
    if '3' in str(n):
        numbers_contain_3.append(n)
print(*numbers_contain_3, sep='\n')

