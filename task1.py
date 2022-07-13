import dis


def isEven(value):
    return value % 2 == 0


def f1(value):
    return not value & 1


dis.dis(isEven)
"""
  4           0 LOAD_FAST                0 (value)
              2 LOAD_CONST               1 (2)
              4 BINARY_MODULO
              6 LOAD_CONST               2 (0)
              8 COMPARE_OP               2 (==)
             10 RETURN_VALUE
Интуитивно понятная и простая реализация.
"""
dis.dis(f1)
"""
  9           0 LOAD_FAST                0 (value)
              2 LOAD_CONST               1 (1)
              4 BINARY_AND
              6 UNARY_NOT
              8 RETURN_VALUE
Экономия на количестве операций, однако менее интуитивно
"""