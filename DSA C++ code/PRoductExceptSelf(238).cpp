#include<iostream>
#include<vector>
using namespace std;

vector<int> ProductExptSelf(int size ,const vector<int> arr){
    vector<int>pro(size,1);
    int prefix =1,suffix = 1;

    for(int i=0;i<size ;i++){
        pro[i] = prefix;
        prefix *= arr[i];
    }
    for(int i=size-1;i >=0;i--){
        pro[i] *= suffix;
        suffix *= arr[i];
    }
    return pro;
}

int main(){
    vector<int>arr;
    int size,val;
    cout<<"Enter size: ";
    cin>>size;
    for(int i=0 ; i<size;i++){
        cout<<"enter: ";
        cin>>val;
        arr.push_back(val);
    }
    vector<int>result;
    result = ProductExptSelf(size,arr);
    for(int i=0;i<result.size();i++){
        cout<<result[i]<<" ";
    }
    return 0;
}