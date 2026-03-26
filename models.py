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
    #fallback p/data 
    date = file.get('date')
    try:
        date = int((file.get('date') or ['1980'])[0][:4])
    except ValueError:
        date = 1980

    file_metadata = {
        "Artist":(file.get('artist') or ['Unknown'])[0],
        "Album Artist:":(file.get('albumartist') or ['Unknown'])[0],
        "Title":(file.get('title') or ['Unknown'])[0],
        "Album":(file.get('album') or ['Unknown'])[0],
        "Track Number":(file.get('tracknumber') or ['Unknown'])[0],
        "Date": date,
        "Path": file_path
        }

    return file_metadata

def get_library(folder_path):

    file_list = []

    for file_path in scan_folder(folder_path):
        file_list.append(read_metadata(file_path))
    
    return file_list


# results_file = read_metadata("C:/Users/anagr/Music/Traced in Air/Adam’s Murmur - demo version - Cynic.flac")

# results_folder = scan_folder("C:/Users/anagr/Music")

# results_all = get_library("C:/Users/anagr/Music")

# print(results_all)

#  
# print(results_file)
