def clear_highlight(canvas, keys, note_positions):
    for key_name, pos in note_positions.items():
        print(key_name, pos)
        if "Cb" in key_name:
            canvas.itemconfig(keys[pos], fill="white")
        elif "Fb" in key_name:
            canvas.itemconfig(keys[pos], fill="white")
        elif "#" in key_name:
            canvas.itemconfig(keys[pos], fill="black")
        elif "b" in key_name:
            canvas.itemconfig(keys[pos], fill="black")
        else:
            canvas.itemconfig(keys[pos], fill="white")


def highlight_chord(canvas, keys, note_positions, chords, chord_name):
    clear_highlight(canvas, keys, note_positions)

    chord_notes = chords[chord_name]
    for note in chord_notes:
        pos = note_positions[note]
        canvas.itemconfig(keys[pos], fill="yellow")
