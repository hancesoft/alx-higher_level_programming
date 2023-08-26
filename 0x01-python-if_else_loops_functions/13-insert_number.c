#include <lists.h>

/**
* insert_node - Insert number into a sorted singly list
* @head: pointer to first node in the list
* @number: number to insert
* Return: pointer to new node, else failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;
	
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	
	if (!node || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
