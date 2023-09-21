#include<stdio.h>

#include <iostream>
using namespace std;

int calculateDays(int N, int D, int X, int Y, int P) {
    int dailyCost = X + (Y * P);
    int days = min(N / Y, D / dailyCost);
    return days;
}

int main() {
    int N, D, X, Y, P;

    cout << "输入小花手里的水瓶数量（N）: ";
    cin >> N;

    cout << "输入小花手里的钱（D）: ";
    cin >> D;

    cout << "输入房租（X）: ";
    cin >> X;

    cout << "输入每天需要的水瓶数（Y）: ";
    cin >> Y;

    cout << "输入超市卖水的价格（P）: ";
    cin >> P;

    int result = calculateDays(N, D, X, Y, P);

    cout << "小花可以坚持 " << result << " 天。" << endl;

    return 0;
}

