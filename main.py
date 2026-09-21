from turtle import *


# Window and Turtle settings
setup(1100, 700)
title("Golden Gate Bridge - Python Turtle")
shape("turtle")
speed(10)
pensize(1)
bgcolor("#D98778")


def move(x, y):
    """Move from the home point using only basic Turtle commands."""
    penup()
    home()

    if x >= 0:
        fd(x)
    else:
        bk(-x)

    if y >= 0:
        lt(90)
        fd(y)
        rt(90)
    else:
        rt(90)
        fd(-y)
        lt(90)


def box(width, height, fill_color, line_color):
    """Draw and color a rectangle."""
    color(line_color, fill_color)
    begin_fill()
    for i in range(2):
        fd(width)
        lt(90)
        fd(height)
        lt(90)
    end_fill()


def brace(x, y, angle, length, width=2):
    """Draw one straight structural brace."""
    move(x, y)
    color("#652A23")
    pensize(width)
    pendown()
    lt(angle)
    fd(length)


# ------------------------------------------------------------
# WARM SUNSET SKY
# ------------------------------------------------------------

move(-550, -210)
pendown()
box(1100, 560, "#E99A7F", "#E99A7F")

move(-550, -125)
pendown()
box(1100, 250, "#F4AF8A", "#F4AF8A")

move(-550, -210)
pendown()
box(1100, 120, "#FFD29F", "#FFD29F")

# Soft sunset streaks
color("#F8B993")
pensize(10)
move(-500, 235)
pendown()
fd(300)
penup()
fd(85)
pendown()
fd(365)

color("#F7C49A")
pensize(7)
move(-390, 160)
pendown()
fd(245)
penup()
fd(70)
pendown()
fd(420)

color("#FFE0AE")
pensize(5)
move(-500, 65)
pendown()
fd(210)
penup()
fd(100)
pendown()
fd(280)


# ------------------------------------------------------------
# DISTANT MOUNTAINS
# ------------------------------------------------------------

# Back mountain range
move(-550, -175)
color("#6F6660", "#786D66")
begin_fill()
pendown()
lt(20)
fd(120)
rt(35)
fd(115)
lt(27)
fd(100)
rt(22)
fd(100)
lt(25)
fd(110)
rt(30)
fd(115)
lt(20)
fd(105)
rt(15)
fd(120)
lt(24)
fd(110)
rt(26)
fd(110)
fd(30)
end_fill()

# Nearer rolling mountains
move(-315, -180)
color("#5F5854", "#655D58")
begin_fill()
pendown()
lt(24)
fd(110)
rt(34)
fd(90)
lt(27)
fd(115)
rt(29)
fd(105)
lt(24)
fd(115)
rt(32)
fd(100)
lt(27)
fd(105)
rt(26)
fd(95)
end_fill()

# เพิ่มรายละเอียดภูเขาด้านหลัง
color("#8A817A")
pensize(1)

penup()
home()
bk(470)
rt(90)
fd(145)
lt(90)
pendown()
lt(14)
fd(34)
rt(25)
fd(28)

penup()
home()
bk(350)
rt(90)
fd(135)
lt(90)
pendown()
lt(10)
fd(30)
rt(20)
fd(36)

penup()
home()
bk(215)
rt(90)
fd(150)
lt(90)
pendown()
lt(18)
fd(27)
rt(30)
fd(32)

penup()
home()
bk(55)
rt(90)
fd(128)
lt(90)
pendown()
lt(12)
fd(38)
rt(24)
fd(35)

penup()
home()
fd(95)
rt(90)
fd(145)
lt(90)
pendown()
lt(16)
fd(30)
rt(27)
fd(34)

penup()
home()
fd(295)
rt(90)
fd(138)
lt(90)
pendown()
lt(11)
fd(36)
rt(22)
fd(31)


# ------------------------------------------------------------
# WATER
# ------------------------------------------------------------

move(-550, -350)
pendown()
box(1100, 175, "#A7B2B8", "#A7B2B8")

# Small horizontal reflections
color("#D8D4CC")
pensize(1)
move(-515, -205)
pendown()
fd(120)
penup()
fd(45)
pendown()
fd(210)
penup()
fd(70)
pendown()
fd(180)
penup()
fd(65)
pendown()
fd(250)

move(-455, -245)
pendown()
fd(165)
penup()
fd(75)
pendown()
fd(120)
penup()
fd(95)
pendown()
fd(235)
penup()
fd(55)
pendown()
fd(145)

