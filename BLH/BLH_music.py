import sys
import os

key = 3
# it's depends on if use 1/16 or F
up_note = True

f = open(os.path.dirname(__file__) + "/raw_music.txt")
raw_music = f.read()
f.close()
print raw_music

note_list = raw_music.split(' ')

pitch_names = {"1": "C", "2": "D", "3": "E", "4": "F", "5": "G", "6": "A", "7": "B","0":"P"}
up_notes = {"1": "1", "2": "1", "4": "2", "8": "4", "F": "8"}

new_note_list = []
for note in note_list:
    print note
    if note[0] != "0":
        # a regular note
        new_note = pitch_names[note[0]]
        if note[1] < "7":
            new_note +=chr(ord(note[1])+key)
        else:
            new_note += note[1]

        if up_note:
            new_note += up_notes[note[2]]
        else:
            new_note += note[2]
    else:
        # a silent note
        # a regular note
        new_note = pitch_names[note[0]]
        if up_note:
            new_note += up_notes[note[1]]
        else:
            new_note += note[1]
    new_note_list.append(new_note)

print new_note_list

f = open(os.path.dirname(__file__) + "/BLH_music.txt", 'w')
data = ' '
f.write(data.join(new_note_list))
f.close()
