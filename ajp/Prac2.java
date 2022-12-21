// Write a program to design a form using 
// the components List and Choice.
import java.awt.*;

/* <applet code= Prac2.class height=100 width= 100> </applet> */
public class Prac2  {
    public static void main(String args[]) {
        Frame f = new Frame("Form elements using list and choice");
        f.setVisible(true);
        f.setBounds(50, 50, 500, 500);
        f.setLayout(new FlowLayout());
        
        List l1 = new List(2);
        l1.add("Item1");
        l1.add("Item2");
        l1.add("Item3");
        l1.add("Item4");
        l1.add("Item5");
        l1.add("Item6");
        l1.add("Item7");
        l1.add("Item8");
        l1.add("Item9");
        l1.add("Item10");
        f.add(l1);

        Choice c = new Choice();
        c.add("Item1");
        c.add("Item2");
        c.add("Item3");
        c.add("Item4");
        f.add(c);
        
    }
}