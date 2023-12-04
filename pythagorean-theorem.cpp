#include <iostream>
#include <cmath>
using namespace std;

string A, B;

int main() {
        A = "980234570928437509284375092834709572034987502938475092837450923847509283470598237409582730495872039847502897435";
        B = "5723487509238475029384750928374059283740592348750927340598273405927340958724309857029347592873459283475098234750";
        std::cout << A;
        std::cout << endl;
        std::cout << B;
        std::cout << std::endl;
        std::cout << "The hypotenuse of the right triangle is: " << sqrt(pow(A, 2.0) + pow(B, 2.0)) << "\n";
        std::cout << std::endl;
        return 0;
}

