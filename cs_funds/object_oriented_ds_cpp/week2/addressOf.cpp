#include <iostream>

void foo()
{
    int x = 42;
    std::cout << "Value: " << x << std::endl;
    std::cout << "Address: " << &x << std::endl;
}

int main()
{
    int num = 7;
    std::cout << "Value: " << num << std::endl;
    std::cout << "Address: " << &num << std::endl;

    foo();

    return 0;
}