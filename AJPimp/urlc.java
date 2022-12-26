import java.net.*;
public class urlc {
    public static void main(String args[])
    {
       try{
        URL url = new URL("https://www.msbte.org.in:5555/filename.txt");
        System.out.println(url.getPort());
        System.out.println(url.getHost());
        System.out.println(url.getProtocol());
        System.out.println(url.getFile());
       }
       catch(Exception e){
        System.out.println(e);
       }
    }
}
