#include <iostream>
using namespace std;

struct node{
    int data;
    node* next;
};

void InsertionAtBeginning(node* &head , int value ,int &Length){
    node* newnode = new node;
    newnode->data = value;
    newnode->next = head;
    head = newnode;
    Length +=1;

}

void InsertionAtSpecificIndex(node* &head, int value, int Index , int &Length){
    if(Index == 0){
        InsertionAtBeginning(head, value , Length);
        return;
    }
    if(Index >Length || Index <0){
        cout<<"invalid index";
        return;
    }

    node* newnode = new node;
    newnode->data = value;
    int count = 0;

    node* current = head;
    while(current != nullptr && count <(Index -2)){
        current = current->next;
        count += 1;
    }
    node* temp = current->next;
    current->next = newnode;
    newnode->next = temp;

    Length +=1;
}

void InsertionAtEnd(node* &head , node* &first , int value){
    node* newnode = new node;
    newnode->data = value;
    newnode->next = nullptr;

    if(head ==  nullptr){
        head = newnode;
        first = newnode;
    }
    else{
        first->next = newnode;
        first = newnode;
    }
}

void DeleteFirstNode(node* &head , int &Length){
    node* temp = head;
    head = head->next;
    delete temp;
    Length -= 1;
}

void DeleteLastNode(node* &head ,int Index, int &Length){
    if(Index > Length || Index <0){
        cout<<"invalid index";
        return;
    }
    node* current = head;
    int count =0;
    while(current->next->next != nullptr && count <(Index-1) ){
        current = current->next;
        count += 1;
    }
    current->next = nullptr;
    Length -= Index;

    cout<<"\nDelete last node\n";
}

void printing(node* head){
    node* current = head;
    while(current != nullptr){
        cout<< current->data<< "->";
        current = current->next;
    }
    cout <<"None\n";
}

int main() {

    int num ,val;
    cout<<"Enter no. of elements to be inserted in linked list : ";
    cin >> num;

    node* head = nullptr;
    node* first = nullptr;

    for(int i = 0 ;i<num ;i++){
        cout<<"enter";
        cin>>val;

        InsertionAtEnd(head , first , val);
    }

    cout<<"\nLinked list\n";
    printing(head);

    // int insert;
    // cout<<"\nEnter value : ";
    // cin >> insert;

    // InsertionAtBeginning(head , insert , num);
    // cout<<"\nAdd at beggining\n";
    // printing(head);

    // int TargetIndex;
    // cout<<"enter index to enter value ";
    // cin>>TargetIndex;
    // InsertionAtSpecificIndex(head , insert , TargetIndex , num);
    // cout<<"\nAdd at "<<TargetIndex<<" in linked list\n";
    // printing(head);

    int Idx;
    cout<<"\nenter index to delete node : ";
    cin >>Idx;

    DeleteLastNode(head ,Idx, num);
    printing(head);

    DeleteFirstNode(head , num);
    cout<<"\nDelete first node\n";
    printing(head);
    

    return 0;
}
