using System;

namespace MyCalculator
{
    class Program
    {
        private const double min_value= -1000;
        private const double max_value= 1000;
       
        static void Main(string[] args)
        {
            double first = 0;
            double second = 0;
            double result = 0;
            int n;
            bool check = true;

            Console.WriteLine("---Calculator---");

            Console.Write("Enter first value\n");
            first = double.Parse(Console.ReadLine());
            if(first<min_value|| first>max_value)
            {
                Console.WriteLine("Input {0} not within {1} and {2} ERROR",first, min_value, max_value);
                check = false;
            }

            if(check)
            {
                Console.Write("Enter second value\n");
                second = double.Parse(Console.ReadLine());
            }
            
            if (second < min_value || second > max_value)
            {
                Console.WriteLine("Input {0} not within {1} and {2} ERROR",second, min_value, max_value);
                check = false;
            }
            
            if(check)
            {
                Console.WriteLine("Choose operator\n");
                Console.WriteLine("1:ADD 2: SUBTRACT 3:MULTIPLY 4:DIVIDE\n");
                n = int.Parse(Console.ReadLine());
                switch(n)
                {
                    case 1:
                        result = first + second;
                        Console.WriteLine("Answer is  " + result);
                        break;
                    case 2:
                        result = first - second;
                        Console.WriteLine("Answer is  " + result);
                        break;
                    case 3:
                        result = first * second;
                        Console.WriteLine("Answer is  " + result);
                        break;
                    case 4:
                        result = first / second;
                        Console.WriteLine("Answer is  " + result);
                        break;
                    default: 
                        Console.WriteLine("Invalid Input!");
                        break;


                }
                
            }
            
            
            Console.WriteLine("Press Enter key to terminate");
            Console.ReadLine();

        }
    }
}
