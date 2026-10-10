#include<iostream>
using namespace std;

int BuySell(int size,int arr[]){
    int max = 0 ,min =arr[0];
    for(int i=0;i<size ; i++){
        
        if(min >arr[i] ){
            min = arr[i];
        }
        int curr = arr[i] - min;
        if(max < curr){
            max = curr;
        }
    }
    return max;
}

int main(){
    int arr[]={7,6,4,3,1};
    int size = sizeof(arr)/sizeof(arr[0]);
    int result = BuySell(size,arr);
    cout<<result;

    return 0;
}