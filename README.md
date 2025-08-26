# 🐍 Python Assignment: Classes & Polymorphism

This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python, including **classes, constructors, inheritance, and polymorphism**.

---

## 📌 Assignment Breakdown

### ✅ Activity 1: Design Your Own Class
We created a **Smartphone** class that inherits from a base **Device** class.  

- **Base Class (`Device`)**
  - Attributes: `brand`, `model`
  - Method: `device_info()` → Displays device details.

- **Child Class (`Smartphone`)**
  - Attributes: `storage`, `battery`
  - Methods:
    - `check_storage()` → Shows available storage.
    - `check_battery()` → Shows battery capacity.

**Example Usage:**
```python
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 5000)
print(phone1.device_info())
print(phone1.check_storage())
print(phone1.check_battery())
```

---

### ✅ Activity 2: Polymorphism Challenge
We implemented **polymorphism** by creating a `Vehicle` base class and defining different versions of the `move()` method in subclasses.

- **Car.move()** → `"🚗 Driving on the road"`
- **Plane.move()** → `"✈️ Flying in the sky"`
- **Boat.move()** → `"🚤 Sailing on the water"`

**Example Usage:**
```python
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
```

---

## 🎯 Key OOP Concepts Demonstrated
1. **Classes & Objects** – Represent real-world entities.
2. **Constructors (`__init__`)** – Initialize objects with unique values.
3. **Inheritance** – `Smartphone` inherits from `Device`.
4. **Encapsulation** – Attributes and methods are grouped logically within classes.
5. **Polymorphism** – `move()` behaves differently across `Car`, `Plane`, and `Boat`.

---

## 📂 Project Structure
```
assignment/
│── smartphone.py      # Activity 1: Smartphone class with inheritance
│── vehicles.py        # Activity 2: Polymorphism example
│── README.md          # This file
```

---

## 🚀 How to Run
1. Clone or download this project folder.
2. Run each activity in your terminal:

```bash
python smartphone.py
python vehicles.py
```

3. Observe the printed outputs for each class and method.

---

## 🏆 Outcome
- Designed custom classes with attributes & methods.
- Implemented constructors to initialize objects.
- Applied **inheritance** for code reusability.
- Explored **polymorphism** by redefining the same method in multiple classes.
