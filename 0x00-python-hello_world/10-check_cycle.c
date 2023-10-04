#include "lists.h"

/**
 * check_cycle - func
 * @list: arg
 *
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *next = list->next,*next2 = list->next->next;

	if (!list)
		return (0);

	while (next)
	{
			
		if(!next->next)
		    break;
		if(!next2->next)
		    break;
		
		next = next->next;
		next2 = next->next;
		
		if (next == next2)
			return 1;
	
    }

	return 0;
}
