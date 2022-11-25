#include <stdio.h>
#include <stdlib.h>

#define BITSET_LENGTH 12
#define INPUT_LENGTH 1000
#define get_bit(bitset, index) ((bitset >> index) & 1)

int create_integer(char bitstring[]) {
    int number = 0;
    for ( int i = 0; i < BITSET_LENGTH; i++ ) {
        if ( bitstring[i] == '1' ) {
            number |= (1 << BITSET_LENGTH-(i+1));
        }
    }

    return number;
}

int create_ideal_bitset(int counter[]) {
    int ideal_bitset = 0;

    for ( int i = 0; i < BITSET_LENGTH; i++ ) {
        if ( counter[i] >= 500 ) {
            ideal_bitset |= (1 << (BITSET_LENGTH-(i+1)));
        }
    }

    return ideal_bitset;
}

void print_bitset(int bitset) {
    for ( int i = BITSET_LENGTH-1; i >= 0; i-- ) {
        printf("%d", get_bit(bitset, i));
    }
}

int find_rating(int all_bitsets[], int type) {
    int total = INPUT_LENGTH;
    int ideal_bitset = 0;
    int rating = 0;
    int done = 0;

    for ( int i = BITSET_LENGTH-1; i >= 0; i-- ) {
        int set_bit_counter = 0;
        int mask = 0;
        int hits = 0;

        for ( int j = 0; j < (BITSET_LENGTH-i); j++ ) {
            mask |= (1 << BITSET_LENGTH-j);
        }
        printf("mask: ");
        print_bitset(mask);
        printf("\n");

        for ( int j = 0; j < INPUT_LENGTH; j++ ) {
            if ( (all_bitsets[j] & mask) == ideal_bitset ) {
                set_bit_counter += get_bit(all_bitsets[j], i);
                rating = all_bitsets[j];
                hits++;
            }
        }

        if ( set_bit_counter >= (total / 2) + type) {
            ideal_bitset |= (type << i);
            
            if ( type == 1) {
                total = set_bit_counter;
            } else {
                total = total - set_bit_counter;
            }

        } else {
            ideal_bitset |= ((~type & 1) << i);
            
            if ( type == 0) {
                total = set_bit_counter;
            } else {
                total = total - set_bit_counter;
            }
        }
        
        printf("ideal: ");
        print_bitset(ideal_bitset);
        printf("\n\n");

        if ( done == 1 ) return rating;
        if ( hits == 1 ) done = 1;
    }

    return ideal_bitset;
}

int main() {
    char bitstring[BITSET_LENGTH];
    int set_bit_counter = 0;
    int all_bitsets[INPUT_LENGTH];

    for ( int i = 0; i < INPUT_LENGTH; i++ ) {
        scanf("%s", bitstring);
        int bitset = create_integer(bitstring);
        all_bitsets[i] = bitset;
    
        //set_bit_counter += get_bit(bitset, BITSET_LENGTH-1); 
    }

    int oxygen_ideal_bitset = 0;
    int co2_ideal_bitset = 0;
    int oxygen = find_rating(all_bitsets, 1);
    int co2 = find_rating(all_bitsets, 0);

    printf("%d%s", oxygen, "\n");
    printf("%d%s", co2, "\n");
    printf("%d%s", co2 * oxygen, "\n");

    return 0;
}