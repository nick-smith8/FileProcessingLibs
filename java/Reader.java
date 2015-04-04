import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Reader {
  BufferedReader r;
  String currentLine;
   
  public Reader(String loc) {
    try {
      r = new BufferedReader(new FileReader(loc));
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  public String readLine() {
    return currentLine;
  }

  public boolean hasLine() {
    try {
      if ((currentLine = r.readLine()) != null)
        return true;
    } catch (IOException e) {
      e.printStackTrace();
    } 
    return false;
  }

  public void closeFile() {
    try {
      r.close();
    } catch (IOException e) {
      e.printStackTrace();
    } 
  }
}
