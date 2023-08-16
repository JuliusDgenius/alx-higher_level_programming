#include "lists.h"

/**
 * reverse_list - Function reverses a singly linked list
 * *head: pointer to 1st node of the reversed linked list
 *
 * Return: returns a pointer to the head of reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *node = *head, *next, *prev = NULL;

    while (node)
    {
        next = node->next;
        node->next = prev;
        prev = node;
        node = next;
    }
    *head = prev;
    return (*head);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: A pointer to pointer to first node
 *
 * Return: returns an integer: 1 if success 0 if fail
 */
int is_palindrome(listint_t **head)
{
    listint_t *tmp, *reverse, *mid;
    size_t size = 0, i;

    if (*head == NULL || (*head)->next == NULL)
        return (1);
    tmp = *head;
    while (tmp)
    {
        size++;
        tmp = tmp->next;
    }

    tmp = *head;
    for (i = 0; i < (size / 2) - 1; i++)
        tmp = tmp->next;
    if ((size % 2) == 0 && tmp->n != tmp->next->n)
        return (0);
    tmp = tmp->next->next;
    reverse = reverse_listint(&tmp);
    mid = reverse;

    tmp = *head;
    while (reverse)
    {
        if (tmp->n != reverse->n)
            return (0);
        tmp = tmp->next;
        reverse = reverse->next;
    }
    reverse_listint(&mid);

    return (1);
}
