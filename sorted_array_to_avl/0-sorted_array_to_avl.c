#include <stdlib.h>
#include <stdio.h>
#include "binary_trees.h"

/**
 * add_node - Recursively builds an AVL tree from a sorted array
 * @array: Pointer to the first element of the array to be converted
 * @size: Number of elements in the array
 * @parent: Pointer to the parent node of the current node
 *
 * Return: Pointer to the created node, or NULL on failure
 */
binary_tree_t *add_node(int *array, size_t size, avl_t *parent)
{
	binary_tree_t *node;

	if (size == 0)
		return (NULL);

	node = malloc(sizeof(avl_t));
	if (node == NULL)
		return (NULL);

	node->n = array[(size - 1) / 2];
	node->parent = parent;
	node->left = NULL;
	node->right = NULL;

	if (size > 2)
		node->left = add_node(array, (size - 1) / 2, node);

	if (size > 1)
		node->right = add_node(array + (size + 1) / 2, size / 2, node);

	return (node);
}

/**
 * sorted_array_to_avl - Converts a sorted array to a Binary Search Tree
 * @array: Pointer to the first element of the array to be converted
 * @size: Number of elements in the array
 *
 * Return: Pointer to the root node of the created AVL tree, or NULL on failure
 */
avl_t *sorted_array_to_avl(int *array, size_t size)
{
	if (!array || size == 0)
		return (NULL);

	return ((avl_t *)add_node(array, size, NULL));
}
