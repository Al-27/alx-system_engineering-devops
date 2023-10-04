#include "lists.h"

/**
 *insert_node - f
 *@head: Arg
 *@number: arg
 *
 *Return: type
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL, *new;
    
    if(!head)
        return NULL;
    
    
    node = *head;

	new = malloc(sizeof(listint_t));
    
	if (new == NULL)
		return (NULL);
    
	new->n = number;

	if (!node || node->n >= number)
	{
		new->next = node;
		*head = new;
		return new;
	}
    

	while (node &&  node->next->n < number && node->next)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return new;
}


