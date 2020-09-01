import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.stream.Stream;


public class Main {
    public static void main(String[] args) throws IOException {
        List<String> main_categories = new ArrayList<>();
        main_categories.add("Internet");
        main_categories.add("ScientificEngineering");
        main_categories.add("Business");
        main_categories.add("Communication");
        main_categories.add("System");
        main_categories.add("Games");
        main_categories.add("Multimedia");



        for(String main_category : main_categories) {
            String root = "E:\\data\\sourceforge\\" + main_category +"\\";
            String discard_dir = "E:\\discard\\";

            File file = new File(root);
            File[] sub_category_dir = file.listFiles();

            assert sub_category_dir != null;
            for (File sub : sub_category_dir) {
                //System.out.println(sub.toString());
                File[] sub_apps = sub.listFiles();

                assert sub_apps != null;
                for (File app : sub_apps) {
                    //System.out.println(app.toString());
                    File[] contents = app.listFiles();

                    if (contents != null) {
                        for (File content : contents) {

                            String dir_name = content.toString();

                            if (dir_name.equals(app.toString() + "\\ast") &&
                                    (Objects.requireNonNull(content.listFiles()).length == 0)) {
                                System.out.println(dir_name + " directory not exist ast & api");
                                deleteFile(app.toString());
                                break;
                            }
                        }
                    }
                }
                System.out.println("---------------------------------------------------");
            }
        }
    }
    public static void deleteFile(String path) {
        File deleteFolder = new File(path);

        if(deleteFolder.exists()){
            File[] deleteFolderList = deleteFolder.listFiles();

            for (int i = 0; i < deleteFolderList.length; i++) {
                if(deleteFolderList[i].isFile()) {
                    deleteFolderList[i].delete();
                }else {
                    deleteFile(deleteFolderList[i].getPath());
                }
                deleteFolderList[i].delete();
            }
            deleteFolder.delete();
        }
    }

}
