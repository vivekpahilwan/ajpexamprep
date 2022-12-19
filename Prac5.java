// Write a program using AWT to create a menu bar
//  where menu bar contains menu items such as File, 
//  Edit, View and create a submenu under the File 
//  menu: New and Open.


import java.awt.*;
public class Prac5 {
    Prac5(){
        Frame f = new Frame("Menu bar example");
        f.setVisible(true);
        f.setBounds(50,50,500,500);
        f.setLayout(null);

        MenuBar mb = new MenuBar();
        Menu m1 = new Menu("File");
        Menu m2 = new Menu("Option");
        Menu m3 = new Menu("Help");

        MenuItem file1 = new MenuItem("File 1");
        MenuItem file2 = new MenuItem("File 2");
        MenuItem file3 = new MenuItem("File 3");

        mb.add(m1);
        mb.add(m2);
        mb.add(m3);

        m1.add(file1);
        m2.add(file2);
        m3.add(file3);
        f.setMenuBar(mb);

    }
    public static void main(String args[])
    {
       new Prac5();
    }
}
