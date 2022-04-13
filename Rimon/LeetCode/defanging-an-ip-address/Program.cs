// Leetcode https://leetcode.com/problems/defanging-an-ip-address/
using System;
using System.Text;
namespace defanging_an_ip_address
{
    class Program
    {
        static void Main(string[] args)
        {
            var builder = new StringBuilder();
            var s = "128.256.10.5";
            foreach(Char i in s){
                if(i == '.'){
                    builder.Append("[.]");
                }
                else
                    builder.Append(i);
            }
            s = builder.ToString();
            Console.WriteLine(s);
        }
    }
}
