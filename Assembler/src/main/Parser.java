package main;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/**
 * @author goneal26
 * 
 * This class will contain the API to open and read the assembly file, parsing out comments and whitespace and storing symbols.
 * The class operates as a singleton.
 */

public class Parser {
	private static Parser instance;
	private String fileName;
	
	private Parser() {
		
	}
	
	
	/**
	 * This function reads the lines from each file into an arrayList of each line
	 * 
	 * @param filePath - the relative/absolute path for the file you want to convert to machine code
	 * @return lines - an arrayList of each line (String) in the file after removing all comments
	 */
	public static ArrayList<String> readLinesFromFile(String filePath) {
		ArrayList<String> lines = new ArrayList<String>();
		try {
			BufferedReader reader = new BufferedReader(new FileReader(filePath));
			String line;
			while ((line = reader.readLine()) != null) {
				if (line.split(";")[0] != null) {
					lines.add(line.split(";")[0]);
				}
			}
			
			reader.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		return lines;
	}
	
	// make sure this is a singleton
	public static Parser init() {
		if (instance == null) {
			instance = new Parser();
		}
		return instance;
	}
}
