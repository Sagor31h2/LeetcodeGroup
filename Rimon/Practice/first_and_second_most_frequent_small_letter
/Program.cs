// Find most frequent and second most frequent small letter from a given string

using System;
using System.Collections.Generic;
namespace first_and_second_most_frequent_small_letter
{
    class Program
    {
        static void Main(string[] args)
        {
            // var str = "Hello There I am Rimon";
            // var str = "abcdABCDabcdaaeeeeecd";
            var mp = new Dictionary<char,int>();
            foreach(Char i in str){
                if( i>= 'a' && i<='z'){
                    if(mp.ContainsKey(i)){
                        mp[i]+=1;
                    }
                    else
                        mp[i] = 1;
                }
            }
            mp['.'] = -1;
            Char a='.';
            Char b='.';
            foreach(Char i in mp.Keys){
                if (mp[i]>mp[a]){
                    b = a;
                    a = i;
                }
                else{
                    if (mp[i]>mp[b] && mp[i] != mp[a]){
                        b = i;
                    }
                }
            }
            Console.WriteLine(a);
            Console.WriteLine(b);
        }
    }
}
