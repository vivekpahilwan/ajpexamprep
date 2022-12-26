
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class jtexf extends Frame implements ActionListener {
    Label l = new Label("Label");

    JTextField jtf = new JTextField(20);
    Button b = new Button("Button");
    JPasswordField jpf = new JPasswordField(20);

    jtexf() {
        setVisible(true);
        setSize(500, 500);
        setLayout(new FlowLayout());
        add(jtf);
        jpf.setEchoChar('%');
        add(jpf);

        add(b);

        add(l);
        b.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e) {
        String pass = new String(jpf.getPassword());
        String user = new String(jtf.getText());

        l.setText(user + pass);
    }

    public static void main(String args[]) {
        new jtexf();
    }
}