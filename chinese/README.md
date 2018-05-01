# Chinese language support
The dictionary is built on the [CEDICT](https://cc-cedict.org/editor/editor.php) open Chinese dictionary. If you use this language in the service, please consider contributing to their project, whether with enhancements or donations. The difficulty ranking is provided by the [HSK](https://en.wikipedia.org/wiki/Hanyu_Shuiping_Kaoshi) word levels.

## The dictionary
The raw dictionary is found in `cedict_ts.u8`. You should [download the latest version](https://www.mdbg.net/chinese/dictionary?page=cc-cedict) before building.

### Building the dictionary
Build it by running `python parse_cedict.py`. You should then see the `hsk.json` file, which is what the microservice will serve.

## HSK difficulty ratings
The difficulty ratings are stored in `hsk.json`, which are applied to the dictionary when it is built. They are stored with dictionary ids to identify which specific entry is being referred to. (Some words have more than one entry, but only one is appropriate)

### Applying the ratings
1. To recreate this, you should get the word lists in JSON, and then you can run the disambiguation tool.
2. Run `python apply_hsk_values.py <hsk_word_file> <output_file.json>`.
3. This will automatically apply ratings for the words with only one entry, and prompt you to choose which entry to use if there is more than one.
4. Add the output from the file into `hsk.json` under the appropriate level.
5. Rebuild the dictionary to update your server.
