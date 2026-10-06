#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node*next;
};

void InsertionAtbeggining(struct node** headref , int value , int *Length){
    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    if(newnode == NULL){
        printf("memory allocation failed 1\n");
        return;
    }

    newnode->data = value;
    newnode->next = (*headref);
    (*headref) = newnode;
    
    (*Length) +=1;
}

void InsertionAtspecificIndex(struct node** headref , int value , int Index , int *Length){

    if(Index == 0){
        InsertionAtbeggining(headref , value,Length);
        return;
    }

    struct node* newnode = (struct node*)malloc(sizeof(struct node));
    if(newnode == NULL){
        printf("memory not allocated 2\n");
        return;
    }

    newnode->data = value;
    
    int count = 0;
    struct node* current = (*headref);
    while(current->next != NULL && count < (Index -1)){
        current = current->next;
        count +=1;
    }
    struct node* temp = current->next;
    current->next = newnode;
    newnode->next = temp;

    (*Length) +=1;
}

void InsertionAtEnd(struct node** headref, struct node** firstref ,int value){
    struct node * newnode = (struct node*)malloc(sizeof(struct node));
    if(newnode == NULL){
        printf("memory not allocated 3\n");
        return;
    }
    newnode->data = value;
    newnode->next=NULL;

    if(*headref == NULL){
        *headref = newnode;
        *firstref = newnode;
    }
    else{
        (*firstref)->next = newnode;
        (*firstref) = newnode; 
    }

}

void DeleteFirstNode(struct node** headref ,int *Length){
    if(*headref == NULL){
        printf("List is empty");
        return;
    }
    struct node*temp = (*headref);
    (*headref) = (*headref)->next;
    free(temp);
    (*Length) -= 1;
}

void DeleteFromSpecificIndex(struct node** headref , int Index ,int *Length){
    if(*headref == NULL || Index < 0 || Index >= *Length){
        printf("Invalid index or empty list");
    }
    if(Index == 0){
        DeleteFirstNode(headref , Length);
        return;
    }
    
    struct node* current = (*headref);
    int count = 0;

    
    while(current != NULL && count <(Index -1)){
        current =current->next;
        count +=1;
    }
    
    struct node* temp = current->next;
    current->next = NULL;
    free(temp);
    (*Length) = Index +1;
}

void DeleteLastNode(struct node** headref , int *Length){
    struct node* current = (*headref);

    if(current == NULL){
        printf("Memory not allocated 5");
        return;
    }

    while(current->next->next != NULL){
        current = current->next;
    }
    free(current->next) ;
    current->next = NULL;
    (*Length) -= 1;
}

void printing(struct node** headref){
    struct node * newnode = *headref;
    if(newnode == NULL){
        printf("Memory not allocated 6");
        return;
    }
    while (newnode != NULL){
        printf("%d->",newnode->data);
        newnode = newnode->next;
    }
    printf("NONE \n");
}


int main() {
    
    struct node* head = NULL;
    struct node* first = NULL;


    int num , a;
    printf("Enter number of elements to be inserted in linked list: ");
    scanf("%d",&num);

    for(int i =0;i<num;i++){
        printf("Enter");
        scanf("%d",&a);
        InsertionAtEnd(&head , &first , a);

    }
    printing(&head);

    int target;
    printf("Enter an element : ");
    scanf("%d",&target);

    InsertionAtbeggining(&head , target ,&num);
    printf("\nInsertion at beggining \n");
    
    printing(&head);
    
    int Index;
    printf("enter index to insert value : ");
    scanf("%d",&Index);

    if(Index > num){
        printf("Index not found");
    }
    else{
        InsertionAtspecificIndex(&head , target , Index , &num);
    }

    printf("\nInsertoin at index %d \n",Index);
    printing(&head);


    DeleteFirstNode(&head , &num);
    printf("\nDeleting First Node\n");
    printing(&head);

    DeleteLastNode(&head ,&num);
    printf("\nDeleting Last Node\n");
    printing(&head);

    int target;
    printf("Enter Index to Delete from :");
    scanf("%d",&target);

    DeleteFromSpecificIndex(&head , target, &num);
    printf("\nDeleting from Specific Indedx\n");
    printing(&head);

    struct node* temp ;
    while(head != NULL){
        temp = head;
        head = head->next;
        free(temp);
    }
    
    return 0;
}