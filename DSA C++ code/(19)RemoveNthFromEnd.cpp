
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution
{
public:
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        int len = 0;
        ListNode *temp = head;
        while (temp)
        {
            len += 1;
            temp = temp->next;
        }
        if (len <= 1 && n == 1)
        {
            return nullptr;
        }
        if (len == n)
        {
            return head->next;
        }
        int count = 1;
        ListNode *current = head;
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
};