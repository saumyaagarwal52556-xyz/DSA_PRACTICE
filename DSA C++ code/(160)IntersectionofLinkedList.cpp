struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(nullptr) {}
  };

class Solution {
public:
    int lengthoflist(ListNode *headA){
        int leng = 0;
        ListNode* curr = headA;
        while(curr){
            leng += 1;
            curr = curr->next;
        }
        return leng;
    }
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* firstcopy = headA;
        ListNode* secondcopy = headB;

        int lenA = lengthoflist(firstcopy);
        int lenB = lengthoflist(secondcopy);

        if(lenA < lenB){
            for(int i=0;i<lenB-lenA ;i++){
                headB = headB->next;
            }
        }
        else{
            for(int i =0;i<lenA-lenB;i++){
                headA = headA->next;
            }
        }
        while(headA && headB){
            if(headA == headB){
                return headA;
            }
            headA = headA->next;
            headB = headB->next;
        }
        return nullptr;
        
    }
};