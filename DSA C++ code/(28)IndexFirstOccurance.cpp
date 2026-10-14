#include<iostream>
#include<string>
using namespace std;
int FirstOccurance(string main , string sub){
    size_t pros = main.find(sub);  //it will check whether sub is present inside main
    if(pros != string::npos){  //npos means not found or no position
        return pros;
    }
    else{
        return -1;
    }
}

int main(){
    string haystack = "leetcode";
    string needle = "leet";

    int result = FirstOccurance(haystack , needle);
    cout<<result;
    
    return 0;
}