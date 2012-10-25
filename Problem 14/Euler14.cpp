//
//  Euler14.cpp
//  
//
//  Created by José Miguel Molina Arboledas on 07/05/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
using namespace std;

bool isEven(unsigned long int n);

int main() {
    unsigned long int number = 0;
    unsigned long int maxNumber = 0;
    unsigned long int numberx = 0;
    unsigned long int changes = 0;
    unsigned long int maxChanges = 0;
    for (unsigned long int i = 1; i < 1000000; i++) {
        numberx = i;
        number = i;
        changes = 0;
        while (numberx != 1) {
            if (isEven(numberx)) {
                numberx = numberx/2;
            } else {
                numberx = 3*numberx + 1;
            }
            changes++;
        }
        cout << changes << " in " << number << endl;
        if (changes > maxChanges) {
            maxChanges = changes;
            maxNumber = number;
        }
    }
    
    cout << maxNumber << endl; // 837799
}

bool isEven(unsigned long int n) {
    if (n % 2 == 0) {
        return true;
    } else {
        return false;
    }
}