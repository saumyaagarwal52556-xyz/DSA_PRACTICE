#include <iostream>
using namespace std;

int count(int num , int &cnt){
    if(num ==0){
        return cnt;
    }
    cnt++;
    return count( num /10 , cnt);
}

int main(){
    int cont =0 ,num =123456789;
    int result = count(num , cont);

    cout<<result;
    return 0;
}



class Solution {
  public:
    int countDigits(int n) {
        // Code here
        if(n<0){
            n=-n;
        }
        if(n <10){
            return 1;
        }
        
        return 1+countDigits(n /10);
    }
};