package visitor;

import Node.ParsingNode;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.stmt.*;
import com.github.javaparser.ast.type.PrimitiveType;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;

import java.util.ArrayList;

/**
 * Created by chaebyeonghun on 2018. 3. 10..
 */
public class FourthStructVisitor extends VoidVisitorAdapter<Integer> {
    private ArrayList<ParsingNode> parsingNodes = new ArrayList<>();
    public void out(String node, int indentLevel){
        parsingNodes.add(new ParsingNode(node, indentLevel));
    }
    public ArrayList<ParsingNode> getParsingNodes(){
        return parsingNodes;
    }

    @Override
    public void visit(MethodDeclaration md, Integer arg) {
        out(md.getClass().getSimpleName(), arg);
        super.visit(md, arg + 1);
    }
    @Override
    public void visit(ClassOrInterfaceDeclaration n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(PrimitiveType n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(DoStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(IfStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(ForStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(TryStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(BlockStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(BreakStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(WhileStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);
    }


    @Override
    public void visit(MethodCallExpr n, Integer arg) {
        out(n.getNameAsString(), arg);
        super.visit(n, arg+1);

    }

    @Override
    public void visit(SwitchStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(ThrowStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(SuperExpr n, Integer arg) {
        System.out.println("supersibal");
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);
        System.out.println("supersibal");

    }

    @Override
    public void visit(ReturnStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);

    }

    @Override
    public void visit(CatchClause n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);

    }

    @Override
    public void visit(ContinueStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);

    }

    @Override
    public void visit(AssertStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(ForeachStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);

    }


    /*@Override
    public void visit(ExpressionStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);
    }*/

    @Override
    public void visit(VariableDeclarator n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);

    }

    @Override
    public void visit(ConstructorDeclaration n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);

    }

    @Override
    public void visit(FieldDeclaration n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);

    }

    @Override
    public void visit(SynchronizedStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);

    }

    @Override
    public void visit(SwitchEntryStmt n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg+1);

    }
    @Override
    public void visit(NameExpr n, Integer arg){
        out(n.getNameAsString(), arg);
        super.visit(n, arg+1);
        System.out.println(n.getNameAsString());
    }

    @Override
    public void visit(ClassExpr n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(CharLiteralExpr n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(StringLiteralExpr n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg + 1);

    }
    @Override
    public void visit(LongLiteralExpr n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(DoubleLiteralExpr n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(BooleanLiteralExpr n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(ArrayInitializerExpr n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg + 1);
    }
    @Override
    public void visit(final UnaryExpr n, final Integer arg) {
        out(n.getOperator().asString(), arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(BinaryExpr n, Integer arg) {
        out(n.getOperator().asString(), arg);
        super.visit(n, arg + 1);

        //Operator 추출

   }

    @Override
    public void visit(NullLiteralExpr n, Integer arg) {
        out(n.getClass().getSimpleName(), arg);
        super.visit(n, arg);
    }

    @Override
    public void visit(SimpleName n, Integer arg) {
        if(n.getParentNode().get().getClass().getSimpleName().equals("VariableDeclarator")){
            out(n.getIdentifier(), arg);
            super.visit(n, arg + 1);
        }


    }
}
