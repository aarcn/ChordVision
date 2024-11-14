chords = {
    # Major Triads
    "Cmaj": ["C", "E", "G"],
    "C#maj": ["C#", "F", "G#"], "Dbmaj": ["Db", "F", "Ab"],
    "Dmaj": ["D", "F#", "A"],
    "D#maj": ["D#", "G", "A#"], "Ebmaj": ["Eb", "G", "Bb"],
    "Emaj": ["E", "G#", "B"],
    "Fmaj": ["F", "A", "C"],
    "F#maj": ["F#", "A#", "C#"], "Gbmaj": ["Gb", "Bb", "Db"],
    "Gmaj": ["G", "B", "D"],
    "G#maj": ["G#", "C", "D#"], "Abmaj": ["Ab", "C", "Eb"],
    "Amaj": ["A", "C#", "E"],
    "A#maj": ["A#", "D", "F"], "Bbmaj": ["Bb", "D", "F"],
    "Bmaj": ["B", "D#", "F#"], "Cbmaj": ["Cb", "Eb", "Gb"],

    # Minor Triads
    "Cmin": ["C", "Eb", "G"],
    "C#min": ["C#", "E", "G#"], "Dbmin": ["Db", "Fb", "Ab"],
    "Dmin": ["D", "F", "A"],
    "D#min": ["D#", "F#", "A#"], "Ebmin": ["Eb", "Gb", "Bb"],
    "Emin": ["E", "G", "B"],
    "Fmin": ["F", "Ab", "C"],
    "F#min": ["F#", "A", "C#"], "Gbmin": ["Gb", "Bbb", "Db"],
    "Gmin": ["G", "Bb", "D"],
    "G#min": ["G#", "B", "D#"], "Abmin": ["Ab", "Cb", "Eb"],
    "Amin": ["A", "C", "E"],
    "A#min": ["A#", "C#", "F"], "Bbmin": ["Bb", "Db", "F"],
    "Bmin": ["B", "D", "F#"], "Cbmin": ["Cb", "Ebb", "Gb"],

    # Diminished Triads
    "Cdim": ["C", "Eb", "Gb"],
    "Ddim": ["D", "F", "Ab"],
    "Edim": ["E", "G", "Bb"],
    "Fdim": ["F", "Ab", "Cb"],
    "Gdim": ["G", "Bb", "Db"],
    "Adim": ["A", "C", "Eb"],
    "Bdim": ["B", "D", "F"], "Cbdim": ["Cb", "Ebb", "Gb"],

    # Augmented Triads
    "Caug": ["C", "E", "G#"],
    "Daug": ["D", "F#", "A#"],
    "Eaug": ["E", "G#", "B#"],
    "Faug": ["F", "A", "C#"],
    "Gaug": ["G", "B", "D#"],
    "Aaug": ["A", "C#", "E#"],
    "Baug": ["B", "D#", "F#"], "Cbaug": ["Cb", "Eb", "G"],

    # Major 7th Chords
    "Cmaj7": ["C", "E", "G", "B"],
    "Dmaj7": ["D", "F#", "A", "C#"],
    "Emaj7": ["E", "G#", "B", "D#"],
    "Fmaj7": ["F", "A", "C", "E"],
    "Gmaj7": ["G", "B", "D", "F#"],
    "Amaj7": ["A", "C#", "E", "G#"],
    "Bmaj7": ["B", "D#", "F#", "A#"], "Cbmaj7": ["Cb", "Eb", "Gb", "Bb"],

    # Minor 7th Chords
    "Cmin7": ["C", "Eb", "G", "Bb"],
    "Dmin7": ["D", "F", "A", "C"],
    "Emin7": ["E", "G", "B", "D"],
    "Fmin7": ["F", "Ab", "C", "Eb"],
    "Gmin7": ["G", "Bb", "D", "F"],
    "Amin7": ["A", "C", "E", "G"],
    "Bmin7": ["B", "D", "F#", "A"], "Cbmin7": ["Cb", "Ebb", "Gb", "Bbb"],

    # Dominant 7th Chords
    "C7": ["C", "E", "G", "Bb"],
    "D7": ["D", "F#", "A", "C"],
    "E7": ["E", "G#", "B", "D"],
    "F7": ["F", "A", "C", "Eb"],
    "G7": ["G", "B", "D", "F"],
    "A7": ["A", "C#", "E", "G"],
    "B7": ["B", "D#", "F#", "A"], "Cb7": ["Cb", "Eb", "Gb", "Bbb"],

    # Minor 7 Flat 5 Chords (Half-Diminished)
    "Cm7b5": ["C", "Eb", "Gb", "Bb"],
    "Dm7b5": ["D", "F", "Ab", "C"],
    "Em7b5": ["E", "G", "Bb", "D"],
    "Fm7b5": ["F", "Ab", "Cb", "Eb"],
    "Gm7b5": ["G", "Bb", "Db", "F"],
    "Am7b5": ["A", "C", "Eb", "G"],
    "Bm7b5": ["B", "D", "F", "A"], "Cbm7b5": ["Cb", "Ebb", "Gb", "Bbb"],

    # Diminished 7th Chords
    "Cdim7": ["C", "Eb", "Gb", "Bbb"],
    "Ddim7": ["D", "F", "Ab", "Cb"],
    "Edim7": ["E", "G", "Bb", "Db"],
    "Fdim7": ["F", "Ab", "Cb", "Ebb"],
    "Gdim7": ["G", "Bb", "Db", "Fb"],
    "Adim7": ["A", "C", "Eb", "Gb"],
    "Bdim7": ["B", "D", "F", "Ab"], "Cbdim7": ["Cb", "Ebb", "Gb", "Bbb"],

    # Extended Chords
    "C9": ["C", "E", "G", "Bb", "D"],
    "Cmaj9": ["C", "E", "G", "B", "D"],
    "Cmin9": ["C", "Eb", "G", "Bb", "D"],
    "C11": ["C", "E", "G", "Bb", "D", "F"],
    "Cmaj11": ["C", "E", "G", "B", "D", "F"],
    "Cmin11": ["C", "Eb", "G", "Bb", "D", "F"],
    "C13": ["C", "E", "G", "Bb", "D", "F", "A"],
    "Cmaj13": ["C", "E", "G", "B", "D", "F", "A"],
    "Cmin13": ["C", "Eb", "G", "Bb", "D", "F", "A"],

    # Sus Chords
    "Csus2": ["C", "D", "G"],
    "Csus4": ["C", "F", "G"],
    "Dsus2": ["D", "E", "A"],
    "Dsus4": ["D", "G", "A"],
    "Esus2": ["E", "F#", "B"],
    "Esus4": ["E", "A", "B"],
    "Fsus2": ["F", "G", "C"],
    "Fsus4": ["F", "Bb", "C"],
    "Gsus2": ["G", "A", "D"],
    "Gsus4": ["G", "C", "D"],
    "Asus2": ["A", "B", "E"],
    "Asus4": ["A", "D", "E"],
    "Bsus2": ["B", "C#", "F#"], "Cbsus2": ["Cb", "Db", "Gb"],
    "Bsus4": ["B", "E", "F#"], "Cbsus4": ["Cb", "Fb", "Gb"]
}
