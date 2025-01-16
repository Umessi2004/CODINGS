import java.util.Scanner;

public class driverstring {
    // capitalize each letter of the first word of the sentence
    // public static void main(String a[]) {
    // Scanner sc = new Scanner(System.in);
    // String s = sc.nextLine();
    // StringBuilder Capitalize = new StringBuilder();
    // String words[] = s.split(" ");
    // for (String word : words) {
    // if (!word.isEmpty()) {
    // Capitalize.append(Character.toUpperCase(word.charAt(0))).append(word.substring(1).toLowerCase())
    // .append(" ");
    // }
    // }
    // System.out.println(Capitalize.toString());
    // }
    // @SuppressWarnings("ConvertToTryWithResources")
    //
    // replace a string with a new string
    // public static void main(String args[])
    // {
    // System.out.println("enter the string ");
    // Scanner sc=new Scanner(System.in);
    // String s=sc.nextLine();
    // System.out.println("enter the old string ");
    // String sold=sc.nextLine();
    // System.out.println("enter the new string ");
    // String snew=sc.nextLine();
    // s=s.replace(sold,snew);
    // System.out.println("now the new string "+s);
    // sc.close();
    // }
    //
    // Write a java program to find the number of occurrence of each character in
    // the String s="Silicon Institute of Technology" by excluding space and
    // ignoring case.
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            String s = sc.nextLine();
            s = s.replace(" ", "");
            s = s.toLowerCase();
            int[] charcount = new int[26];
            for (int i = 0; i < s.length(); i++) {
                charcount[s.charAt(i) - 'a']++;
            }
            for (int i = 0; i < charcount.length; i++) {
                if (charcount[i] >= 1) {
                    System.out.println((char) (i + 'a') + "--->" + charcount[i]);
                }
            }
        }
    }

}
