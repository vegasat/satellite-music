from midiutil import MIDIFile
from mingus.core import chords
import mingus.extra.lilypond as Lilypond
import constant

NOTES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
OCTAVES = list(range(11))
NOTES_IN_OCTAVE = len(NOTES)

def swap_accidentals(note):
    if note == 'Db':
        return 'C#'
    if note == 'D#':
        return 'Eb'
    if note == 'E#':
        return 'F'
    if note == 'Gb':
        return 'F#'
    if note == 'G#':
        return 'Ab'
    if note == 'A#':
        return 'Bb'
    if note == 'B#':
        return 'C'
    return note

def note_to_number(note, octave):
    note = NOTES.index(swap_accidentals(note))
    note += (NOTES_IN_OCTAVE * octave)
    return note

def number_to_note(midi_number):
    octave = midi_number // NOTES_IN_OCTAVE
    note_index = midi_number % NOTES_IN_OCTAVE
    note = NOTES[note_index]
    return note


def notes_to_number(notes, octave):
	outNotes = []
	for note in notes:
		outNotes.append(note_to_number(note, octave))
	return outNotes

def genChords(r, song, length=None):
	if length==None:
		length = r.choice([3, 4, 4, 4, 4, 6])
	chords = [notes_to_number(x(song.keyRoot), 4) for x in r.sample(constant.chordGen, length)]
	print("Generated chords")
	return chords

def chordsDump(song):
	chords = []
	for part in song.structure:
		print(part)
		print(chords)
		chords += song.chords[part]
	return chords

def chordsToMidi(midi, song, chords, filename): #pad only
	print(chords)
	midi.addTempo(1, 1, song.BPM)
	for i, chord in enumerate(chords):
		for note in chord:
			midi.addNote(1, 1, note+12, (i*4), 4, 90)
