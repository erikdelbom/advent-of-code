#include <stdio.h>
#include <string.h>

int main() {
    char direction[8];
    int magnitude;
    
    int x = 0;
    int y = 0;

    while ( scanf("%s", direction) == 1 ) {
        scanf("%d", &magnitude);

        if ( strcmp(direction, "forward") == 0 ) {
            x += magnitude;
            
        } else if ( strcmp(direction, "up") == 0 ) {
            y -= magnitude;

        } else if ( strcmp(direction, "down") == 0 ) {
            y += magnitude;
        }
    }

    int position = x * y;
    printf("%d%s", position, "\n");

    return 0;
}