#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

#define STOP 0.0001

void GaussJacobi_Method(float x1, float x2, float x3)
{
    cout << "GAUSS-JACOBI:" << endl;
    vector<float> fL = {3,1,1,7}, sL = {1,4,2,4}, tL = {0,2,5, 5};
    float x1_ = x1, x2_ = x2, x3_ = x3;
    int counter = 0;
    do {
        counter ++;
        x1 = x1_;
        x2 = x2_;
        x3 = x3_;
        x1_ = (fL[3] - fL[1] * x2 - fL[2] * x3) / fL[0];
        x2_ = (sL[3] - sL[0] * x1 - sL[2] * x3) / sL[1];
        x3_ = (tL[3] - tL[0] * x1 - tL[1] * x2) / tL[2];
    }while(abs(x1_ - x1) > STOP | abs(x2 - x2_) > STOP | abs(x3 - x3_) > STOP );

    cout << "COUNTER = " << counter << endl;
    cout << x1_ << endl;
    cout << x2_ << endl;
    cout << x3_ << endl;
}

void GaussSeidel_Method(float x1, float x2, float x3)
{
    cout << "GAUSS-SEIDEL:" << endl;
    vector<float> fL = {3,1,1,7}, sL = {1,4,2,4}, tL = {0,2,5, 5};
    float x1_ = x1, x2_ = x2, x3_ = x3;
    int counter = 0;
    do {
        counter ++;
        x1 = x1_;
        x2 = x2_;
        x3 = x3_;
        x1_ = (fL[3] - fL[1] * x2 - fL[2] * x3) / fL[0];
        x2_ = (sL[3] - sL[0] * x1_ - sL[2] * x3) / sL[1];
        x3_ = (tL[3] - tL[0] * x1_ - tL[1] * x2_) / tL[2];
    }while(abs(x1_ - x1) > STOP | abs(x2 - x2_) > STOP | abs(x3 - x3_) > STOP );

    cout << "COUNTER = " << counter << endl;
    cout << x1_ << endl;
    cout << x2_ << endl;
    cout << x3_ << endl;
}

int main() {
    GaussJacobi_Method(0,0,0);
    cout << "############################" << endl;
    GaussSeidel_Method(0,0,0);
    return 0;
}
