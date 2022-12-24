// Write a program to demonstrate status of key on 
//  Applet window such as KeyPressed, KeyReleased, 
//  KeyUp, KeyDown.

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class Prac10 extends JFrame implements KeyListener {
    JLabel l = new JLabel("Label name");

    Prac10() {
        setVisible(true);
        setLayout(new FlowLayout());
        JTextArea ta = new JTextArea(10, 20);
        ta.addKeyListener(this);

        add(l);
        add(ta);
    }

    public void keyPressed(KeyEvent e) {
        l.setText("Key Pressed");
    }

    public void keyReleased(KeyEvent e) {
        l.setText("Key Released");
    }

    public void keyTyped(KeyEvent e) {
        l.setText("Key Typed");
    }

    public static void main(String args[]) {
        Prac10 obj = new Prac10();
    }
}
