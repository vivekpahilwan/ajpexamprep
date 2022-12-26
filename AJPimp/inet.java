import java.net.*;

public class inet {
    public static void main(String args[]) {
        try {
            InetAddress ip = InetAddress.getByName("localhost");
            System.out.println(ip.getHostAddress());
            System.out.println(ip.getHostName());
            
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
