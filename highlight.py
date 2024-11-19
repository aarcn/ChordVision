def clear_highlight(canvas, keys, note_positions):
    for key_name, pos in note_positions.items():
        if "#" in key_name:
            canvas.itemconfig(keys[pos], fill="black")
        if "b" in key_name:
            canvas.itemconfig(keys[pos], fill="black")
        else:
            canvas.itemconfig(keys[pos], fill="white")


def highlight_chord(canvas, keys, note_positions, chords, chord_name):
    clear_highlight(canvas, keys, note_positions)

    chord_notes = chords[chord_name]
    for note in chord_notes:
        pos = note_positions[note]
        canvas.itemconfig(keys[pos], fill="yellow")
