import Node.ParsingNode;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Field;
import java.util.ArrayList;

/**
 * Created by chaebyeonghun on 2018. 2. 22..
 */
//File print Class
public class FileOutController {

    public static String outputPath;
    String projectName;
    ArrayList<ArrayList<ParsingNode>> nodeDatas;
    ArrayList<String> paths;

    public FileOutController(ArrayList<ArrayList<ParsingNode>> nodeDatas, ArrayList<String> paths, String outputPath, String projectName){
        this.nodeDatas = nodeDatas;
        this.paths = paths;
        FileOutController.outputPath = outputPath;
        this.projectName = projectName;

    }
    //Execute Getting Vector Presentation
    public void fileOut() throws IOException{
        BufferedWriter bw;
        System.out.println("@@@@@@@@@@@" + nodeDatas.size());
        System.out.println("!!!!!!!!" + paths.size());
        try{
            for(int i = 0; i < nodeDatas.size(); i++){
                bw = new BufferedWriter(new FileWriter( outputPath + projectName +"_" + this.paths.get(i)+".txt"));
                for(int j = 0; j < nodeDatas.get(i).size(); j++){
                    bw.write(nodeDatas.get(i).get(j).getNodeRepresentation());
                    bw.newLine();
                }
                bw.close();
            }

        }catch(IOException e){
            e.printStackTrace();
            System.out.println("System fail");
        }finally {
            System.out.println("Node Creation Success!");
        }

    }
}
