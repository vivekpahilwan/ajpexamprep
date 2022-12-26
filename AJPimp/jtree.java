import java.awt.*;
import javax.swing.*;
import javax.swing.tree.*;
public class jtree extends Frame{
    jtree(){

        setVisible(true);
        setSize(500,500);
        setLayout(new FlowLayout());

        DefaultMutableTreeNode india = new DefaultMutableTreeNode("INDIA");
        DefaultMutableTreeNode mh = new DefaultMutableTreeNode("Maharashtra");
        DefaultMutableTreeNode gj = new DefaultMutableTreeNode("Gujarat");
        DefaultMutableTreeNode kr = new DefaultMutableTreeNode("Karnataka");
        JTree jt = new JTree(india);
        india.add(kr);
        india.add(mh);
        india.add(gj);

        add(jt);
        
    }
    public static void main(String args[])
    {
       new jtree();
    }
}
