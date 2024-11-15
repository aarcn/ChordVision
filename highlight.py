def clear_highlight(canvas, keys):
    canvas.itemconfig(keys[0], fill="white")
    canvas.itemconfig(keys[1], fill="black")
    canvas.itemconfig(keys[2], fill="white")
    canvas.itemconfig(keys[3], fill="black")
    canvas.itemconfig(keys[4], fill="white")
    canvas.itemconfig(keys[5], fill="white")
    canvas.itemconfig(keys[6], fill="black")
    canvas.itemconfig(keys[7], fill="white")
    canvas.itemconfig(keys[8], fill="black")
    canvas.itemconfig(keys[9], fill="white")
    canvas.itemconfig(keys[10], fill="black")
    canvas.itemconfig(keys[11], fill="white")
    canvas.itemconfig(keys[12], fill="white")
    canvas.itemconfig(keys[13], fill="black")
    canvas.itemconfig(keys[14], fill="white")
    canvas.itemconfig(keys[15], fill="black")
    canvas.itemconfig(keys[16], fill="white")
    canvas.itemconfig(keys[17], fill="white")
    canvas.itemconfig(keys[18], fill="black")
    canvas.itemconfig(keys[19], fill="white")
    canvas.itemconfig(keys[20], fill="black")
    canvas.itemconfig(keys[21], fill="white")
    canvas.itemconfig(keys[22], fill="black")
    canvas.itemconfig(keys[23], fill="white")


def highlight_chord(canvas, keys, note_positions, chords, chord_name):
    clear_highlight(canvas, keys)

    notes = chords.get(chord_name)
    if notes:
        for note in notes:
            pos = note_positions.get(note)
            if pos is not None:
                canvas.itemconfig(keys[pos], fill="yellow")
