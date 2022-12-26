// Write a program to demonstrate the use of 
// JTextField and JPasswordField using Listener Interface.

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Prac12 extends Frame implements ActionListener {

    JTextField tf = new JTextField(30);
    JPasswordField jp = new JPasswordField(30);
    Label l = new Label("Label");
    Button b = new Button("Button");

    Prac12() {
        setVisible(true);
        setSize(500, 500);
        setLayout(new FlowLayout());
        add(tf);
        add(jp);
        add(b);
        add(l);
        b.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e) {
        String data = "Username " + tf.getText();
        String pass = new String(jp.getPassword());
        l.setText(data + pass);
    }

    public static void main(String args[]) {
        new Prac12();
    }
}