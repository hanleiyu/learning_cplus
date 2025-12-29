#include <iostream>
#include "Sales_item.h"
using namespace std;

void main(){
    // 1.3
    cout << "Hello World" << endl;

    //1.4
    cout << 2025 * 12 * 29 << endl;
    
    //1.9
    int sum = 0, val = 50;
    while(val <= 100){
        sum += val;
        ++val;
    }
    cout << "sum of 50 to 100 is " << sum << endl;

    //1.11
    cout << "Please enter two numbers" << endl;
    int num1, num2;
    cin >> num1 >> num2;
    if(num1 > num2){
        swap(num1, num2);
    }
    while(num1 <= num2){
        cout << num1;
        num1 ++;
    }
    cout << endl;
}