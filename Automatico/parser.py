# Yacc parser

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexer import tokens

# 1-10 Productions
def p_program(p):
	'''program : declarationList'''
	#print("Program")
	pass

def p_declaration_list(p):
	'''declarationList : declarationList declaration 
 											| declaration '''
	#print("Declaration list")
	pass

def p_declaration(p):
	'''declaration : varDeclaration 
 									| funDeclaration
          				| comment'''
	#print("Declaration")
	pass


def p_comment(p):
	'''comment : BLOCKCOMMENT'''
	#print("Comment")
	pass


def p_var_declaration(p):
	'varDeclaration : typeSpecifier varDeclList SEMMICOLON'
	#print("Single Var Declaration")
	pass


def p_var_dec_list(p):
	'''varDeclList : varDeclList COMMA varDecInitialize 
 									| varDecInitialize'''
	#print("Other Single Var Declaration")
	pass

def p_var_dec_initialize(p):
	'''varDecInitialize : varDeclId 
											| varDeclId ASSIGMENT simpleExpression'''
	#print("Var Declaration Initialize")
	pass

def p_var_dec_id(p):
	'''varDeclId : IDENTIFIER '''
	#print("Var Declaration Id")
	pass

def p_array_var_dec_id(p):
	'''varDeclId : IDENTIFIER LBRACKET INTNUMBER RBRACKET'''
	#print("Array Var Declaration Id")
	pass

def p_type_specifer(p):
	'''typeSpecifier : INT 
 				| FLOAT 
     		| CHAR 
				| BOOL 
    		| VOID'''
	#print("Data type")
	pass

def p_fun_declaration(p):
	'funDeclaration : typeSpecifier IDENTIFIER LPAREN params RPAREN statement'
	#print("Fun declaration")
	pass


def p_params(p):
	'''params : paramList 
 						| empty'''
	#print("Params")
	pass


def p_param_list(p):
	'''paramList : paramList SEMMICOLON paramTypeList 
 								| paramTypeList'''
	#print("Param List")
	pass

# 11
def p_param_type_list(p):
	'''paramTypeList : typeSpecifier paramIdList'''
	#print("Argument Type List")
	pass

def p_param_id_list(p):
	'''paramIdList : paramIdList COMMA paramId
			| paramId '''
	#print("Arguments Id List")
	pass

def p_param_id(p):
	'''paramId : IDENTIFIER '''
	#print("Argument Id ")
	pass

def p_array_param_id(p):
	'''paramId : IDENTIFIER LBRACKET RBRACKET '''
	#print("Argument Array Id ")
	pass

def p_compound_stmt(p):
	'''compoundStmt : LBRACE localDeclarations statementList RBRACE '''
	#print("Compound Statement")
	pass

def p_local_declarations(p):
	'''localDeclarations : localDeclarations varDeclaration
		| empty '''
	#print("Local Declarations")
	pass

def p_statement_list(p):
	'''statementList : statementList statement
		| empty  
		| comment'''
	#print("Statement List")
	pass

def p_statement(p):
	'''statement : expressionStmt
		| compoundStmt
		| selectionStmt
		| iterationStmt
		| returnStmt
		| breakStmt '''
	#print("Statement")
	pass

def p_expression_stmt(p):
	'''expressionStmt : expression SEMMICOLON        
		| SEMMICOLON '''
	#print("Expression Statement End")
	pass

def p_selection_statement(p):
	'''selectionStmt : IF LPAREN expression RPAREN statement'''
	#print("IF Statement")
	pass

def p_selection_statement_else(p):
	'''selectionStmt : IF LPAREN expression RPAREN statement ELSE statement'''
	#print("IF/ELSE Statement")
	pass

# 20
def p_iteration_statement(p):
	'''iterationStmt : WHILE LPAREN expression RPAREN statement'''
	#print("Iteration While Statement")
	pass

def p_iteration_for_statement(p):
	'''iterationStmt : FOR LPAREN IDENTIFIER IN IDENTIFIER RPAREN statement'''
	#print("Iteration For Statement")
	pass

def p_iteration_do_while_statement(p):
	'''iterationStmt : DO statement WHILE LPAREN expression RPAREN statement'''
	#print("Iteration Do While Statement")
	pass

def p_return_statement(p):
	'''returnStmt : RETURN  SEMMICOLON
			| RETURN expression SEMMICOLON'''
	#print("Return Statement")
	pass

