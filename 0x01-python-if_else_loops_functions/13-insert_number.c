#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Fxn to inserts number in a given sorted singly linked list
 * @head: Pointer to the first node of the linked list
 * @number: The number to be inserted into list
 *
 * Return: return the address of the new node if successful, else NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *currentNode = NULL, *node = NULL;

	if (head != NULL)
	{
		node = malloc(sizeof(listint_t));
		if (node != NULL)
		{
			node->n = number;
			currentNode = *head;
			while ((currentNode != NULL) && (currentNode->n < number))
			{
				if (((currentNode->next != NULL) && (currentNode->next->n < number)))
					currentNode = currentNode->next;
				else
					break;
			}
			if ((currentNode != NULL) && (currentNode->n < number))
			{
				node->next = currentNode->next;
				currentNode->next = node;
			}
			else
			{
				node->next = *head;
				*head = node;
			}
		}
	}
	return (node);
}
