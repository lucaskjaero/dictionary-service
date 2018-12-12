defmodule DictionaryServiceWeb.VocabularyController do
  use DictionaryServiceWeb, :controller

  def request(conn, %{"language" => language, "word" => word}) do
    json(conn, %{data: lookup_word(language, word)})
  end

  defp lookup_word("chinese", word) do
    DictionaryService.WordLookup.lookup(word)
  end

  defp lookup_word(_language, _word) do
    "Not found"
  end
end
