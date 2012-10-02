//
//  Euler9.cpp
//  
//
//  Created by José Miguel Molina Arboledas on 06/05/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
using namespace std;

bool isPythagoreanTriplet(int a, int b, int c);
unsigned int a = 0;
unsigned int b = 1;
unsigned int c = 2;
bool cCompleted = false;

int main(void) {
    while (true) {
        cCompleted = false;
        if (isPythagoreanTriplet(a, b, c)) {
            if (a + b + c == 1000) {
                cout << "abc = " << a*b*c << endl; // Result: 31875000
                break;
            }
        }
        if (b == 999) {
            a++;
            b = a + 1;
            c = b + 1;
        }
        if(c == 1000) {
            cCompleted = true;
            b++;
            c = b + 1;
        }
        if (!cCompleted) {
            c++;
        }
    }
}

bool isPythagoreanTriplet(int a, int b, int c) {
    if (a < b && b < c) {
        if ((a*a + b*b) == (c*c)) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}