import json
import io


def parse_entry(line):
    # No trailing return
    cleaned_line = line.replace("\n", "")

    # Since the definition can have slashes, let's take this off first
    front, back = cleaned_line.split("/", 1)
    definition = back[:-1] # No trailing /

    # Extract the pinyin next since there's a defined pattern for this
    head, tail = front.split("[")
    pinyin = tail.replace("]", "")

    # Carve up the rest
    traditional, simplified, _ = head.split(" ")

    return {
        "traditional": traditional,
        "simplified": simplified,
        "pinyin": pinyin,
        "definition": definition
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

        entries = apply_hsk_level(entries, hsk["HSK1"], 1)
        entries = apply_hsk_level(entries, hsk["HSK2"], 2)
        entries = apply_hsk_level(entries, hsk["HSK3"], 3)
        entries = apply_hsk_level(entries, hsk["HSK4"], 4)
        entries = apply_hsk_level(entries, hsk["HSK5"], 5)

    return entries


def main():
    entries = []
    with io.open("cedict_ts.u8", encoding="utf-8") as cedict_file:
        entries.extend([parse_entry(line) for line in cedict_file if line[0] != "#"])

    # Assign unique ID to match to difficulty levels
    for index, entry in enumerate(entries):
        entry['id'] = index

    entries = apply_hsk(entries)

    with io.open('cedict.json', 'w', encoding="utf-8") as outfile:
        json.dump(entries, outfile, ensure_ascii=False)


if __name__ == '__main__':
    main()
