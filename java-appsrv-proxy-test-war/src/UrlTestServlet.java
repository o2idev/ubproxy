

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.URL;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class UrlTestServlet
 */
@WebServlet("/test")
public class UrlTestServlet extends HttpServlet {

  private static final String HTTP_PARAM_NAME_URL = "url";

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	@Override
  protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {

	  URL url = new URL( req.getParameter( HTTP_PARAM_NAME_URL ));
	  res.setContentType("text/plain");
	  PrintWriter w = res.getWriter();
	  w.println("retrieving URL content from: < " + url + " >:\n");
	  BufferedReader r = new BufferedReader( new InputStreamReader( url.openConnection().getInputStream()));
	  String l;
	  while ((l = r.readLine()) != null)
		w.println(l);
	}

}
