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
    ListNode *reverselist(ListNode *head)
    {
        ListNode *prev = nullptr;
        ListNode *curr = head;

        while (curr)
        {
            ListNode *nextnode = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextnode;
        }
        return prev;
    }

    bool isPalindrome(ListNode *head)
    {
        ListNode *copyHead = new ListNode(head->val);
        ListNode *copylist = copyHead;
        ListNode *curr = head->next;
        while (curr)
        {
            copylist->next = new ListNode(curr->val);
            copylist = copylist->next;
            curr = curr->next;
        }
        ListNode *second = reverselist(copyHead);
        ListNode *first = head;

        while (second)
        {
            if (first->val != second->val)
            {
                return false;
            }
            first = first->next;
            second = second->next;
        }
        return true;
    }
};