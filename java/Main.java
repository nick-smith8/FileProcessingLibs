import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {

  public static String result = "";

	public static void main(String[] args) {
    String inFile = "../input/info.txt";
    String outFile = "../output/output.txt";

    Reader reader = new Reader(inFile);
    Writer writer = new Writer(outFile);

    String line = "";
    for (int i = 0; reader.hasLine(); i++) {
      line = reader.readLine();
      process(line, i);
    }

    writer.writeLine(result);
 
    reader.closeFile();
    writer.closeFile();
	}

  public static void process(String line, int index) {
    System.out.println(line + " " + index);
    result += (line + " " + index + "\n");
  }

}
