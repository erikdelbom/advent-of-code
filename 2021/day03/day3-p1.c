#include <stdio.h>

#define BITSET_LENGTH 12

int main() {
    char bitstring[BITSET_LENGTH];
    int count[BITSET_LENGTH] = { 0 };

    while ( scanf("%s", bitstring) == 1 ) {
        for ( int i = 0; i < BITSET_LENGTH; i++ ) {
            if ( bitstring[i] == '1' ) {
                count[i]++;
            } else {
                count[i]--;
            }
        }
    }

    int gamma = 0;
    int epsilon = 0;
    
    for ( int i = 0; i < BITSET_LENGTH; i++ ) {
        if ( count[i] > 0 ) {
            gamma |= (1 << BITSET_LENGTH-(i+1));
        } else {
            epsilon |= (1 << BITSET_LENGTH-(i+1));
        }
    }

    printf("%s%d%s", "Gamma: ", gamma, "\n");
    printf("%s%d%s", "Epsilon: ", epsilon, "\n");
    printf("%s%d%s", "Multiplied: ", epsilon * gamma, "\n");

    return 0;
}