import mingus
import mingus.extra.lilypond as Lilypond


AVGTHRESHOLD = 100
keys = ["C", "D", "E", "F", "G", "A", "B"]
keysExt = ["#", "b", "", "", ""] #make the likelihood of keys being sharp or flat lower
pickableparts = ["verse", "bridge", "chorus", "prechorus"]
#offsets = [-7, -6, -6, -5, -5, -5, -4, -4, -4, -4, -3, -3, -3, -3, -3, -2, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7]
offsets = [-3, -3, -2, -2, -2, -2, -1, -1, -1, -1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3]


chordGen = [mingus.core.chords.I, mingus.core.chords.I7, mingus.core.chords.II, mingus.core.chords.II7, mingus.core.chords.III, mingus.core.chords.III7, mingus.core.chords.IV, mingus.core.chords.III7, mingus.core.chords.IV, mingus.core.chords.IV7, mingus.core.chords.V, mingus.core.chords.V7, mingus.core.chords.VI, mingus.core.chords.VI7, mingus.core.chords.II, mingus.core.chords.VII7]
