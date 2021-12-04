import tomita
import tomita.legacy.pysynth_c
import tomita.legacy.play_wav

#https://en.wikipedia.org/wiki/Isao_Tomita

# Notes are ‘a’ through ‘g’ of course, # optionally with ‘#’ or ‘b’ appended for sharps or flats. # Finally the octave number (defaults to octave 4 if not given). # An asterisk at the end makes the note a little louder (useful for the beat). # ‘r’ is a rest.

# Note value is a number: # 1=Whole Note; 2=Half Note; 4=Quarter Note, etc. # Dotted notes can be written in two ways: # 1.33 = -2 = dotted half # 2.66 = -4 = dotted quarter # 5.33 = -8 = dotted eighth


#can use this import
#song1 = tomita.legacy.pysynth_c.song1
#or here is the raw song
song1 = [
['c',4],['d',4],['e',4],['f',4],['g',4],['a',4],['b',4],['c5',2],['r',1],
['c3',4],['d3',4],['e3',4],['f3',4],['g3',4],['a3',4],['b3',4],['c4',2],['r',1],
['c1*', 1], ['c2*', 1], ['c3*', 1], ['c4*', 1], ['c5*', 1], ['c6*', 1], ['c7*', 1], ['c8*', 1],
]
#this line writes the song to a wav file
#then click on the new wav file to play it
tomita.legacy.pysynth_c.make_wav(song1, bpm=120, transpose=0, pause=0.05, boost=1.1, repeat=0, fn='song1.wav', silent=False)

#more demosongs here: 
#https://github.com/g4brielvs/python-tomita/blob/master/tomita/legacy/demosongs.py

#song2 = tomita.legacy.pysynth_c.song2
#tomita.legacy.pysynth_c.make_wav(song2, bpm=120, transpose=0, pause=0.05, boost=1.1, repeat=0, fn='song2.wav', silent=False)



