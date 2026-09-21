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
