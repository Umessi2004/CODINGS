class Thread1 extends Thread{
    int num;
    Thread1(int x){
        num=x;
    }
    @Override
    public void run() {
        if(num%2==0){
            System.out.println("the number is even");
        }
        else{
            System.out.println("the number is odd");
        }
    }
}
class Thread2 extends Thread{
    int num;
    Thread2(int num){
        this.num=num;
    }
    @Override
    public void run() {
        int i;
        for (i=2; i<num/2; i++){
            if(num%i==0){
                System.out.println("the number is composite");
                break;
            }
        }
        if (i==num/2) {
            System.out.println("the number is prime");
        }
    }
}
public class thread12 {
    public static void main(String[] args) {
        Thread1 t1= new Thread1(17);
        Thread2 t2= new Thread2(17);
        t1.start();
        try {
            t1.wait(1000);
        } catch (InterruptedException e) {
        }
        t2.start();
    }
}
