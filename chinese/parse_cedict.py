

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
