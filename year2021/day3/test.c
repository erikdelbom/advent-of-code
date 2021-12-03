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

int main() {
    char bitstring[BITSET_LENGTH];
    int set_bit_counter = 0;
    int all_bitsets[INPUT_LENGTH];

    for ( int i = 0; i < INPUT_LENGTH; i++ ) {
        scanf("%s", bitstring);
        int bitset = create_integer(bitstring);
        all_bitsets[i] = bitset;
    
        set_bit_counter += get_bit(bitset, BITSET_LENGTH-1); 
    }

    int oxygen_ideal_bitset = 0;
    int co2_ideal_bitset = 0;
    int oxygen = 0;
    int co2 = 0;
    int half = INPUT_LENGTH / 2;

    for ( int i = BITSET_LENGTH-1; i >= 0; i-- ) {
        if ( set_bit_counter >= half ) {
            oxygen_ideal_bitset |= (1 << i); 
        } else {
            co2_ideal_bitset |= (1 << i);
        }

        set_bit_counter = 0;

        printf("ideal oxygen: ");
        print_bitset(oxygen_ideal_bitset);
        printf("\n");

        int mask = 0;
        int hits = 0;

        for ( int j = 0; j < (BITSET_LENGTH-i); j++ ) {
            mask |= (1 << BITSET_LENGTH-1-j);
        }
        printf("mask: ");
        print_bitset(mask);
        printf("\n");

        for ( int j = 0; j < INPUT_LENGTH; j++ ) {
            if ( (all_bitsets[j] & mask) == oxygen_ideal_bitset ) {
                hits += 1;
                set_bit_counter += get_bit(all_bitsets[j], i-1);
                oxygen = all_bitsets[j];
            }
        }
        printf("%s%d%s", "counter: ", set_bit_counter, "\n\n");

        if ( set_bit_counter == 1 ) break;
    }
    printf("oxygen: ");
    print_bitset(oxygen);
    printf("\n");
    // 1000 0000 0000 0000
    // 0000 0000 0000 0000





    // int oxygen_ideal = create_ideal_bitset(counter);
    // int co2_ideal = ~oxygen_ideal & 0x0FFF;
    // int oxygen = 0;
    // int co2 = 0;

    // for ( int i = 0; i < BITSET_LENGTH; i++ ) {
    //     for ( int j = 0; j < INPUT_LENGTH; j++ ) {
    //         int mask = (0xFFF >> i);

    //         if ( (oxygen_ideal >> i) & mask == (all_bitsets[i] >> i) & mask ) {
    //             oxygen = all_bitsets[j];
    //         }
    //     }
    // }

    // for ( int i = 0; i < BITSET_LENGTH; i++ ) {
    //     for ( int j = 0; j < INPUT_LENGTH; j++ ) {
    //         int mask = (0xFFF >> i);

    //         if ( (co2_ideal >> i) & mask == (all_bitsets[i] >> i) & mask ) {
    //             co2 = all_bitsets[j];
    //         }
    //     }
    // }
    
    // printf("%s%d%s", "Oxygen: ", oxygen, "\n");
    // printf("%s%d%s", "CO2: ", co2, "\n");

    // for ( int i = BITSET_LENGTH-1; i >= 0; i-- ) {
    //     printf("%d%s", get_bit(oxygen, i), "   ");
    // }
    // printf("\n");


    // for ( int i = BITSET_LENGTH-1; i >= 0; i-- ) {
    //     printf("%d%s", get_bit(co2, i), "   ");
    // }
    // printf("\n");

    return 0;
}

// 100100101010