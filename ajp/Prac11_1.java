import java.awt.*;
import java.awt.event.*;

public class Prac11_1 extends Frame implements MouseListener {

    Label l = new Label("Idle");

    Prac11_1() {
        setVisible(true);
        l.setBounds(50, 50, 50, 50);
        setSize(500, 500);
        l.addMouseListener(this);
        add(l);
        // setLayout(new FlowLayout());

    }

    public void mouseExited(MouseEvent e) {
        l.setText("Mouse Exited");
    }

    public void mouseEntered(MouseEvent e) {
        l.setText("Mouse Entered");
    }

    public void mouseReleased(MouseEvent e) {
        l.setText("Mouse Released");
    }

    public void mousePressed(MouseEvent e) {
        l.setText("Mouse Pressed");
    }

    public void mouseClicked(MouseEvent e) {
        l.setText("Mouse Clicked");
    }

    public static void main(String args[]) {
        Prac11_1 obj = new Prac11_1();
    }
}