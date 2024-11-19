def create_keyboard(canvas):
    white_key_width = 27
    white_key_height = 100

    black_key_width = 18
    black_key_height = 60

    keys = []

    # White keys
    A0 = canvas.create_rectangle(0 * white_key_width, 0, 1 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    B0 = canvas.create_rectangle(1 * white_key_width, 0, 2 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    C1 = canvas.create_rectangle(2 * white_key_width, 0, 3 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    D1 = canvas.create_rectangle(3 * white_key_width, 0, 4 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    E1 = canvas.create_rectangle(4 * white_key_width, 0, 5 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    F1 = canvas.create_rectangle(5 * white_key_width, 0, 6 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    G1 = canvas.create_rectangle(6 * white_key_width, 0, 7 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    A1 = canvas.create_rectangle(7 * white_key_width, 0, 8 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    B1 = canvas.create_rectangle(8 * white_key_width, 0, 9 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    C2 = canvas.create_rectangle(9 * white_key_width, 0, 10 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    D2 = canvas.create_rectangle(10 * white_key_width, 0, 11 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    E2 = canvas.create_rectangle(11 * white_key_width, 0, 12 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    F2 = canvas.create_rectangle(12 * white_key_width, 0, 13 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    G2 = canvas.create_rectangle(13 * white_key_width, 0, 14 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    A2 = canvas.create_rectangle(14 * white_key_width, 0, 15 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    B2 = canvas.create_rectangle(15 * white_key_width, 0, 16 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    C3 = canvas.create_rectangle(16 * white_key_width, 0, 17 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    D3 = canvas.create_rectangle(17 * white_key_width, 0, 18 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    E3 = canvas.create_rectangle(18 * white_key_width, 0, 19 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    F3 = canvas.create_rectangle(19 * white_key_width, 0, 20 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    G3 = canvas.create_rectangle(20 * white_key_width, 0, 21 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    A3 = canvas.create_rectangle(21 * white_key_width, 0, 22 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    B3 = canvas.create_rectangle(22 * white_key_width, 0, 23 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    C4 = canvas.create_rectangle(23 * white_key_width, 0, 24 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    D4 = canvas.create_rectangle(24 * white_key_width, 0, 25 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    E4 = canvas.create_rectangle(25 * white_key_width, 0, 26 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    F4 = canvas.create_rectangle(26 * white_key_width, 0, 27 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    G4 = canvas.create_rectangle(27 * white_key_width, 0, 28 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    A4 = canvas.create_rectangle(28 * white_key_width, 0, 29 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    B4 = canvas.create_rectangle(29 * white_key_width, 0, 30 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    C5 = canvas.create_rectangle(30 * white_key_width, 0, 31 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    D5 = canvas.create_rectangle(31 * white_key_width, 0, 32 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    E5 = canvas.create_rectangle(32 * white_key_width, 0, 33 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    F5 = canvas.create_rectangle(33 * white_key_width, 0, 34 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    G5 = canvas.create_rectangle(34 * white_key_width, 0, 35 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    A5 = canvas.create_rectangle(35 * white_key_width, 0, 36 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    B5 = canvas.create_rectangle(36 * white_key_width, 0, 37 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    C6 = canvas.create_rectangle(37 * white_key_width, 0, 38 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    D6 = canvas.create_rectangle(38 * white_key_width, 0, 39 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    E6 = canvas.create_rectangle(39 * white_key_width, 0, 40 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    F6 = canvas.create_rectangle(40 * white_key_width, 0, 41 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    G6 = canvas.create_rectangle(41 * white_key_width, 0, 42 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    A6 = canvas.create_rectangle(42 * white_key_width, 0, 43 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    B6 = canvas.create_rectangle(43 * white_key_width, 0, 44 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    C7 = canvas.create_rectangle(44 * white_key_width, 0, 45 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    D7 = canvas.create_rectangle(45 * white_key_width, 0, 46 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    E7 = canvas.create_rectangle(46 * white_key_width, 0, 47 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    F7 = canvas.create_rectangle(47 * white_key_width, 0, 48 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    G7 = canvas.create_rectangle(48 * white_key_width, 0, 49 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    A7 = canvas.create_rectangle(49 * white_key_width, 0, 50 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    B7 = canvas.create_rectangle(50 * white_key_width, 0, 51 * white_key_width, white_key_height, fill="white",
                                 outline="black")
    C8 = canvas.create_rectangle(51 * white_key_width, 0, 52 * white_key_width, white_key_height, fill="white",
                                 outline="black")

    # Black keys
    A_sharp0 = canvas.create_rectangle((1 * white_key_width) - (black_key_width // 2), 0,
                                       (1 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    C_sharp1 = canvas.create_rectangle((2 * white_key_width) - (black_key_width // 2), 0,
                                       (2 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    D_sharp1 = canvas.create_rectangle((3 * white_key_width) - (black_key_width // 2), 0,
                                       (3 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    F_sharp1 = canvas.create_rectangle((5 * white_key_width) - (black_key_width // 2), 0,
                                       (5 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    G_sharp1 = canvas.create_rectangle((6 * white_key_width) - (black_key_width // 2), 0,
                                       (6 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    A_sharp1 = canvas.create_rectangle((7 * white_key_width) - (black_key_width // 2), 0,
                                       (7 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    C_sharp2 = canvas.create_rectangle((9 * white_key_width) - (black_key_width // 2), 0,
                                       (9 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    D_sharp2 = canvas.create_rectangle((10 * white_key_width) - (black_key_width // 2), 0,
                                       (10 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    F_sharp2 = canvas.create_rectangle((12 * white_key_width) - (black_key_width // 2), 0,
                                       (12 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    G_sharp2 = canvas.create_rectangle((13 * white_key_width) - (black_key_width // 2), 0,
                                       (13 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    A_sharp2 = canvas.create_rectangle((14 * white_key_width) - (black_key_width // 2), 0,
                                       (14 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    C_sharp3 = canvas.create_rectangle((16 * white_key_width) - (black_key_width // 2), 0,
                                       (16 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    D_sharp3 = canvas.create_rectangle((17 * white_key_width) - (black_key_width // 2), 0,
                                       (17 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    F_sharp3 = canvas.create_rectangle((19 * white_key_width) - (black_key_width // 2), 0,
                                       (19 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    G_sharp3 = canvas.create_rectangle((20 * white_key_width) - (black_key_width // 2), 0,
                                       (20 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    A_sharp3 = canvas.create_rectangle((21 * white_key_width) - (black_key_width // 2), 0,
                                       (21 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    C_sharp4 = canvas.create_rectangle((23 * white_key_width) - (black_key_width // 2), 0,
                                       (23 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    D_sharp4 = canvas.create_rectangle((24 * white_key_width) - (black_key_width // 2), 0,
                                       (24 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    F_sharp4 = canvas.create_rectangle((26 * white_key_width) - (black_key_width // 2), 0,
                                       (26 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    G_sharp4 = canvas.create_rectangle((27 * white_key_width) - (black_key_width // 2), 0,
                                       (27 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    A_sharp4 = canvas.create_rectangle((28 * white_key_width) - (black_key_width // 2), 0,
                                       (28 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    C_sharp5 = canvas.create_rectangle((30 * white_key_width) - (black_key_width // 2), 0,
                                       (30 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    D_sharp5 = canvas.create_rectangle((31 * white_key_width) - (black_key_width // 2), 0,
                                       (31 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    F_sharp5 = canvas.create_rectangle((33 * white_key_width) - (black_key_width // 2), 0,
                                       (33 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    G_sharp5 = canvas.create_rectangle((34 * white_key_width) - (black_key_width // 2), 0,
                                       (34 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    A_sharp5 = canvas.create_rectangle((35 * white_key_width) - (black_key_width // 2), 0,
                                       (35 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    C_sharp6 = canvas.create_rectangle((37 * white_key_width) - (black_key_width // 2), 0,
                                       (37 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    D_sharp6 = canvas.create_rectangle((38 * white_key_width) - (black_key_width // 2), 0,
                                       (38 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    F_sharp6 = canvas.create_rectangle((40 * white_key_width) - (black_key_width // 2), 0,
                                       (40 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    G_sharp6 = canvas.create_rectangle((41 * white_key_width) - (black_key_width // 2), 0,
                                       (41 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    A_sharp6 = canvas.create_rectangle((42 * white_key_width) - (black_key_width // 2), 0,
                                       (42 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    C_sharp7 = canvas.create_rectangle((44 * white_key_width) - (black_key_width // 2), 0,
                                       (44 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    D_sharp7 = canvas.create_rectangle((45 * white_key_width) - (black_key_width // 2), 0,
                                       (45 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    F_sharp7 = canvas.create_rectangle((47 * white_key_width) - (black_key_width // 2), 0,
                                       (47 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    G_sharp7 = canvas.create_rectangle((48 * white_key_width) - (black_key_width // 2), 0,
                                       (48 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")
    A_sharp7 = canvas.create_rectangle((49 * white_key_width) - (black_key_width // 2), 0,
                                       (49 * white_key_width) + (black_key_width // 2), black_key_height, fill="black",
                                       outline="black")

    keys.append(A0)
    keys.append(A_sharp0)
    keys.append(B0)
    keys.append(C1)
    keys.append(C_sharp1)
    keys.append(D1)
    keys.append(D_sharp1)
    keys.append(E1)
    keys.append(F1)
    keys.append(F_sharp1)
    keys.append(G1)
    keys.append(G_sharp1)
    keys.append(A1)
    keys.append(A_sharp1)
    keys.append(B1)
    keys.append(C2)
    keys.append(C_sharp2)
    keys.append(D2)
    keys.append(D_sharp2)
    keys.append(E2)
    keys.append(F2)
    keys.append(F_sharp2)
    keys.append(G2)
    keys.append(G_sharp2)
    keys.append(A2)
    keys.append(A_sharp2)
    keys.append(B2)
    keys.append(C3)
    keys.append(C_sharp3)
    keys.append(D3)
    keys.append(D_sharp3)
    keys.append(E3)
    keys.append(F3)
    keys.append(F_sharp3)
    keys.append(G3)
    keys.append(G_sharp3)
    keys.append(A3)
    keys.append(A_sharp3)
    keys.append(B3)
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
    keys.append(C6)
    keys.append(C_sharp6)
    keys.append(D6)
    keys.append(D_sharp6)
    keys.append(E6)
    keys.append(F6)
    keys.append(F_sharp6)
    keys.append(G6)
    keys.append(G_sharp6)
    keys.append(A6)
    keys.append(A_sharp6)
    keys.append(B6)
    keys.append(C7)
    keys.append(C_sharp7)
    keys.append(D7)
    keys.append(D_sharp7)
    keys.append(E7)
    keys.append(F7)
    keys.append(F_sharp7)
    keys.append(G7)
    keys.append(G_sharp7)
    keys.append(A7)
    keys.append(A_sharp7)
    keys.append(B7)
    keys.append(C8)

    return keys


note_positions = {
        # First Octave (A0-B0)
        "A0": 0, "A#0": 1, "Bb0": 1, "B0": 2,

        # Second Octave (C1-B1)
        "C1": 3, "C#1": 4, "Db1": 4, "D1": 5, "D#1": 6, "Eb1": 6,
        "E1": 7, "F1": 8, "F#1": 9, "Gb1": 9, "G1": 10, "G#1": 11, "Ab1": 11,
        "A1": 12, "A#1": 13, "Bb1": 13, "B1": 14,

        # Third Octave (C2-B2)
        "C2": 15, "C#2": 16, "Db2": 16, "D2": 17, "D#2": 18, "Eb2": 18,
        "E2": 19, "F2": 20, "F#2": 21, "Gb2": 21, "G2": 22, "G#2": 23, "Ab2": 23,
        "A2": 24, "A#2": 25, "Bb2": 25, "B2": 26,

        # Fourth Octave (C3-B3)
        "C3": 27, "C#3": 28, "Db3": 28, "D3": 29, "D#3": 30, "Eb3": 30,
        "E3": 31, "F3": 32, "F#3": 33, "Gb3": 33, "G3": 34, "G#3": 35, "Ab3": 35,
        "A3": 36, "A#3": 37, "Bb3": 37, "B3": 38,

        # Fifth Octave (C4-B4)
        "C4": 39, "C#4": 40, "Db4": 40, "D4": 41, "D#4": 42, "Eb4": 42,
        "E4": 43, "F4": 44, "F#4": 45, "Gb4": 45, "G4": 46, "G#4": 47, "Ab4": 47,
        "A4": 48, "A#4": 49, "Bb4": 49, "B4": 50,

        # Sixth Octave (C5-B5)
        "C5": 51, "C#5": 52, "Db5": 52, "D5": 53, "D#5": 54, "Eb5": 54,
        "E5": 55, "F5": 56, "F#5": 57, "Gb5": 57, "G5": 58, "G#5": 59, "Ab5": 59,
        "A5": 60, "A#5": 61, "Bb5": 61, "B5": 62,

        # Seventh Octave (C6-B6)
        "C6": 63, "C#6": 64, "Db6": 64, "D6": 65, "D#6": 66, "Eb6": 66,
        "E6": 67, "F6": 68, "F#6": 69, "Gb6": 69, "G6": 70, "G#6": 71, "Ab6": 71,
        "A6": 72, "A#6": 73, "Bb6": 73, "B6": 74,

        # Eighth Octave (C7-B7)
        "C7": 75, "C#7": 76, "Db7": 76, "D7": 77, "D#7": 78, "Eb7": 78,
        "E7": 79, "F7": 80, "F#7": 81, "Gb7": 81, "G7": 82, "G#7": 83, "Ab7": 83,
        "A7": 84, "A#7": 85, "Bb7": 85, "B7": 86,

        # Ninth Octave (C8)
        "C8": 87
    }
