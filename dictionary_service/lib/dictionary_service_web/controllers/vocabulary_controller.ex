defmodule DictionaryServiceWeb.VocabularyController do
  use DictionaryServiceWeb, :controller

  def request(conn, %{"language" => language, "word" => word}) do
    IO.puts(lookup_word(language, word))
    # render(conn, "index.html")
    render(conn, lookup_word(language, word))
  end

  defp lookup_word("chinese", word) do
    DictionaryService.WordLookup.lookup(word)
  end

  defp lookup_word(_language, _word) do
    "Not found"
  end
end
