# Python Operators Overview

The Python language supports **seven types of operators**:

- **Arithmetic operators**
- **Assignment operators**
- **Relational or comparison operators**
- **Logical operators**
- **Membership operators**
- **Identity operators**
- **Bitwise operators**

---

## Arithmetic Operators

Arithmetic operators are used to perform mathematical operations between numeric values.

| Operator | Name            | Function                                                                 |
|----------|-----------------|--------------------------------------------------------------------------|
| `+`      | Addition        | Adds the values of both operands.                                        |
| `-`      | Subtraction     | Subtracts the value of the right operand from the value of the left operand. |
| `*`      | Multiplication  | Multiplies the values of both operands.                                  |
| `/`      | Division        | Divides the value of the left operand by the value of the right operand. |
| `%`      | Modulus         | Returns the remainder after division.                                    |
| `//`     | Floor Division  | Returns the quotient without decimal point digits (integer result).      |
| `**`     | Exponent        | Calculates the exponential (power) of the operand.                       |

## Assignment Operators

| Symbol | Name           | Description                                                                 |
|--------|----------------|-----------------------------------------------------------------------------|
| =      | Assignment      | Assigns value from right to left operand.                                   |
| +=     | Add AND         | Adds and assigns result to left operand.                                    |
| -=     | Subtract AND    | Subtracts and assigns result to left operand.                               |
| *=     | Multiply AND    | Multiplies and assigns result to left operand.                              |
| /=     | Divide AND      | Divides and assigns result to left operand.                                 |
| %=     | Modulus AND     | Takes modulus and assigns result.                                           |
| **=    | Exponent AND    | Raises to power and assigns result.                                         |
| //=    | Floor Division  | Performs floor division and assigns result.                                 |

---

## Relational (Comparison) Operators

| Operator | Name            | Description                                                               |
|----------|-----------------|---------------------------------------------------------------------------|
| ==       | Equal to        | True if both operands are equal.                                           |
| !=       | Not equal to    | True if operands are not equal.                                            |
| >        | Greater than    | True if left operand is greater.                                           |
| <        | Less than       | True if left operand is less.                                              |
| >=       | Greater or equal| True if left is greater or equal to right.                                 |
| <=       | Less or equal   | True if left is less or equal to right.                                    |

---

## Logical Operators

| Operator | Description                                                |
|----------|------------------------------------------------------------|
| and      | True if **both** operands are True                         |
| or       | True if **at least one** operand is True                   |
| not      | True if the operand is **False**, and vice versa           |

---

## Membership Operators

| Operator | Description                                                                      |
|----------|----------------------------------------------------------------------------------|
| in       | True if value exists in sequence (e.g., list, string, set)                      |
| not in   | True if value does **not** exist in the sequence                                |

---

## Identity Operators

| Operator | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| is       | True if both variables point to the **same object in memory**               |
| is not   | True if variables **do not point** to the same object                       |

---

## Bitwise Operators

| Symbol | Operator | Description                                                              |
|--------|----------|--------------------------------------------------------------------------|
| &      | AND      | Copies a bit if found in **both** operands                               |
| \|     | OR       | Copies a bit if found in **either** operand                              |
| ~      | NOT      | Flips all the bits (1 → 0, 0 → 1)                                        |
| ^      | XOR      | Copies a bit if set in **only one** operand                              |
| >>     | Shift right | Shifts bits to the right by given number of places                     |
| <<     | Shift left  | Shifts bits to the left by given number of places                      |

---

## Operator Precedence (Highest to Lowest)

| Order | Operation Type            | Symbols (Examples)                                     |
|-------|---------------------------|--------------------------------------------------------|
| 1     | Parentheses               | `()`                                                   |
| 2     | Exponentiation            | `**`                                                   |
| 3     | Unary operators           | `+`, `-`, `~`                                          |
| 4     | Multiply/Divide/Modulus   | `*`, `/`, `%`, `//`                                    |
| 5     | Addition/Subtraction      | `+`, `-`                                               |
| 6     | Bitwise shift             | `>>`, `<<`                                             |
| 7     | Bitwise AND               | `&`                                                    |
| 8     | Bitwise OR / XOR          | `|`, `^`                                               |
| 9     | Comparison                | `<`, `<=`, `>`, `>=`                                   |
| 10    | Equality                  | `==`, `!=`                                             |
| 11    | Assignment                | `=`, `+=`, `-=`, etc.                                  |
| 12    | Identity                  | `is`, `is not`                                         |
| 13    | Membership                | `in`, `not in`                                         |
| 14    | Logical                   | `not`, `and`, `or`                                     |
