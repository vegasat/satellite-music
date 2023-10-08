from midiutil import MIDIFile

kick = 36  # Bass Drum 1
clap = 39
snare = 38  # Acoustic Snare
chh = 42  # Closed Hi-hat
ohh = 46  # Open Hi-hat
tom1 = 41  # Low Tom
tom2 = 48  # Hi-Mid Tom
tom3 = 50  # High Tom
ride = 51  # Ride Cymbal 1
crash = 49  # Crash Cymbal 1
splash = 55  # Splash Cymbal

def toMidi(midi, drum_patterns, tempo, output_file_name):

    track = 0
    time = 0
    midi.addTrackName(track, time, "Drum Track")
    midi.addTempo(track, time, tempo)

    channel = 9

    for i, beat in enumerate(drum_patterns):
    	for drum in beat:
    		midi.addNote(track, channel, drum, (i/4), 0.25, 90)

def genDrum(song, random):
	mainPattern = []
	for part in song.structure:
		random.seed(song.hash+part)
		#get the time of the bar from the chords
		length = 8  
		pattern = [[] for _ in range(length)]
		print(part, length, pattern)
		if part in ["intro", "outro"]:
			#odds
			drums = [clap]*1+[kick]*3+[snare]*4+[chh]*3+[ohh]*2+[tom1]*1+[tom2]*1+[tom3]*1+[random.choice([ride, crash, splash])]*1
			for x in range(random.randint(1,2)): #1-3 drum tracks for intro
				print()
				if x == 0:# first uuusually doesn't have an offset
					offset = 0
				else:
					offset = random.randint(1,int(length/4))
					if random.randint(1, 25) == 5:
						offset += 1 #very rarely do we get a an odd offset
				skip = random.randint(1, 2)
				print("Skip:",skip)
				print("Offset:",offset)
				print("Length:",length)
				picked = random.choice(drums)
				print("Picked:",picked)
				for i in range(offset, length, skip):
					print("i:",i)
					pattern[i].append(picked)
				print("Pattern after ifor:",pattern)
				#remove already picked from selection
				drums = [drum for drum in drums if drum != picked]
		if part == "chorus":
			#odds
			drums = [clap]*2+[kick]*5+[snare]*2+[chh]*4+[ohh]*2+[tom1]*1+[tom2]*1+[tom3]*1+[random.choice([ride])]*1
			pattern = [[] for _ in range(length)]
			for x in range(random.randint(2,4)):
				print()
				if x == 0:# first uuusually doesn't have an offset
					offset = 0
				else:
					offset = random.choice([0, 1, 2, 3, 0, 1])
					if random.randint(1, 15) == 5:
						offset += 1 #very rarely do we get a an odd offset
				skip = random.choice([1, 2, 4])
				print("Skip:",skip)
				print("Offset:",offset)
				print("Length:",length)
				picked = random.choice(drums)
				print("Picked:",picked)
				for i in range(offset, length, skip):
					print("i:",i)
					pattern[i].append(picked)
				print("Pattern after ifor:",pattern)
				#remove already picked from selection
				drums = [drum for drum in drums if drum != picked]
		if part == "prechorus":
			#odds
			drums = [clap]*1+[kick]*2+[snare]*2+[chh]*3+[ohh]*2+[tom2]*1+[tom3]*2+[random.choice([ride, crash, splash])]*1
			pattern = [[] for _ in range(length)]
			for x in range(random.randint(1,3)):
				print()
				if x == 0:# first uuusually doesn't have an offset
					offset = 0
				else:
					offset = random.randint(1,length/4)
					if random.randint(1, 15) == 5:
						offset += 1 #very rarely do we get a an odd offset
				skip = random.randint(1, 4)
				print("Skip:",skip)
				print("Offset:",offset)
				print("Length:",length)
				picked = random.choice(drums)
				print("Picked:",picked)
				for i in range(offset, length, skip):
					print("i:",i)
					pattern[i].append(picked)
				print("Pattern after ifor:",pattern)
				#remove already picked from selection
				drums = [drum for drum in drums if drum != picked]
		if part == "bridge":
			#odds
			drums = [clap]*2+[kick]*2+[snare]*2+[chh]*3+[ohh]*3+[tom1]*2+[tom2]*2+[tom3]*2+[random.choice([ride, crash, splash])]*1
			pattern = [[] for _ in range(length)]
			for x in range(random.randint(1,2)):
				print()
				if x == 0:# first uuusually doesn't have an offset
					offset = 0
				else:
					offset = random.randint(1,length/4)
					if random.randint(1, 40) == 5:
						offset += 1 #very rarely do we get a an odd offset
				skip = random.randint(1, 8)
				print("Skip:",skip)
				print("Offset:",offset)
				print("Length:",length)
				picked = random.choice(drums)
				print("Picked:",picked)
				for i in range(offset, length, skip):
					print("i:",i)
					pattern[i].append(picked)
				print("Pattern after ifor:",pattern)
				#remove already picked from selection
				drums = [drum for drum in drums if drum != picked]
		if part == "verse":
			#odds
			drums = [clap]*1+[kick]*4+[snare]*3+[chh]*1+[ohh]*1+[tom1]*1+[tom2]*1+[tom3]*1+[random.choice([ride, crash, splash])]*1
			pattern = [[] for _ in range(length)]
			for x in range(random.randint(1,2)):
				print()
				if x == 0:# first uuusually doesn't have an offset
					offset = 0
				else:
					offset = random.randint(1,length/4)*2
					if random.randint(1, 40) == 5:
						offset += 1 #very rarely do we get a an odd offset
				skip = random.randint(1, 3)*2
				print("Skip:",skip)
				print("Offset:",offset)
				print("Length:",length)
				picked = random.choice(drums)
				print("Picked:",picked)
				for i in range(offset, length, skip):
					print("i:",i)
					pattern[i].append(picked)
				print("Pattern after ifor:",pattern)
				#remove already picked from selection
				drums = [drum for drum in drums if drum != picked]
		print(pattern,"*",part)
		mainPattern += pattern*len(song.chords[part])*2
	return mainPattern
