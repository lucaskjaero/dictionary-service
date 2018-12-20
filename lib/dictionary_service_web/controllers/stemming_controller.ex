defmodule DictionaryServiceWeb.StemmingController do
  use DictionaryServiceWeb, :controller

  def request(conn, %{"language" => language, "text" => text}) do
    json(conn, %{tokens: stem(language, text), status: "OK"})
  end

  defp stem(language, document) do
    DictionaryService.Stemmer.stem(language, document)
    |> Enum.map(fn word -> word["lemma"] end)
  end
end
