#include <math.h>
#include <iostream>
#include <iomanip>


int main()
{
	std::cout.precision(3);
	double e = expm1(1);
	for (int i = 1; i <= 26; i++)
	{
		std::cout << std::fixed <<  "Ano " << std::setw(2) << i - 1  << " | " << e << std::endl;
		e = e * i - 1;
	}

	return 0;
}