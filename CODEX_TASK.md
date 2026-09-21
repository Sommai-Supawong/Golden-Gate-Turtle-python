# Golden Gate Bridge Turtle — Codex Task

## Objective

ปรับปรุงโปรเจกต์ Python Turtle เดิมให้สามารถวาดภาพสะพาน Golden Gate Bridge โดยอ้างอิงจากภาพ:

`reference/bridge-reference.png`

ภาพอ้างอิงนี้คือ Source of Truth หลัก

ห้ามวาดสะพานจากความจำหรือออกแบบองค์ประกอบใหม่เอง

ผลลัพธ์ต้องมีองค์ประกอบและสัดส่วนใกล้เคียงภาพอ้างอิงมากที่สุดเท่าที่ทำได้ ภายใต้ข้อจำกัดของ Python Turtle ระดับพื้นฐาน ม.4

---

# Important Customer Requirement

ลูกค้าต้องการโค้ดลักษณะเดียวกับที่เรียนในห้อง เช่น:

```python
from turtle import *

shape("turtle")
speed(5)
color("red")
pensize(5)

begin_fill()

bk(100)
fd(200)
rt(90)
fd(50)

end_fill()

home()

done()