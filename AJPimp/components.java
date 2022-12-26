
import java.awt.*;
import javax.swing.*;

public class components extends Frame {
    List li = new List(2);
    TextArea ta = new TextArea(10, 10);
    Checkbox cb1 = new Checkbox("Checkbox1");
    Checkbox cb2 = new Checkbox("Checkbox2");
    CheckboxGroup cbg = new CheckboxGroup();
    Checkbox cb3 = new Checkbox("Checkbox3", true, cbg);
    Checkbox cb4 = new Checkbox("Checkbox4", cbg, true);

    components() {
        setVisible(true);
        setSize(500, 500);
        setLayout(new FlowLayout());

        add(ta);

        li.add("Item1");
        li.add("Item2");
        li.add("Item3");
        li.add("Item4");
        li.add("Item5");
        add(li);

        add(cb1);
        add(cb2);

        add(cb3);
        add(cb4);

    }

    public static void main(String args[]) {
        new components();
    }
}
