#include<iostream>
#include<algorithm>
using namespace std;

int MostWter(int size , int arr[]){

    int maxi =0;
    int left = 0;
    int right = size -1;
    while(left<right){
        int width = right - left;
        int height = min(arr[left] , arr[right]);

        maxi =max(maxi, width * height);
        if(arr[left] < arr[right]){
            left +=1;
        }
        else{
            right -=1;
        }
    }
    return maxi;
}

int main(){
    int size = 9;

    int arr[]={1,8,6,2,5,4,8,3,7};
    int result = MostWter(size , arr);
    cout<<result;
    return 0;
}