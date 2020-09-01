package Node;

import org.apache.commons.lang3.StringUtils;

/**
 * Created by chaebyeonghun on 2018. 2. 22..
 */
public class ParsingNode {

    private String nodeType;
    private int indentLevel;

    public ParsingNode(String nodeType, int indentLevel){
        this.nodeType = nodeType;
        this.indentLevel = indentLevel;
    }

    public int getIndentLevel() {
        return indentLevel;
    }

    public String getNodeType() {
        return nodeType;
    }
    public String getNodeRepresentation(){
        return  StringUtils.repeat('\t', indentLevel) + nodeType;

    }
}
