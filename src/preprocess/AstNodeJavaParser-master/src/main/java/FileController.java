import java.io.*;
import java.util.ArrayList;

/**
 * Created by chaebyeonghun on 2018. 2. 21..
 */

public class FileController {

    private ArrayList<String> fileNames;
    private ArrayList<String> pathFileNames;
    private String path;
    public static int filecnt = 0;


    public FileController(String path) throws IOException {

        fileNames = new ArrayList<>();
        pathFileNames = new ArrayList<>();
        this.path = path;
        setFileList();

    }
    private void setFileList() throws IOException {

        File dirFile = new File(path);
        File[] fileList = dirFile.listFiles();


        for(File tempFile : fileList) {
            if(tempFile.isFile()) {
                if(tempFile.getName().endsWith(".java")){
                    String tempFileName = tempFile.getName();
                        this.fileNames.add(tempFileName);
                        this.pathFileNames.add(path+"/"+tempFileName);

                }

            }
        }
    }
    public ArrayList<String> getFileNames(){
        return this.fileNames;
    }
    public ArrayList<String> getPathFileNames(){
        System.out.println("The number of File Per project : " + this.pathFileNames.size());
        filecnt += this.pathFileNames.size();
        System.out.println("Cumulative file count : " + filecnt);
        return this.pathFileNames;
    }
    public void printFileList(){
        System.out.println(fileNames.toString());
    }
    public void printPathFileList(){
        System.out.println(fileNames.toString());
    }


}
