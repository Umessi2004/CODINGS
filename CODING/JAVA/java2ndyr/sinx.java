import java.util.*;

public class sinx {
    // public static void main(String[] args) {
    // Scanner n= new Scanner(System.in);
    // System.out.println("enter the degree: ");
    // double x= n.nextDouble();
    // x=x*(Math.PI/180.0);
    // double term=x, sum=term;
    // int i=1;
    // while(i<100){
    // term = -(term * x * x) / (2 * i * (2 * i + 1));
    // sum+=term;
    // i++;
    // }
    // System.out.println("sin(x): "+sum);
    // }
    public static void main(String[] args) {
        Scanner n = new Scanner(System.in);
        System.out.println("Enter the degree: ");
        double degree = n.nextDouble();
        double x = degree * (Math.PI / 180.0);
        double term = x;
        double sum = term;
        double threshold = 1e-15; 
        int i = 1;
        while (Math.abs(term) > threshold) {
            term = -(term * x * x) / (2 * i * (2 * i + 1));
            sum += term;
            i++;
        }
        System.out.println("sin(" + degree + "°) using Taylor series: " + sum);
        System.out.println("sin(" + degree + "°) using Math.sin: " + Math.sin(x));
        n.close();
    }
}
