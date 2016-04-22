import csv
import sys
import os

import pprint

input_dir = ""
output_file = ""

speakers = {}
speakers_table = {}

def check_file_name(file):
    if file.endswith(".csv"):
        return True
    return False


def output_speaker_table(speakers_dict, path):

    key_list = [key for key in speakers_dict]
    table = []
    subjects = list(set([key[:2] for key in key_list]))
    subjects.sort()
    table.append(["visit"]+ subjects) # the header

    with open(path.replace(".txt", ".csv"), "wb") as output:
        writer = csv.writer(output)
        writer.writerows(table)

    #for key in key_list:


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


    output_speaker_table(speakers, output_file)


    pprint.pprint(speakers)