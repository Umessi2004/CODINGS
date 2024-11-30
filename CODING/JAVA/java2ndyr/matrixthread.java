import java.util.Scanner;

class AddMatrix extends Thread{
    int arr1[][] = new int[3][3];
    int arr2[][] = new int[3][3];
    static int sum[][]=new int[3][3];
    int p;
    AddMatrix(int arr1[][],int arr2[][],int p)
    {
        this.arr1=arr1.clone();
        this.arr2=arr2.clone();
        this.p=p;
    }

    public void run()
    {
        for(int i=0;i<arr1[0].length;i++)
        {
            sum[p][i]=arr1[p][i]+arr2[p][i];
        }
    }
}

public class matrixthread{
    public static void main(String[] args) {
        int arr1[][]=new int[3][3];
        Scanner sc = new Scanner(System.in);
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                arr1[i][j]=sc.nextInt();
            }
        }
        int arr2[][]=new int[3][3];
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                arr2[i][j]=sc.nextInt();
            }
        }
        AddMatrix thread1=new AddMatrix(arr1,arr2,0);
        AddMatrix thread2=new AddMatrix(arr1,arr2,1);
        AddMatrix thread3=new AddMatrix(arr1,arr2,2);
        thread2.start();
        thread3.start();
        thread1.start();
        sc.close();
        try{
            Thread.sleep(1500);
        }
        catch(InterruptedException e){

        }
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                System.out.println(AddMatrix.sum[i][j]+"  ");
            }
            System.out.println("\n");
        }
    }
   
}
