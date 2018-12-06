defmodule DictionaryServiceWeb.VocabularyController do
  use DictionaryServiceWeb, :controller

  def request(conn, %{"language" => language, "word" => word}) do
    lookup_word(language, word)
    render(conn, "index.html")
  end

  defp lookup_word("chinese", word) do
  end

  defp lookup_word(_language, _word) do
    "Not found"
  end
end
