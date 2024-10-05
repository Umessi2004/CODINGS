import java.util.Scanner;

class driverscalar {
    int sizeA;
    int sizeB;
    int[] vectorA, vectorB;

    void input(int[] vectorA, Scanner sc) {
        for (int i = 0; i < vectorA.length; i++) {
            vectorA[i] = sc.nextInt();
        }
    }

    int scalarprod(int[] A, int[] B) {
        int product = 0;
        for (int i = 0; i < A.length; i++) {
            product += (A[i] * B[i]);
        }
        return product;
    }

    void display(int p) {
        System.out.println("the scalar product is: " + p);
    }
}

public class scalarproduct {
    public static void main(String[] args) {
        driverscalar vector = new driverscalar();
        try (Scanner s = new Scanner(System.in)) {
            System.out.println("enter the size of 1st vector: ");
            vector.sizeA = s.nextInt();
            System.out.println("enter the size of 2nd vector: ");
            vector.sizeB = s.nextInt();
        // initializing the array
        vector.vectorA = new int[vector.sizeA];
        vector.vectorB = new int[vector.sizeB];

        //scanner ob is taken as parameter coz individual input sc object in input method closes
        //at first call and system.in is not available for next call
        
        // inputting the 2 vectors
        System.out.println("enter the elements of vectorA: ");
        vector.input(vector.vectorA, s);
        System.out.println("enter the elements of vectorB: ");
        vector.input(vector.vectorB, s);

        // doing the scalar product
        int product = vector.scalarprod(vector.vectorA, vector.vectorB);
        vector.display(product);
        }
    }
}
