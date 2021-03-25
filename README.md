# Fundamental Concepts

## Compilation Process
1. Lexical Analysis (Lexing) - idenify/break code into tokens
2. Syntax Analysis (Parsing) - create a tree to combine and prioritize execution
3. Semantic Analysis - language specific rules checks, i.e. type/parameter mismatches, use of undeclared variables, etc.
4. Optimization - code is re-written to be more efficient based on techniques the compiler is aware of
5. Code Generation

## Python Execution
1. The Python VM runs Bytecode instructions
2. While Python is an interpreted scripting language, code is actually compiled to Bytecode before execution

## Bytecode Example
```
('f = (c * 9 / 5) + 32')

0 LOAD_NAME				0 (c)
2 LOAD_CONST			0 (9)
4 BINARY_MULTIPLY
6 LOAD_CONST			1 (5)
8 BINARY_TRUE_DIVIDE	
10 LOAD_CONST			2 (32)
12 BINARY_ADD
14 STORE_NAME			1 (f)
16 LOAD_CONST			3 (None)
18 RETURN_VALUE
```

## REPL
1. Read-Evaluate-Print-Loop
2. To access REPL, simply type 'Python' at the CMD prompt
```
>>> exit()
>>> exit()
```