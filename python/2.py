'''
输入一个长度为4的倍数的字符串，字符串中仅包含WASD四个字母。将这个字符串中的连续子串用同等长度的仅包含WASD的字符串替换，如果替换后整个字符串中WASD四个字母出现的频数相同，那么我们称替换后的字符串是“完美走位”。
求子串的最小长度。如果输入字符串已经平衡则输出0。
输入
一行字符表示给定的字符串s。 数据范围： 1<=n<=10^5且n是4的倍数，字符串中仅包含WASD四个字母。
输出
一个整数表示答案
示例1：
输入： WASDAASD
输出： 1
说明： 将第二个A替换为W，即可得到完美走位 。
示例2：
输入： AAAA
输出： 3
说明： 将其中三个连续的A替换为WSD，即可得到完美走位
'''

import collections  #提供了一些有用的容器数据类型，如 defaultdict

def isTrue(map):
    for i in map.values(): #迭代访问 map 中的所有值。
        if i > 0:
            return False
    return True

str = input()  #wasd map[W] = map[W] + 1
len = len(str)
count = len // 4

map = collections.defaultdict(int)

for i in range(len):
    map[str[i]] += 1

for key in map:
    map[key] -= count

min_1 = float('inf')
for i in range(len):
    cIndexI = str[i]
    res = 0
    copyMap = map.copy()
    if copyMap[cIndexI] > 0:
        for j in range(i, len):
            cIndexJ = str[j]
            copyMap[cIndexJ] -= 1
            res += 1
            if isTrue(copyMap):
                break
    if isTrue(copyMap):
        min_1 = min(min_1, res)

print(min_1)
