using System;

namespace _1_1_IsUnique
{
    class Program
    {
        static void Main(string[] args)
        {
            int c = 0;
            var s = "strings";
            foreach(Char i in s){
                int d = i - 'a';
                // Console.WriteLine(d);
                if( (c & 1<<d) > 0){
                    Console.WriteLine("False");
                    c = -1;
                    break;
                }
                c |= 1<<d;
            }
            if(c!=-1)
                Console.WriteLine("True");
        }
    }
}
