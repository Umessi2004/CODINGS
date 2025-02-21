import java.util.Random;

public class QuickSort {
    public static void main(String[] args) {
        int n = 1000;
        int[] arr = generateRandomArray(n);

        long starttime = System.nanoTime();
        //int arr[]={9,8,7,6,5,4,3,2,1};
        quicksort(arr, 0, arr.length-1);
        long endtime = System.nanoTime();

        long elapsedtime = endtime - starttime;

        disp_arr(arr);

        System.out.println("Time taken for Quick Sort: " + elapsedtime + " nanoseconds");
    }

    public static void quicksort(int arr[], int low, int high) {
        if (low < high) {
            int pivotIndex = partition2(arr, low, high);
            quicksort(arr, low, pivotIndex - 1); // Left part
            quicksort(arr, pivotIndex + 1, high); // Right part
        }
    }

    public static void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static int partition1(int arr[], int low, int high) {
        //this partition algo is not working properly
        int mid = (low + high) / 2;  // Choosing the middle element as pivot
        int pivot = arr[mid];
    
        int i = low, j = high;
    
        while (i <= j) {
            while (arr[i] < pivot) { // Find an element on left greater than pivot
                i++;
            }
            while (arr[j] > pivot) { // Find an element on right smaller than pivot
                j--;
            }
            if (i <= j) {  // Swap elements that are out of place
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
            i++;
            j--;
        }
        return i;  // Return correct partition index
    }
    
    public static int partition2(int arr[], int low, int high) {
        int pivot = arr[high];  // Choose the rightmost element as pivot
        int i = low - 1;        // Index of smaller element

        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {  // If current element is smaller than or equal to pivot
                i++;
                swap(arr, i, j);    // Swap it to correct position
            }
        }
        swap(arr, i + 1, high);  // Move pivot to its correct position
        return i + 1;  // Return index of pivot
    }
    static int[] generateRandomArray(int size) {
        int[] arr = new int[size];
        Random rand = new Random();
        for (int i = 0; i < size; i++) {
            arr[i] = rand.nextInt(10000);
        }
        return arr;
    }

    static void disp_arr(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
