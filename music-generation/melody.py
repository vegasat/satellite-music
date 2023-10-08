import constant
import statistics
import math
import mingus
import mingus.extra.lilypond as Lilypond
from midiutil import MIDIFile
from music import note_to_number, number_to_note
import utils

"""
def melody(song):
	MyMIDI = MIDIFile(1)
	MyMIDI.addTempo(0, 0, song.BPM)
	baseOctave = 4
	random.seed(song.hash)
	key = song.keyRoot
	notes = mingus.core.keys.get_notes(key)
	absoluteTime = 0
	soFarNotes = [key]
	for i, part in enumerate(song.pixelGroups):
		print("Part:",song.structure[i])
		length = len(song.chords[song.structure[i]])*4
		#calculates the stdev of our pixels
		stdev = statistics.stdev(part)
		print("stdev:",stdev)
		current = 0
		#more stdev means more notes and more random
		while current <= length:
			print("Note.")
			if current != 0: #first note SHOULD NOT be skipped
				#determine if we skip this note
				if random.randint(0, int(stdev*1.5))<15: #higher the stdev, higher the chance of skipping
					print("Skipped.")
					#skip note
					current+=1
					absoluteTime += 1
					continue
			delta = random.choice(constant.offsets) #x notes off
			duration = random.choice(utils.durationProcess(stdev))
			absoluteTime += duration
			current += duration
			note = notes[utils.get_looping_index(notes, notes.index(soFarNotes[-1])+delta)]
			soFarNotes.append(note)
			MyMIDI.addNote(0, 0, note_to_number(note, baseOctave), absoluteTime/4, duration/4, 90)
	with open("melody.mid", "wb") as out:
		MyMIDI.writeFile(out)
"""
def melody(midi, song, random):
	midi.addTempo(2, 2, song.BPM)

	key = song.keyRoot
	scale = mingus.core.keys.get_notes(key)
	LENGTHPERCHORD = 4
	time = 0
	numberOfChords = len(song.allChords)
	pixelChords = utils.split_list(song.allPixels, numberOfChords) #divides up the pixels by the number of chords, each chord has it's part of the image.
	for i, chord in enumerate(song.allChords):
		stdev = statistics.stdev(pixelChords[i])
		for x in range(8):
			note = number_to_note(random.choice(chord))
			duration = random.choice(utils.durationProcess(stdev))
			#there's a 15% chance that we jump to a note outside our chord.
			if random.randint(0,7) == 5:
				note = scale[
					utils.get_looping_index(
						scale,
						scale.index(note)+random.choice([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3])
						)
				]
			time += 1
			midi.addNote(2, 2, note_to_number(note, 4), time/2, duration/2, 120)
	