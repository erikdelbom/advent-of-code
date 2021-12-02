#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

struct Movement {
    int magnitude;
    char * direction;
};

void print_movement(struct Movement * movement) {
    printf("%s%s", movement->direction, " ");
    printf("%d%s", movement->magnitude, "\n");
}

bool read_movement(struct Movement * movement) {
    char direction[8];
    int magnitude;
    scanf("%s", direction);
    if ( scanf("%d", &magnitude) != 1 ) {
        return false;
    }

    movement->direction = direction;
    movement->magnitude = magnitude;

    return true;
}

void update_position(struct Movement * movement, int * x, int * y) {
    if ( strcmp(movement->direction, "forward") ) {
        x += movement->magnitude;
    } else if ( strcmp(movement->direction, "up") ) {
        y -= movement->magnitude;
    } else if ( strcmp(movement->direction, "down") ) {
        y += movement->magnitude;
    }
}

int main() {
    struct Movement movement;
    int x = 0;
    int y = 0;

    while ( read_movement(&movement) ) {
        update_position(&movement, &x, &y);
        print_movement(&movement);
    }

    int result = x * y;

    printf("%d%s", result, "\n");

    return 0;
}