// Write a program to create a two-level 
// card deck that allows the user to select 
// component of Panel using CardLayout

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Prac4 {
    public static void main(String args[]) {
        Frame f = new Frame();
        f.setVisible(true);
        f.setBounds(50, 50, 500, 500);
        f.setLayout(new FlowLayout());
        CardLayout cl = new CardLayout(30, 40);
        Container c = new Container();
        
        c.setLayout(cl);
        Button b1 = new Button("Button 1");
        Button b2 = new Button("Button 2");
        Button b3 = new Button("Button 3");

        b1.addActionListener(this);
        b2.addActionListener(this);
        b3.addActionListener(this);
        c.add("a", b1);
        c.add("b", b2);
        c.add("c", b3);

        f.add(c);

    }
    void actionPerformed(ActionEvent event){
        cl.next(c);

    }
}
