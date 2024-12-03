from keyboard import create_keyboard, note_positions
from highlight import highlight_chord
from chords import chords
import tkinter

root = tkinter.Tk()
root.title("ChordVision")
canvas = tkinter.Canvas(root, width=1404, height=150)
canvas.pack()
keys = create_keyboard(canvas)

chord_entry = tkinter.Entry(root)
chord_entry.pack()

chord_label = tkinter.Label(root, text="Enter a chord")
chord_label.pack()

chord_listbox = tkinter.Listbox(root)
chord_listbox.pack()
for chord in chords.keys():
    chord_listbox.insert(tkinter.END, chord)

chord_entry.bind("<Return>", lambda e: highlight_chord(canvas, keys, note_positions,
                                                       chords, chord_entry.get()))


def on_chord_select(event):
    selected_chord = chord_listbox.get(chord_listbox.curselection())
    highlight_chord(canvas, keys, note_positions, chords, selected_chord)


chord_listbox.bind("<<ListboxSelect>>", on_chord_select)

root.mainloop()