color("#87969F")
move(-520, -300)
pendown()
fd(215)
penup()
fd(55)
pendown()
fd(170)
penup()
fd(85)
pendown()
fd(260)

move(-380, -330)
pendown()
fd(155)
penup()
fd(80)
pendown()
fd(205)
penup()
fd(70)
pendown()
fd(165)

# เพิ่มเส้นสะท้อนบนผิวน้ำ
color("#C5CDD0")
pensize(1)

penup()
home()
bk(510)
rt(90)
fd(225)
lt(90)
pendown()
fd(58)
penup()
fd(24)
pendown()
fd(44)

penup()
home()
bk(300)
rt(90)
fd(270)
lt(90)
pendown()
fd(72)
penup()
fd(28)
pendown()
fd(53)

penup()
home()
bk(70)
rt(90)
fd(215)
lt(90)
pendown()
fd(65)
penup()
fd(32)
pendown()
fd(48)

penup()
home()
fd(115)
rt(90)
fd(258)
lt(90)
pendown()
fd(54)
penup()
fd(25)
pendown()
fd(71)

penup()
home()
fd(330)
rt(90)
fd(285)
lt(90)
pendown()
fd(62)
penup()
fd(20)
pendown()
fd(46)

color("#7E909A")
penup()
home()
bk(265)
rt(90)
fd(345)
lt(90)
pendown()
fd(75)

penup()
home()
fd(35)
rt(90)
fd(315)
lt(90)
pendown()
fd(82)


# ------------------------------------------------------------
# FOREGROUND LAND FROM THE DRAFT
# ------------------------------------------------------------

# Left mountain, descending naturally to the waterline
move(-550, -25)
color("#5D3A30", "#704331")
begin_fill()
pendown()
rt(25)
fd(70)
rt(20)
fd(65)
lt(8)
fd(65)
rt(53)
fd(35)
rt(90)
fd(161)
rt(90)
fd(150)
end_fill()

# Warm ridges on the left mountain
color("#8A5031")
pensize(2)
move(-530, -65)
pendown()
rt(24)
fd(105)

move(-500, -110)
pendown()
rt(18)
fd(85)

# เพิ่มเส้นพื้นผิวภูเขาด้านซ้าย
color("#5D3A30")
pensize(1)

penup()
home()
bk(540)
rt(90)
fd(92)
lt(90)
pendown()
rt(20)
fd(34)
lt(9)
fd(28)

penup()
home()
bk(485)
rt(90)
fd(128)
lt(90)
pendown()
rt(28)
fd(31)
lt(14)
fd(24)

penup()
home()
bk(440)
rt(90)
fd(153)
lt(90)
pendown()
rt(18)
fd(26)


# ------------------------------------------------------------
# BRIDGE DECK AND SMALL TRIANGULAR TRUSS
# ------------------------------------------------------------

speed(8)

# Thin deck rising gently to the right
move(-465, -84)
color("#652A23", "#A94432")
pensize(2)
lt(2.7)
begin_fill()
pendown()
fd(970)
lt(90)
fd(14)
lt(90)
fd(970)
lt(90)
fd(14)
end_fill()

# Repeated small triangles under the full bridge
move(-460, -85)
color("#652A23")
pensize(1)
lt(2.7)
pendown()
for i in range(69):
    lt(60)
    fd(14)
    rt(120)
    fd(14)
    lt(60)

# Strong top and bottom deck lines
move(-465, -70)
color("#652A23")
pensize(2)
lt(2.7)
pendown()
fd(970)

move(-465, -85)
lt(2.7)
pendown()
fd(970)

# เพิ่มราวสะพานและเสาไฟขนาดเล็ก
color("#743027")
pensize(1)

move(-285, -62)
pendown()
lt(90)
fd(10)
rt(90)
fd(4)

move(-205, -58)
pendown()
lt(90)
fd(10)
rt(90)
fd(4)

move(-125, -54)
pendown()
lt(90)
fd(10)
rt(90)
fd(4)

move(-45, -50)
pendown()
lt(90)
fd(10)
rt(90)
fd(4)

move(35, -47)
pendown()
lt(90)
fd(10)
rt(90)
fd(4)

move(290, -35)
pendown()
lt(90)
fd(10)
rt(90)
fd(4)

move(370, -31)
pendown()
lt(90)
fd(10)
rt(90)
fd(4)

