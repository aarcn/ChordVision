chords = {
    # Major Triads
    "Cmaj": ["C4", "E4", "G4"],
    "C#maj": ["C#4", "E#4", "G#4"], "Dbmaj": ["Db4", "F4", "Ab4"],
    "Dmaj": ["D4", "F#4", "A4"],
    "D#maj": ["D#4", "G4", "A#4"], "Ebmaj": ["Eb4", "G4", "Bb4"],
    "Emaj": ["E4", "G#4", "B4"],
    "Fmaj": ["F4", "A4", "C5"],
    "F#maj": ["F#4", "A#4", "C#5"], "Gbmaj": ["Gb4", "Bb4", "Db5"],
    "Gmaj": ["G4", "B4", "D5"],
    "G#maj": ["G#4", "B#4", "D#5"], "Abmaj": ["Ab4", "C5", "Eb5"],
    "Amaj": ["A4", "C#5", "E5"],
    "A#maj": ["A#4", "D5", "E#5"], "Bbmaj": ["Bb4", "D5", "F5"],
    "Bmaj": ["B4", "D#5", "F#5"], "Cbmaj": ["Cb4", "Eb4", "Gb4"],

    # Minor Triads
    "Cmin": ["C4", "Eb4", "G4"],
    "C#min": ["C#4", "E4", "G#4"], "Dbmin": ["Db4", "Fb4", "Ab4"],
    "Dmin": ["D4", "F4", "A4"],
    "D#min": ["D#4", "F#4", "A#4"], "Ebmin": ["Eb4", "Gb4", "Bb4"],
    "Emin": ["E4", "G4", "B4"],
    "Fmin": ["F4", "Ab4", "C5"],
    "F#min": ["F#4", "A4", "C#5"], "Gbmin": ["Gb4", "A4", "Db5"],
    "Gmin": ["G4", "Bb4", "D5"],
    "G#min": ["G#4", "B4", "D#5"], "Abmin": ["Ab4", "Cb5", "Eb5"],
    "Amin": ["A4", "C5", "E5"],
    "A#min": ["A#4", "C#5", "E#5"], "Bbmin": ["Bb4", "Db5", "F5"],
    "Bmin": ["B4", "D5", "F#5"], "Cbmin": ["Cb4", "D4", "Gb4"],

    # Diminished Triads
    "Cdim": ["C4", "Eb4", "Gb4"],
    "Ddim": ["D4", "F4", "Ab4"],
    "Edim": ["E4", "G4", "Bb4"],
    "Fdim": ["F4", "Ab4", "Cb5"],
    "Gdim": ["G4", "Bb4", "Db5"],
    "Adim": ["A4", "C5", "Eb5"],
    "Bdim": ["B4", "D5", "F5"], "Cbdim": ["Cb4", "D4", "Gb4"],

    # Augmented Triads
    "Caug": ["C4", "E4", "G#4"],
    "Daug": ["D4", "F#4", "A#4"],
    "Eaug": ["E4", "G#4", "B#4"],
    "Faug": ["F4", "A4", "C#5"],
    "Gaug": ["G4", "B4", "D#5"],
    "Aaug": ["A4", "C#5", "E#5"],
    "Baug": ["B4", "D#5", "G5"], "Cbaug": ["Cb4", "Eb4", "G4"],

    # Major 7th Chords
    "Cmaj7": ["C4", "E4", "G4", "B4"],
    "Dmaj7": ["D4", "F#4", "A4", "C#5"],
    "Emaj7": ["E4", "G#4", "B4", "D#5"],
    "Fmaj7": ["F4", "A4", "C5", "E5"],
    "Gmaj7": ["G4", "B4", "D5", "F#5"],
    "Amaj7": ["A4", "C#5", "E5", "G#5"],
    "Bmaj7": ["B4", "D#5", "F#5", "A#5"], "Cbmaj7": ["Cb4", "Eb4", "Gb4", "Bb4"],

    # Minor 7th Chords
    "Cmin7": ["C4", "Eb4", "G4", "Bb4"],
    "Dmin7": ["D4", "F4", "A4", "C5"],
    "Emin7": ["E4", "G4", "B4", "D5"],
    "Fmin7": ["F4", "Ab4", "C5", "Eb5"],
    "Gmin7": ["G4", "Bb4", "D5", "F5"],
    "Amin7": ["A4", "C5", "E5", "G5"],
    "Bmin7": ["B4", "D5", "F#5", "A5"], "Cbmin7": ["Cb4", "D4", "Gb4", "A4"],

    # Dominant 7th Chords
    "C7": ["C4", "E4", "G4", "Bb4"],
    "D7": ["D4", "F#4", "A4", "C5"],
    "E7": ["E4", "G#4", "B4", "D5"],
    "F7": ["F4", "A4", "C5", "Eb5"],
    "G7": ["G4", "B4", "D5", "F5"],
    "A7": ["A4", "C#5", "E5", "G5"],
    "B7": ["B4", "D#5", "F#5", "A5"], "Cb7": ["Cb4", "Eb4", "Gb4", "A4"],

    # Minor 7 Flat 5 Chords (Half-Diminished)
    "Cm7b5": ["C4", "Eb4", "Gb4", "Bb4"],
    "Dm7b5": ["D4", "F4", "Ab4", "C5"],
    "Em7b5": ["E4", "G4", "Bb4", "D5"],
    "Fm7b5": ["F4", "Ab4", "Cb5", "Eb5"],
    "Gm7b5": ["G4", "Bb4", "Db5", "F5"],
    "Am7b5": ["A4", "C5", "Eb5", "G5"],
    "Bm7b5": ["B4", "D5", "F5", "A5"], "Cbm7b5": ["Cb4", "D4", "Gb4", "A4"],

    # Diminished 7th Chords
    "Cdim7": ["C4", "Eb4", "Gb4", "A4"],
    "Ddim7": ["D4", "F4", "Ab4", "Cb5"],
    "Edim7": ["E4", "G4", "Bb4", "Db5"],
    "Fdim7": ["F4", "Ab4", "Cb5", "D5"],
    "Gdim7": ["G4", "Bb4", "Db5", "Fb5"],
    "Adim7": ["A4", "C5", "Eb5", "Gb5"],
    "Bdim7": ["B4", "D5", "F5", "Ab5"], "Cbdim7": ["Cb4", "D4", "Gb4", "Ab4"],

    # Extended Chords
    "C9": ["C4", "E4", "G4", "Bb4", "D5"],
    "Cmaj9": ["C4", "E4", "G4", "B4", "D5"],
    "Cmin9": ["C4", "Eb4", "G4", "Bb4", "D5"],
    "C11": ["C4", "E4", "G4", "Bb4", "D5", "F5"],
    "Cmaj11": ["C4", "E4", "G4", "B4", "D5", "F5"],
    "Cmin11": ["C4", "Eb4", "G4", "Bb4", "D5", "F5"],
    "C13": ["C4", "E4", "G4", "Bb4", "D5", "F5", "A5"],
    "Cmaj13": ["C4", "E4", "G4", "B4", "D5", "F5", "A5"],
    "Cmin13": ["C4", "Eb4", "G4", "Bb4", "D5", "F5", "Ab5"],

    # Sus Chords
    "Csus2": ["C4", "D4", "G4"],
    "Csus4": ["C4", "F4", "G4"],
    "Dsus2": ["D4", "E4", "A4"],
    "Dsus4": ["D4", "G4", "A4"],
    "Esus2": ["E4", "F#4", "B4"],
    "Esus4": ["E4", "A4", "B4"],
    "Fsus2": ["F4", "G4", "C5"],
    "Fsus4": ["F4", "Bb4", "C5"],
    "Gsus2": ["G4", "A4", "D5"],
    "Gsus4": ["G4", "C5", "D5"],
    "Asus2": ["A4", "B4", "E5"],
    "Asus4": ["A4", "D5", "E5"],
    "Bsus2": ["B4", "C#5", "F#5"], "Cbsus2": ["Cb4", "Db4", "Gb4"],
    "Bsus4": ["B4", "E5", "F#5"], "Cbsus4": ["Cb4", "Fb4", "Gb4"]
}
