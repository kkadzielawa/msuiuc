#include <iostream>
#include "Cube.cpp"

using std::cout;
using std::endl;

int main()
{

    uiuc::Cube c;

    int length = 3;

    c.setLength(length);

    double volume = c.getVolume();

    cout << "For length " << length << " volume is " << volume << "." << endl;

    return 0;
}