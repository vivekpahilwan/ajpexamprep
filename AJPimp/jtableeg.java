
import javax.swing.*;
import javax.swing.JTree.*;
import java.awt.*;

public class jtableeg extends Frame {

    String col[] = { "Roll", "Name" };
    String row[][] = { { "1", "Vivek" }, { "2", "Prajwal" }, { "3", "Keyur" }, { "4", "Krish" }, { "1", "Vivek" },
            { "2", "Prajwal" }, { "3", "Keyur" }, { "4", "Krish" }, { "1", "Vivek" }, { "2", "Prajwal" },
            { "3", "Keyur" }, { "4", "Krish" }, { "1", "Vivek" }, { "2", "Prajwal" }, { "3", "Keyur" },
            { "4", "Krish" },{ "1", "Vivek" }, { "2", "Prajwal" }, { "3", "Keyur" }, { "4", "Krish" },{ "1", "Vivek" }, { "2", "Prajwal" }, { "3", "Keyur" }, { "4", "Krish" },{ "1", "Vivek" }, { "2", "Prajwal" }, { "3", "Keyur" }, { "4", "Krish" },{ "1", "Vivek" }, { "2", "Prajwal" }, { "3", "Keyur" }, { "4", "Krish" },{ "1", "Vivek" }, { "2", "Prajwal" }, { "3", "Keyur" }, { "4", "Krish" },{ "1", "Vivek" }, { "2", "Prajwal" }, { "3", "Keyur" }, { "4", "Krish" } };
    JTable jt = new JTable(row, col);
    JScrollPane jsp = new JScrollPane(jt);

    jtableeg() {
        setVisible(true);
        setSize(500, 500);
        setLayout(new FlowLayout());

        add(jsp);
    }

    public static void main(String args[]) {
        new jtableeg();
    }
}
