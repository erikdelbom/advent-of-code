#include <stdio.h>

// void clear(int * arr) {
//     for ( int i == 0; i < 3; i++ ) {
//         arr[i] = 0;
//     }
// }

int sum(int * arr) {
    int sum = 0;
    for ( int i = 0; i < 3; i++ ) {
        sum += arr[i];
    }

    return sum;
}

void print(int * arr) {
    for ( int i = 0; i < 3; i++ ) {
        printf("%d%c", arr[i], ' ');
    }
}

int main() {
    int a_arr[3];
    int b_arr[3];
    int c_arr[3];
    int d_arr[3];
    
    int depth;
    int count = 0;
    int interval = 0;

    scanf("%d", &depth);
    a_arr[0] = depth;
    scanf("%d", &depth);
    a_arr[1] = depth;
    b_arr[0] = depth;
    scanf("%d", &depth);
    a_arr[2] = depth;
    b_arr[1] = depth;
    c_arr[0] = depth;

    while ( scanf("%d", &depth) == 1 ) {
        if ( interval == 0 ) {
            b_arr[2] == depth;
            c_arr[1] == depth;
            d_arr[0] == depth;
            
            printf("%s", "prev arr ");
            print(a_arr);
            printf("%s", "\n");
            printf("%s", "second arr ");
            print(b_arr);
            printf("%s", "\n");
            printf("%s", "\n");
            if ( sum(a_arr) < sum(b_arr) ) {
                count++;
            }
            //clear(a_arr);
        }
        else if ( interval == 1 ) {
            a_arr[0] == depth;
            c_arr[2] == depth;
            d_arr[1] == depth;
            
            printf("%s", "prev arr ");
            print(b_arr);
            printf("%s", "\n");
            printf("%s", "second arr ");
            print(c_arr);
            printf("%s", "\n");
            printf("%s", "\n");

            if ( sum(b_arr) < sum(c_arr) ) {
                count++;
            }
            //clear(b_arr);
        }
        else if ( interval == 2 ) {
            a_arr[1] == depth;
            b_arr[0] == depth;
            d_arr[2] == depth;
            printf("%s", "prev arr ");
            print(c_arr);
            printf("%s", "\n");
            printf("%s", "second arr ");
            print(d_arr);
            printf("%s", "\n");
            printf("%s", "\n");
            if ( sum(c_arr) < sum(d_arr) ) {
                count++;
            }
            //clear(c_arr);
        }
        else if ( interval == 3 ) {
            a_arr[2] == depth;
            b_arr[1] == depth;
            c_arr[0] == depth;
            printf("%s", "prev arr ");
            print(c_arr);
            printf("%s", "\n");
            printf("%s", "second arr ");
            print(d_arr);
            printf("%s", "\n");
            printf("%s", "\n");
            if ( sum(c_arr) < sum(d_arr) ) {
                count++;
            }
            interval = -1;
        }
            //clear(d_arr);
        interval++;
    }

    printf("%d%s", count, "\n");

    return 0;
}