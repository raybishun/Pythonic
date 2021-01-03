# Fundamental Concepts

## Compilation Process

1. Lexical Analysis (Lexing) - idenify/break code into tokens
2. Syntax Analysis (Parsing) - create a tree to combine and prioritize execution
3. Semantic Analysis - specific language rule checks, i.e. type/parameter mismatches, use of undeclared variables, etc.
4. Optimization - code is re-written be more efficient based on techniques the compiler is aware of
5. Code Generation

## Python Execution

1. The Python VM runs Bytecode instructions
2. While Pyhton is an interpreted scripting language, code is actually compiled to Bytecode before execution

## REPL

1. Read-evaluate-print-loop
2. To access, simply type 'Python' at the CMD prompt
3. >>> (is the REPL prompt)
4. >>> exit() - to exit