using System;

namespace multiple_of_3
{
    class Program
    {
        static void Main(string[] args)
        {
            var a = 200;
            var b = -3;
            var k = a - a%3 ;
            while (k>=b){
                if(k!=0)
                    Console.WriteLine(k);
                k -=3;
            }
        }
    }
}
