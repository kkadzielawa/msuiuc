#include <iostream>
using std::cout;
using std::endl;

int main()
{

    int num = 7; // regular value variable
    cout << "num: " << num << endl;
    cout << "&num: " << &num << endl;

    int *p = &num; // define pointer p pointing to memory address of num
    cout << "p: " << p << endl;
    cout << "&p: " << &p << endl;
    cout << "*p: " << *p << endl;

    *p = 42;
    cout << "*p: " << *p << endl;
    cout << "num: " << num << endl;
}
