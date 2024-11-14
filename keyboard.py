def create_keyboard(canvas):
    white_key_width = 30
    black_key_width = 20
    white_key_height = 100
    black_key_height = 60

    keys = []

    C = canvas.create_rectangle(0 * white_key_width, 0, 1 * white_key_width,
                                white_key_height, fill="white", outline="black")
    D = canvas.create_rectangle(1 * white_key_width, 0, 2 * white_key_width,
                                white_key_height, fill="white", outline="black")
    E = canvas.create_rectangle(2 * white_key_width, 0, 3 * white_key_width,
                                white_key_height, fill="white", outline="black")
    F = canvas.create_rectangle(3 * white_key_width, 0, 4 * white_key_width,
                                white_key_height, fill="white", outline="black")
    G = canvas.create_rectangle(4 * white_key_width, 0, 5 * white_key_width,
                                white_key_height, fill="white", outline="black")
    A = canvas.create_rectangle(5 * white_key_width, 0, 6 * white_key_width,
                                white_key_height, fill="white", outline="black")
    B = canvas.create_rectangle(6 * white_key_width, 0, 7 * white_key_width,
                                white_key_height, fill="white", outline="black")

    C_sharp = canvas.create_rectangle(1 * white_key_width - black_key_width // 2, 0,
                                      1 * white_key_width + black_key_width // 2,
                                      black_key_height, fill="black", outline="black")
    D_sharp = canvas.create_rectangle(2 * white_key_width - black_key_width // 2, 0,
                                      2 * white_key_width + black_key_width // 2,
                                      black_key_height, fill="black", outline="black")
    F_sharp = canvas.create_rectangle(4 * white_key_width - black_key_width // 2, 0,
                                      4 * white_key_width + black_key_width // 2,
                                      black_key_height, fill="black", outline="black")
    G_sharp = canvas.create_rectangle(5 * white_key_width - black_key_width // 2, 0,
                                      5 * white_key_width + black_key_width // 2,
                                      black_key_height, fill="black", outline="black")
    A_sharp = canvas.create_rectangle(6 * white_key_width - black_key_width // 2, 0,
                                      6 * white_key_width + black_key_width // 2,
                                      black_key_height, fill="black", outline="black")

    keys.append(C)
    keys.append(C_sharp)
    keys.append(D)
    keys.append(D_sharp)
    keys.append(E)
    keys.append(F)
    keys.append(F_sharp)
    keys.append(G)
    keys.append(G_sharp)
    keys.append(A)
    keys.append(A_sharp)
    keys.append(B)

    return keys


note_positions = {
    "C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4,
    "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8,
    "A": 9, "A#": 10, "Bb": 10, "B": 11
}
