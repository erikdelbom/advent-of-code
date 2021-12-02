#include <stdio.h>
#include <string.h>

int main() {
    char direction[8];
    int magnitude;
    
    int x = 0;
    unsigned long y = 0;
    int aim = 0;

    while ( scanf("%s", direction) == 1 ) {
        scanf("%d", &magnitude);

        if ( strcmp(direction, "forward") == 0 ) {
            x += magnitude;
            y += aim * magnitude;

        } else if ( strcmp(direction, "up") == 0 ) {
            aim -= magnitude;

        } else if ( strcmp(direction, "down") == 0 ) {
            aim += magnitude;
        }
    }

    unsigned long position = x * y;
    printf("%ld%s", position, "\n");

    return 0;
}