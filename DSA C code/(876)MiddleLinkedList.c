#include<stdio.h>

struct ListNode {
      int val;
      struct ListNode *next;
 };
 
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode* temp = head;
    int leng = 0;
    while(temp){
        leng += 1;
        temp = temp->next;
    }
    if(leng == 1){
        return head;
    }
    if(leng<=0){
        return NULL;
    }
    int count = 0;
    struct ListNode* curr = head;
    while(curr && count<(leng / 2)){
        curr = curr->next;
        count += 1;
    }
    return curr;
    
}