# Arithmetic Formatter

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

> A beginner-friendly project that arranges arithmetic problems vertically, making them easy to read and solve — especially for kids.

## 📌 About

This project was built as part of the **Scientific Computing with Python Certification** on [freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/python-project-arithmetic-formatter).

The `arithmetic_arranger()` function takes a list of arithmetic problems (addition and subtraction only) and formats them into a clean, vertically aligned string.

---

## 🚀 Features

- Handles up to **five** arithmetic problems at a time
- Supports **addition** and **subtraction**
- **Vertically aligns** all operations
- Optional flag to **display answers**

---

## 🧠 Example Output

```python
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
diff
Copy
Edit
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```
python
Copy
Edit
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
yaml
Copy
Edit
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    ----
  40     -3800     19998      474
🛠 Usage
bash
Copy
Edit
# Run the script
```
python main.py
```
Or use the function inside another script:
```
from main import arithmetic_arranger
```
```
output = arithmetic_arranger(["32 + 8", "1 - 3801"], True)
print(output)
```
📄 License
This project is licensed under the MIT License.

🌐 Certification Link
This project was completed as part of freeCodeCamp's Scientific Computing with Python.

---

Let me know when you're ready to do the next project — I can generate the full repo structure and README just like this.
