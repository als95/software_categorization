import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class APIFileOutController {
    public static String outputPath;
    String projectName;
    ArrayList<ArrayList<String>> apiNames;
    ArrayList<String> paths;

    public APIFileOutController(ArrayList<ArrayList<String>> apiNames, ArrayList<String> paths, String outputPath, String projectName) {
        this.apiNames = apiNames;
        this.paths = paths;
        APIFileOutController.outputPath = outputPath;
        this.projectName = projectName;
    }

    public void fileOut() throws IOException {
        BufferedWriter bw;

        try {
            for(int i = 0; i < apiNames.size(); i++){
                bw = new BufferedWriter(new FileWriter( outputPath + projectName +"_api_" + this.paths.get(i)+".txt"));
                for(int j = 0; j < apiNames.get(i).size(); j++){
                    bw.write(apiNames.get(i).get(j));
                    bw.newLine();
                }
                bw.close();
            }
        } catch(IOException e){
            e.printStackTrace();
            System.out.println("System fail");
        } finally {
            System.out.println("API Creation Success!");
        }
    }
}
