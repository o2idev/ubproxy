

import java.net.InetSocketAddress;
import java.net.Proxy;
import java.net.URL;

public class ProxyTester {

  public static void main(String[] args) throws Exception {
    System.out.println( "supply HTTP or HTTPS url as param");
    URL url = new URL(args[0]);
    System.out.println("header fields:" + 
        //url.openConnection(new Proxy(Proxy.Type.HTTP, new InetSocketAddress("proxy-list", 8080)))
        url.openConnection()
      .getHeaderFields());
  }

}
