#include <iostream>
using namespace std;

int main() {
    int n, sum = 0;

    // Step 1: Take input from user
    cout << "Enter the value of n: ";
    cin >> n;

    // Step 2: Loop from 1 to n and add each number to sum
    for(int i = 1; i <= n; i++) {
        sum = sum + i; // or sum += i;
    }

    // Step 3: Output the result
    cout << "Sum of first " << n << " natural numbers is: " << sum << endl;

    return 0;
}
