#include <stdio.h>
#include <unistd.h>

void vuln_func() {
    char buf[128];
    read(STDIN_FILENO, buf, 256);
}

int main() {
    printf("%p\n", &main);
    vuln_func();
    write(STDOUT_FILENO, "Hello world!\n", 13);
    return 0;
}
