import java.awt.*;
import java.awt.event.*;
class AEvent extends Frame implements ActionListener
{
    int num3;
    Button b1,b2,b3,b4;
    Label l1,l2,l3,l4;
    TextField t1,t2,t3,t4;
    AEvent()
    {
        setSize(600,600);
        setLayout(null);
        setVisible(true);

        l1=new Label("number");
        l1.setBounds(50,50,90,30);
        t1=new TextField();
        t1.setBounds(170,50,90,30);


        l2=new Label("number");
        l2.setBounds(50,80,90,30);
        t2=new TextField();
        t2.setBounds(170,80,90,30);

        l3=new Label("result");
        l3.setBounds(50,150,90,30);
        t3=new TextField();
        t3.setBounds(170,150,90,30);

        b1=new Button("sum");
        b1.setBounds(50,300,50,50);

        b2=new Button("mul");
        b2.setBounds(180,300,50,50);

        b3=new Button("count");
        b3.setBounds(250,300,50,50);

        b4=new Button("reset");
        b4.setBounds(350,300,50,50);

        add(l1);
        add(l2);
        add(t1);
        add(t2);
        add(t3);
        add(l3);
        add(b1);
        add(b2);
        add(b3);
        add(b4);

        b1.addActionListener(this);
        b2.addActionListener(this);
        b3.addActionListener(this);
        b4.addActionListener(this);

    }
    public void actionPerformed(ActionEvent e)
    {
        // int num;
        // String s1=t1.getText();
        // if(s1.isEmpty())
        // {
        //     System.out.println("enetr the number ");
        // }
        // else
        // {
            
        //     int fact=1;
            
        //     try {
        //         num = Integer.parseInt(s1);  // Convert input to an integer
        //     } catch (NumberFormatException ex) {
        //         System.out.println("Invalid number entered. Please enter a valid integer.");
        //         return; 
        //     }
        //     for(int i=1;i<=num;i++)
        //     {
        //        fact=fact*i;
        //     }
            
        //     String result=String.valueOf(fact);
        //     t2.setText(result);
        // }
        int num1,num2;
        String result,count;
        String s1=t1.getText();
        String s2=t2.getText();

        num1=Integer.parseInt(s1);
        num2=Integer.parseInt(s2);
        if(e.getSource()==b1)
        {
            num3=num1+num2;

        }
        if(e.getSource()==b2)
        {
            num3=num1*num2;

        }
        if(e.getSource()==b3)
        {
            num3++;


        }
        if(e.getSource()==b4)
        {
            num3=0;

        }

        result=String.valueOf(num3);
        t3.setText(result);

    }


}

public class factorial
{
    public static void main(String args[])
    {
        new AEvent();
    }
}