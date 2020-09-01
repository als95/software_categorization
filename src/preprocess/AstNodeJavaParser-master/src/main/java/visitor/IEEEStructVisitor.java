package visitor;

import Node.ParsingNode;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;

import java.util.ArrayList;

public class IEEEStructVisitor extends VoidVisitorAdapter<Integer> {

    private ArrayList<ParsingNode> parsingNodes = new ArrayList<>();

    public ArrayList<ParsingNode> getParsingNodes() {
        return parsingNodes;
    }

}
