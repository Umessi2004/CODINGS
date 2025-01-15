import java.util.*;
class Myexception extends Exception{
    Myexception(String message){
        super(message);
    }
}
public class bankbalance{
    String Name;
    int accno;
    double balance;
    bankbalance(String Name, int accno, double balance){
        this.Name=Name;
        this.accno=accno;
        this.balance=balance;
    }
    void withdraw(double b){
        if(!checkbalance()){
            try {
                throw new Myexception("balance is insufficient");
            } catch (Myexception e) {
                System.out.println(" "+e.getMessage());
            }
        }
        else{
            balance=balance-b;
        }
    }
    void deposit(double b){
        balance=balance+b;

    }
    boolean checkbalance(){
        return balance<=500;
    }
    void printbalance(){
        System.out.println("acc balance: "+balance);
        System.out.println("accno: "+accno);
        System.out.println("Name: "+Name);
    }
    public static void main(String[] args) {
        String n;
        int accn;
        double balance;
        Scanner sc= new Scanner(System.in);
        System.out.println("enter your name:");
        n=sc.nextLine();
        System.out.println("enter your accno:");
        accn=sc.nextInt();
        System.out.println("enter your balance:");
        balance=sc.nextDouble();
        bankbalance canarabank=new bankbalance(n,accn,balance);
        System.out.println("enter the amount you want to deposit or withdraw");
        double b= sc.nextDouble();
        System.out.println("DO YOU WANT TO DEPOSIT OR WITHDRAW?{deposit/withdraw}]");
        String x= sc.nextLine();
        if(x.equals("deposit")){
            canarabank.deposit(b);
        }
        else if (x.equals("withdraw")){
            canarabank.withdraw(b);
        }
        canarabank.printbalance();
    }
}

