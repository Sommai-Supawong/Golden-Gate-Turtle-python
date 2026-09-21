# Golden Gate Bridge - Python Turtle

This project draws a colored Golden Gate Bridge scene with Python's built-in
Turtle module. It is written in a straightforward style suitable for a
Mathayom 4 student.

## Reference images

- `reference/bridge-draft.png` is the guide for geometry, composition, towers,
  suspension cables, hanger cables, deck truss, mountains, water, and rocks.
- `reference/bridge-reference.png` is the guide for the warm sunset palette,
  reddish-orange bridge, muted mountains, blue-gray water, and brown rocks.

The final scene is intended to look like a colored version of the supplied
black-and-white draft.

## Requirements

- Python 3
- The standard-library `turtle` module

No third-party packages are needed.

## Run

Open a terminal in this folder and run:

```powershell
python main.py
```

The Turtle window visibly draws the scene. When the drawing is complete, close
the Turtle window to finish the program.

## Main Turtle commands used

The artwork is built with beginner-friendly commands such as `fd()`, `bk()`,
`rt()`, `lt()`, `circle()`, `home()`, `penup()`, `pendown()`, `color()`,
`pensize()`, `begin_fill()`, and `end_fill()`. Simple `for` loops are used for
repeated details such as truss triangles, tower beams, and hanger cables.

`PRINT_CODE.txt` contains the exact same source code as `main.py` for convenient
printing and submission.
## Functions

โปรเจกต์นี้มีการสร้างฟังก์ชันเพิ่มเติมเพื่อช่วยลดการเขียนคำสั่ง Turtle ซ้ำ ๆ และทำให้โค้ดอ่านง่ายขึ้น

### `move(x, y)`

ใช้สำหรับย้ายตำแหน่ง Turtle ไปยังพิกัดที่กำหนด โดยไม่วาดเส้นระหว่างการเคลื่อนที่

**Parameters**

* `x` — ตำแหน่งในแนวนอน
* `y` — ตำแหน่งในแนวตั้ง

ฟังก์ชันนี้จะนำ Turtle กลับไปยังจุดเริ่มต้นด้วย `home()` ก่อน แล้วจึงเคลื่อนที่ไปยังตำแหน่ง `(x, y)` ที่ต้องการ

**ตัวอย่าง**

```python
move(-550, -210)
```

ใช้สำหรับกำหนดตำแหน่งเริ่มต้นก่อนวาดองค์ประกอบต่าง ๆ เช่น ท้องฟ้า ภูเขา น้ำ สะพาน และก้อนหิน

---

### `box(width, height, fill_color, line_color)`

ใช้สำหรับวาดรูปสี่เหลี่ยมผืนผ้าและกำหนดสีพื้นกับสีเส้นขอบ

**Parameters**

* `width` — ความกว้างของสี่เหลี่ยม
* `height` — ความสูงของสี่เหลี่ยม
* `fill_color` — สีภายในสี่เหลี่ยม
* `line_color` — สีเส้นขอบ

ฟังก์ชันนี้ใช้คำสั่ง `begin_fill()` และ `end_fill()` เพื่อระบายสีภายในรูป

**ตัวอย่าง**

```python
box(1100, 560, "#E99A7F", "#E99A7F")
```

ในโปรเจกต์นี้ใช้สำหรับสร้างองค์ประกอบ เช่น

* พื้นหลังท้องฟ้า
* พื้นน้ำ
* พื้นสะพาน
* เสาสะพาน
* คานของสะพาน
* ฐานเสาสะพาน

---

### `brace(x, y, angle, length, width=2)`

ใช้สำหรับวาดเส้นค้ำยันหรือเส้นโครงสร้างเฉียงของสะพาน

**Parameters**

* `x` — ตำแหน่งเริ่มต้นในแนวนอน
* `y` — ตำแหน่งเริ่มต้นในแนวตั้ง
* `angle` — มุมของเส้น
* `length` — ความยาวของเส้น
* `width` — ความหนาของเส้น โดยค่าเริ่มต้นคือ `2`

ฟังก์ชันจะย้าย Turtle ไปยังตำแหน่งที่กำหนด หมุนตามมุม แล้ววาดเส้นตรงตามความยาวที่กำหนด

**ตัวอย่าง**

```python
brace(-380, 35, 60, 90, 2)
brace(-335, 35, 120, 90, 2)
```

เมื่อใช้เส้นสองเส้นในทิศทางตรงข้ามกัน จะเกิดเป็นรูปตัว `X` ซึ่งใช้แทนโครงค้ำยันของเสาสะพาน Golden Gate Bridge

---

## Function Summary

| Function                                     | หน้าที่                                         |
| -------------------------------------------- | ----------------------------------------------- |
| `move(x, y)`                                 | ย้าย Turtle ไปยังตำแหน่งที่ต้องการโดยไม่วาดเส้น |
| `box(width, height, fill_color, line_color)` | วาดและระบายสีรูปสี่เหลี่ยมผืนผ้า                |
| `brace(x, y, angle, length, width)`          | วาดเส้นเฉียงสำหรับโครงค้ำยันของสะพาน            |

ฟังก์ชันเหล่านี้ช่วยให้โค้ดมีโครงสร้างที่ชัดเจน ลดการเขียนคำสั่งซ้ำ และช่วยให้สามารถสร้างองค์ประกอบต่าง ๆ ของภาพ Golden Gate Bridge ได้ง่ายขึ้น
