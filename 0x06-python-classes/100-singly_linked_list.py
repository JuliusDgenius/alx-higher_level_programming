#!/usr/bin/python3
class Node:
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initializes instances of Node class
        Args:
            data (int): data of the node.
            next_node (Node): A ptr to next node of a Slinked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data of the Node of a singly linked list"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets the data field of a node in a singly linked list
        Args:
            value (int): the value of data in the list
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next node in a linked list"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        """Initializes a private instance of sinlgy linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correction position in the list
        (increasing order)
        Args:
            value (int): An integer value to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Defines string rep of a singly linked list"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
