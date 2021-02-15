#include <math.h>
#include <iostream>
#include <iomanip>

double function1(double x)
{
	//return (x - 2 * log(x) - 5); //a
	return pow(2, pow(x, 0.5)) - 10 * x + 1; //b
	//return cotg(x) * sin(3 * x) - x + 1;
}

double BissectionMethod_AbsoluteStop(double a, double b)
{
	int i = 0;
	double xn = (a + b) / 2;
	while (abs(b-a) > 0.000001) {
		i++;
		if ((function1(xn) * function1(a)) < 0)
			b = xn;
		else
			a = xn;
		xn = (a + b) / 2;
	}
	std::cout << i << std::endl;
	return xn;
}

double BissectionMethod_NullAtRoot(double a, double b)
{
	int i = 0;
	double xn = (a + b) / 2;
	while (abs(function1(a) - function1(b)) > 0.000001)
	{
		i++;
		if ((function1(a) * function1(xn)) > 0)
			a = xn;
		else
			b = xn;
		xn = (a + b) / 2;
	}
	std::cout << i << std::endl;
	return xn;
}

double BissectionMethod_TwoConsecutivesStop(double a, double b)
{
	int i = 0;
	double xn = 0, x2 = 1;
	while (abs(xn - x2) > 0.000001)
	{
		i++;
		x2 = xn;
		xn = (a + b) / 2;
		if (function1(xn) * function1(a) < 0)
			b = xn;
		else
			a = xn;
	}
	std::cout << i << std::endl;
	return xn;
}

double RopeMethod_AbsoluteStop(double a, double b)
{
	int i = 0;
	double xn = 0;
	while (abs(b - a) > 0.000001)
	{
		i++;
		xn = (a * function1(b) - b * function1(a)) / (function1(b) - function1(a));
		if (function1(xn) * function1(a) < 0)
			b = xn;
		else
			a = xn;
	}
	std::cout << i << std::endl;
	return xn;
}

double RopeMethod_NullAtRoot(double a, double b)
{
	int i = 0;
	double xn = 0;
	while (abs(function1(a) - function1(b)) > 0.000001)
	{
		i++;
		xn = (a * function1(b) - b * function1(a)) / (function1(b) - function1(a));
		if (function1(a) * function1(xn) < 0)
			b = xn;
		else
			a = xn;
	}
	std::cout << i << std::endl;
	return xn;
}

double RopeMethod_TwoConsecutivesStop(double a, double b)
{
	int i = 0;
	double xn = 1, x2 = 0.5;
	while (abs(xn - x2) > 0.000001)
	{
		i++;
		x2 = xn;
		xn = (a * function1(b) - b * function1(a)) / (function1(b) - function1(a));
		if (function1(a) * function1(xn) < 0)
			b = xn;
		else
			a = xn;
	}
	std::cout << i << std::endl;
	return xn;
}

int main()
{
	std::cout << BissectionMethod_AbsoluteStop(0, 0.5) << std::endl;
	std::cout << BissectionMethod_NullAtRoot(0, 0.5) << std::endl;
	std::cout << BissectionMethod_TwoConsecutivesStop(0, 0.5) << std::endl;
	std::cout << RopeMethod_AbsoluteStop(0.01,0.5) << std::endl;
	std::cout << RopeMethod_NullAtRoot(0.01, 0.5) << std::endl;
	std::cout << RopeMethod_TwoConsecutivesStop(0.01, 0.5) << std::endl;
	return 0;
}