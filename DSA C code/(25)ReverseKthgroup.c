#include<stdio.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *reverseKGroup(struct ListNode *head, int k)
{
    struct ListNode *temp = head;
    for (int i = 0; i < k; i++)
    {
        if (temp == NULL)
        {
            return head;
        }
        temp = temp->next;
    }

    struct ListNode *prev = reverseKGroup(temp, k);

    // reversing
    struct ListNode *curr = head;
    for (int i = 0; i < k; i++)
    {
        struct ListNode *nextnode = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextnode;
    }
    return prev;
}