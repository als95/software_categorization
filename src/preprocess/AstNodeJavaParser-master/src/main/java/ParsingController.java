import com.github.javaparser.JavaParser;
import com.github.javaparser.ParseProblemException;
import com.github.javaparser.ast.*;
import visitor.FourthStructVisitor;
import visitor.HandCraftStructVisitor;
import visitor.RepresentationNodeVisitor;
import visitor.RevisedStructVisitor;

import Node.ParsingNode;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;

/**
 * Created by chaebyeonghun on 2018. 2. 20..
 */
// Parsing Control function
// There are functions that can parse the node and print the result as parsed.
public class ParsingController {

    ArrayList<CompilationUnit> units = new ArrayList<>();

    public static void main(String[] args) throws IOException {


        ArrayList<CompilationUnit> units = new ArrayList<>();
        FileController fileController = new FileController("/Users/chaebyeonghun/Desktop/AstJavaParser/src/source/");
    }

    /*
    * Getting File list at Constructor and then Creation CompilationUnit. and Add at ArrayList
    * */
    public ParsingController(ArrayList<String> fileList) throws FileNotFoundException, ParseProblemException {

        for (String filename : fileList) {
            try{
                CompilationUnit tempCu = JavaParser.parse(new FileInputStream(filename));
                units.add(tempCu);
            }catch (ParseProblemException e){
                System.out.println("Source Code Parsing Problem is occured " + filename);
                //units.remove(units.size() - 1);
            }
        }
    }

    //All tree
    public ArrayList<ArrayList<ParsingNode>> parsingNodeByFullTreeStructure() {

        TreeStructVisitor rnSelector;
        ArrayList<ArrayList<ParsingNode>> nodeDatas = new ArrayList<>();
        for(CompilationUnit cu : units){
            rnSelector = new TreeStructVisitor();
            rnSelector.visit(cu,0);
            nodeDatas.add(rnSelector.getParsingNodes());
        }

        return nodeDatas;
    }
    //Captain? Node
    public ArrayList<ArrayList<ParsingNode>> parsingNodeByRepresentiveTreeStructure(){
        RepresentationNodeVisitor rnSelector;
        ArrayList<ArrayList<ParsingNode>> nodeDatas = new ArrayList<>();
        for(CompilationUnit cu : units){
            rnSelector = new RepresentationNodeVisitor();
            rnSelector.visit(cu,0);
            nodeDatas.add(rnSelector.getParsingNodes());
        }

        return nodeDatas;
    }
    public ArrayList<ArrayList<ParsingNode>> parsingNodeByRevisedStructure(){
        RevisedStructVisitor rsSelector;
        ArrayList<ArrayList<ParsingNode>> nodeDatas = new ArrayList<>();
        for(CompilationUnit cu : units){
            rsSelector = new RevisedStructVisitor();
            rsSelector.visit(cu,0);
            nodeDatas.add(rsSelector.getParsingNodes());
        }
       // System.out.println("Node Count per Project : " + nodeDatas.size());
        return nodeDatas;
    }
    public ArrayList<ArrayList<ParsingNode>> parsingNodeByFourthStructure(){
        FourthStructVisitor rsSelector;
        ArrayList<ArrayList<ParsingNode>> nodeDatas = new ArrayList<>();
        for(CompilationUnit cu : units){
            rsSelector = new FourthStructVisitor();
            rsSelector.visit(cu,0);
            nodeDatas.add(rsSelector.getParsingNodes());
        }
        return nodeDatas;
    }
    public ArrayList<ArrayList<ParsingNode>> parsingNodeByHandCraftStructure(){
        HandCraftStructVisitor rsSelector;
        ArrayList<ArrayList<ParsingNode>> nodeDatas = new ArrayList<>();
        for(CompilationUnit cu : units){
            rsSelector = new HandCraftStructVisitor();
            rsSelector.visit(cu,0);
            nodeDatas.add(rsSelector.getParsingNodes());
        }
        return nodeDatas;
    }



    public void printParsingNode(){
        TreeStructVisitor rnSelector;
        ArrayList<ArrayList<ParsingNode>> nodeDatas = new ArrayList<>();
        for(CompilationUnit cu : units){
            rnSelector = new TreeStructVisitor();
            rnSelector.visit(cu,0);

            nodeDatas.add(rnSelector.getParsingNodes());
        }
        for(int i = 0; i < nodeDatas.size(); i++){
            for(int j = 0 ; j < nodeDatas.get(i).size(); j++){
                System.out.println(nodeDatas.get(i).get(j).getNodeRepresentation());
            }
        }
    }
    public void printRepresentationParsingNode(){
        RepresentationNodeVisitor rnSelector;
        ArrayList<ArrayList<ParsingNode>> nodeDatas = new ArrayList<>();
        for(CompilationUnit cu : units){
            rnSelector = new RepresentationNodeVisitor();
            rnSelector.visit(cu,0);

            nodeDatas.add(rnSelector.getParsingNodes());
        }
        for(int i = 0; i < nodeDatas.size(); i++){
            for(int j = 0 ; j < nodeDatas.get(i).size(); j++){
                System.out.println(nodeDatas.get(i).get(j).getNodeRepresentation());
            }
        }
    }
    public void printRevisedStructParsingNode(){
        RevisedStructVisitor selector;
        ArrayList<ArrayList<ParsingNode>> nodeDatas = new ArrayList<>();
        for(CompilationUnit cu : units){
            selector = new RevisedStructVisitor();

            selector.visit(cu, 0);
            nodeDatas.add(selector.getParsingNodes());
        }
        for(int i = 0; i < nodeDatas.size(); i++){
            for(int j = 0 ; j < nodeDatas.get(i).size(); j++){
                System.out.println(nodeDatas.get(i).get(j).getNodeRepresentation());
            }
        }
    }
    public void printFourthStructParsingNode(){
        FourthStructVisitor selector;
        ArrayList<ArrayList<ParsingNode>> nodeDatas = new ArrayList<>();
        for(CompilationUnit cu : units){
            selector = new FourthStructVisitor();

            selector.visit(cu, 0);
            nodeDatas.add(selector.getParsingNodes());
        }
        for(int i = 0; i < nodeDatas.size(); i++){
            for(int j = 0 ; j < nodeDatas.get(i).size(); j++){
                System.out.println(nodeDatas.get(i).get(j).getNodeRepresentation());
            }
        }

    }
    public void printHandCraftStructParsingNode(){
        HandCraftStructVisitor selector;
        ArrayList<ArrayList<ParsingNode>> nodeDatas = new ArrayList<>();
        for(CompilationUnit cu : units){
            selector = new HandCraftStructVisitor();

            selector.visit(cu, 0);
            nodeDatas.add(selector.getParsingNodes());
        }
        for(int i = 0; i < nodeDatas.size(); i++){
            for(int j = 0 ; j < nodeDatas.get(i).size(); j++){
                System.out.println(nodeDatas.get(i).get(j).getNodeRepresentation());
            }
        }
    }


}

