import java.awt.*;
import java.awt.event.*;

class Awt extends Frame implements ActionListener {
    Button b1, b2, b3, b4, b5, b6;
    Label l1, l2, l3;
    TextField t1, t2, t3;
    int resultout;

    Awt() {
        setSize(600, 600);
        setLayout(null);
        setVisible(true);
        l1 = new Label("1st number");
        l2 = new Label("2nd number");
        l3 = new Label("RESULT");

        l1.setBounds(200, 80, 90, 30);
        l2.setBounds(200, 150, 90, 30);
        l3.setBounds(200, 280, 90, 30);

        t1 = new TextField();
        t2 = new TextField();
        t3 = new TextField();

        t1.setBounds(300, 80, 90, 30);
        t2.setBounds(300, 150, 90, 30);
        t3.setBounds(300, 280, 90, 30);

        b1 = new Button("fact1");
        b2 = new Button("sum");
        b3 = new Button("mul");
        b4 = new Button("count");
        b5 = new Button("reset");
        b6 = new Button("red");
        
        b1.setBounds(35, 400, 50, 30);
        b2.setBounds(155, 400, 50, 30);
        b3.setBounds(275, 400, 50, 30);
        b4.setBounds(395, 400, 50, 30);
        b5.setBounds(515, 400, 50, 30);
        b6.setBounds(515, 480, 50, 30);

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
        add(b5);
        add(b6);

        b1.addActionListener(this);
        b2.addActionListener(this);
        b3.addActionListener(this);
        b4.addActionListener(this);
        b5.addActionListener(this);
        b6.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e) {
        String s1 = t1.getText();
        String s2 = t2.getText();
        int n1 = Integer.parseInt(s1);
        int n2 = Integer.parseInt(s2);
        String res;
        if (e.getSource() == b1) {
            if (s1.isEmpty()) {
                // t1.setText("enter 1st num");
                System.out.println("enter number");
            } else {
                int fact = 1;
                n1 = Integer.parseInt(s1);
                try {
                    if (n1 < 1) {
                        throw new NumberFormatException();
                    }
                } catch (NumberFormatException ex) {
                    System.out.println("invalid number" + ex.getMessage());
                }
                for (int i = 1; i <= n1; i++) {
                    fact *= i;
                }
                resultout = fact;

            }
        }
        if (e.getSource() == b2) {
            if (s1.isEmpty()) {
                // t1.setText("enter 1st num");
                System.out.println("enter number");
            }
            if (s2.isEmpty()) {
                // t1.setText("enter 1st num");
                System.out.println("enter number");
            }
            resultout = n1 + n2;
        }
        if (e.getSource() == b3) {
            resultout = n1 * n2;
        }
        if (e.getSource() == b4) {
            resultout++;
        }
        if (e.getSource() == b5) {
            resultout = 0;
        }
        if(e.getSource()==b6){
            if(getBackground().equals(Color.white)){
                setBackground(Color.red);
            }
            else{
                setBackground(Color.white);

            }

        }
        res = String.valueOf(resultout);
        t3.setText(res);
    }

}

public class AwtExample {
    public static void main(String A[]) {
        new Awt();
    }
}
