# Android Debug Bridge Script Generator
# Takes seven different statements and transforms them into a useable script for automating Android tasks

from ADBProgram import *
from ply import lex
import sys

tokens = (
    'LAUNCH',
    'TYPETEXT',
    'PRESS',
    'LONGPRESS',
    'TEXT',
    'HOME',
    'MENU',
    'BACK',
    'POWER',
    'WAIT',
    'DRAG',
    'TYPELINE',
    'SEMICOLON'
)
 
# These are all caught in the IDENT rule, typed there.
reserved = {
    'HOME'          : 'HOME',
    'MENU'          : 'MENU',
    'BACK'          : 'BACK',
    'POWER'         : 'POWER',
    'WAIT'          : 'WAIT',
    'DRAG'          : 'DRAG',
    'LAUNCH'        : 'LAUNCH',
    'TYPETEXT'      : 'TYPETEXT',
    'TYPELINE'      : 'TYPELINE',
    'PRESS'         : 'PRESS',
    'LONGPRESS'     : 'LONGPRESS'
}
 
# t_ignore is special, and does just what it says.  Spaces and tabs
t_ignore = ' \t\n\r'
 
# These are the simple maps
t_SEMICOLON     = r';'
t_LAUNCH        = 'LAUNCH'
t_WAIT          = 'WAIT'
t_TYPETEXT      = 'TYPETEXT'
t_TYPELINE      = 'TYPELINE'
t_PRESS         = 'PRESS'
t_LONGPRESS     = 'LONGPRESS'
t_DRAG          = 'DRAG'


def t_TEXT(t):
    r'[a-zA-Z_0-9_._/]+'
    t.type = reserved.get(t.value, 'TEXT')
    if t.value.isdigit():
        t.value = int(t.value)
    else:
        t.value = str(t.value)

    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print "Illegal character '%s' on line %d" % (t.value[0], t.lexer.lineno)
    return t
 
lex.lex()
 
#-----   LEXER (end)   -------------------------------
 
######   YACC   #####################################
 
import ply.yacc as yacc
 
# create a function for each production (note the prefix)
# The rule is given in the doc string


def p_program(p):
    'program : stmt_list'
    P = Program(p[1])
    P.eval()


def p_stmt_list(p):
    '''stmt_list : stmt SEMICOLON stmt_list
        | stmt SEMICOLON'''
    if len(p) == 3:  # single stmt => new list
        p[0] = StmtList()
        p[0].insert(p[1])
    else:  # we have a stmtList, keep adding to front
        p[3].insert(p[1])
        p[0] = p[3]


def p_stmt( p ) :
    '''stmt : launch_stmt
        | typetext_stmt
        | typeline_stmt
        | press_stmt
        | longpress_stmt
        | home_stmt
        | menu_stmt
        | back_stmt
        | wait_stmt
        | drag_stmt
        | power_stmt'''
    p[0] = p[1]
 

def p_text_list(p):
    '''text_list : TEXT text_list
        | TEXT TEXT'''
    p[0] = p[1] + ' ' + p[2]


def p_launch_stmt(p):
    'launch_stmt : LAUNCH TEXT'
    p[0] = Launch(p[2])
 

def p_wait_stmt(p):
    'wait_stmt : WAIT TEXT'
    p[0] = Wait(p[2])


def p_typetext_stmt(p):
    '''typetext_stmt : TYPETEXT text_list
        | TYPETEXT TEXT'''
    p[0] = TypeText(p[2], False)


def p_typeline_stmt(p):
    '''typeline_stmt : TYPELINE text_list
        | TYPELINE TEXT'''
    p[0] = TypeText(p[2], True)


def p_press_stmt(p):
    'press_stmt : PRESS TEXT TEXT'
    p[0] = PressScreen(p[2], p[3])


def p_longpress_stmt(p):
    'longpress_stmt : LONGPRESS TEXT TEXT'
    p[0] = LongPressScreen(p[2], p[3])


def p_home_stmt(p):
    'home_stmt : HOME'
    p[0] = Home()


def p_menu_stmt(p):
    'menu_stmt : MENU'
    p[0] = Menu()


def p_power_stmt(p):
    'power_stmt : POWER'
    p[0] = Power()


def p_back_stmt(p):
    'back_stmt : BACK'
    p[0] = Back()


def p_drag_stmt(p):
    'drag_stmt : DRAG TEXT TEXT TEXT TEXT'
    p[0] = Drag(p[2], p[3], p[4], p[5])


# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input!", str(p)
    sys.exit(2)

# now, build the parser
yacc.yacc()

data = ""
adbCmds = open(sys.argv[1], "r")

for line in adbCmds:
    data = data + line
 
adbCmds.close()
yacc.parse(data.strip())