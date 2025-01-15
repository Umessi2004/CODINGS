class Goods{
    int value;
    boolean canProduce= true;
    synchronized void put(int data){
        if(!canProduce){
            try {
                wait();
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
        value=data;
        System.out.println("put: "+value);
        canProduce=false;
        notify();
    }
    synchronized void get(){
        if(canProduce){
            try{
                wait();
            }catch(InterruptedException e){
                System.out.println(e.getMessage());
            }
        }
        System.out.println("got: "+value);
        canProduce=true;
        notify();
    }
}
class Producer extends Thread{
    Goods g;
    Producer(Goods g){
        this.g=g;//copy constructor
    }
    @Override
    public void run() {
        int value=1;
        while (true) { 
            g.put(value++);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
            }
        }
    }
}
class Consumer extends Thread{
    Goods g;
    Consumer(Goods g){
        this.g=g;//copy constructor
    }
    @Override
    public void run() {
        while (true) { 
            g.get();
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
            }
        }
    }
}
public class producerconsumer{
    public static void main(String[] args) {
        Goods g= new Goods();
        Producer p = new  Producer(g);
        Consumer c = new  Consumer(g);
        p.start();
        c.start();
    }
}