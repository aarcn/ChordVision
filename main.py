import tkinter
from keyboard import create_keyboard, note_positions
from chords import chords
from highlight import highlight_chord

root = tkinter.Tk()
root.title("ChordVision")
canvas = tkinter.Canvas(root, width=210, height=150)
canvas.pack()
chord_entry = tkinter.Entry(root)
chord_entry.pack()

keys = create_keyboard(canvas)

chord_entry.bind("<Return>", lambda e: highlight_chord(canvas, keys, note_positions, chords, chord_entry.get()))

label = tkinter.Label(root, text="Enter a chord")
label.pack()

root.mainloop()
