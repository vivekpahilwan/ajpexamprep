import java.awt.*;
import javax.swing.*;

public class jpbar extends Frame {
    JProgressBar jp = new JProgressBar();
    jpbar(){

        setVisible(true);
        setSize(500,500);
        setLayout(new FlowLayout());

        jp.setString("18%");
        jp.setValue(18);
        jp.setStringPainted(true);
        add(jp);

    }
    public static void main(String args[]) {
        new jpbar();
    }
}