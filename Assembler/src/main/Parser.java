package main;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * @author goneal26
 * 
 * This class will contain the API to open and read the .asm file, parsing out comments and whitespace and storing symbols.
 * The class operates as a singleton.
 */

public class Parser {
	private static Parser instance;
	private String fileName;
	private File file;
	
	private Parser(String fname) {
		if (!fname.isEmpty() && !fname.isBlank() && fname != null) {
			this.fileName = fname;
			this.file = readFile(this.fileName);
		}
	}
	
	
	
	public File readFile(String fname) {
		try {
			File myFile = new File(fname);
			Scanner s = 
		}
	}
	
	// make sure this is a singleton
	public static Parser init(String fname) {
		if (instance == null) {
			instance = new Parser(fname);
		}
		return instance;
	}
}
