
import javax.swing.*;
import java.awt.*;

public class menueg extends Frame {
    menueg() {
        setVisible(true);
        setSize(500, 500);
        setLayout(new FlowLayout());

        MenuBar mb = new MenuBar();
        Menu m1 = new Menu("FILE");
        Menu m2 = new Menu("EDIT");
        Menu m3 = new Menu("VIEW");

        MenuItem f1 = new MenuItem("NEW");
        MenuItem f2 = new MenuItem("OPEN");

        mb.add(m1);
        mb.add(m2);
        mb.add(m3);

        m1.add(f1);
        m1.add(f2);

        setMenuBar(mb);

    }

    public static void main(String args[]) {
        new menueg();
    }
}
