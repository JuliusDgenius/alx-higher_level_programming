#include "lists.h"

/**
 * check_cycle - to check if a singly linked list has a cycle
 * @list: A pointer to the list
 *
 * Return: return 1 if cycle is present. Else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr;
	listint_t *previous;

	ptr = list;
	previous = list;
	while (list && ptr && ptr->next)
	{
		list = list->next;
		previous = previous->next->next;

		if (list == previous)
		{
			list = previous;
			previous = ptr;
			while (1)
			{
				ptr = previous;
				while (ptr->next != list && ptr->next != previous)
				{
					ptr = ptr->next;
				}
				if (ptr->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
