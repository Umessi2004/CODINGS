import java.util.*;
class Mythread extends Thread{
    static int sum;
    int not;
    int flag;
    Mythread(int flag,int not){
        this.not=not;
        this.flag=flag;
    }
    int[] a1={1,2,3,4,5,6};
    int[] a2={1,2,3,4,5,6};
    @Override
    public void run() {
        int lb=a1.length/not*flag;
        int ub=lb+ a1.length/not-1;
        for (int i=lb; i<=ub; i++){
            sum=sum+(a1[i]*a2[i]);
        }
    }
}
public class scalarproduct {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.print("enter the no of threads: ");
        int not=sc.nextInt();
        Mythread[] t=new Mythread[not];
        for (int i=0; i<not; i++){
            t[i]=new Mythread(i,not);
            t[i].start();
        }
        try {
            for(int i=0; i<not; i++){
                t[i].join();
            }
        } catch (Exception e) {
        }
        System.out.println("sum:"+Mythread.sum);
    }
}
