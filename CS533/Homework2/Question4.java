import java.util.Scanner;
//A.16 Pg 449
public class Question4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the radius of your circle: ");
        double radius = input.nextDouble();
        
        System.out.printf("\nCircle's Diameter: %.2f", 2 * radius);
        System.out.printf("\nCircle's Circumference: %.2f", Math.PI * 2 * radius);
        System.out.printf("\nCircle's Area: %.2f", Math.PI * Math.pow(radius, 2));

        input.close();
    }
}