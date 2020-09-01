import com.github.javaparser.ast.*;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.modules.*;
import com.github.javaparser.ast.stmt.*;
import com.github.javaparser.ast.type.*;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import Node.ParsingNode;

import java.util.ArrayList;

/**
 * Created by chaebyeonghun on 2018. 2. 25..
 *
 *
 */

public class TreeStructVisitor extends VoidVisitorAdapter<Integer> {

    ArrayList<ParsingNode> parsingNodes = new ArrayList<>();

    public void out(Node n, int indentLevel) {

        parsingNodes.add(new ParsingNode(n.getClass().getSimpleName(), indentLevel));
    }

    public ArrayList<ParsingNode> getParsingNodes() {
        return parsingNodes;
    }

    @Override
    public void visit(final ArrayAccessExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final ArrayCreationExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final ArrayInitializerExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final AssertStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final AssignExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final BinaryExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }


    @Override
    public void visit(final BlockStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final BooleanLiteralExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final BreakStmt n, final Integer arg) {
        out(n, arg);
    }

    @Override
    public void visit(final CastExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final CatchClause n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final CharLiteralExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final ClassExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final ClassOrInterfaceDeclaration n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final ClassOrInterfaceType n, final Integer arg) {
        out(n, arg);
        System.out.println(n.asString());
        System.out.println(n.asClassOrInterfaceType().asString());
        super.visit(n, arg + 1);
    }

   /* @Override
    public void visit(final CompilationUnit n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }*/

    @Override
    public void visit(final ConditionalExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final ConstructorDeclaration n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final ContinueStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);

    }

    @Override
    public void visit(final DoStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final DoubleLiteralExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }


    @Override
    public void visit(final EmptyStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }


    @Override
    public void visit(final EnclosedExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final EnumConstantDeclaration n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final EnumDeclaration n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final ExplicitConstructorInvocationStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final ExpressionStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final FieldAccessExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final FieldDeclaration n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final ForeachStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final ForStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final IfStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final InitializerDeclaration n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final InstanceOfExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final IntegerLiteralExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final LabeledStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final LongLiteralExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);

    }


    @Override
    public void visit(final MemberValuePair n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final MethodCallExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final MethodDeclaration n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final NameExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final NullLiteralExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);

    }

    @Override
    public void visit(final ObjectCreationExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final Parameter n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final PrimitiveType n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    //
    @Override
    public void visit(Name n, Integer arg) {
        //out(n, arg);
    }

    @Override
    public void visit(SimpleName n, Integer arg) {
        //out(n, arg);
        //System.out.println(n.asString());
    }

    @Override
    public void visit(ArrayType n, Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(ArrayCreationLevel n, Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final IntersectionType n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final UnionType n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final ReturnStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final StringLiteralExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final SuperExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final SwitchEntryStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final SwitchStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final SynchronizedStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final ThisExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final ThrowStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final TryStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(LocalClassDeclarationStmt n, Integer arg) {
        super.visit(n, arg);
    }

    @Override
    public void visit(final TypeParameter n, final Integer arg) {
        out(n, arg);

        super.visit(n, arg+1);
    }

    @Override
    public void visit(final UnaryExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final UnknownType n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final VariableDeclarationExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final VariableDeclarator n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }


    @Override
    public void visit(final VoidType n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);

    }

    @Override
    public void visit(final WhileStmt n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(final WildcardType n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(LambdaExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(MethodReferenceExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(TypeExpr n, final Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(ModuleDeclaration n, Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(ModuleRequiresStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(ModuleExportsStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(ModuleProvidesStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(ModuleUsesStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(ModuleOpensStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(UnparsableStmt n, Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(ReceiverParameter n, Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

    @Override
    public void visit(VarType n, Integer arg) {
        out(n, arg);
        super.visit(n, arg+1);
    }

}