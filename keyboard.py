def create_keyboard(canvas):
    white_key_width = 30
    black_key_width = 20
    white_key_height = 100
    black_key_height = 60

    keys = []

    # Fourth Octave
    C4 = canvas.create_rectangle(0 * white_key_width, 0, 1 * white_key_width,
                                 white_key_height, fill="white", outline="black")
    D4 = canvas.create_rectangle(1 * white_key_width, 0, 2 * white_key_width,
                                 white_key_height, fill="white", outline="black")
    E4 = canvas.create_rectangle(2 * white_key_width, 0, 3 * white_key_width,
                                 white_key_height, fill="white", outline="black")
    F4 = canvas.create_rectangle(3 * white_key_width, 0, 4 * white_key_width,
                                 white_key_height, fill="white", outline="black")
    G4 = canvas.create_rectangle(4 * white_key_width, 0, 5 * white_key_width,
                                 white_key_height, fill="white", outline="black")
    A4 = canvas.create_rectangle(5 * white_key_width, 0, 6 * white_key_width,
                                 white_key_height, fill="white", outline="black")
    B4 = canvas.create_rectangle(6 * white_key_width, 0, 7 * white_key_width,
                                 white_key_height, fill="white", outline="black")

    # Fifth Octave
    C5 = canvas.create_rectangle(0 * white_key_width, 0, 1 * white_key_width,
                                 white_key_height, fill="white", outline="black")
    D5 = canvas.create_rectangle(1 * white_key_width, 0, 2 * white_key_width,
                                 white_key_height, fill="white", outline="black")
    E5 = canvas.create_rectangle(2 * white_key_width, 0, 3 * white_key_width,
                                 white_key_height, fill="white", outline="black")
    F5 = canvas.create_rectangle(3 * white_key_width, 0, 4 * white_key_width,
                                 white_key_height, fill="white", outline="black")
    G5 = canvas.create_rectangle(4 * white_key_width, 0, 5 * white_key_width,
                                 white_key_height, fill="white", outline="black")
    A5 = canvas.create_rectangle(5 * white_key_width, 0, 6 * white_key_width,
                                 white_key_height, fill="white", outline="black")
    B5 = canvas.create_rectangle(6 * white_key_width, 0, 7 * white_key_width,
                                 white_key_height, fill="white", outline="black")

    # Fourth Octave
    C_sharp4 = canvas.create_rectangle(1 * white_key_width - black_key_width // 2, 0,
                                       1 * white_key_width + black_key_width // 2,
                                       black_key_height, fill="black", outline="black")
    D_sharp4 = canvas.create_rectangle(2 * white_key_width - black_key_width // 2, 0,
                                       2 * white_key_width + black_key_width // 2,
                                       black_key_height, fill="black", outline="black")
    F_sharp4 = canvas.create_rectangle(4 * white_key_width - black_key_width // 2, 0,
                                       4 * white_key_width + black_key_width // 2,
                                       black_key_height, fill="black", outline="black")
    G_sharp4 = canvas.create_rectangle(5 * white_key_width - black_key_width // 2, 0,
                                       5 * white_key_width + black_key_width // 2,
                                       black_key_height, fill="black", outline="black")
    A_sharp4 = canvas.create_rectangle(6 * white_key_width - black_key_width // 2, 0,
                                       6 * white_key_width + black_key_width // 2,
                                       black_key_height, fill="black", outline="black")

    # Fifth Octave
    C_sharp5 = canvas.create_rectangle(1 * white_key_width - black_key_width // 2, 0,
                                       1 * white_key_width + black_key_width // 2,
                                       black_key_height, fill="black", outline="black")
    D_sharp5 = canvas.create_rectangle(2 * white_key_width - black_key_width // 2, 0,
                                       2 * white_key_width + black_key_width // 2,
                                       black_key_height, fill="black", outline="black")
    F_sharp5 = canvas.create_rectangle(4 * white_key_width - black_key_width // 2, 0,
                                       4 * white_key_width + black_key_width // 2,
                                       black_key_height, fill="black", outline="black")
    G_sharp5 = canvas.create_rectangle(5 * white_key_width - black_key_width // 2, 0,
                                       5 * white_key_width + black_key_width // 2,
                                       black_key_height, fill="black", outline="black")
    A_sharp5 = canvas.create_rectangle(6 * white_key_width - black_key_width // 2, 0,
                                       6 * white_key_width + black_key_width // 2,
                                       black_key_height, fill="black", outline="black")

    keys.append(C4)
    keys.append(C_sharp4)
    keys.append(D4)
    keys.append(D_sharp4)
    keys.append(E4)
    keys.append(F4)
    keys.append(F_sharp4)
    keys.append(G4)
    keys.append(G_sharp4)
    keys.append(A4)
    keys.append(A_sharp4)
    keys.append(B4)
    keys.append(C5)
    keys.append(C_sharp5)
    keys.append(D5)
    keys.append(D_sharp5)
    keys.append(E5)
    keys.append(F5)
    keys.append(F_sharp5)
    keys.append(G5)
    keys.append(G_sharp5)
    keys.append(A5)
    keys.append(A_sharp5)
    keys.append(B5)

    return keys


note_positions = {
    # Fourth Octave (C4-B4)
    "C4": 0, "C#4": 1, "Db4": 1, "D4": 2, "D#4": 3, "Eb4": 3, "E4": 4,
    "F4": 5, "F#4": 6, "Gb4": 6, "G4": 7, "G#4": 8, "Ab4": 8,
    "A4": 9, "A#4": 10, "Bb4": 10, "B4": 11,

    # Fifth Octave (C5-B5)
    "C5": 12, "C#5": 13, "Db5": 13, "D5": 14, "D#5": 15, "Eb5": 15, "E5": 16,
    "F5": 17, "F#5": 18, "Gb5": 18, "G5": 19, "G#5": 20, "Ab5": 20,
    "A5": 21, "A#5": 22, "Bb5": 22, "B5": 23
}
