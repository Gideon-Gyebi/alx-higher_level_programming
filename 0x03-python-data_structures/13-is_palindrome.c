#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reversing a singly linked listint_t list.
 * @head: A pointer to the starting node of the list to be reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

  /* Iterate through the linked list, starting from the head. */
	while (node)
	{
    /* Save the next node in the `next` pointer. */
		next = node->next;
    /* Reverse the `node` pointer. */
		node->next = prev;
    /* Move the `prev` pointer to the `node` pointer. */
		prev = node;
    /* Move the `node` pointer to the `next` pointer. */
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome (0).
 *         If the linked list is a palindrome (1).
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

  /* Get the middle of the linked list. */
	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

  /* If the linked list has an even number of nodes, check if the middle two nodes are equal. */
	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

  /* Reverse the second half of the linked list. */
	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

  /* Compare the first half of the linked list to the reversed second half. */
	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
  /* Reverse the second half of the linked list back to its original order. */
	reverse_listint(&mid);

	return (1);
}
