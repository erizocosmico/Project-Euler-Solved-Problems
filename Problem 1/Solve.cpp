// Project Euler problem 1
// Find the sum of all the multiples of 3 or 5 below 1000.

#include <iostream>
using namespace std;

unsigned int solution = 0;

int main(void) 
{
	for (int i = 1; i < 1000; i++)
	{
		if (i % 3 == 0 || i % 5 == 0)
		{
			solution += i;
		}
	}
	
	cout << solution << endl;
}