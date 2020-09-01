import java.io.File;

public class FolderDelete {

    private File file;

    FolderDelete(File input_file) {
        file = input_file;
    }

    void dir_delete(){
        try{
            while(file.exists()){
                File[] file_list = file.listFiles();

                assert file_list != null;
                for (int i = 0; i < file_list.length; i++){
                    if(file_list[i].isDirectory()) dir_delete();

                    file_list[i].delete();
                    System.out.println("file delete completion !");
                }

                if((file_list.length == 0) && this.file.isDirectory()) {
                    this.file.delete();
                    System.out.println("folder delete completion !");
                }
            }
        } catch (Exception e){
            e.getStackTrace();
        }
    }
}
