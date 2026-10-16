#include <iostream>
#include <string>
using namespace std;

int lengthOfLastWord(string s)
{
    int max = 0;
    int count = 0;

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] != ' ')
        {
            count += 1;
            max = count;
        }
        else if (s[i] == ' ' && i < (s.length()))
        {
            count = 0;
        }
    }
    return max;
}

int main(){
    string str="Hello world";
    int result = lengthOfLastWord(str);
    cout<<result;

    return 0;
}