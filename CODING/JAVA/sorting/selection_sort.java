import java.util.Random;

public class selection_sort {
    public static void main(String a[]) {
        int n = 100;
        int[] arr = generateRandomArray(n);

        long starttime = System.nanoTime();
        selectionsort(arr);
        long endtime = System.nanoTime();

        long elapsedtime = endtime - starttime;

        disp_arr(arr);

        System.out.println("time taken for selection sort is: " + elapsedtime + "nanosecond");
    }

    static void selectionsort(int[] arr) {
        int min, temp;
        for (int i = 0; i < arr.length-1; i++) {
            min = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[min]) {
                    min = j;
                }
            }
            temp = arr[min];
            arr[min] = arr[i];
            arr[i] = temp;
        }
    }

    static void disp_arr(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    static int[] generateRandomArray(int size) {
        int[] arr = new int[size];
        Random rand = new Random();
        for (int i = 0; i < size; i++) {
            arr[i] = rand.nextInt(10000);
        }
        return arr;
    }
}
