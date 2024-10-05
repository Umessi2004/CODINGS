import java.util.Scanner;

class define {
    int row, col;
    int[][] arr;

    // input method
    void inputelements() {
        try (Scanner sc = new Scanner(System.in);) {
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < col; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }
            // sc.close();
        }
    }

    // display method
    void display() {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}

public class array {
    public static void main(String[] args) {
        // array object is created
        define arr1 = new define();
        try (Scanner sc = new Scanner(System.in)) {

            // input of the array r and c from the object
            System.out.println("enter the no. of rows: ");
            arr1.row = sc.nextInt();
            System.out.println("enter the no. of cols: ");
            arr1.col = sc.nextInt();

            // initialization of the array bu the arr1 object
            arr1.arr = new int[arr1.row][arr1.col];

            // calling the input method function
            System.out.println("enter the elements: ");
            arr1.inputelements();

            // calling the display function
            arr1.display();
        }
    }
}
