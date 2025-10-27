# Python Identifier Rules

## Basic Rules
- Must begin with a **letter** (`A-Z`, `a-z`) or an **underscore** (`_`)
- Can be followed by **letters**, **digits** (`0-9`), or **underscores**
- **Cannot** contain punctuation or special characters (`@`, `#`, `$`, etc.)
- Python is **case-sensitive** (`Variable` ≠ `variable`)

## Naming Conventions
- **Class names**: Start with an **uppercase** letter
- **Other identifiers**: Typically start with a **lowercase** letter

## Underscore Usage
- `_name` → **Private** (internal use)
- `__name` → **Strongly private** (name mangling applies)
- `name__` → **Special name**, defined by Python (e.g., `__init__`)

## Examples
```python
_valid_name = "OK"
ClassName = "OK"
__hidden = "Strongly private"
__init__ = "Special method"
myVar = "Case sensitive"
## 📝 Quotation in Python

Python supports three types of quotation marks to define string literals:

- **Single quotes**: `'Hello'`
- **Double quotes**: `"Hello"`
- **Triple quotes**: `'''Hello'''` or `"""Hello"""`
