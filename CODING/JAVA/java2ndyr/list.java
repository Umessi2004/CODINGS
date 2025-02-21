import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class list {
    public static void main(String a[]){
        List <Integer> ls= new ArrayList<>();
        Iterator <Integer> it= ls.iterator();
        //ascending order
        ls.add(1);
        ls.add(2);
        ls.add(4);
        ls.add(9);
        ls.add(11);
        ls.add(5);
        ls.add(90);
        ls.add(5);
        int temp;
        for(int i=0; i<ls.size(); i++){
            for(int j=0; j<ls.size()-1-i; j++){
                if(ls.get(j)>ls.get(j+1)){
                    temp=ls.get(j);
                    ls.set(j, ls.get(j+1));
                    ls.set(j+1, temp);
                }
            }
        }
        while(it.hasNext()){
            System.out.println(it.next());
        }
        System.out.println("the list:"+ls);
    }
}
