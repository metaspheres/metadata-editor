from pathlib import Path
from mutagen import File

def scan_folder(folder_path):

    path = Path(folder_path)
    file_list = []

    for file_name in path.rglob('*'):
        if file_name.is_file() and file_name.suffix in (".mp3",".flac",".m4a",".wav",".ogg"):
            file_list.append(file_name)

    return file_list

def read_metadata(file_path):
    file = File(file_path)
    # to do
    # return dictionary w/fields - title, artist, album, track number, date (year)
    # handle missing tags....
    return file

results_file = read_metadata("C:/Users/anagr/Music/Traced in Air/Adam’s Murmur - demo version - Cynic.flac")

# results_folder = scan_folder("C:/Users/anagr/Music")

# print(results_folder)

print(results_file)