#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - function to print all elements of a linked list
 * @head: Pointer to the head of the linked list
 * Return: returns the number of nodes in linked list
 */
size_t print_listint(const listint_t *head)
{
	const listint_t *currentNode;
	/* The number of nodes in list */
	unsigned int n;

	currentNode = head;
	n = 0;

	while (currentNode != NULL)
	{
		printf("%i\n", currentNode->n);
		currentNode = currentNode->next;
		n++;
	}
	return (n);
}

/**
 * add_nodeint - to add a new node at the beginning of list
 * @head: The pointer to the pointer of the start of the list
 * @n: The integer to be included in the node
 *
 * Return: address of the new wlwmwnt or NULL when fail.
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = n;
	newNode->next = *head;
	*head = newNode;

	return (newNode);
}

/**
 * free_listint - frees memory of a linked list
 * @head: The pointer to the list to be freed
 *
 * Return: Nothing
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
