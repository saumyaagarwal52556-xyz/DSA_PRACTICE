#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

bool Duplicate( int size ,const vector<int> &arr ){
    unordered_map<int,int>freq;
    for(int i=0;i<size;i++){
        freq[arr[i]] ++;
        if(freq.at(arr[i]) >=2){
            return true;
        }    
    }
    return false;
}

int main(){
    vector<int> arr;
    int size ,val;
    cout<<"enter size : ";
    cin>>size;

    for(int i=0;i<size;i++){
        cout<<"Enter: ";
        cin>>val;
        arr.push_back(val);
    }

    bool result = Duplicate(size, arr);
    cout<<boolalpha<<result;
    return 0;
}

