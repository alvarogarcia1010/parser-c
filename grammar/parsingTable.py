S = 0
S1 = 1
I = 2
S2 = 3
Z = 4
C = 5
J = 6
B = 7
D = 8
G = 9
T = 10
R = 11
N = 12
P = 13
L = 14
H = 15
E = 16
K = 17
U = 18
V = 19
Q = 20
A = 21
W = 22
F1 = 23

terminales = (
  'INT',
  'FLOAT',
  'CHAR',
  'IF',
  'ELSE',
  'MAIN',
  'RETURN',
  'IDENTIFIER',
  'COMMA',
  'INT_VAL',
  'ASIGNACION',
  'APOSTROFE',
  'FLOAT_VAL',
  'SEMICOLON',
  'BLOCK_START',
  'BLOCK_END',
  'OPENING_BRACKET',
  'CLOSING_BRACKET',
  'OPENING_PARENTHESIS',
  'CLOSING_PARENTHESIS',
  'MAYOR',
  'MENOR',
  'EQUAL',
  'NO_EQUAL',
  'AND',
  'SUM',
  'SUBTRACT',
  'MULTIPLICATION',
  'DIVISION',
  'MODULO',
  'EOF'
)

parsingTable = [
  [S, 'IDENTIFIER', None],
  [S, 'COMMA', None],
  [S, 'OPENING_BRACKET', None],
  [S, 'INT_VAL', None],
  [S, 'CLOSING_BRACKET', None],
  [S, 'ASIGNACION', None],
  [S, 'APOSTROFE', None],
  [S, 'FLOAT_VAL', None],
  [S, 'SEMICOLON', None],
  [S, 'BLOCK_START', None],
  [S, 'BLOCK_END', None],
  [S, 'INT', ['INT', 'MAIN', 'OPENING_PARENTHESIS', 'CLOSING_PARENTHESIS', 'BLOCK_START', S1, 'RETURN', 'INT_VAL', 'SEMICOLON', 'BLOCK_END']],
  [S, 'FLOAT', None],
  [S, 'CHAR', None],
  [S, 'MAIN', None],
  [S, 'OPENING_PARENTHESIS', None],
  [S, 'CLOSING_PARENTHESIS', None],
  [S, 'RETURN', None],
  [S, 'MAYOR', None],
  [S, 'MENOR', None],
  [S, 'EQUAL', None],
  [S, 'NO_EQUAL', None],
  [S, 'AND', None],
  [S, 'IF', None],
  [S, 'ELSE', None],
  [S, 'SUM', None],
  [S, 'SUBTRACT', None],
  [S, 'MULTIPLICATION', None],
  [S, 'DIVISION', None],
  [S, 'MODULO', None],
  [S, 'EOF', ['vacia']], # S1

  [S1, 'IDENTIFIER', [Z, S1]],
  [S1, 'COMMA', None],
  [S1, 'OPENING_BRACKET', None],
  [S1, 'INT_VAL', None],
  [S1, 'CLOSING_BRACKET', None],
  [S1, 'ASIGNACION', None],
  [S1, 'APOSTROFE', None],
  [S1, 'FLOAT_VAL', None],
  [S1, 'SEMICOLON', None],
  [S1, 'BLOCK_START', None],
  [S1, 'BLOCK_END', ['vacia']],
  [S1, 'INT', [S2, S1]],
  [S1, 'FLOAT', [S2, S1]],
  [S1, 'CHAR', [S2, S1]],
  [S1, 'MAIN', None],
  [S1, 'OPENING_PARENTHESIS', None],
  [S1, 'CLOSING_PARENTHESIS', None],
  [S1, 'RETURN', ['vacia']],
  [S1, 'MAYOR', None],
  [S1, 'MENOR', None],
  [S1, 'EQUAL', None],
  [S1, 'NO_EQUAL', None],
  [S1, 'AND', None],
  [S1, 'IF', [I, S1]],
  [S1, 'ELSE', None],
  [S1, 'SUM', None],
  [S1, 'SUBTRACT', None],
  [S1, 'MULTIPLICATION', None],
  [S1, 'DIVISION', None],
  [S1, 'MODULO', None],
  [S1, 'EOF', None], # I

  [I, 'IDENTIFIER', None],
  [I, 'COMMA', None],
  [I, 'OPENING_BRACKET', None],
  [I, 'INT_VAL', None],
  [I, 'CLOSING_BRACKET', None],
  [I, 'ASIGNACION', None],
  [I, 'APOSTROFE', None],
  [I, 'FLOAT_VAL', None],
  [I, 'SEMICOLON', None],
  [I, 'BLOCK_START', None],
  [I, 'BLOCK_END', None],
  [I, 'INT', None],
  [I, 'FLOAT', None],
  [I, 'CHAR', None],
  [I, 'MAIN', None],
  [I, 'OPENING_PARENTHESIS', None],
  [I, 'CLOSING_PARENTHESIS', None],
  [I, 'RETURN', None],
  [I, 'MAYOR', None],
  [I, 'MENOR', None],
  [I, 'EQUAL', None],
  [I, 'NO_EQUAL', None],
  [I, 'AND', None],
  [I, 'IF', ['IF', 'OPENING_PARENTHESIS', C, 'CLOSING_PARENTHESIS', 'BLOCK_START', S1, 'BLOCK_END', J]],
  [I, 'ELSE', None],
  [I, 'SUM', None],
  [I, 'SUBTRACT', None],
  [I, 'MULTIPLICATION', None],
  [I, 'DIVISION', None],
  [I, 'MODULO', None],
  [I, 'EOF', None], # S2

  [S2, 'IDENTIFIER', None],
  [S2, 'COMMA', None],
  [S2, 'OPENING_BRACKET', None],
  [S2, 'INT_VAL', None],
  [S2, 'CLOSING_BRACKET', None],
  [S2, 'ASIGNACION', None],
  [S2, 'APOSTROFE', None],
  [S2, 'FLOAT_VAL', None],
  [S2, 'SEMICOLON', None],
  [S2, 'BLOCK_START', None],
  [S2, 'BLOCK_END', None],
  [S2, 'INT', [T, 'IDENTIFIER', R]],
  [S2, 'FLOAT', [T, 'IDENTIFIER', R]],
  [S2, 'CHAR', [T, 'IDENTIFIER', R]],
  [S2, 'MAIN', None],
  [S2, 'OPENING_PARENTHESIS', None],
  [S2, 'CLOSING_PARENTHESIS', None],
  [S2, 'RETURN', None],
  [S2, 'MAYOR', None],
  [S2, 'MENOR', None],
  [S2, 'EQUAL', None],
  [S2, 'NO_EQUAL', None],
  [S2, 'AND', None],
  [S2, 'IF', None],
  [S2, 'ELSE', None],
  [S2, 'SUM', None],
  [S2, 'SUBTRACT', None],
  [S2, 'MULTIPLICATION', None],
  [S2, 'DIVISION', None],
  [S2, 'MODULO', None],
  [S2, 'EOF', None], # Z

  [Z, 'IDENTIFIER', ['IDENTIFIER', 'ASIGNACION', E, 'SEMICOLON']],
  [Z, 'COMMA', None],
  [Z, 'OPENING_BRACKET', None],
  [Z, 'INT_VAL', None],
  [Z, 'CLOSING_BRACKET', None],
  [Z, 'ASIGNACION', None],
  [Z, 'APOSTROFE', None],
  [Z, 'FLOAT_VAL', None],
  [Z, 'SEMICOLON', None],
  [Z, 'BLOCK_START', None],
  [Z, 'BLOCK_END', None],
  [Z, 'INT', None],
  [Z, 'FLOAT', None],
  [Z, 'CHAR', None],
  [Z, 'MAIN', None],
  [Z, 'OPENING_PARENTHESIS', None],
  [Z, 'CLOSING_PARENTHESIS', None],
  [Z, 'RETURN', None],
  [Z, 'MAYOR', None],
  [Z, 'MENOR', None],
  [Z, 'EQUAL', None],
  [Z, 'NO_EQUAL', None],
  [Z, 'AND', None],
  [Z, 'IF', None],
  [Z, 'ELSE', None],
  [Z, 'SUM', None],
  [Z, 'SUBTRACT', None],
  [Z, 'MULTIPLICATION', None],
  [Z, 'DIVISION', None],
  [Z, 'MODULO', None],
  [Z, 'EOF', None], # C

  [C, 'IDENTIFIER', [B, D, B, G]],
  [C, 'COMMA', None],
  [C, 'OPENING_BRACKET', None],
  [C, 'INT_VAL', [B, D, B, G]],
  [C, 'CLOSING_BRACKET', None],
  [C, 'ASIGNACION', None],
  [C, 'APOSTROFE', None],
  [C, 'FLOAT_VAL', None],
  [C, 'SEMICOLON', None],
  [C, 'BLOCK_START', None],
  [C, 'BLOCK_END', None],
  [C, 'INT', None],
  [C, 'FLOAT', None],
  [C, 'CHAR', None],
  [C, 'MAIN', None],
  [C, 'OPENING_PARENTHESIS', None],
  [C, 'CLOSING_PARENTHESIS', None],
  [C, 'RETURN', None],
  [C, 'MAYOR', None],
  [C, 'MENOR', None],
  [C, 'EQUAL', None],
  [C, 'NO_EQUAL', None],
  [C, 'AND', None],
  [C, 'IF', None],
  [C, 'ELSE', None],
  [C, 'SUM', None],
  [C, 'SUBTRACT', None],
  [C, 'MULTIPLICATION', None],
  [C, 'DIVISION', None],
  [C, 'MODULO', None],
  [C, 'EOF', None], # J 

  [J, 'IDENTIFIER', ['vacia']],
  [J, 'COMMA', None],
  [J, 'OPENING_BRACKET', None],
  [J, 'INT_VAL', None],
  [J, 'CLOSING_BRACKET', None],
  [J, 'ASIGNACION', None],
  [J, 'APOSTROFE', None],
  [J, 'FLOAT_VAL', None],
  [J, 'SEMICOLON', None],
  [J, 'BLOCK_START', None],
  [J, 'BLOCK_END', None],
  [J, 'INT', ['vacia']],
  [J, 'FLOAT', ['vacia']],
  [J, 'CHAR', ['vacia']],
  [J, 'MAIN', None],
  [J, 'OPENING_PARENTHESIS', None],
  [J, 'CLOSING_PARENTHESIS', None],
  [J, 'RETURN', None],
  [J, 'MAYOR', None],
  [J, 'MENOR', None],
  [J, 'EQUAL', None],
  [J, 'NO_EQUAL', None],
  [J, 'AND', None],
  [J, 'IF', ['vacia']],
  [J, 'ELSE', ['ELSE', 'BLOCK_START', S1, 'BLOCK_END']],
  [J, 'SUM', None],
  [J, 'SUBTRACT', None],
  [J, 'MULTIPLICATION', None],
  [J, 'DIVISION', None],
  [J, 'MODULO', None],
  [J, 'EOF', None], # B 

  [B, 'IDENTIFIER', ['IDENTIFIER']],
  [B, 'COMMA', None],
  [B, 'OPENING_BRACKET', None],
  [B, 'INT_VAL', ['INT_VAL']],
  [B, 'CLOSING_BRACKET', None],
  [B, 'ASIGNACION', None],
  [B, 'APOSTROFE', None],
  [B, 'FLOAT_VAL', None],
  [B, 'SEMICOLON', None],
  [B, 'BLOCK_START', None],
  [B, 'BLOCK_END', None],
  [B, 'INT', None],
  [B, 'FLOAT', None],
  [B, 'CHAR', None],
  [B, 'MAIN', None],
  [B, 'OPENING_PARENTHESIS', None],
  [B, 'CLOSING_PARENTHESIS', None],
  [B, 'RETURN', None],
  [B, 'MAYOR', None],
  [B, 'MENOR', None],
  [B, 'EQUAL', None],
  [B, 'NO_EQUAL', None],
  [B, 'AND', None],
  [B, 'IF', None],
  [B, 'ELSE', None],
  [B, 'SUM', None],
  [B, 'SUBTRACT', None],
  [B, 'MULTIPLICATION', None],
  [B, 'DIVISION', None],
  [B, 'MODULO', None],
  [B, 'EOF', None], # D

  [D, 'IDENTIFIER', None],
  [D, 'COMMA', None],
  [D, 'OPENING_BRACKET', None],
  [D, 'INT_VAL', None],
  [D, 'CLOSING_BRACKET', None],
  [D, 'ASIGNACION', None],
  [D, 'APOSTROFE', None],
  [D, 'FLOAT_VAL', None],
  [D, 'SEMICOLON', None],
  [D, 'BLOCK_START', None],
  [D, 'BLOCK_END', None],
  [D, 'INT', None],
  [D, 'FLOAT', None],
  [D, 'CHAR', None],
  [D, 'MAIN', None],
  [D, 'OPENING_PARENTHESIS', None],
  [D, 'CLOSING_PARENTHESIS', None],
  [D, 'RETURN', None],
  [D, 'MAYOR', ['MAYOR']],
  [D, 'MENOR', ['MENOR']],
  [D, 'EQUAL', ['EQUAL']],
  [D, 'NO_EQUAL', ['NO_EQUAL']],
  [D, 'AND', ['AND']],
  [D, 'IF', None],
  [D, 'ELSE', None],
  [D, 'SUM', None],
  [D, 'SUBTRACT', None],
  [D, 'MULTIPLICATION', None],
  [D, 'DIVISION', None],
  [D, 'MODULO', None],
  [D, 'EOF', None], # S1 

  [G, 'IDENTIFIER', None],
  [G, 'COMMA', None],
  [G, 'OPENING_BRACKET', None],
  [G, 'INT_VAL', None],
  [G, 'CLOSING_BRACKET', None],
  [G, 'ASIGNACION', None],
  [G, 'APOSTROFE', None],
  [G, 'FLOAT_VAL', None],
  [G, 'SEMICOLON', None],
  [G, 'BLOCK_START', None],
  [G, 'BLOCK_END', None],
  [G, 'INT', None],
  [G, 'FLOAT', None],
  [G, 'CHAR', None],
  [G, 'MAIN', None],
  [G, 'OPENING_PARENTHESIS', None],
  [G, 'CLOSING_PARENTHESIS', ['vacia']],
  [G, 'RETURN', None],
  [G, 'MAYOR', [D, B, G]],
  [G, 'MENOR', [D, B, G]],
  [G, 'EQUAL', [D, B, G]],
  [G, 'NO_EQUAL', [D, B, G]],
  [G, 'AND', [D, B, G]],
  [G, 'IF', None],
  [G, 'ELSE', None],
  [G, 'SUM', None],
  [G, 'SUBTRACT', None],
  [G, 'MULTIPLICATION', None],
  [G, 'DIVISION', None],
  [G, 'MODULO', None],
  [G, 'EOF', None], # T 

  [T, 'IDENTIFIER', None],
  [T, 'COMMA', None],
  [T, 'OPENING_BRACKET', None],
  [T, 'INT_VAL', None],
  [T, 'CLOSING_BRACKET', None],
  [T, 'ASIGNACION', None],
  [T, 'APOSTROFE', None],
  [T, 'FLOAT_VAL', None],
  [T, 'SEMICOLON', None],
  [T, 'BLOCK_START', None],
  [T, 'BLOCK_END', None],
  [T, 'INT', ['INT']],
  [T, 'FLOAT', ['FLOAT']],
  [T, 'CHAR', ['CHAR']],
  [T, 'MAIN', None],
  [T, 'OPENING_PARENTHESIS', None],
  [T, 'CLOSING_PARENTHESIS', None],
  [T, 'RETURN', None],
  [T, 'MAYOR', None],
  [T, 'MENOR', None],
  [T, 'EQUAL', None],
  [T, 'NO_EQUAL', None],
  [T, 'AND', None],
  [T, 'IF', None],
  [T, 'ELSE', None],
  [T, 'SUM', None],
  [T, 'SUBTRACT', None],
  [T, 'MULTIPLICATION', None],
  [T, 'DIVISION', None],
  [T, 'MODULO', None],
  [T, 'EOF', None], # R

  [R, 'IDENTIFIER', None],
  [R, 'COMMA', ['COMMA', 'IDENTIFIER', R]],
  [R, 'OPENING_BRACKET', ['OPENING_BRACKET', 'INT_VAL', 'CLOSING_BRACKET', N]],
  [R, 'INT_VAL', None],
  [R, 'CLOSING_BRACKET', None],
  [R, 'ASIGNACION', ['ASIGNACION', P]],
  [R, 'APOSTROFE', None],
  [R, 'FLOAT_VAL', None],
  [R, 'SEMICOLON', ['SEMICOLON']],
  [R, 'BLOCK_START', None],
  [R, 'BLOCK_END', None],
  [R, 'INT', None],
  [R, 'FLOAT', None],
  [R, 'CHAR', None],
  [R, 'MAIN', None],
  [R, 'OPENING_PARENTHESIS', None],
  [R, 'CLOSING_PARENTHESIS', None],
  [R, 'RETURN', None],
  [R, 'MAYOR', None],
  [R, 'MENOR', None],
  [R, 'EQUAL', None],
  [R, 'NO_EQUAL', None],
  [R, 'AND', None],
  [R, 'IF', None],
  [R, 'ELSE', None],
  [R, 'SUM', None],
  [R, 'SUBTRACT', None],
  [R, 'MULTIPLICATION', None],
  [R, 'DIVISION', None],
  [R, 'MODULO', None],
  [R, 'EOF', None], # N

  [N, 'IDENTIFIER', None],
  [N, 'COMMA', ['COMMA', 'IDENTIFIER', R]],
  [N, 'OPENING_BRACKET', None],
  [N, 'INT_VAL', None],
  [N, 'CLOSING_BRACKET', None],
  [N, 'ASIGNACION', ['ASIGNACION', 'BLOCK_START', 'INT_VAL', U]],
  [N, 'APOSTROFE', None],
  [N, 'FLOAT_VAL', None],
  [N, 'SEMICOLON', ['SEMICOLON']],
  [N, 'BLOCK_START', None],
  [N, 'BLOCK_END', None],
  [N, 'INT', None],
  [N, 'FLOAT', None],
  [N, 'CHAR', None],
  [N, 'MAIN', None],
  [N, 'OPENING_PARENTHESIS', None],
  [N, 'CLOSING_PARENTHESIS', None],
  [N, 'RETURN', None],
  [N, 'MAYOR', None],
  [N, 'MENOR', None],
  [N, 'EQUAL', None],
  [N, 'NO_EQUAL', None],
  [N, 'AND', None],
  [N, 'IF', None],
  [N, 'ELSE', None],
  [N, 'SUM', None],
  [N, 'SUBTRACT', None],
  [N, 'MULTIPLICATION', None],
  [N, 'DIVISION', None],
  [N, 'MODULO', None],
  [N, 'EOF', None], # P

  [P, 'IDENTIFIER', None],
  [P, 'COMMA', None],
  [P, 'OPENING_BRACKET', None],
  [P, 'INT_VAL', [L, H]],
  [P, 'CLOSING_BRACKET', None],
  [P, 'ASIGNACION', None],
  [P, 'APOSTROFE', ['APOSTROFE', 'IDENTIFIER', 'APOSTROFE', K]],
  [P, 'FLOAT_VAL', [L, H]],
  [P, 'SEMICOLON', None],
  [P, 'BLOCK_START', None],
  [P, 'BLOCK_END', None],
  [P, 'INT', None],
  [P, 'FLOAT', None],
  [P, 'CHAR', None],
  [P, 'MAIN', None],
  [P, 'OPENING_PARENTHESIS', None],
  [P, 'CLOSING_PARENTHESIS', None],
  [P, 'RETURN', None],
  [P, 'MAYOR', None],
  [P, 'MENOR', None],
  [P, 'EQUAL', None],
  [P, 'NO_EQUAL', None],
  [P, 'AND', None],
  [P, 'IF', None],
  [P, 'ELSE', None],
  [P, 'SUM', None],
  [P, 'SUBTRACT', None],
  [P, 'MULTIPLICATION', None],
  [P, 'DIVISION', None],
  [P, 'MODULO', None],
  [P, 'EOF', None], # L

  [L, 'IDENTIFIER', None],
  [L, 'COMMA', None],
  [L, 'OPENING_BRACKET', None],
  [L, 'INT_VAL', ['INT_VAL']],
  [L, 'CLOSING_BRACKET', None],
  [L, 'ASIGNACION', None],
  [L, 'APOSTROFE', None],
  [L, 'FLOAT_VAL', ['FLOAT_VAL']],
  [L, 'SEMICOLON', None],
  [L, 'BLOCK_START', None],
  [L, 'BLOCK_END', None],
  [L, 'INT', None],
  [L, 'FLOAT', None],
  [L, 'CHAR', None],
  [L, 'MAIN', None],
  [L, 'OPENING_PARENTHESIS', None],
  [L, 'CLOSING_PARENTHESIS', None],
  [L, 'RETURN', None],
  [L, 'MAYOR', None],
  [L, 'MENOR', None],
  [L, 'EQUAL', None],
  [L, 'NO_EQUAL', None],
  [L, 'AND', None],
  [L, 'IF', None],
  [L, 'ELSE', None],
  [L, 'SUM', None],
  [L, 'SUBTRACT', None],
  [L, 'MULTIPLICATION', None],
  [L, 'DIVISION', None],
  [L, 'MODULO', None],
  [L, 'EOF', None], # H

  [H, 'IDENTIFIER', None],
  [H, 'COMMA', ['COMMA', 'IDENTIFIER', R]],
  [H, 'OPENING_BRACKET', None],
  [H, 'INT_VAL', None],
  [H, 'CLOSING_BRACKET', None],
  [H, 'ASIGNACION', None],
  [H, 'APOSTROFE', None],
  [H, 'FLOAT_VAL', None],
  [H, 'SEMICOLON', ['SEMICOLON']],
  [H, 'BLOCK_START', None],
  [H, 'BLOCK_END', None],
  [H, 'INT', None],
  [H, 'FLOAT', None],
  [H, 'CHAR', None],
  [H, 'MAIN', None],
  [H, 'OPENING_PARENTHESIS', None],
  [H, 'CLOSING_PARENTHESIS', None],
  [H, 'RETURN', None],
  [H, 'MAYOR', None],
  [H, 'MENOR', None],
  [H, 'EQUAL', None],
  [H, 'NO_EQUAL', None],
  [H, 'AND', None],
  [H, 'IF', None],
  [H, 'ELSE', None],
  [H, 'SUM', None],
  [H, 'SUBTRACT', None],
  [H, 'MULTIPLICATION', None],
  [H, 'DIVISION', None],
  [H, 'MODULO', None],
  [H, 'EOF', None], # E

  [E, 'IDENTIFIER', [Q, A]],
  [E, 'COMMA', None],
  [E, 'OPENING_BRACKET', None],
  [E, 'INT_VAL', [Q, A]],
  [E, 'CLOSING_BRACKET', None],
  [E, 'ASIGNACION', None],
  [E, 'APOSTROFE', None],
  [E, 'FLOAT_VAL', [Q, A]],
  [E, 'SEMICOLON', None],
  [E, 'BLOCK_START', None],
  [E, 'BLOCK_END', None],
  [E, 'INT', None],
  [E, 'FLOAT', None],
  [E, 'CHAR', None],
  [E, 'MAIN', None],
  [E, 'OPENING_PARENTHESIS', [Q, A,]],
  [E, 'CLOSING_PARENTHESIS', None],
  [E, 'RETURN', None],
  [E, 'MAYOR', None],
  [E, 'MENOR', None],
  [E, 'EQUAL', None],
  [E, 'NO_EQUAL', None],
  [E, 'AND', None],
  [E, 'IF', None],
  [E, 'ELSE', None],
  [E, 'SUM', None],
  [E, 'SUBTRACT', None],
  [E, 'MULTIPLICATION', None],
  [E, 'DIVISION', None],
  [E, 'MODULO', None],
  [E, 'EOF', None], # K

  [K, 'IDENTIFIER', None],
  [K, 'COMMA', ['COMMA', 'IDENTIFIER', R]],
  [K, 'OPENING_BRACKET', None],
  [K, 'INT_VAL', None],
  [K, 'CLOSING_BRACKET', None],
  [K, 'ASIGNACION', None],
  [K, 'APOSTROFE', None],
  [K, 'FLOAT_VAL', None],
  [K, 'SEMICOLON', ['SEMICOLON']],
  [K, 'BLOCK_START', None],
  [K, 'BLOCK_END', None],
  [K, 'INT', None],
  [K, 'FLOAT', None],
  [K, 'CHAR', None],
  [K, 'MAIN', None],
  [K, 'OPENING_PARENTHESIS', None],
  [K, 'CLOSING_PARENTHESIS', None],
  [K, 'RETURN', None],
  [K, 'MAYOR', None],
  [K, 'MENOR', None],
  [K, 'EQUAL', None],
  [K, 'NO_EQUAL', None],
  [K, 'AND', None],
  [K, 'IF', None],
  [K, 'ELSE', None],
  [K, 'SUM', None],
  [K, 'SUBTRACT', None],
  [K, 'MULTIPLICATION', None],
  [K, 'DIVISION', None],
  [K, 'MODULO', None],
  [K, 'EOF', None], # U

  [U, 'IDENTIFIER', None],
  [U, 'COMMA', ['COMMA', 'INT_VAL', U]],
  [U, 'OPENING_BRACKET', None],
  [U, 'INT_VAL', None],
  [U, 'CLOSING_BRACKET', None],
  [U, 'ASIGNACION', None],
  [U, 'APOSTROFE', None],
  [U, 'FLOAT_VAL', None],
  [U, 'SEMICOLON', None],
  [U, 'BLOCK_START', None],
  [U, 'BLOCK_END', ['BLOCK_END', V]],
  [U, 'INT', None],
  [U, 'FLOAT', None],
  [U, 'CHAR', None],
  [U, 'MAIN', None],
  [U, 'OPENING_PARENTHESIS', None],
  [U, 'CLOSING_PARENTHESIS', None],
  [U, 'RETURN', None],
  [U, 'MAYOR', None],
  [U, 'MENOR', None],
  [U, 'EQUAL', None],
  [U, 'NO_EQUAL', None],
  [U, 'AND', None],
  [U, 'IF', None],
  [U, 'ELSE', None],
  [U, 'SUM', None],
  [U, 'SUBTRACT', None],
  [U, 'MULTIPLICATION', None],
  [U, 'DIVISION', None],
  [U, 'MODULO', None],
  [U, 'EOF', None], # V

  [V, 'IDENTIFIER', None],
  [V, 'COMMA', ['COMMA', 'IDENTIFIER', R]],
  [V, 'OPENING_BRACKET', None],
  [V, 'INT_VAL', None],
  [V, 'CLOSING_BRACKET', None],
  [V, 'ASIGNACION', None],
  [V, 'APOSTROFE', None],
  [V, 'FLOAT_VAL', None],
  [V, 'SEMICOLON', ['SEMICOLON']],
  [V, 'BLOCK_START', None],
  [V, 'BLOCK_END', None],
  [V, 'INT', None],
  [V, 'FLOAT', None],
  [V, 'CHAR', None],
  [V, 'MAIN', None],
  [V, 'OPENING_PARENTHESIS', None],
  [V, 'CLOSING_PARENTHESIS', None],
  [V, 'RETURN', None],
  [V, 'MAYOR', None],
  [V, 'MENOR', None],
  [V, 'EQUAL', None],
  [V, 'NO_EQUAL', None],
  [V, 'AND', None],
  [V, 'IF', None],
  [V, 'ELSE', None],
  [V, 'SUM', None],
  [V, 'SUBTRACT', None],
  [V, 'MULTIPLICATION', None],
  [V, 'DIVISION', None],
  [V, 'MODULO', None],
  [V, 'EOF', None], # Q

  [Q, 'IDENTIFIER', [F1, W]],
  [Q, 'COMMA', None],
  [Q, 'OPENING_BRACKET', None],
  [Q, 'INT_VAL', [F1, W]],
  [Q, 'CLOSING_BRACKET', None],
  [Q, 'ASIGNACION', None],
  [Q, 'APOSTROFE', None],
  [Q, 'FLOAT_VAL', [F1, W]],
  [Q, 'SEMICOLON', None],
  [Q, 'BLOCK_START', None],
  [Q, 'BLOCK_END', None],
  [Q, 'INT', None],
  [Q, 'FLOAT', None],
  [Q, 'CHAR', None],
  [Q, 'MAIN', None],
  [Q, 'OPENING_PARENTHESIS', [F1, W]],
  [Q, 'CLOSING_PARENTHESIS', None],
  [Q, 'RETURN', None],
  [Q, 'MAYOR', None],
  [Q, 'MENOR', None],
  [Q, 'EQUAL', None],
  [Q, 'NO_EQUAL', None],
  [Q, 'AND', None],
  [Q, 'IF', None],
  [Q, 'ELSE', None],
  [Q, 'SUM', None],
  [Q, 'SUBTRACT', None],
  [Q, 'MULTIPLICATION', None],
  [Q, 'DIVISION', None],
  [Q, 'MODULO', None],
  [Q, 'EOF', None], # A

  [A, 'IDENTIFIER', None],
  [A, 'COMMA', None],
  [A, 'OPENING_BRACKET', None],
  [A, 'INT_VAL', None],
  [A, 'CLOSING_BRACKET', None],
  [A, 'ASIGNACION', None],
  [A, 'APOSTROFE', None],
  [A, 'FLOAT_VAL', None],
  [A, 'SEMICOLON', ['vacia']],
  [A, 'BLOCK_START', None],
  [A, 'BLOCK_END', None],
  [A, 'INT', None],
  [A, 'FLOAT', None],
  [A, 'CHAR', None],
  [A, 'MAIN', None],
  [A, 'OPENING_PARENTHESIS', None],
  [A, 'CLOSING_PARENTHESIS', ['vacia']],
  [A, 'RETURN', None],
  [A, 'MAYOR', None],
  [A, 'MENOR', None],
  [A, 'EQUAL', None],
  [A, 'NO_EQUAL', None],
  [A, 'AND', None],
  [A, 'IF', None],
  [A, 'ELSE', None],
  [A, 'SUM', ['SUM', Q, A]],
  [A, 'SUBTRACT', ['SUBTRACT', Q, A]],
  [A, 'MULTIPLICATION', None],
  [A, 'DIVISION', None],
  [A, 'MODULO', None],
  [A, 'EOF', None], # W

  [W, 'IDENTIFIER', None],
  [W, 'COMMA', None],
  [W, 'OPENING_BRACKET', None],
  [W, 'INT_VAL', None],
  [W, 'CLOSING_BRACKET', None],
  [W, 'ASIGNACION', None],
  [W, 'APOSTROFE', None],
  [W, 'FLOAT_VAL', None],
  [W, 'SEMICOLON', ['vacia']],
  [W, 'BLOCK_START', None],
  [W, 'BLOCK_END', None],
  [W, 'INT', None],
  [W, 'FLOAT', None],
  [W, 'CHAR', None],
  [W, 'MAIN', None],
  [W, 'OPENING_PARENTHESIS', None],
  [W, 'CLOSING_PARENTHESIS', ['vacia']],
  [W, 'RETURN', None],
  [W, 'MAYOR', None],
  [W, 'MENOR', None],
  [W, 'EQUAL', None],
  [W, 'NO_EQUAL', None],
  [W, 'AND', None],
  [W, 'IF', None],
  [W, 'ELSE', None],
  [W, 'SUM', ['vacia']],
  [W, 'SUBTRACT', ['vacia']],
  [W, 'MULTIPLICATION', ['MULTIPLICATION', F1, W]],
  [W, 'DIVISION', ['DIVISION', F1, W]],
  [W, 'MODULO', ['MODULO', F1, W]],
  [W, 'EOF', None], # F1

  [F1, 'IDENTIFIER', ['IDENTIFIER']],
  [F1, 'COMMA', None],
  [F1, 'OPENING_BRACKET', None],
  [F1, 'INT_VAL', ['INT_VAL']],
  [F1, 'CLOSING_BRACKET', None],
  [F1, 'ASIGNACION', None],
  [F1, 'APOSTROFE', None],
  [F1, 'FLOAT_VAL', ['FLOAT_VAL']],
  [F1, 'SEMICOLON', None],
  [F1, 'BLOCK_START', None],
  [F1, 'BLOCK_END', None],
  [F1, 'INT', None],
  [F1, 'FLOAT', None],
  [F1, 'CHAR', None],
  [F1, 'MAIN', None],
  [F1, 'OPENING_PARENTHESIS', ['OPENING_PARENTHESIS', E, 'CLOSING_PARENTHESIS']],
  [F1, 'CLOSING_PARENTHESIS', None],
  [F1, 'RETURN', None],
  [F1, 'MAYOR', None],
  [F1, 'MENOR', None],
  [F1, 'EQUAL', None],
  [F1, 'NO_EQUAL', None],
  [F1, 'AND', None],
  [F1, 'IF', None],
  [F1, 'ELSE', None],
  [F1, 'SUM', None],
  [F1, 'SUBTRACT', None],
  [F1, 'MULTIPLICATION', None],
  [F1, 'DIVISION', None],
  [F1, 'MODULO', None],
  [F1, 'EOF', None]
]