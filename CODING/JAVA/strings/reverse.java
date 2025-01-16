public class reverse {
    public static void main(String[] args) {
        String s="UMESH";
        String n="";
        for (int i=s.length()-1; i>=0; i--){
            char c=s.charAt(i);
            String ch=Character.toString(c);
            n=n.concat(ch);
        }     
        System.out.println(n);
    }
}
