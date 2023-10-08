import hashlib
from PIL import Image
import os

def get_looping_index(my_list, index_delta):
    # Calculate the effective index by taking modulo the length of the list
    list_length = len(my_list)
    effective_index = (index_delta % list_length)

    # Handle negative indices
    if effective_index < 0:
        effective_index += list_length

    return effective_index

def durationProcess(stdev):
	base = [1, 2, 3, 4, 5]
	if stdev>40:
		base.append(1)
		base.append(1)
		base.append(2)
	if stdev>30:
		base.append(1)
		base.append(2)
	if stdev>20:
		base.append(2)
		base.append(3)
		base.append(4)
	if stdev>10:
		base.append(3)
		base.append(4)
		base.append(3)
	return base

def split_list(input_list, n):
    # Calculate the size of each part
    part_size = len(input_list) // n
    
    # Use list comprehension to split the list into parts
    parts = [input_list[i:i+part_size] for i in range(0, len(input_list), part_size)]
    
    return parts

def midi_to_mp3(midi_file, mp3_file, soundfont="OPLLandOPLL2DrumFix2.sf2"):
    # Convert MIDI to WAV using fluidsynth
    wav_file = mp3_file.replace('.mp3', '.wav')
    os.system(f'fluidsynth/bin/fluidsynth -ni {soundfont} {midi_file} -F {wav_file} -r 44100')

def filehash(filename):
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

	   # loop till the end of the file
	   chunk = 0
	   while chunk != b'':
		   # read only 1024 bytes at a time
		   chunk = file.read(1024)
		   h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()


def average_pixel_value(filename):
	try:
		# Open the grayscale image
		image = Image.open(filename)

		# Ensure the image is in grayscale (L mode)
		if image.mode != "L":
			image = image.convert("L")

		# Get the width and height of the image
		width, height = image.size

		# Initialize a variable to store the sum of pixel values
		pixel_sum = 0

		# Loop through all the pixel values and calculate the sum
		for y in range(height):
			for x in range(width):
				pixel_value = image.getpixel((x, y))
				pixel_sum += pixel_value

		# Calculate the average pixel value
		average_value = pixel_sum / (width * height)

		# Close the image
		image.close()

		return average_value

	except Exception as e:
		return None  # Handle errors gracefully, return None for simplicity
