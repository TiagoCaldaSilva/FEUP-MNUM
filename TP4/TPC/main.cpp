#include <iostream>
#include <math.h>

#define STOP 0.000001
#define GUESS 2

double function(double x)
{
    return x * exp( pow( x , 2 ) - 4 ) - 1;
}

double difFunction(double x)
{
    return 2*pow(x, 2)*exp(pow(x, 2) - 4) + exp(pow(x, 2) - 4);
}

double GFunction(double x)
{
    return sqrt(4-log(x));
}


void Bisection_Method(double xn, double yn)
{
    double xn_ = (xn + yn) / 2, x2;
    unsigned int counter = 0;
    do {
        x2 = xn_;
        counter++;
        if(function(xn_)*function(xn) > 0) xn = xn_;
        else yn = xn_;
        xn_ = (xn + yn) / 2;
    } while(abs(xn_-x2) > STOP);
    std::cout << "Bisection Method:" << std::endl;
    std::cout << "Counter: " << counter << std::endl;
    std::cout << "Value: " << xn_ << std::endl;
    std::cout << "//=//=//=//=//=//=//=//=//=//=//=//" << std::endl;
}

void Rope_Method(double a, double b)
{
    double xn_ = a, xn2;
    unsigned int counter = 0;
    do {
        xn2 = xn_;
        xn_ = (a*function(b)-b*function(a)) / (function(b) - function(a));
        if(function(a)*function(xn_) < 0)
            b = xn_;
        else
            a = xn_;
        counter++;
    }while(abs(xn_ - xn2) > STOP);
    std::cout << "Rope Method:" << std::endl;
    std::cout << "Counter: " << counter << std::endl;
    std::cout << "Value: " << xn_ << std::endl;
    std::cout << "//=//=//=//=//=//=//=//=//=//=//=//" << std::endl;
}

void Newtons_Method(double xn)
{
    unsigned int counter = 0;
    double xn_ = xn;
    do {
        xn = xn_;
        xn_ = xn - (function(xn) / difFunction(xn));
        counter ++;
    } while(abs(xn_ - xn) > STOP);
    std::cout << "Newton's Method:" << std::endl;
    std::cout << "Counter: " << counter << std::endl;
    std::cout << "Value: " << xn_ << std::endl;
    std::cout << "//=//=//=//=//=//=//=//=//=//=//=//" << std::endl;
}

void PicardPeano_Method(double xn)
{
    unsigned int counter = 0;
    double xn_ = xn;
    do {
        xn = xn_;
        xn_ = GFunction(xn);
        counter++;
    } while(abs(xn_ - xn) > STOP);
    std::cout << "Picard-Peano Method:" << std::endl;
    std::cout << "Counter: " << counter << std::endl;
    std::cout << "Value: " << xn_ << std::endl;
    std::cout << "//=//=//=//=//=//=//=//=//=//=//=//" << std::endl;
}

int main() {
    Bisection_Method(1, 2);
    Rope_Method(1,2);
    Newtons_Method(GUESS);
    PicardPeano_Method(GUESS);
    return 0;
}
