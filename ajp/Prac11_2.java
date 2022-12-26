
import java.awt.*;
import java.awt.event.*;

public class Prac11_2 extends Frame implements MouseMotionListener {
    Label l = new Label("Idle");

    Prac11_2() {
        setVisible(true);
        setSize(500, 500);
        add(l);
        l.addMouseMotionListener(this);
    }

    public void mouseMoved(MouseEvent e) {
        l.setText("Mouse Moved");
    }

    public void mouseDragged(MouseEvent e) {
        l.setText("Mouse Dragged");
    }

    public static void main(String args[]) {
        Prac11_2 obj = new Prac11_2();
    }
}
