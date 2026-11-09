#include<stdio.h>

struct ListNode {
      int val;
      struct ListNode *next;
  };
 
struct ListNode* removeElements(struct ListNode* head, int val) {
    if(head == NULL){
        return NULL;
    }
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->val = 0;
    dummy->next = head;
    struct ListNode* curr = dummy;
    while(curr->next){
        if(curr->next->val == val){
            curr->next = curr->next->next;
        }
        else{
            curr = curr->next;
        }
    }
    return dummy->next;
    
}