move(450, -27)
pendown()
lt(90)
fd(10)
rt(90)
fd(4)


# ------------------------------------------------------------
# ONE MAIN SUSPENSION CABLE AND THE OUTER CABLES
# ------------------------------------------------------------

color("#652A23")
pensize(3)

# Left outer cable
move(-465, -76)
pendown()
lt(70)
fd(218)

# The one central cable: left tower -> low point -> right tower
move(-335, 120)
pendown()
rt(80)
circle(196, 80)
circle(284, 86)

# Right outer cable continuing down from the large tower
move(220, 235)
pendown()
rt(43.5)
fd(390)


# ------------------------------------------------------------
# VERTICAL HANGER CABLES
# ------------------------------------------------------------

color("#743027")
pensize(1)

# Short outer hangers on the left
move(-455, -83)
lt(2.7)
pendown()
left_hangers = [35, 75, 115, 155, 195]
for wire_length in left_hangers:
    lt(87.3)
    fd(wire_length)
    bk(wire_length)
    rt(87.3)
    fd(15)

# Dense hangers following the single center cable
move(-325, -77)
lt(2.7)
pendown()
center_hangers = [161, 122, 96, 78, 62, 51, 39, 30,
                  27, 26, 27, 27, 31, 34, 39, 47,
                  55, 66, 80, 96, 118, 143, 177, 234]
for wire_length in center_hangers:
    lt(87.3)
    fd(wire_length)
    bk(wire_length)
    rt(87.3)
    fd(20)

# Hangers on the right outer cable
move(230, -51)
lt(2.7)
pendown()
right_hangers = [277, 259, 241, 223, 205, 187, 169, 151,
                 133, 115, 97, 79, 61, 43, 25]
for wire_length in right_hangers:
    lt(87.3)
    fd(wire_length)
    bk(wire_length)
    rt(87.3)
    fd(18)


# ------------------------------------------------------------
# SMALL LEFT TOWER
# ------------------------------------------------------------

# Two narrow tower legs
move(-390, -185)
pendown()
box(10, 320, "#A94432", "#652A23")

move(-335, -185)
pendown()
box(10, 320, "#A94432", "#652A23")

# Horizontal beams and tower openings
for beam_y in [-178, -82, -28, 28, 78, 122]:
    move(-390, beam_y)
    pendown()
    box(65, 9, "#B94A35", "#652A23")

# Upper X brace
brace(-380, 35, 60, 90, 2)
brace(-335, 35, 120, 90, 2)

# Lower support X below the deck
brace(-380, -169, 62, 97, 3)
brace(-335, -169, 118, 97, 3)

# Pointed details at the top
move(-392, 132)
color("#652A23", "#A94432")
begin_fill()
pendown()
lt(68)
fd(14)
rt(136)
fd(14)
rt(112)
fd(10)
end_fill()

move(-337, 132)
color("#652A23", "#A94432")
begin_fill()
pendown()
lt(68)
fd(14)
rt(136)
fd(14)
rt(112)
fd(10)
end_fill()


# ------------------------------------------------------------
# LARGE RIGHT TOWER
# ------------------------------------------------------------

# Tall legs extending well below the deck
move(140, -195)
pendown()
box(13, 485, "#A94432", "#652A23")

move(210, -195)
pendown()
box(13, 485, "#A94432", "#652A23")

# Strong crossbeams separating the large openings
for beam_y in [-190, -62, 15, 92, 165, 225, 278]:
    move(140, beam_y)
    pendown()
    box(83, 11, "#B94A35", "#652A23")

# Large X brace in the upper tower opening
brace(153, 103, 65, 135, 3)
brace(210, 103, 115, 135, 3)

# Three lower support diamonds/X braces
brace(153, -181, 63, 125, 4)
brace(210, -181, 117, 125, 4)
brace(153, -105, 56, 103, 4)
brace(210, -105, 124, 103, 4)

# Pointed caps at both tower tops
move(138, 288)
color("#652A23", "#A94432")
begin_fill()
pendown()
lt(68)
fd(17)
rt(136)
fd(17)
rt(112)
fd(12)
end_fill()

move(208, 288)
color("#652A23", "#A94432")
begin_fill()
pendown()
lt(68)
fd(17)
rt(136)
fd(17)
rt(112)
fd(12)
end_fill()

# Wide tower footing blocks
move(132, -201)
pendown()
box(30, 10, "#8A5031", "#652A23")

