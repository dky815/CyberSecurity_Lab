#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#ifndef BUF_SIZE
#define BUF_SIZE 78
#endif

int readFile(FILE *fp)
{
    char buffer[BUF_SIZE];
    printf("buffer is at:%p\r\n",buffer);
    fread(buffer, sizeof(char), 300, fp);
    // int index_end = fread(buffer, sizeof(char), BUF_SIZE, fp);
    
    return 1;
}

int main(int argc, char **argv)
{
    FILE *fp;
    char dummy[BUF_SIZE*5]; memset(dummy, 0, BUF_SIZE*5);
    fp = fopen(argv[1], "r");
    readFile(fp);
    printf("Returned Properly\n");
    fclose(fp);
    return 1;
}