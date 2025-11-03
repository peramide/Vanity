### License Plate Validation

This Python program validates Massachusetts vanity license plates based on state vehicle registration rules. It checks if a plate meets the following conditions:

* Starts with **at least two letters**.
* Has a **length of 2–6 characters**.
* **Numbers**, if present, must appear **only at the end** and **cannot start with 0**.
* **No spaces or punctuation marks** are allowed.

---

## 🧠 How It Works

The program prompts the user for a plate number and prints **“Valid”** if it meets all rules or **“Invalid”** otherwise.

```python
def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
```

The `is_valid()` function returns `True` if all RMV (Registry of Motor Vehicles) conditions are met and `False` otherwise.

---

## 🧪 Testing

You can run automated tests with **pytest** or test manually using:

```bash
python plates.py
```

### Example Tests

| Input    | Output  |
| -------- | ------- |
| CS50     | Valid   |
| AAA222   | Valid   |
| AAA22A   | Invalid |
| CS05     | Invalid |
| OUTATIME | Invalid |

---

## 🧰 Technologies

* Python 3
* pytest (for testing)
* CS50 IDE or VS Code

---

