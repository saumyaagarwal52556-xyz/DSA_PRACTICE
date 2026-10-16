#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;


vector<int> TwoSum(int size , int arr[] ,int target){
    unordered_map<int , int>seen;
    for(int a=0 ;a<size;a++){
        int num2 = target - arr[a];

        if(seen.count(num2)){
            return {seen[num2] , a};
        }
        seen[arr[a]] = a;
    }
    return {};
}

int main(){
    int arr[]={3,2,4};
    int size = 3;
    int target = 6;
    vector<int>result;
    result = TwoSum(size ,arr,target);
    for(int val:result){
        cout<<val<<" ";
    }

    return 0;
}

