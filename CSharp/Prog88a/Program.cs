Console.Write("Enter num1: ");
int num1 = int.Parse(Console.ReadLine());
Console.Write("Enter num2: ");
int num2 = int.Parse(Console.ReadLine());

int sum = num1 + num2;
int dif = num1 - num2;
int prd = num1 * num2;
double ave = (double)sum / 2.0;
int abs = Math.Abs(dif);
// Math.Max and Math.Min
int max = 0;
int min = 0;

if (num1 > num2)
{
    max = num1;
}
else
{
    max = num2;
}

if (num1 <= num2)
{
    min = num1;
}
else
{
    min = num2;
}

Console.WriteLine("Sum: " + sum);
Console.WriteLine("Difference: " + dif);
Console.WriteLine("Product: " + prd);
Console.WriteLine("Average: " + ave);
Console.WriteLine("Absolute Value: " + abs);
Console.WriteLine("Max: " + max);
Console.WriteLine("Min: " + min);
