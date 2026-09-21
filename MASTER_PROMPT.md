FINAL REVISION — READY FOR SUBMISSION

Read the existing project and CODEX_TASK.md first.

Then inspect these TWO reference images carefully:

1. reference/bridge-draft.png
   = PRIMARY REFERENCE for geometry, line structure, bridge details, proportions, cables, towers, mountains, rocks, and composition.

2. reference/bridge-reference.png
   = PRIMARY REFERENCE for colors, atmosphere, bridge color, sky, water, mountains, and foreground tones.

This is the FINAL revision before submission.

Do not redesign the scene.
Do not invent a different bridge.
Do not preserve incorrect geometry from the current output.

==================================================
TARGET
==================================================

The final Turtle result should look like:

bridge-draft.png
+
the colors of
bridge-reference.png

In other words:

GEOMETRY / LINES / DETAILS = bridge-draft.png

COLORS / ATMOSPHERE = bridge-reference.png

The final result should look like a colored version of the supplied black-and-white draft.

==================================================
MOST IMPORTANT: FOLLOW THE DRAFT
==================================================

Use reference/bridge-draft.png as the visual source of truth for:

- exact overall bridge composition
- left tower shape and size
- right tower shape and size
- tower openings
- tower top details
- X braces
- lower tower supports
- bridge deck
- small triangular truss pattern
- main suspension cable
- vertical hanger cables
- outer suspension cables
- mountains behind the bridge
- left foreground mountain
- right foreground mountain
- waterline
- rocks in the water
- small water lines

Do not simplify important structural lines that are clearly visible in bridge-draft.png.

The final bridge should resemble the draft much more closely than the current output.

==================================================
MAIN SUSPENSION CABLE
==================================================

Very important:

Between the LEFT and RIGHT towers, use ONE clearly defined main curved suspension cable, matching bridge-draft.png.

Do not create duplicated or overlapping main cable curves.

Its curve must follow the draft:

left tower
→ smooth downward curve
→ lowest point
→ smooth upward curve
→ right tower

After the right tower, continue the outer suspension cable downward toward the right side as shown in the draft.

Also preserve the outer cable on the left side.

==================================================
VERTICAL HANGER CABLES
==================================================

Match bridge-draft.png closely.

- thin lines
- relatively dense spacing
- vertical
- start at the main cable
- end at the bridge deck
- lengths vary naturally according to the cable curve

Do not randomly place them.

Do not make them all the same length.

Follow the draft visually.

==================================================
BRIDGE TOWERS
==================================================

Reproduce the tower line structure from bridge-draft.png as closely as possible.

LEFT TOWER:
- smaller
- narrow
- same perspective as draft
- same approximate openings
- same structural lines
- lower X support

RIGHT TOWER:
- significantly larger
- same general height and width as draft
- reproduce top details
- reproduce large openings
- reproduce X braces
- reproduce horizontal beams
- reproduce lower support/X structures

Do not turn the towers into generic rectangular buildings.

==================================================
BRIDGE DECK AND TRUSS
==================================================

Follow bridge-draft.png.

The bridge deck must remain thin.

The triangular truss underneath must:

- be small
- repeat frequently
- follow the full bridge
- resemble the draft

Do not make oversized triangles.

==================================================
MOUNTAINS AND LAND
==================================================

Use bridge-draft.png for the outlines.

Especially the RIGHT foreground mountain:

Make its:

- position
- height
- slope
- width
- silhouette

match bridge-draft.png as closely as possible.

Do NOT make it a huge rectangular/triangular mass.

It should enter naturally from the right edge just like the draft.

The LEFT foreground mountain should also follow the draft.

Background mountains should follow the draft silhouettes and remain behind the bridge.

==================================================
ROCKS AND WATER DETAILS
==================================================

Follow bridge-draft.png for:

- rock locations
- approximate rock shapes
- waterline
- short horizontal water details

Keep these simple but recognizable.

==================================================
COLOR SOURCE
==================================================

After the geometry matches bridge-draft.png, apply colors inspired by:

reference/bridge-reference.png

Use warm photographic tones.

SKY:
warm sunset peach / orange / cream

Suggested approximate palette:
#D98778
#E99A7F
#F4AF8A
#FFD29F

BRIDGE:
Golden Gate reddish orange

Suggested:
#A94432
#B94A35

Dark structural details:
#652A23
#743027

