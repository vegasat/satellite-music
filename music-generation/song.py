import utils
import random
import mingus
import mingus.extra.lilypond as Lilypond
import constant
import structure
import music
import drums
import melody
from PIL import Image
from midiutil import MIDIFile
import sys

class Song:
	def __init__(self, imagepath):
		print("Song initializer hit")
		self.midi = MIDIFile(6)
		#drum 0
		self.midi.addProgramChange(1, 1, 0, 92) #chords 1
		self.midi.addProgramChange(2, 2, 0, 83) #melody 2
		#vocal 3
		self.image = Image.open(imagepath)
		if self.image.mode != "L":
			self.image = self.image.convert("L")
		width, height = self.image.size
		self.allPixels = []
		
		for y in range(height):
			for x in range(width):
				# Get the pixel value at (x, y)
				pixel_value = self.image.getpixel((x, y))
				# Process the pixel value here
				self.allPixels.append(pixel_value)
		
		self.imagepath = imagepath
		self.hash = utils.filehash(self.imagepath)
		random.seed(self.hash+"1")
		self.avgpixel = utils.average_pixel_value(self.imagepath)

		self.keyRoot = "."
		while not mingus.core.chords.keys.is_valid_key(self.keyRoot):
			self.keyRoot = random.choice(constant.keys)+random.choice(constant.keysExt)
		#we COOOULD do this in a way that involves logic and checks keys against a pre-defined list of keys that are valid they're flat or sharp
		#but we can also brute-force it since most are valid. in my limited test, bruteforcing it is more efficient.

		if self.avgpixel < constant.AVGTHRESHOLD:
			self.keyType = "minor"
			self.keyRoot = self.keyRoot.lower()
		else:
			self.keyType = "major"

		self.structure = structure.generateStructure(song=self)
		#split the pixels into parts
		self.pixelGroups = utils.split_list(self.allPixels, len(self.structure))
		self.pixels = {}
		for i, element in enumerate(self.structure):
			self.pixels[element] = self.pixelGroups[i]
		#for each element of the structure, generate a chord progression
		self.rootChords = music.genChords(random, self)
		self.chords = {}
		for i, element in enumerate(self.structure):
			print("song.py",i,element)
			if element not in self.chords.keys(): #here element is a portion of the structure (verse, chorus...) (aka array of arrays containing notes)
				if random.choice([False]*2+[True]*(i+2)) and i != 0:
					print("Modulating from last")
					#modulate the chord (modulation is in this case just changing a single chord to another one in the same key as random)
					last = list(self.chords[list(self.chords.keys())[-1]]) #last is just the last structure chord progression
					#generate a single chord in the correct key
					insertChord = music.genChords(random, self, length=1)[0]
					last[random.randint(0,len(last)-1)] = insertChord #picks a random chord to be modulated to a different one
					self.chords[element] = last
				else:
					print("Inserting straight root")
					#don't modulate it
					self.chords[element] = self.rootChords
				newChordPosition = random.randint(0,5)
				if newChordPosition == 0: #determine if we put in another chord
					print("Inserting another into current")
					insertChord = music.genChords(random, self, length=1)[0]
					self.chords[element].insert(newChordPosition, insertChord)

		self.chords["outro"] = self.chords["intro"]
		self.drum = {}
		self.BPM = random.randint(130, 180)
		self.allChords = music.chordsDump(self)
		self.allDrums = drums.genDrum(self, random)

		print("Done")

	def render(self):

		drums.toMidi(self.midi, self.allDrums, self.BPM, "drums.mid")
		music.chordsToMidi(self.midi, self, self.allChords, "music.mid")
		melody.melody(self.midi, self, random)

		with open("main.mid", "wb") as out:
			self.midi.writeFile(out)

		utils.midi_to_mp3("main.mid", "music.mp3")


		print("Alldrums:",self.allDrums)
		print("Allchords:",self.allChords)

	def print(self):
		print("Imagepath:",self.imagepath)
		print("Hash:",self.hash)
		print("AVG:",self.avgpixel)
		print("Key type:",self.keyType)
		print("Key:",self.keyRoot+" "+self.keyType)
		print("Structure:","-".join(self.structure))
		print("BPM:",self.BPM)
		print("Chords:",self.chords)
		print("Drums:",self.drum)

song = Song(sys.argv[1])
song.print()
song.render()
