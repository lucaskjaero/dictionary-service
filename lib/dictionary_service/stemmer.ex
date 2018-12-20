defmodule DictionaryService.Stemmer do
  use GenServer

  def stem(language, sentence) do
    GenServer.call(:stemmer, {:stem, language, sentence})
  end

  def start_link(language) do
    GenServer.start_link(__MODULE__, language, name: :stemmer)
  end

  def init(_language) do
    {:ok, %{:token => token}} =
      Goth.Token.for_scope("https://www.googleapis.com/auth/cloud-platform")

    {:ok, token}
  end

  # Call Google natural language api for stemming
  def handle_call({:stem, language, sentence}, _from, token) do
    request = %{
      document: %{
        type: "PLAIN_TEXT",
        content: sentence
      }
    }

    {:ok, response} =
      HTTPoison.post(
        "https://language.googleapis.com/v1/documents:analyzeSyntax",
        Poison.encode!(request),
        [{"Content-Type", "application/json"}, {"Authorization", "Bearer #{token}"}]
      )

    decoded_response = Poison.decode!(response.body)

    {:reply, decoded_response["tokens"], token}
  end
end
