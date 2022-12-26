// Write a program to demonstrate the use of 
//  InetAddress class and its factory methods.

import java.net.InetAddress;

public class Prac14 {
    public static void main(String[] arg) throws Exception {
        try {

            InetAddress ip1 = InetAddress.getByName("www.facebook.com");
            System.out.println(ip1.getHostName());
            System.out.println(ip1.getHostAddress());
            System.out.println(ip1);
            System.out.println("\n");
            InetAddress ip2[] = InetAddress.getAllByName("www.google.com");
            for (int i = 0; i < ip2.length; i++) {
                System.out.println(ip2[i]);

            }
        } catch (Exception e) {
            // TODO: handle exception
        }

    }
}