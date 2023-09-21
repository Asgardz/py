'''
【租车骑绿岛】100分
部门组织绿岛骑行团建活动。租用公共双人自行车，每辆自行车最多坐两人，做最大载重M。给出部门每个人的体重，请问最多需要租用多少双人自行车。
输入描述：
第一行两个数字m、n，分别代表自行车限重，部门总人数。
第二行，n个数字，代表每个人的体重，体重都小于等于自行车限重m。
0<m<=200 
0<n<=1000000 
输出描述：
最小需要的双人自行车数量。

示例1输入输出示例仅供调试，后台判题数据一般不包含示例输入
3 4
3 2 2 1
输出
3
解题思路：
1：题目中有两个隐含的条件：1、一辆车最多骑两个人2、人的重量不可能大于车的载重
2：那么可以用两个指针，一个指向头部left，一个指向尾部right，
如果w【left】+w【right】>车的载重，那么意味着最重的人，加上最轻的人都会超载，只能他一个人骑，right--。
如果w（left】 +w【right】<=车的载重，那么意味着这两个人可以还可以再加人，left ++继续判断直到总重量>车的蛾重。
'''

import sys

m, n = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()
res = 0
for i in range(n-1, -1, -1):
    if weight[i] == 0:
        continue
    if weight[i] == m:
        res += 1
        continue
    for j in range(i-1, -1, -1):
        if weight[j] != 0 and weight[i] + weight[j] <= m:
            weight[j] = 0
            break
    res += 1
print(res)

