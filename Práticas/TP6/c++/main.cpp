#include <iostream>
#import <cmath>

float f(float x)
{
    return (sin(x)) / pow(x, 2);
}

float trapezios(float a, float b, int n)
{
    float h = (b-a) / n;
    float result = f(a);
    for(int i = 1; i <= n; i++)
        result += 2*f(a + i* h);
    result = (h/2) * (result);
    return result;
}

float simpson(float a, float b, int n)
{
    float h = (b-a) / n;
    float result = f(a);
    for(size_t i = 1; i <= n; i++)
    {
        if(!(i % 2))
            result += 2*f(a+i*h);
        else
            result += 4*f(a+i*h);
    }
    result = (h/3) * (result);
    return result;
}

float trapezioError(int n, float a, float b)
{
    float s = trapezios(a, b, n);
    float ss = trapezios(a, b, 2*n);
    float sss = trapezios(a, b, 4*n);
    int QC = (ss - s) / (sss - ss);
    float error = (sss - ss) / (pow(2, QC) - 1);
    return error;
}

float simpsonError(int n, float a, float b)
{
    float s = simpson(a, b, n);
    float ss = simpson(a,b, 2*n);
    float sss = simpson(a, b, 4*n);
    int QC = (ss - s) / (sss - ss);
    float error = (sss - ss) / (pow(2, QC) - 1);
    return error;
}


int main() {
    std::cout << "TRAPEZIOS METHOD: " << trapezios(M_PI /2, M_PI, 4) << std::endl;
    std::cout << "Error: " << trapezioError(4, M_PI, M_PI/2) << std::endl;
    std::cout << "SIMPSONS METHOD: " << simpson(M_PI /2, M_PI, 4) << std::endl;
    std::cout<< "Error: " << simpsonError(4, M_PI, M_PI/2) << std::endl;
    std::cout << "TRAPEZIOS METHOD: " << trapezios(M_PI /2, M_PI, 16) << std::endl;
    std::cout << "Error: " << trapezioError(16, M_PI, M_PI/2) << std::endl;
    std::cout << "SIMPSONS METHOD: " << simpson(M_PI /2, M_PI, 16) << std::endl;
    std::cout<< "Error: " << simpsonError(16, M_PI, M_PI/2) << std::endl;
    return 0;
}

