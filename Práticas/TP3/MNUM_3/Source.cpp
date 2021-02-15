#include <iostream>
#include <math.h>

#define CRITERIO 0.0001

float Function1(float x)
{
	return x - 2 * log(x) - 5; //F1
	//return pow(2, sqrt(x)) - 10 * x + 1; //F2
}

float Function1_(float x)
{
	return 1 - (2 / x); //Derivada de F1
	//return ((log(2) * pow(2, sqrt(x) - 1)) / sqrt(x)) - 10; //Derivada de F2
}


float Newton(float guess)
{
	int counter = 0;
	float xn = guess, xn_ = guess - (Function1(guess) / Function1_(guess));
	while (abs(xn_ - xn) > CRITERIO)
	{
		counter++;
		xn = xn_;
		xn_ = xn - (Function1(xn) / Function1_(xn));
	}
	std::cout << counter << " iteracoes" << std::endl;
	return xn_;
}

float FunctionG(float x)
{
	//return exp((x - 5) / 2); //Function1 -> g1, x0 = 0.01
	//return 2 * log(x) + 5; //Function1 -> g2, x0 = 9
	//return (pow(2, sqrt(x)) + 1) / 10; //Function2 -> g1, x0 = 2
	//return pow(log2(10 * x - 1), 2); //Function2 -> g2, x0 = 98
	return 1 + (1 / tan(x)) * sin(3 * x);
}


float Picard_Peano(float guess)
{
	int counter = 0;
	float xn = guess, xn_ = FunctionG(guess);
	while (abs(xn_ - xn) > CRITERIO)
	{
		counter++;
		xn = xn_;
		xn_ = FunctionG(xn);
	}
	std::cout << counter << " iteracoes" << std::endl;
	return xn;
}


int main()
{
	std::cout << Newton(9.4) << std::endl;
	//std::cout << Picard_Peano(2) << std::endl;
	//std::cout << abs(2 * (log2(10 * 98 - 1)) * (10 / (10 * 98 - 1)) * log2(exp(1))); -> para verificar a segunda raiz da F2
	std::cout << (3 * tan(0.05) * cos(3 * 0.05) - pow((1/ cos(0.05)), 2) * sin(3 * 0.05)) / pow(tan(0.05), 2);
	return 0;
}