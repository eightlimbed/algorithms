/* merge_sort.c - implementation of the merge sorting algorithm */
#include <stdio.h>
#include <stdlib.h>
/**
 * merge - the merging component of merge_sort. combines two subarrays into one.
 * @left: left subarray
 * @right: right subarray
 * @array: main array
 *
 * Return: void
 */
void merge(int *left, unsigned int left_count, int *right, 
		unsigned int right_count, int *array)
{
	unsigned int i, j, k;

	i = j = k = 0;
	while (i < left_count && j < right_count)
	{
		if (left[i] <= right[j])
		{
			array[k] = left[i];
			k++;
			i++;
		}
		else
		{
			array[k] = right[j];
			k++;
			j++;
		}
	}
	/* if one subarray is exhausted before the other one ... */
	while (i < left_count)
	{
		array[k] = left[i];
		k++;
		i++;
	}
	while (j < right_count)
	{
		array[k] = right[j];
		k++;
		j++;
	}
}
/**
 * merge_sort - sorts an array using the merge sort algorithm
 * @array: pointer to first element in array
 * @len: number of elements in array
 *
 * Return: void
 */
void merge_sort(int *array, unsigned int len)
{
	unsigned int mid, i;
	int *left, *right;

	/* initial argument check */
	if (array == NULL)
		return;

	/* base case: subarray with 1 element */
	if (len < 2)
		return;

	/* calculate middle of array */
	mid = len / 2;

	/* allocate space for left and right subarrays */
	left = malloc(mid * sizeof(int));
	if (left == NULL) return;
	right = malloc((len - mid) * sizeof(int));
	if (right == NULL) return;

	/* fill in left subarray */
	for (i = 0; i < mid; i++)
		left[i] = array[i];

	/* fill in right subarray */
	for (i = mid; i < len; i++)
		right[i-mid] = array[i];

	/* sort both sides recursively */
	merge_sort(left, mid);
	merge_sort(right, len-mid);

	/* merge both sides into array */
	merge(left, mid, right, len-mid, array);
	free(left);
	free(right);
	return;
}

int main(void)
{
	int array[] = {0, 6, 213, 12039, -12, 20, 8, 1, 4, 2, 30, 3, 5};
	unsigned int len, i;

	for (len = 0; len < sizeof(array) / sizeof(int); len++);
	printf("----- BEFORE -----\n");
	for (i = 0; i < len; i++)
	{
		printf("%d", array[i]);
		if (i < len - 1)
			printf(", ");
	}
	printf("\n");
	merge_sort(array, len);
	printf("----- AFTER -----\n");
	for (i = 0; i < len; i++)
	{
		printf("%d", array[i]);
		if (i < len - 1)
			printf(", ");
	}
	printf("\n");
	return (0);
}
