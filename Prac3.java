
// Write a program to design simple 
// calculator with the use of GridLayout

import java.awt.*;
public class Prac3 {
    public static void main(String args[]) {
        Frame f = new Frame("Grid Layout Calculator");
        f.setVisible(true);
        f.setLayout(new GridLayout(4,3));
        f.setBounds(50,50,500,500);

        
        Button b1 = new Button("1");
        Button b2 = new Button("2");
        Button b3 = new Button("3");
        Button b4 = new Button("4");
        Button b5 = new Button("5");
        Button b6 = new Button("6");
        Button b7 = new Button("7");
        Button b8 = new Button("8");
        Button b9 = new Button("9");
        Button clear = new Button("Clear");
        Button b0 = new Button("0");
        Button Cal = new Button("Calculate");

        // f.add(tf);
        f.add(b1);
        f.add(b2);
        f.add(b3);
        f.add(b4);
        f.add(b5);
        f.add(b6);
        f.add(b7);
        f.add(b8);
        f.add(b9);
        f.add(clear);
        f.add(b0);
        f.add(Cal);
    }
}
