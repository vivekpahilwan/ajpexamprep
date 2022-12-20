// Write a program to launch a JProgressBar

import javax.swing.*;
import java.awt.*;
public class Prac9 extends JFrame {
    Prac9() {
        setTitle("JProgressBar");
        setVisible(true);
        setSize(300, 300);
        setLayout(new FlowLayout());


        // Create JProgressBar obj
        JProgressBar jpb = new JProgressBar();
        jpb.setSize(50,50);

        // setstring to 100% (whatever you want to display)
        jpb.setString("100%");

        // setValue to 100
        jpb.setValue(100);

        // String will be visible or not
        jpb.setStringPainted(true);

        // add JProgressBar to frame
        add(jpb);

    }

    public static void main(String[] args) {
        new Prac9();
    }
}
