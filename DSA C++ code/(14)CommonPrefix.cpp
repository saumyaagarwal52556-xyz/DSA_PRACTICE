#include<iostream>
#include<string>
#include<vector>
using namespace std;

string CommonPrefix(const vector<string>& strs){
    if(strs.empty()) return "";

    string result = strs[0];
    for(int i=1;i<strs.size() ; i++){
        // here strs[i] acts as main and we are finding does result is present in main at index 0 if not reduce the result
        cout<<strs[i].find(result)<<" "<<i<<"\n";
        while (strs[i].find(result) != 0){
            result = result.substr(0, result.length() -1 );  //remove the last letter
        }
    }
    return result;
}

int main(){
    vector<string> strs={"flower","flow","flight"};
    string output = CommonPrefix(strs);
    cout<<output;
    return 0;
}