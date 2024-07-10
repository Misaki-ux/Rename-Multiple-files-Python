#GROUP SCRIPT FOR RENAME FILES FROM .mkv, .avi, .mp4.
import os
import re
#File name after modification
fileOP = 'SCORPION - S01.ep'
folder = r"D:\serie\SCORPION (2014-2018) - Complete TV Series, Season 1,2,3,4 S01,S02,S03,S04 - 720p Web-DL x264\Season 1 (2014-15)"

# Regular expression to match the episode number with an optional space and capture the file extension
pattern = re.compile(r'SCORPION - S01[ ]?E(\d+).*\.(mkv|avi|mp4)')

# Iterate over files in the folder
for filename in os.listdir(folder):
    # Search for the pattern in the file name
    match = pattern.search(filename)
    if match:
        try:
            # Extract episode number and file extension from the old file name
            episode_number = match.group(1)
            file_extension = match.group(2)
            # Generate new file name
            new_name = os.path.join(folder, f'{fileOP}{episode_number}.{file_extension}')
            old_file_path = os.path.join(folder, filename)
            new_file_path = os.path.join(folder, new_name)
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_name}")
        except Exception as e:
            print(f"Failed to rename {filename}: {e}")
    else:
        print(f"Skipped: {filename} (does not match expected pattern)")


"""--------------OLD SCRIPT----------
fileOP='Shameless S03.ep'
folder = r"D:\serie\Shameless\Shameless.US.S03.Season.3"

oldName1 = folder + "/" + 'Shameless S02.ep01.mkv'
newName1 = folder + "/" + fileOP + '01' + '.mkv' 

oldName2 = folder + "/" + 'Shameless S02.ep02.mkv'
newName2 = folder + "/" + fileOP + '02' + '.mkv' 

oldName3 = folder + "/" + 'Shameless S02.ep03.mkv'
newName3 = folder + "/" + fileOP + '03' + '.mkv'

oldName4 = folder + "/" + 'Shameless S02.ep04.mkv'
newName4 = folder + "/" + fileOP + '04' + '.mkv'

oldName5 = folder + "/" + 'Shameless S02.ep05.mkv'
newName5 = folder + "/" + fileOP + '05' + '.mkv' 

oldName6 = folder + "/" + 'Shameless S02.ep06.mkv'
newName6 = folder + "/" + fileOP + '06' + '.mkv' 

oldName7 = folder + "/" + 'Shameless S02.ep07.mkv'
newName7 = folder + "/" + fileOP + '07' + '.mkv'

oldName8 = folder + "/" + 'Shameless S02.ep08.mkv'
newName8 = folder + "/" + fileOP + '08' + '.mkv'

oldName9 = folder + "/" + 'Shameless S02.ep09.mkv'
newName9 = folder + "/" + fileOP + '09' + '.mkv' 

oldName10 = folder + "/" + 'Shameless S02.ep10.mkv'
newName10 = folder + "/" + fileOP + '10' + '.mkv' 

oldName11 = folder + "/" + 'Shameless S02.ep11.mkv'
newName11 = folder + "/" + fileOP + '11' + '.mkv'

oldName12 = folder + "/" + 'Shameless S02.ep12.mkv'
newName12 = folder + "/" + fileOP + '12' + '.mkv'

os.rename(oldName1, newName1)
os.rename(oldName2, newName2)
os.rename(oldName3, newName3)
os.rename(oldName4, newName4)
os.rename(oldName5, newName5)
os.rename(oldName6, newName6)
os.rename(oldName7, newName7)
os.rename(oldName8, newName8)
os.rename(oldName9, newName9)
os.rename(oldName10, newName10)
os.rename(oldName11, newName11)
os.rename(oldName12, newName12)
"""