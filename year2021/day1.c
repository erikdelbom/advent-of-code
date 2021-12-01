#include <stdio.h>

int main() {
    int prev_depth;
    int depth;
    int count = 0;
    
    scanf("%d", &prev_depth);

    while ( scanf("%d", &depth) == 1 ) {    
        if ( depth > prev_depth ) {
            count++;
        }
        prev_depth = depth;

    }
    printf("%d%s", count, "\n");

    
    return 0;
}