#include <stdio.h>
#include <stdlib.h>
struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    int carry = 0;
    struct ListNode *result = NULL;
    struct ListNode *copy = NULL;

    while (l1 || l2 || carry)
    {
        int val1 = l1 ? l1->val : 0;
        int val2 = l2 ? l2->val : 0;

        int total = val1 + val2 + carry;
        carry = total / 10;
        int digit = total % 10;

        struct ListNode *newList = (struct ListNode *)malloc(sizeof(struct ListNode));
        newList->val = digit;
        newList->next = NULL;
        if (result == NULL)
        {
            result = newList;
            copy = newList;
        }
        else
        {
            copy->next = newList;
            copy = newList;
        }
        if (l1)
        {
            l1 = l1->next;
        }
        if (l2)
        {
            l2 = l2->next;
        }
    }
    return result;
}