def p_break_stmt(p):
	'''breakStmt : BREAK SEMMICOLON '''
	#print("Break Statement")
	pass

def p_expression(p):
	'''expression : IDENTIFIER ASSIGMENT expression
		| IDENTIFIER PLUS ASSIGMENT expression
		| IDENTIFIER MINUS ASSIGMENT expression
		| simpleExpression '''
	#print("Expression")
	pass

def p_var(p):
	'''var : IDENTIFIER
		| IDENTIFIER LBRACKET expression RBRACKET '''
	#print("Var")
	pass

def p_simple_expression(p):
	'''simpleExpression : simpleExpression OR orExpression 
		| orExpression'''
	#print("Simple Expression")
	pass

def p_or_expression(p):
	'''orExpression : orExpression AND unaryRelExpression
		| unaryRelExpression'''
	#print("OR Expression")
	pass

def p_unary_rel_expression(p):    
	'''unaryRelExpression : NOT unaryRelExpression 
			| relExpression'''
	#print("Unary Rel Expression")
	pass

def p_rel_expression(p):
	'''relExpression : addExpression relop addExpression
		| addExpression'''
	#print("Rel Expression")
	pass

def p_greater_relop(p):
	'''relop : GREATER'''
	#print("Relop Expression Greater")
	pass

def p_lower_relop(p):
	'''relop : LOWER'''
	#print("Relop Expression Lower")
	pass

def p_equals_relop(p):
	'''relop : EQUALS'''
	#print("Relop Expression Equals")
	pass

def p_gratherthan_relop(p):
	'''relop : GREATERTHAN'''
	#print("Relop Expression GREATERTHAN")
	pass

def p_lowerthan_relop(p):
	'''relop : LOWERTHAN'''
	#print("Relop Expression LOWERTHAN")
	pass

# 30
def p_add_expression(p):
	'''addExpression : addExpression addop term
							| term'''
	#print("SUM OR MIN Expression")
	pass

def p_addop_plus(p):
	'''addop : PLUS'''
	#print("Plus")
	pass

def p_addop_minus(p):
	'''addop : MINUS'''
	#print("Minus")
	pass

def p_term(p):
	'''term : term mulop unaryExpression
					| unaryExpression'''
	#print("TIMES, DIVIDE OR MOD Term Expression")
	pass

def p_mulop_times(p):
	'''mulop : TIMES'''
	#print("Mulop Expression TIMES")
	pass

def p_mulop_divide(p):
	'''mulop : DIVIDE '''
	#print("Mulop Expression DIVIDE")
	pass

def p_mulop_mod(p):
	'''mulop : MOD'''
	#print("Mulop Expression MOD")
	pass

def p_unary_expression(p):
	'''unaryExpression : unaryExpression
							| factor'''
	#print("Unary Expression")
	pass

def p_factor(p):
	'''factor : LBRACKET expression RBRACKET
							| var
							| call
							| constant'''
	#print("factor")
	pass

def p_constant_int(p):
	'''constant : INTNUMBER'''
	#print("Constant Expression INTNUMBER")
	pass

def p_constant_float(p):
	'''constant : FLOATNUMBER'''
	#print("Constant Expression FLOATNUMBER")
	pass

def p_constant_false(p):
	'''constant : FALSE'''
	#print("Constant Expression FALSE")
	pass

def p_constant_true(p):
	'''constant : TRUE '''
	#print("Constant Expression TRUE")
	pass

def p_call(p):
	'''call : IDENTIFIER LBRACKET args RBRACKET '''
	#print("call Expression")
	pass

def p_args(p):
	'''args : argList
					| empty '''
	#print("Args Expression")
	pass

def p_arg_list(p):
	'''argList : argList COMMA expression
							| expression '''
	#print("Arg List Expression")
	pass

def p_empty(p):
	'empty :'
	pass

# Error rule for syntax errors
def p_error(p):
	print(p)
	print("Syntax error, unexpected token: ", p.type, " with value: '", p.value, "'",
				" at line: ", p.lineno - 4, " position: ", p.lexpos)
 
# Build the parser

def readSource(fd):
    with open(fd, 'r') as file:
        data = file.read()
    return parserData(data)


def parserData(data):
	parser = yacc.yacc()
	result = parser.parse(data)
	print(result)

readSource('../Examples/SuccessfulExample.c')



