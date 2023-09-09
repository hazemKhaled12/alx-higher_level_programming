#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check for the cycle in the linked list
 * @list: pointer to list to check
 * Return: 1 if cycle, 0  otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
