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
        Menu m2 = new Menu("Edit");
        Menu m3 = new Menu("View");

        MenuItem neww = new MenuItem("New");
        MenuItem open = new MenuItem("Open");

        mb.add(m1);

        m1.add(neww);
        m1.add(open);

        mb.add(m2);
        mb.add(m3);
        f.setMenuBar(mb);

    }
    public static void main(String args[])
    {
       new Prac5();
    }
}
