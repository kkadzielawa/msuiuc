#include <iostream>
using namespace std;

int main(void)
{
    double dval;
    dval = 3;
    double *p = &dval;
    cout << "Value of dval is: " << &p << endl;
}
