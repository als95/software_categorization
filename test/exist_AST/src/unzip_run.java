import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class unzip_run {
    public static void main(String[] args) throws IOException {

        List<String> categories = new ArrayList<String>();
        categories.add("Communication");
        categories.add("Games");
        categories.add("Multimedia");
        categories.add("System");
        categories.add("Business");

        for(String category : categories) {
            String root = "E:\\data\\sourceforge\\" + category + "\\";
//        String root = "C:\\Users\\MH\\Desktop\\test_zip";
            Unzip uz = new Unzip();
            UnzipTest uzt = new UnzipTest();
            try (Stream<Path> walk = Files.walk(Paths.get(root))) {
//            List<String> files_name = walk.map(Path::toString)
//                    .filter(f -> f.endsWith(".zip"))
//                    .collect(Collectors.toList());
//            System.out.println(files_name.size());
                List<Path> files_path = walk.filter(f -> f.toString().endsWith(".zip"))
                        .collect(Collectors.toList());
                System.out.println("The number of zip file : " + files_path.size());

                for (Path name : files_path) {
                    System.out.println(name.toString());
//                uz.unzip(name.toString(), name.getParent().toString());
//                    uzt.run(name.toString(), name.getParent().toString());
                }


            } catch (IOException e) {
                e.printStackTrace();
            } catch (Throwable throwable) {
                throwable.printStackTrace();
            }
        }
    }
}
