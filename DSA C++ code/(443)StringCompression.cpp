#include<iostream>
#include<vector>
#include<string>
using namespace std;

int CompressString(vector<char> &arr){
    int read = 0;
    int write = 0;

    while(read < arr.size()){
        char current = arr[read];
        int count = 0;

        while(read < arr.size() && arr[read] == current){
            read += 1;
            count += 1;
        }
        arr[write] = current;
        write += 1;
        
        if(count > 1){
            string temp = to_string(count);
            for(char digit : temp){
                arr[write] = {digit};
                write += 1;
           }
        }
    }
    arr.resize(write);
    for(int i=0 ; i<arr.size() ;i++){
        cout<<arr[i] <<" ";
    }
    return arr.size();
}

int main(){
    vector<char> arr;
    arr = {'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'};
    int result = CompressString(arr);
    cout<<"\n"<<result;

    return 0;
}