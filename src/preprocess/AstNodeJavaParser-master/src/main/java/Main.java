import Node.ParsingNode;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.lang.reflect.Array;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * Created by chaebyeonghun on 2018. 2. 21..
 */
public class Main {

    public static final String treeOption = "TREE_OPTION";
    public static final String revisedOption = "REVISED_OPTION";
    public static final String representationOption = "REPRESENTATION_OPTION";
    public static final String fourthOption = "FOURTH_OPTION";
    public static final String handCraftOption = "HAND_OPTION";

    /*
     *  output_Path is path for ast.txt (test)
     */
    public static String output_Path;
    public static String api_output_Path;


    public static <global> void main(String[] args) throws IOException {

        String root = "E:\\data\\sourceforge\\Internet";
        File root_file = new File(root);
        File[] categories = root_file.listFiles();


        assert categories != null;
        for (File category : categories) {
            String file_path = category.toString() + "\\";

            ArrayList<String> projectList = new ArrayList<>();
            ArrayList<String> projectNameList = new ArrayList<>();

            File main_category = new File(file_path); // SoftwareDevelopment
            System.out.println("dirFile : " + main_category);
            File[] sub_category = main_category.listFiles(); // agile, etc..

            Stream<Path> walk = Files.walk(Paths.get(file_path));
            List<String> result = walk.filter(Files::isDirectory).map(Path::toString).collect(Collectors.toList());

            List<String> str_sub_dir = new ArrayList<String>(); // distribute ast and api

            assert sub_category != null;
            for (File sub_dir : sub_category) { // sub_dir -> agile, etc..
                System.out.println("--------------------");
                System.out.println(sub_dir.getName());
                str_sub_dir.add(sub_dir.getName());
            }


            //        for (int i = 0; i < str_sub_dir.size(); ++i) {
            //
            //            File ast_path = new File(file_path + str_sub_dir.get(i) + "\\ast");
            //            File api_path = new File(file_path + str_sub_dir.get(i) + "\\api");
            //
            //            ast_path.mkdir();
            //            api_path.mkdir();
            //        }
            for (int i = 0; i < str_sub_dir.size(); i++) { // 25
                File[] apps = sub_category[i].listFiles(); // agile internal, algorithms internal, etc..
                System.out.println("-- log -- ");
                System.out.println(apps.length);
                int apps_size = apps.length;

                for (int j = 0; j < apps_size; j++) {
                    File ast_path = new File(file_path + str_sub_dir.get(i) + "\\" + apps[j].getName() + "\\ast");
                    File api_path = new File(file_path + str_sub_dir.get(i) + "\\" + apps[j].getName() + "\\api");

                    ast_path.mkdir();
                    api_path.mkdir();
                }
                //            for (File app : apps){
                //                File ast_path = new File(file_path + apps[i].getName() + "\\" + app.getName() + "\\ast");
                //                File api_path = new File(file_path + apps[i].getName() + "\\" + app.getName() + "\\api");
                //
                //                ast_path.mkdir();
                //                api_path.mkdir();
                //            }
            }


            for (String last_folder : result) {
                File dir = new File(last_folder);
                projectList.add(dir.getAbsolutePath()); //
                projectNameList.add(dir.getName()); //
            }


            System.out.println(" __projectList__ : " + projectList);
            System.out.println(" __projectNameList__ : " + projectNameList);
            System.out.println(projectList.size());

            for (int i = 0; i < projectList.size(); i++) {
                for (File sub : sub_category) { // sub : agile..
                    File[] apps = sub.listFiles();
                    assert apps != null;
                    for (File app : apps) {
                        if (projectList.get(i).contains(app.getName())) {
                            output_Path = file_path + sub.getName() + "\\" + app.getName() + "\\ast\\";
                            System.out.println("-- AST :: " + output_Path);
                            break;
                        }
                    }
                    testRevised(projectList.get(i), output_Path, projectNameList.get(i));
                }
                //testRevised(projectList.get(i), output_Path, projectNameList.get(i));
            }

            for (int i = 0; i < projectList.size(); i++) {
                for (File sub : sub_category) { // sub : agile..
                    File[] apps = sub.listFiles();
                    assert apps != null;
                    for (File app : apps) {
                        if (projectList.get(i).contains(app.getName())) {
                            api_output_Path = file_path + sub.getName() + "\\" + app.getName() + "\\api\\";
                            System.out.println("-- API :: " + api_output_Path);
                            break;
                        }
                    }
                    saveAPIName(projectList.get(i), api_output_Path, projectNameList.get(i));
                }
                //saveAPIName(projectList.get(i), api_output_Path, projectNameList.get(i));
            }
        }
    }

    private static void testRevised(String path, String outputPath, String projectName) throws FileNotFoundException, IOException {
        FileController fileController = new FileController(path);

        ParsingController parsingController = new ParsingController(fileController.getPathFileNames());
        ArrayList<ArrayList<ParsingNode>> parsingNodes = parsingController.parsingNodeByRevisedStructure();
        FileOutController fileOutController = new FileOutController(parsingNodes, fileController.getFileNames(), outputPath, projectName);
        try {
            fileOutController.fileOut();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void saveAPIName(String path, String outputPath, String projectName) throws FileNotFoundException, IOException {
        FileController fileController = new FileController(path);

        APIParsingController apiParsingController = new APIParsingController(fileController.getPathFileNames());
        APIFileOutController apiFileOutController = new APIFileOutController(apiParsingController.getApis(), fileController.getFileNames(), outputPath, projectName);
        try {
            apiFileOutController.fileOut();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void printAST(String option, String path) throws FileNotFoundException, IOException{
        FileController fileController = new FileController(path);
        ParsingController ps;
        switch (option){
            case treeOption:
                ps = new ParsingController(fileController.getPathFileNames());
                ps.printParsingNode();
                break;
            case revisedOption:
                ps = new ParsingController(fileController.getPathFileNames());
                ps.printRevisedStructParsingNode();
                break;
            case representationOption:
                ps = new ParsingController(fileController.getPathFileNames());
                ps.printRepresentationParsingNode();
                break;
            case fourthOption:
                ps = new ParsingController(fileController.getPathFileNames());
                ps.printFourthStructParsingNode();
                break;
            case handCraftOption:
                ps = new ParsingController(fileController.getPathFileNames());
                ps.printHandCraftStructParsingNode();
                break;
            default:
                System.out.println("Wrong code");

        }


    }
}

