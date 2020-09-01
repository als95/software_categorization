package visitor;

import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.stmt.*;
import com.github.javaparser.ast.type.*;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;

import Node.ParsingNode;

import java.util.ArrayList;


/**
 * Created by chaebyeonghun on 2018. 2. 25..
 */
// TreeStructorVisitor
public class RevisedStructVisitor extends VoidVisitorAdapter<Integer> {

    private ArrayList<ParsingNode> parsingNodes = new ArrayList<>();

    public void out(Node n, int indentLevel) {

        //parsingNodes.add(new Node.ParsingNode(n.getClass().getSimpleName(), indentLevel));
        switch (n.getClass().getSimpleName()) {
            case "MethodDeclaration":
                parsingNodes.add(new ParsingNode(n.getClass().getSimpleName() + "@" + splitCamelCase(((MethodDeclaration) n).getNameAsString()), indentLevel));
                break;
            case "ClassOrInterfaceDeclaration":
                parsingNodes.add(new ParsingNode(n.getClass().getSimpleName() + "@" + splitCamelCase(((ClassOrInterfaceDeclaration) n).getNameAsString()), indentLevel));
                break;
            case "MethodCallExpr":
                parsingNodes.add(new ParsingNode(n.getClass().getSimpleName() + '@' + splitCamelCase(((MethodCallExpr) n).asMethodCallExpr().getName().toString()), indentLevel));
                break;
            case "ConstructorDeclaration":
                parsingNodes.add(new ParsingNode(n.getClass().getSimpleName() + "@" + splitCamelCase(((ConstructorDeclaration) n).getNameAsString()), indentLevel));
                break;
            case "PrimitiveType":
                parsingNodes.add(new ParsingNode(n.getClass().getSimpleName() + "@" + ((PrimitiveType) n).asString(), indentLevel));
                break;
            case "NameExpr":
                parsingNodes.add(new ParsingNode(n.getClass().getSimpleName() + "@" + splitCamelCase(((NameExpr)n).getNameAsString()), indentLevel));
                break;
            default:
                parsingNodes.add(new ParsingNode(n.getClass().getSimpleName(), indentLevel));
                break;

        }

    }
    static String splitCamelCase(String s) {
        return s.replaceAll(
                String.format("%s|%s|%s",
                        "(?<=[A-Z])(?=[A-Z][a-z])",
                        "(?<=[^A-Z])(?=[A-Z])",
                        "(?<=[A-Za-z])(?=[^A-Za-z])"
                ),
                ","
        ).toLowerCase();
    }
    public ArrayList<ParsingNode> getParsingNodes() {
        return parsingNodes;
    }

    @Override
    public void visit(MethodDeclaration md, Integer arg) {
        out(md, arg);
        super.visit(md, arg + 1);
    }

    @Override
    public void visit(ClassOrInterfaceDeclaration n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(PrimitiveType n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
        //System.out.println("PrimitiveType " + n.asString());

    }

    @Override
    public void visit(DoStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);

    }

    @Override
    public void visit(IfStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);

    }

    @Override
    public void visit(ForStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(TryStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);

    }

    @Override
    public void visit(BlockStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(BreakStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);

    }

    @Override
    public void visit(WhileStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);

    }


    @Override
    public void visit(MethodCallExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
        //System.out.println("MethodCallExpr" + n.asMethodCallExpr().getName());
    }

    @Override
    public void visit(SwitchStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(ThrowStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }


    @Override
    public void visit(SuperExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);

    }

    @Override
    public void visit(ReturnStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);

    }

    @Override
    public void visit(CatchClause n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);

    }


    @Override
    public void visit(ContinueStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);

    }

    @Override
    public void visit(AssertStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(ForeachStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);

    }

    @Override
    public void visit(ExpressionStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(VariableDeclarator n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
        //System.out.println("VariableDelcarator  " + n.getName());


    }

    @Override
    public void visit(ConstructorDeclaration n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
        //System.out.println("ConstructorDeclaration" + n.getNameAsString());


    }

    @Override
    public void visit(FieldDeclaration n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);

    }

    @Override
    public void visit(SynchronizedStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);

    }

    @Override
    public void visit(SwitchEntryStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);

    }

    @Override
    public void visit(NameExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
       // System.out.println("NameExpr" + n.toString());
    }

    @Override
    public void visit(IntegerLiteralExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(ClassExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
        //System.out.println("Class Expr  " + n.asClassExpr().asClassExpr().toClassExpr().toString());
       // System.out.println("Class Expr  " + n.getTypeAsString());
    }

    @Override
    public void visit(CharLiteralExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(StringLiteralExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(LongLiteralExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(DoubleLiteralExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(BooleanLiteralExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(ArrayInitializerExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(CastExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(ThisExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(Parameter n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(UnaryExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(AssignExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(BinaryExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(ConditionalExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(VariableDeclarationExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }
    //TODO

    @Override
    public void visit(TypeExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(UnionType n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(NullLiteralExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(InitializerDeclaration n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(LambdaExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(TypeParameter n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(AnnotationDeclaration n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(AnnotationMemberDeclaration n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(ArrayCreationExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(ClassOrInterfaceType n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
        //System.out.println("ClassOrInterfaceType " + n.asString());

    }

    @Override
    public void visit(VarType n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(FieldAccessExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(ObjectCreationExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }

    @Override
    public void visit(MethodReferenceExpr n, Integer arg) {
        out(n, arg);
        super.visit(n, arg + 1);
    }
}
