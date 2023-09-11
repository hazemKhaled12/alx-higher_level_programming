#include "lists.h"

/**
 * is_palindrome - singly linked list
 * @head: head of list
 * Return: 0 or 1 based on if palindrome
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (is_palind(head, *head));
}

/**
 * is_palind - Check if palindrom
 * @head: head list
 * @end: end list
 * Return: 0 or 1 based on if palindrome
 **/

int is_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (is_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
