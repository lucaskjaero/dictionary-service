import json
import sys


def load_cedict():
    with open("cedict.json") as cedict:
        return json.load(cedict)


def load_hsk_word_file(filename):
    with open(filename) as hsk:
        hsk_words = json.load(hsk)
        return [word['hanzi'] for word in hsk_words]


def choose_option(hsk_word, options):
    print(hsk_word)
    for index, candidate in enumerate(options):
        print("%s: %s" % (index, chinese_dictionary[candidate]))

    selection = input("Choose option: ")

    if selection == "all":
        return options

    # Allow multiple selections
    if "," in selection:
        selections = [int(option) for option in selection.split(",")]
    else:
        selections = [int(selection)]

    return [options[selected_id] for selected_id in selections]


chinese_dictionary = load_cedict()


def main():
    level_words = []
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    print("Loading file " + input_file)

    for hsk_word in load_hsk_word_file(input_file):
        options = [word['id'] for word in chinese_dictionary if word['simplified'] == hsk_word]

        if len(options) == 1:
            level_words.append({
                "id": options[0],
                "simplified": hsk_word
            })

        elif len(options) == 0:
            pass

        else:
            for selection in choose_option(hsk_word, options):
                level_words.append({
                    "id": selection,
                    "simplified": hsk_word
                })

    with open(output_file, 'w') as outfile:
        json.dump(level_words, outfile, ensure_ascii=False)


if __name__ == '__main__':
    main()
