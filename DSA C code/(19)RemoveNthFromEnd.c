#include<stdio.h>
struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *removeNthFromEnd(struct ListNode *head, int n)
{
    int len = 0;
    struct ListNode *temp = head;
    while (temp)
    {
        len += 1;
        temp = temp->next;
    }
    if (len <= 1 && n == 1)
    {
        return NULL;
    }
    if (len == n)
    {
        return head->next;
    }
    int count = 1;
    struct ListNode *current = head;
    while (current && count < (len - n))
    {
        current = current->next;
        count += 1;
    }
    if (current && current->next)
    {
        current->next = current->next->next;
    }
    return head;
}