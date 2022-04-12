//Reverse Each Word in a String

using System;
using System.Text;
using System.Collections;
namespace temp
{
    class Program
    {
        static void Main(string[] args)
        {
            String s = "Reverse Each Word in a String";
            // Console.WriteLine(s);
            // var st = new  List<string> ();
            var st = new Stack() ;
            var builder = new StringBuilder();
            for(int i = 0; i<s.Length; i++ ){
                if(s[i] == ' '){
                    while(st.Count>0){
                        var t = st.Pop();
                        builder.Append(t);
                    }
                    builder.Append(' ');
                }
                else 
                    st.Push(s[i]);
            } 

            while(st.Count>0){
                builder.Append(st.Pop());
            }
            s = builder.ToString();
            Console.WriteLine(s);
        }
    }
}
