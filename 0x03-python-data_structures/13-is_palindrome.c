#include "lists.h"
/**
 * is_palindrome - checks if the list is palindrome
 * @head: the list's head
 * Return: 0 if the list is not a palindrome and 1 otherwise
 */
int is_palindrome(listint_t **head)
{
listint_t *current;
int i = 0, j = 0, len = 0;
if (*head == NULL)
{
	return (1);
}
	current = *head;
	while (current != NULL)
	{
		current = current->next;
		len++;
	}
	current = *head;
	int array[len];
	for (i = 0; i <= len ; i++)
	{
		array[i] = current->n;
		current = current ->next;
	}

	if (len % 2 == 0)
	{
		for (i = 1; i <= len / 2 ; i++)
		{
			for (j = len; j >= len; j--)
			{
				if (array[i] == array[j])
				{
					continue;
				}
				else
				{
					return (0);
				}
			}
		}
	}
	else
	{
		for (i = 1; i <= (len - 1) / 2; i++)
		{
			for (j = len; j >= (len - 1) / 2; j--)
			{
				if (array[i] == array[j])
				{
					continue;
				}
				else
				{
					return (0);
				}
			}
		}
	}
	return (1);
}
