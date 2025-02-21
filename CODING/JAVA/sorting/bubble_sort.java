import java.util.*;
public class bubble_sort{
    public static void main(String a[]){
        int n=100;
        int[] arr= generateRandomArray(n);
        
        long starttime=System.nanoTime();
        bubblesort(arr);
        long endtime=System.nanoTime();
        
        long elapsedtime=endtime-starttime;
        
        disp_arr(arr);
        
        System.out.println("time taken for bubble sort is: "+elapsedtime+"nanosecond");
    }
    static void bubblesort(int [] arr){
        int temp;
        boolean swapped= false;
        for (int i=0; i<arr.length-1; i++){
            for (int j=0; j<arr.length-i-1; j++){
                if(arr[j]>arr[j+1]){
                    temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
                swapped=true;
            }
            if(!swapped){
                break; //it breaks the loop because the array is already sorted and no need to iterate//
            }
        }
        
    }
    static void disp_arr(int [] arr){
        for (int i=0; i<arr.length; i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
    //this function generates random number
    static int[] generateRandomArray(int size){
        int[] arr= new int[size];
        Random rand= new Random();
        for (int i=0; i<size; i++){
            arr[i]=rand.nextInt(10000);
        }
        return arr;
    }
}