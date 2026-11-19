#include<iostream>
#include<vector>
using namespace std;

void merge(vector<int> &arr1 , vector<int> &arr2){
    int m = arr1.size() - arr2.size();
    int n = arr2.size();

    while(n>0){

        if(m>0 && arr1[m-1] > arr2[n-1]){
            arr1[m+n-1] = arr1[m-1];
            m -=1;
        }
        else{
            arr1[m+n-1] = arr2[n-1];
            n -=1;
        }
    }
}

int main(){

    vector<int>arr1;
    vector<int>arr2;
    arr1={1,2,3,0,0,0};
    arr2={2,5,6};

    merge(arr1,arr2);

    for(int i=0 ; i<arr1.size() ;i++){
        cout<<arr1[i] <<" ";
    }

    return 0;
}