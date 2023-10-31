#include "lists.h"
/**
 * insert_node - inserts number value into n in order
 * @head: the list head
 * @number: the number we cant to insert
 * Return: adress if works NULL else
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *plus, *new;

new = malloc(sizeof(listint_t));
if (new == NULL){
	return (NULL);}
new->n = number;
new->next = NULL;

if (head == NULL)
{
	new = head;
	return (new);
}

	plus = *head;
	current = NULL;

while (plus != NULL && plus->n < number)
	{
		current = head;
		plus = plus->next;
	}
if (current == NULL)
{
	new->next = *head;
	*head = new;
}

		if (plus->n > number)
		{
			current->n = number;
			return(current);
		}
		else
		{
			current = current->next;
		}
	}
return (NULL);
}
