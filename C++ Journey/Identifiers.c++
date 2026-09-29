#include <iostream>
using namespace std;
class students
{
    public:

        void show ()
        {
            int marks = 90;
            cout << marks;

        }
};
int main()
{
    students s1;
    s1.show();
    return 0;

}