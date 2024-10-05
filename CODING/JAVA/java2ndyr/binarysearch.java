import java.util.*;

class search {
    int size;
    int[] arr;
    int x;

    void input(Scanner sc) {
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
    }

    boolean issorted(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < arr[i - 1]) {
                return true;
            }
        }
        return false;
    }

    void sorting(int[] a) {
        Arrays.sort(a);
    }
    void display(int[] arr){
        for(int i=0; i<arr.length; i++){
            System.out.print(arr[i]+" ");
        }
    }

    void binary_search(int x) {
        if (issorted(arr)) {
            System.out.println("array is not sorted, let me sort for you...");
            sorting(arr);
            display(arr);
            System.out.println();
        }
        int l = 0;
        int h = arr.length - 1;
        while (l <= h) {
            int mid = (l + h) / 2;
            if (arr[mid] == x) {
                System.out.println("element found at index: " + mid);
                return;
            } else if (arr[mid] > x) {
                h = mid - 1;
            } else if (arr[mid] < x) {
                l = mid+1;
            }
        }
        System.out.println("ele not found");
    }
}

public class binarysearch {
    static search var = new search();

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("enter the size of the array: ");
            var.size = sc.nextInt();

            // initializing the array
            var.arr = new int[var.size];

            // inputting the elements
            System.out.println("enter the elements: ");
            var.input(sc);

            System.out.print("enter the element you want to search: ");
            var.x = sc.nextInt();

            // calling the methods to perform search
            var.binary_search(var.x);
        }
    }

}
