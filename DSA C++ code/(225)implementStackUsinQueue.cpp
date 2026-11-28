#include<iostream>
#include <queue>
using namespace std;
class MyStack {
public:
    queue<int>main;
    queue<int>helper;

    MyStack() {
        
    }
    
    void push(int x) {
        while(!main.empty()){
            helper.push(main.front());
            main.pop();
        }
        main.push(x);

        while(!helper.empty()){
            main.push(helper.front());
            helper.pop();
        }
    }
    
    int pop() {
        int ans = main.front();
        main.pop();
        return ans;
    }
    
    int top() {
        return main.front();
    }
    
    bool empty() {
        return main.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */