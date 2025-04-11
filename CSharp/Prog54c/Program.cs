// See https://aka.ms/new-console-template for more information
Console.Write("Enter radius: ");
double rad = int.Parse(Console.ReadLine());

double area = Math.PI * Math.Pow(rad, 2);
double circumference = 2 * Math.PI * rad;

Console.WriteLine(Math.Round(area, 3));
Console.WriteLine(Math.Round(circumference, 3));

Console.ReadKey();
