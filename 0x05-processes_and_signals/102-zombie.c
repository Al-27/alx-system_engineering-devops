#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> 

/**
 * main - 
 * Return: int
*/
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - 
 * Return: int
*/
int main(void)
{
    int parenID = (int)getpid(), i = 0, child;

    for(;i < 5; i++)
    {
        if(parenID == getpid())
        {
            child =  fork();
            if(child == 0)
            {
                infinite_while();
            }
            else
            {
                 printf("Zombie process created, PID: %d\n", child);
            }
        }
    }

    return (0);
}

    
