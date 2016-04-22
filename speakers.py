import csv
import sys
import os

import pprint

input_dir = ""
output_file = ""

speakers = {}


def check_file_name(file):
    if file.endswith(".csv"):
        return True
    return False

if __name__ == "__main__":

    input_dir = sys.argv[1]
    output_file = sys.argv[2]

    for file in os.listdir(input_dir):
        if check_file_name(file):
            key = file[0:5]
            speakers[key] = {"audio": [], "video": []}

    for file in os.listdir(input_dir):
        print file
        if check_file_name(file):
            with open(os.path.join(input_dir, file), "rU") as input:
                key = file[0:5]
                reader = csv.reader(input)
                reader.next()
                if "audio" in file:
                    audio_speakers = [row[4] for row in reader]
                    speakers[key]["audio"] = list(set(audio_speakers))
                elif "video" in file:
                    video_speakers = [row[6] for row in reader]
                    speakers[key]["video"] = list(set(video_speakers))

    with open(output_file, "wb") as output:
        output.write(pprint.pformat(speakers, 4))

    pprint.pprint(speakers)