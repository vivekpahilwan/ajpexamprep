// Write a program to demonstrate the use of 
//  InetAddress class and its factory methods.

import java.awt.*;
import java.awt.event.*;
import javax.swing.JFrame;

public class Prac13 extends MouseAdapter {
    JFrame f = new JFrame("Frame Title");
    Label l = new Label("Label name");

    Prac13() {
        f.setVisible(true);
        f.setSize(500,500);
        f.add(l);
        f.setLayout(new FlowLayout());
        l.addMouseListener(this);
    }

    public void mouseEntered(MouseEvent e) {
        l.setText("Mouse Entered");
    }

    public void mouseExited(MouseEvent e) {
        l.setText("Mouse Exited");
    }
    public static void main(String args[]) {
        new Prac13();
    }
}
