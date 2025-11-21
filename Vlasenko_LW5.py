from dataclasses import dataclass
import math

# 1. Комплексні числа
@dataclass(frozen = True)
class Real:
    real: float

@dataclass(frozen = True)
class Imaginary:
    imaginary: float

@dataclass(frozen = True)
class Complex:
    real: Real
    imaginary: Imaginary

def sum_complex(c1: Complex, c2: Complex) -> Complex:
    match c1, c2:
        case (Complex(real = Real(real = r1), imaginary = Imaginary(imaginary = i1)),
              Complex(real = Real(real = r2), imaginary = Imaginary(imaginary = i2))):
            new_real = Real(r1 + r2)
            new_imaginary = Imaginary(i1 + i2)
            return Complex(new_real, new_imaginary)
        case _:
            return TypeError("Не тип Complex.")

def dif_complex(c1: Complex, c2: Complex) -> Complex:
    match c1, c2:
        case (Complex(real = Real(real = r1), imaginary = Imaginary(imaginary =i1)),
              Complex(real = Real(real = r2), imaginary = Imaginary(imaginary = i2))):
            new_real = Real(r1 - r2)
            new_imaginary = Imaginary(i1 - i2)
            return Complex(new_real, new_imaginary)
        case _:
            return TypeError("Не тип Complex.")
        
def prod_complex(c1: Complex, c2: Complex) -> Complex:
    match c1, c2:
        case (Complex(Real(r1), Imaginary(i1)),
              Complex(Real(r2), Imaginary(i2))):
            return Complex(Real(r1 * r2 - i1 * i2), Imaginary(r1 * i2 + i1 * r2))
        case _:
            return TypeError("Не тип Complex.")

def conj_complex(c: Complex) -> Complex:
    match c1, c2:
        case (Complex(Real(r1), Imaginary(i1))):
            return Complex(Real(r1), Imaginary(-i1))
        case _:
            return TypeError("Не тип Complex.")

def mod_complex(c: Complex) -> float:
    match c1, c2:
        case (Complex(Real(r1), Imaginary(i1))):
            return math.sqrt(r1 ** 2 + i1 ** 2)
        case _:
            return TypeError("Не тип Complex.")

# 2. Вектори 2D (Vector2) і базові операції
@dataclass(frozen = True)
class Vector2:
    x: float
    y: float

def norm_vector2(v: Vector2) -> float:
    match v:
        case (Vector2(x, y)):
            return math.sqrt(x ** 2 + y ** 2)
        case _:
            return TypeError("Не тип Vector2")

def dot_vector2(v1: Vector2, v2: Vector2) -> float:
    match v1, v2:
        case (Vector2(x1, y1),
              Vector2(x2, y2)):
            return x1 * x2 + y1 * y2
        case _:
            return TypeError("Не тип Vector2")
        
# 3. Матриця 2x2 і лінійні перетворення
@dataclass(frozen = True)
class Matrix2x2:
    x11: float; x12: float
    x21: float; x22: float

def det_matrix2x2(m: Matrix2x2) -> float:
    match m:
        case (Matrix2x2(x11, x12, x21, x22)):
            return x11 * x22 + x12 * x21
        case _:
            return TypeError("Не тип Matrix2x2")

def inv_matrix2x2(m: Matrix2x2) -> Matrix2x2:
    match m:
        case (Matrix2x2(x11, x12, x21, x22)):
            return x11 * x22 + x12 * x21
        case _:
            return TypeError("Не тип Matrix2x2")
        
def prod_matrix2x2(m1: Matrix2x2, m2: Matrix2x2) -> float:
    match m1, m2:
        case (Matrix2x2(x11, x12, x21, x22), Matrix2x2(y11, y12, y21, y22)):
            return Matrix2x2(x11 * y11 + x12 * y21, x11 * y12 + x12 * y22,
                             x21 * y11 + x22 * y21, x21 * y12 + x22 * y22)
        case _:
            return TypeError("Не тип Matrix2x2")