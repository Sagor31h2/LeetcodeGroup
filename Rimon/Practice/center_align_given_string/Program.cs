using System;

namespace center_align_given_string
{
    class Program
    {
        static void Main(string[] args)
        {
            var s = "a\naa\naaa\naaaa\naaaaa\naaaaaa\naaaaaaa";
            var l = 0;
            foreach(char i in s){
                if(i == '\n'){
                    l = 0;
                    continue;
                }
                l+=1;
            }
            // l = l/2;
            var k = 0;
            while (l>=0){
                //print l number of space
                //print the line
                for(int i = 0; i<l; i++){
                    Console.Write(" ");
                }
                while(k<s.Length){
                    if(s[k] == '\n'){
                        k++;
                        Console.Write("\n");
                        break;
                    }
                    Console.Write(s[k]+" ");
                    k++;
                    
                }
                l--;
            }


            Console.WriteLine();
        }
    }
}
