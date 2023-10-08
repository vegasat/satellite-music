
# Satelitte music

We decided to develop a program that takes a raw satellite image from NASA's database and turns it into a music video. This involved using a NASA .tiff image as a creative starting point, with Python employed to craft music adhering to the technical precision of music theory. Custom algorithms handled drums, chords, and melodies. The result is a program that generates distinct soundtracks for each input image. Blender was used for video development, utilizing SAR's image data for 3D visuals and sound visualization.

# Python - music
Python is employed to generate music from an image.

## Quick start
A simple demo can be done by using the included image (SS_01502_STD_F2536.jpg)
Note that this code is tested on Windows. Users should install `fluidsynth` before using.
Additionally, a General MIDI .sf2 named OPLLandOPLL2DrumFix2.sf2 should be provided in the Python root for it to work. One can be obtained at: https://musical-artifacts.com/artifacts/3236/

Firstly, install the requirements via PIP
```bash
pip install -r requirements.txt
```
Then, just run the `song.py` and provide an image as an argument.
```bash
py song.py SS_01502_STD_F2536.jpg
```
> **_NOTE:_**  `py` is usually the default path for **Windows** installations of Python via the Python launched. If you're running on Linux, the default is `python3`. Adjust accordingly.

## Code
The code is in development.
The `Song` class provides easy access to most, if not all attributes of the entire song.
The `render()` method of the class is responsible for final generation of the music, so if you're looking to expand the code, add another track or instrument, I'd start there.
