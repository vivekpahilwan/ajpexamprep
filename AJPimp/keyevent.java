import java.awt.*;
import java.awt.event.*;

public class keyevent extends Frame implements KeyListener {

    Label l = new Label("Idle",Label.RIGHT);
    TextField tf = new TextField(20);
    keyevent() {
        setVisible(true);
        setSize(500, 500);
        setLayout(new GridLayout(1,1));

        add(tf);
        add(l);
        tf.addKeyListener(this);

    }

    public void keyReleased(KeyEvent e) {
        l.setText("Key Up");
    }

    public void keyPressed(KeyEvent e) {
        l.setText("Key Down");
    }

    public void keyTyped(KeyEvent e) {
        l.setText("Key Typed");
    }

    public static void main(String args[]) {
        new keyevent();
    }
}
