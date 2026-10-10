// #include<iostream>
// #include<vector>
// using namespace std;

// int sumArray(int size,const vector<int> &arr){
//     if(size <=0){
//         return 0;
//     }
//     return arr[size -1]+sumArray(size-1 , arr);
// }

// int main(){
//     vector<int> arr;
//     int size ,val;
//     cout<<"Enter size : ";
//     cin>>size;
//     for(int i=0;i<size;i++){
//         cout<<"Enter : ";
//         cin>>val;
//         arr.push_back(val);
//     }
//     int result = sumArray(size, arr);
//     cout<<"\n"<<result;

//     return 0;
// }

// #include<iostream>
// using namespace std;

// int fact(int num){
//     if(num<=0){
//         return 1;
//     }
//     return num*fact(num-1);
// }

// int main(){
//     int num;
//     cout<<"Enter :";
//     cin>>num;
//     int result = fact(num);
//     cout<<result;

//     return 0;
// }

// #include<iostream>
// using namespace std;

// int fibonn(int num){
//     if(num ==0){
//         return 0;
//     }
//     else if(num ==1){
//         return 1;
//     }
//     return fibonn(num-1) + fibonn(num-2);

// }
// // 0 1 1 2 3 5 8
// int main(){

//     int result = fibonn(6);
//     cout<<result; 

//     return 0;
// }

// #include<iostream>
// using namespace std;

// int sumDigit(int num){
//     if(num <=0){
//         return 0;
//     }
//     return (num%10)+sumDigit(num/10);
// }

// int main(){
    
//     int num = 123456789;
//     int result = sumDigit(num);
//     cout<<result; 

//     return 0;
// }


// #include<iostream>
// #include<vector>
// using namespace std;

// void MaxMin( int indx ,const vector<int> &arr ,int &max,int &min){
//     if(indx == arr.size()){
//         return ;
//     }
//     if(max < arr[indx] && indx <arr.size()){
//         max = arr[indx];
//     }
//     if(min > arr[indx] && indx<arr.size()){
//         min = arr[indx];
//     }
//     MaxMin(indx+1 , arr , max , min);
// }

// int main(){

//     vector<int>arr;
//     int size,val;
//     cout<<"Enter size : ";
//     cin >>size;

//     for(int i=0;i<size;i++){
//         cout<<"enter : ";
//         cin>> val;
//         arr.push_back(val);
//     }
    
//     int max = arr[0];
//     int min = arr[0];
//     MaxMin(0 , arr , max, min); 
//     cout<<"max "<<max;
//     cout<<"\nmin "<<min;

//     return 0;
// }

// #include<iostream>
// #include<algorithm>
// #include<string>
// using namespace std;

// void Reverse(string &s , int size , int indx){
//     if(indx == (size)/2 ){
//         return;
//     }
    
//     swap(s[indx] , s[size-indx-1]);
//     Reverse(s , size , indx +1);
    
// }

// int main(){
//     string s="qwertyui";
//     int size = s.length();
//     int indx = 0;
//     Reverse( s , size , indx);
//     cout<<s;

//     return 0;
// }

// #include<iostream>
// using namespace std;

// int Power(int num , int pow){
//     if(pow <=0){
//         return 1;
//     }
//     return num * Power(num , pow -1);
// }

// int main(){
//     int num = 2;
//     int pow = 5;
//     int result = Power(num ,pow);
//     cout<<result;
//     return 0;
// }

// #include<iostream>
// #include<string>
// using namespace std;

// bool Palindrome(string s, int indx ,int size){
//     if(indx > size/2){
//         return true;
//     }
//     if(s[indx] != s[size-indx-1]  && indx<= (size)/2){
//         return false;
//     }
//     return Palindrome(s , indx +1 , size);
// }

// int main(){
//     string s ="abcdecba";
//     int indx =0;
//     int size = s.length();
//     bool result = Palindrome(s, indx, size );
//     cout<<boolalpha<< result; 
//     return 0;
// }