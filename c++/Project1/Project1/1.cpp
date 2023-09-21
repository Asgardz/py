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

    cout << "����С�������ˮƿ������N��: ";
    cin >> N;

    cout << "����С�������Ǯ��D��: ";
    cin >> D;

    cout << "���뷿�⣨X��: ";
    cin >> X;

    cout << "����ÿ����Ҫ��ˮƿ����Y��: ";
    cin >> Y;

    cout << "���볬����ˮ�ļ۸�P��: ";
    cin >> P;

    int result = calculateDays(N, D, X, Y, P);

    cout << "С�����Լ�� " << result << " �졣" << endl;

    return 0;
}