DISTANT MOUNTAINS:
muted warm gray / brown

Suggested:
#766B63
#625B57

WATER:
muted blue-gray

Suggested:
#A7B2B8
#909FA8

RIGHT / LEFT FOREGROUND ROCK:
warm dark brown / orange-brown

Suggested:
#704331
#8A5031
#5D3A30

Do not use bright cartoon colors.

==================================================
COLORING RULE
==================================================

Keep the LINE STRUCTURE visible.

Do not let filled colors cover structural lines.

Recommended process:

1. draw/fill background
2. fill landscape
3. fill bridge major shapes
4. redraw important bridge outlines/details above fills if necessary

The final result should retain the clarity of bridge-draft.png while gaining the color atmosphere of bridge-reference.png.

==================================================
CUSTOMER CODE REQUIREMENT
==================================================

The code must still look like beginner Mathayom 4 Python Turtle code.

Use primarily:

from turtle import *

shape("turtle")
speed()
color()
pensize()

fd()
bk()
rt()
lt()

circle()

penup()
pendown()

home()

begin_fill()
end_fill()

for loops may be used only for simple repeated details.

==================================================
STRICTLY FORBIDDEN
==================================================

DO NOT USE:

goto()
setpos()
setposition()
setx()
sety()

DO NOT use:

- classes / OOP
- NumPy
- OpenCV
- Pillow
- pygame
- matplotlib
- SVG
- image tracing libraries
- external dependencies
- complex vector mathematics
- advanced coordinate systems

Do not secretly recreate goto() using complicated mathematics.

Use home(), fd(), bk(), rt(), lt(), penup(), and pendown() for positioning.

==================================================
VISIBLE DRAWING
==================================================

The Turtle must visibly draw the artwork when main.py is run.

Do NOT use tracer(0).

Use a reasonable drawing speed.

For example:

speed(10)

for large background fills

and:

speed(7)

or:

speed(8)

for bridge details.

At the end:

hideturtle()
done()

==================================================
DO NOT CHANGE ALREADY CORRECT REQUIREMENTS
==================================================

Preserve:

- colored result
- visible Turtle animation
- beginner code style
- no goto()
- printable source code

Do not introduce unnecessary project architecture.

==================================================
FINAL QUALITY PASS
==================================================

This is the FINAL pass.

Do not stop after the first code modification.

Compare the result directly against BOTH reference images.

First compare geometry against:

reference/bridge-draft.png

Check:

[ ] left tower position and proportions
[ ] right tower position and proportions
[ ] tower openings
[ ] X braces
[ ] bridge deck
[ ] small truss pattern
[ ] ONE central suspension cable
[ ] outer suspension cables
[ ] vertical hanger cables
[ ] right foreground mountain
[ ] left mountain
[ ] background mountains
[ ] water
[ ] rocks

Then compare colors against:

reference/bridge-reference.png

Check:

[ ] warm sunset sky
[ ] reddish-orange bridge
[ ] muted mountain colors
[ ] blue-gray water
[ ] warm foreground rocks
[ ] good overall contrast

Fix obvious differences before stopping.

==================================================
FINAL PROJECT FILES
==================================================

Make sure these are finished:

main.py
README.md
PRINT_CODE.txt

Update PRINT_CODE.txt so it contains the EXACT final contents of main.py.

Update README.md only if necessary so it accurately describes the final program.

==================================================
FINAL VALIDATION
==================================================

Before considering the work complete:

1. Run/syntax-check main.py.
2. Confirm there is no goto(), setpos(), setposition(), setx(), or sety().
3. Confirm there are no external dependencies.
4. Confirm Turtle visibly draws the image.
5. Confirm the bridge geometry follows bridge-draft.png.
6. Confirm colors follow bridge-reference.png.
7. Confirm there is only ONE main suspension curve between the two towers.
8. Confirm vertical hanger lines match the draft structure.
9. Confirm the right mountain follows the draft and does not overpower the bridge.
10. Confirm PRINT_CODE.txt exactly matches main.py.
11. Confirm the code remains understandable and printable for a Mathayom 4 student.

Do not respond with only an explanation.

Actually modify and finalize the project.

This is the final revision for delivery.

Start by opening:
reference/bridge-draft.png
and
reference/bridge-reference.png

Then compare them with the current output and refine main.py until the result is ready to submit.