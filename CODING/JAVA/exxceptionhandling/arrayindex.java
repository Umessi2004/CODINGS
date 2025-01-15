public class arrayindex {
    public static void main(String[] args) {
        int[] a={1,2,3,4,5,6,7};
        try{
            System.out.println("array ele in index"+5+"="+a[5]);
        }
        catch(ArrayIndexOutOfBoundsException e){
            System.out.println("array index is out"+e.getMessage());
        }
        
    }
}
