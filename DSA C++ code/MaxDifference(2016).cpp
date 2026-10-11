#include<iostream>
using namespace std;

int maxDif(int size, int arr[]){
    int max = -1;
    int mini = arr[0];
    for(int i = 0; i<size ; i++){
        if(mini > arr[i]){ 
            mini = arr[i];
        }
        int dif = arr[i] - mini;
        if(max < dif && dif >0){
            max = dif;
        }
    }
    
    return max;
}

int main(){
    int size = 4;
    int arr[]={9,4,3,2};
    int result = maxDif(size,arr);
    cout<<result;
    return 0;
}