import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Writer {
  BufferedWriter w;
  String currentLine;
   
  public Writer(String loc) {
    try {
      w = new BufferedWriter(new FileWriter(loc));
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  public void writeLine(String line) {
    try {
      w.write(line);
    } catch(IOException e) {
      e.printStackTrace();
    }
  }

  public void closeFile() {
    try {
      w.close();
    } catch (IOException e) {
      e.printStackTrace();
    } 
  }
}
