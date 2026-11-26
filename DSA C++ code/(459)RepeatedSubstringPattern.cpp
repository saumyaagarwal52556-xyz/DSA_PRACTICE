#include<iostream>
#include<string>

using namespace std;

bool RepeatedPattern(string str){
    string temp = str + str;
    temp = temp.substr(1 , temp.length()-2);
    if(temp.find(str) != string::npos){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    string str="abcabc";
    bool result = RepeatedPattern(str);
    cout<<boolalpha<<result;
    return 0;
}