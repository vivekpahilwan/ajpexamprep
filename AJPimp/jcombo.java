
import javax.swing.*;
import javax.swing.JTree.*;
import java.awt.*;
public class jcombo extends Frame {
    jcombo(){

        setVisible(true);
        setSize(500, 500);
        setLayout(new FlowLayout());


        String objs []={"Vivek","Krish","Prajwal","Keyur","Rohit","Dhiraj","Baki sagle aplech","Baki sagle aplech","Baki sagle aplech","Baki sagle aplech","Baki sagle aplech","Baki sagle aplech","Baki sagle aplech","Baki sagle aplech"};
        JComboBox jb = new JComboBox(objs);

        JScrollPane jp = new JScrollPane(jb);
        add(jp);

    }
    public static void main(String args[])
    {
       new jcombo();
    }
}
