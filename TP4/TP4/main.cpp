#include <iostream>
#include <math.h>
#define STOP pow(10, -6)
float f1(float x, float y)
{
    return 2*pow(x,2) -x*y-5*x+1;
}

float f2(float x,float y)
{
    return x+3*log(x)-pow(y, 2);
}

float df1(char c, float x, float y)
{
    switch (c)
    {
        case 'x':
            return 4*x-y-5;
        case 'y':
            return -x;
    }
}

float df2(char c, float x, float y)
{
    switch (c)
    {
        case 'x':
            if(x == 0){
                std::cout << "ERROR" << std::endl; break;}
            return 1+3/x;
        case 'y':
            return -2*y;
    }
}

void Newtons_Method(float xn, float yn)
{
    float xn_ = xn;
    float yn_ = yn;
    int counter =  0;
    do {
        xn = xn_;
        yn = yn_;
        counter++;
        xn_ = xn - ((f1(xn, yn) * df2('y', xn, yn) - f2(xn, yn) * df1('y', xn, yn)) /
                    (df1('x', xn, yn) * df2('y', xn, yn) - df2('x', xn, yn) * df1('y', xn, yn)));
        yn_ = yn - ((f2(xn, yn) * df1('x', xn, yn) - f1(xn, yn) * df2('x', xn, yn)) /
                    (df1('x', xn, yn) * df2('y', xn, yn) - df2('x', xn, yn) * df1('y', xn, yn)));
    } while(abs(xn_- xn) > STOP && abs(yn_ -yn) > STOP);
    std::cout << "Counter: " << counter << std::endl;
    std::cout << "X: " << xn_ << std::endl;
    std::cout << "Y: " << yn_ << std::endl;
}


float G(int n, float x, float y)
{
    switch (n) {
        case 1:
            return sqrt((x * y + 5 * x - 1) / 2);
        case 2:
            return sqrt(3 * log(x) + x);
    }
}

void Picard_Peano_Method(float xn, float yn)
{
    float xn_ = xn;
    float yn_ = yn;
    int counter = 0;
    do{
        xn = xn_;
        yn = yn_;
        counter++;
        xn_ = G(1, xn, yn);
        yn_ = G(2, xn, yn);
    } while(abs(xn_-xn) > STOP && abs(yn_-yn) > STOP);
    std::cout << "Counter: " << counter << std::endl;
    std::cout << "X: " << xn_ << std::endl;
    std::cout << "Y: " << yn_ << std::endl;
}

void Gauss_Seidel_Method(float xn, float yn)
{
    float xn_ = xn;
    float yn_ = yn;
    int counter = 0;
    do {
        counter++;
        xn = xn_;
        yn = yn_;
        xn_ = G(1, xn, yn);
        yn_ = G(2, xn_, yn);
    } while(abs(xn_-xn) > STOP && abs(yn_ - yn) > STOP);
    std::cout << "Counter: " << counter << std::endl;
    std::cout << "X: " << xn_ << std::endl;
    std::cout << "Y: " << yn_ << std::endl;
}

int main() {
    Newtons_Method(4,4);
    std::cout << "============================" << std::endl;
    Picard_Peano_Method(4,4);
    std::cout << "============================" << std::endl;
    Gauss_Seidel_Method(4,4);
    return 0;
}
