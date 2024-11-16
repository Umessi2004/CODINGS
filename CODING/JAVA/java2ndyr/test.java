class demo {
    static int a = 10;
}

public class test {
    public static void main(String args[]) {
        demo d1 = new demo();
        demo d2 = new demo();
        d1.a = 20;
        System.out.println(d2.a);
    }
}
