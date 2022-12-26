
import java.awt.*;
import java.awt.event.*;

import javax.swing.JFrame;

public class winadapter extends WindowAdapter {
    Label l = new Label("Label Name");

    winadapter() {
        JFrame f = new JFrame("Frame Title");
        f.setVisible(true);
        f.setSize(500, 500);
        f.setLayout(new FlowLayout());
        f.setDefaultCloseOperation(f.EXIT_ON_CLOSE);

        f.add(l);
        f.addWindowFocusListener(this);
    }

    public void windowLostFocus(WindowEvent e) {
        l.setText("Window Deactivated");
    }

    public void windowGainedFocus(WindowEvent e) {
        l.setText("Window Activated");
    }

    public static void main(String args[]) {
        new winadapter();
    }
}
