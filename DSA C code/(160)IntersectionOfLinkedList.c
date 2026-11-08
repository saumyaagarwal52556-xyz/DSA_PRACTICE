struct ListNode {
      int val;
      struct ListNode *next;
  };


int lengthoflist(struct ListNode *headA){
    int leng = 0;
    struct ListNode* curr = headA;
    while(curr){
        leng += 1;
        curr = curr->next;
    }
    return leng;
}

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode* firstcopy = headA;
    struct ListNode* secondcopy = headB;

    int lenA = lengthoflist(firstcopy);
    int lenB = lengthoflist(secondcopy);

    if(lenA < lenB){
        for(int i=0;i<lenB - lenA;i++){
            headB = headB->next;
        }
    }
    else{
        for(int i=0;i< lenA - lenB;i++){
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
    return NULL;
    
}