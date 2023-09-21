def find_unique_digits_number(l, r):
    for x in range(l, r + 1):
        x_str = str(x)
        if len(set(x_str)) == len(x_str):
            return x
    return -1

# 读取输入的组数
n = int(input())
result = []
# 针对每一组输入进行处理
for _ in range(n):
    l, r = map(int, input().split())
    res = find_unique_digits_number(l, r)
    result.append(res)
for i in range(len(result)):
    print(result[i])
