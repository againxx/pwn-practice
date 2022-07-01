#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    char buf1[10], buf2[10], *s;
    int num;

    // safe
    memcpy(buf1, argv[1], 10);
    strcpy(buf2, "AAAABBBBC");
    printf("%s %s\n", buf1, buf2);

    // unknown
    memcpy(buf1, argv[2], atoi(argv[3]));
    strcpy(buf2, argv[1]);
    printf("%s %s\n", buf1, buf2);

    // unsafe
    // memcpy(buf1, argv[1], 11);
    // strcpy(buf2, "AAAABBBBCC");

    s = fgets(buf1, 11, stdin);
    printf(buf1, &num);
}
