defmodule DictionaryServiceWeb.VocabularyController do
  use DictionaryServiceWeb, :controller

  def request(conn, %{"language" => language, "word" => word}) do
    json(conn, %{entries: lookup_word(language, word), status: "OK"})
  end

  defp lookup_word("chinese", word) do
    DictionaryService.ChineseLookup.lookup(word)
  end

  defp lookup_word(_language, _word) do
    "Not found"
  end
end