move(202, -201)
pendown()
box(30, 10, "#8A5031", "#652A23")

move(122, -207)
pendown()
box(120, 7, "#8A5031", "#652A23")


# ------------------------------------------------------------
# RIGHT FOREGROUND CLIFF -- LOW, SLOPING, AND DRAFT-LIKE
# ------------------------------------------------------------

move(385, -178)
color("#5D3A30", "#704331")
begin_fill()
pendown()
lt(52)
fd(15)
rt(3)
fd(16)
lt(5)
fd(14)
rt(4)
fd(15)
rt(8)
fd(12)
rt(2)
fd(13)
lt(5)
fd(12)
rt(4)
fd(13)
lt(19)
fd(14)
rt(3)
fd(13)
lt(5)
fd(14)
rt(4)
fd(14)
rt(20)
fd(14)
lt(3)
fd(13)
rt(5)
fd(14)
lt(2)
fd(14)
lt(14)
fd(8)
rt(3)
fd(9)
lt(5)
fd(8)
rt(54)
fd(3)
rt(90)
fd(355)
rt(90)
fd(165)
rt(90)
fd(172)
end_fill()

# Warm rock-face marks
color("#8A5031")
pensize(3)
move(438, -120)
pendown()
lt(54)
fd(75)

move(475, -80)
pendown()
lt(48)
fd(68)

move(510, -35)
pendown()
lt(55)
fd(48)

# เพิ่มพื้นผิวของภูเขาด้านขวา
color("#5D3A30")
pensize(1)

move(405, -165)
pendown()
lt(48)
fd(24)
rt(12)
fd(18)

move(430, -145)
pendown()
lt(56)
fd(29)
lt(7)
fd(18)

move(455, -118)
pendown()
lt(44)
fd(26)
rt(9)
fd(22)

move(480, -92)
pendown()
lt(58)
fd(23)
rt(14)
fd(20)

move(500, -66)
pendown()
lt(47)
fd(25)
lt(8)
fd(17)

move(525, -35)
pendown()
lt(61)
fd(21)

color("#9B603F")
pensize(2)

move(420, -135)
pendown()
lt(50)
fd(16)

move(468, -70)
pendown()
lt(42)
fd(19)

move(515, -18)
pendown()
lt(57)
fd(15)


# ------------------------------------------------------------
# ROCKS IN THE WATER
# ------------------------------------------------------------

# Left rock
move(-430, -286)
color("#493B36", "#665049")
begin_fill()
pendown()
lt(26)
fd(45)
rt(34)
fd(52)
rt(54)
fd(43)
rt(118)
fd(83)
end_fill()

# Middle rock
move(-155, -320)
color("#493B36", "#5D4740")
begin_fill()
pendown()
lt(24)
fd(34)
rt(28)
fd(47)
rt(70)
fd(38)
rt(104)
fd(69)
end_fill()

# Right cluster near the cliff
move(245, -315)
color("#493B36", "#604A42")
begin_fill()
pendown()
lt(28)
fd(43)
rt(36)
fd(52)
rt(62)
fd(44)
rt(110)
fd(77)
end_fill()

# เพิ่มเงาและรอยแตกบนก้อนหิน
color("#493B36")
pensize(1)

move(-405, -270)
pendown()
lt(18)
fd(18)
rt(30)
fd(15)

move(-375, -276)
pendown()
rt(15)
fd(20)

move(-135, -307)
pendown()
lt(16)
fd(17)
rt(28)
fd(14)

move(-105, -312)
pendown()
rt(12)
fd(18)

move(270, -300)
pendown()
lt(20)
fd(19)
rt(32)
fd(16)

move(305, -304)
pendown()
rt(14)
fd(21)

# เส้นชายฝั่งสั้น ๆ รอบก้อนหิน
color("#87969F")
pensize(1)

move(-455, -295)
pendown()
fd(24)
penup()
fd(12)
pendown()
fd(31)

move(-185, -329)
pendown()
fd(28)
penup()
fd(11)
pendown()
fd(26)

move(225, -325)
pendown()
fd(30)
penup()
fd(13)
pendown()
fd(34)

# Short ripples beside the rocks
color("#D8D4CC")
pensize(1)
move(-485, -290)
pendown()
fd(80)

move(-205, -324)
pendown()
fd(110)

move(205, -320)
pendown()
fd(145)


# Finish the visible Turtle drawing
hideturtle()
done()
