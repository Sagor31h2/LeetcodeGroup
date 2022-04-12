using System;

namespace Practice
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] l = {3,34,5,4,56,7,67,45,34,67,2,2,2};
            var a = 0;
            var b = 0;
            foreach (int i in l){
                if(i>a){
                    b = a;
                    a = i;
                }
                else
                    if(i>b && i!=a)
                        b = i; 
            }
            Console.Write("{0},{1}\n ",a,b);
        }
    }
}
