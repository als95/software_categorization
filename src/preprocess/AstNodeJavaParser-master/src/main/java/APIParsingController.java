import com.github.javaparser.JavaParser;
import com.github.javaparser.ParseProblemException;
import com.github.javaparser.ast.CompilationUnit;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class APIParsingController {
    ArrayList<ArrayList<String>> apis = new ArrayList<ArrayList<String>>();

    public APIParsingController(ArrayList<String> fileList) throws FileNotFoundException, ParseProblemException {
        int i = 0;
        for (String fileName : fileList) {
            try{
                CompilationUnit tempCu = JavaParser.parse(new FileInputStream(fileName));

                apis.add(i, new ArrayList<String>());
                for (int j = 0; j < tempCu.getImports().size(); j++) {
                    apis.get(i).add(j, tempCu.getImport(j).getName().getIdentifier());
                }


            }catch (ParseProblemException e){
                System.out.println("Source Code Parsing Problem is occured " + fileName);
            }
        }
    }

    public ArrayList<ArrayList<String>> getApis() {
        return apis;
    }
}
