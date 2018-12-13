import json
import io


def parse_entry(line):
    # No trailing return
    cleaned_line = line.replace("\n", "")

    # Since the definition can have slashes, let's take this off first
    front, back = cleaned_line.split("/", 1)
    # No trailing / and multiple definitions
    definitions = back[:-1].split("/")

    # Extract the pinyin next since there's a defined pattern for this
    head, tail = front.split("[")
    # Remove trailing space
    pinyin = tail.replace("]", "")[:-1]

    # Carve up the rest
    traditional, simplified, _ = head.split(" ")

    return {
        "traditional": traditional,
        "simplified": simplified,
        "pinyin": pinyin,
        "definitions": definitions
    }


def apply_hsk_level(entries, words, number):
    for word in words:
        id = word['id']

        # Be prepared for the day that the order changes
        assert entries[id]['simplified'] == word['simplified']

        entries[id]['HSK'] = number

    return entries


def apply_hsk(entries):
    with io.open("hsk.json", encoding='utf-8') as hsk_file:
        hsk = json.load(hsk_file)

        entries = apply_hsk_level(entries, hsk["HSK6"], 6)
        entries = apply_hsk_level(entries, hsk["HSK5"], 5)
        entries = apply_hsk_level(entries, hsk["HSK4"], 4)
        entries = apply_hsk_level(entries, hsk["HSK3"], 3)
        entries = apply_hsk_level(entries, hsk["HSK2"], 2)
        entries = apply_hsk_level(entries, hsk["HSK1"], 1)

    return entries


def main():
    entries = []
    with io.open("cedict_ts.u8", encoding="utf-8") as cedict_file:
        entries.extend(
            [parse_entry(line) for line in cedict_file if line[0] != "#"]
        )

    # Assign unique ID to match to difficulty levels
    for index, entry in enumerate(entries):
        entry['id'] = index

    entries = apply_hsk(entries)

    with io.open('cedict.json', 'w', encoding="utf-8") as outfile:
        json.dump(entries, outfile, ensure_ascii=False)


if __name__ == '__main__':
    main()
