#include <stdio.h>

int climbStairs(int n) {
    if (n <= 1) return 1;
    if (n == 2) return 2;
    int a = 1, b = 2;
    for (int i = 3; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int main() {
    int n = 7;
    printf("Ways to climb %d stairs: %d\n", n, climbStairs(n));
    return 0;
}