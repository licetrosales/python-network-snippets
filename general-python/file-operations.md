# 📂 Python File Opening Modes Cheat Sheet

To work with files in Python, use the `open()` function:

```python
file = open(file_name, mode='r', buffering=-1, encoding=None)
```
## Parameters **`file_name`** (`str`): Name of the file to open.

- **`mode`** *(optional)*: Controls how the file is opened (read/write/append, binary/text).

- **`buffering`** *(optional)*:
  - `0`: No buffering (only in binary mode)
  - `1`: Line buffering
  - `>1`: Size of buffer
  - `<0`: Use default system buffer

- **`encoding`** *(optional)*: Used for text files. Common values:
  - Linux/macOS: `"utf-8"`
  - Windows: `"cp1252"`

| Mode  | Description                                                  |
| ----- | ------------------------------------------------------------ |
| `r`   | **Read** (default). File must exist.                         |
| `rb`  | **Read binary**. File must exist.                            |
| `r+`  | **Read/write**. File must exist.                             |
| `rb+` | **Read/write binary**. File must exist.                      |
| `w`   | **Write only**. Overwrites or creates new file.              |
| `wb`  | **Write binary**. Overwrites or creates new file.            |
| `w+`  | **Read/write**. Overwrites or creates new file.              |
| `wb+` | **Read/write binary**. Overwrites or creates new file.       |
| `a`   | **Append**. Creates file if not exists. Pointer at end.      |
| `ab`  | **Append binary**.                                           |
| `a+`  | **Read/append**. Creates file if not exists. Pointer at end. |
| `ab+` | **Read/append binary**.                  
