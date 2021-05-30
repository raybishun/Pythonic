# -----------------------------------------------------------------------------
# Types: Numbers: Floating-Point Accuracy
# -----------------------------------------------------------------------------
"""
    Floats are stored in memory as binary fractions.
    However, not all decimals can be represented as binary fractions,
    i.e., 0.1 doesn't have a binary fraction equivalent.
    As such, the CPU makes an approximation.
    So be aware of round issues when using Floats; 
    depending on the level of percision, i.e. money,
    a solution might be to convert into cents ( and use integers).
"""
