// Write a program using swing to display a 
// ScrollPane and JComboBox in an JApplet with 
// the items – English, Marathi, Hindi, Sanskrit.

import javax.swing.*;
import java.awt.*;
public class Prac6 {
    
    public static void main(String args[])
    {   
        Frame f = new Frame("Scroll pane and jcombobox");
        f.setBounds(50,50,500,500);
        f.setVisible(true);

        //created a string array and added all emenents
        String s[] ={"English","Marathi","Hindi","Sanskrit"}; 

        // Created a JcomboBox object and passed the string object as a  constructor while making the object of JComboBox
        JComboBox jb = new JComboBox(s);


        jb.setBounds(50,50,150,50);

        //added the JComboBox to the frame 
        f.add(jb);
        f.setLayout(null);
    }
}
