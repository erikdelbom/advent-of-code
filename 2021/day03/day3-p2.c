#include <stdio.h>
#include <stdlib.h>

#define BITSET_LENGTH 12
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

struct dynamic_array {
    int capacity;
    int size;
    int * items;
};

void dynamic_array_insert(struct dynamic_array * array, int number) {
    if ( array->size == array->capacity ) {
        int new_capacity = 1.5 * array->capacity;
        array->items = (int * ) realloc(array->items, (sizeof(int) * new_capacity));
        array->capacity = new_capacity;
    }
    array->items[array->size] = number;
    array->size++;
}

void dynamic_array_remove(struct dynamic_array * array, int index) {
    for ( int i = index; i < array->size; i++ ) {
        array->items[i] = array->items[i+1];
    }
    
    if ( array->size < array->capacity / 2 ) {
        int new_capacity = array->capacity / 2;
        array->items = (int * ) realloc(array->items, (sizeof(int) * new_capacity));
        array->capacity = new_capacity; 
    }
    
    array->size--;
}


int main() {
    char bitstring[BITSET_LENGTH];
    struct dynamic_array oxygen = {2, 0, new int[2]};
    struct dynamic_array co2 = {2, 0, new int[2]};
    int counter[BITSET_LENGTH];

    while ( scanf("%s", bitstring) == 1 ) {      
        dynamic_array_insert(&oxygen, create_integer(bitstring));
        dynamic_array_insert(&co2, create_integer(bitstring));
    }

    int index = BITSET_LENGTH-1;
    int ones = 0;
    int zeros = 0;

    for ( int i = 0; i < BITSET_LENGTH; i++) {
        if ( oxygen.size == 1 ) break;
        
        for ( int i = 0; i < oxygen.size; i++ ) {
            if ( get_bit(oxygen.items[i], index) == 1 ) {
                ones++;
            } else {
                zeros++;
            }
        }

        if ( ones >= zeros ) {
            for ( int i = 0; i < oxygen.size; i++ ) {
                if ( get_bit(oxygen.items[i], index) == 0 ) {
                    dynamic_array_remove(&oxygen, i);
                    i--;
                } 
            }

        } else {
            for ( int i = 0; i < oxygen.size; i++ ) {
                if ( get_bit(oxygen.items[i], index) == 1 ) {
                    dynamic_array_remove(&oxygen, i);
                    i--;
                } 
            }
        }

        index--;
        ones = 0;
        zeros = 0;
    }

    index = BITSET_LENGTH-1;
    ones = 0;
    zeros = 0;

    for ( int i = 0; i < BITSET_LENGTH; i++) {
        if ( co2.size == 1 ) break;
        
        for ( int i = 0; i < co2.size; i++ ) {
            if ( get_bit(co2.items[i], index) == 1 ) {
                ones++;
            } else {
                zeros++;
            }
        }

        if ( ones >= zeros ) {
            for ( int i = 0; i < co2.size; i++ ) {
                if ( get_bit(co2.items[i], index) == 1 ) {
                    dynamic_array_remove(&co2, i);
                    i--;
                } 
            }

        } else {
            for ( int i = 0; i < co2.size; i++ ) {
                if ( get_bit(co2.items[i], index) == 0 ) {
                    dynamic_array_remove(&co2, i);
                    i--;
                } 
            }
        }

        index--;
        ones = 0;
        zeros = 0;
    }

    printf("%d%s", oxygen.items[0] * co2.items[0], "\n");

    return 0;
}