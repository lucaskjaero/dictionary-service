defmodule DictionaryService.WordLookup do
  use GenServer

  def lookup(word) do
    GenServer.call(:lookup, {:lookup, word})
  end

  def start_link(language) do
    GenServer.start_link(__MODULE__, language, name: :lookup)
  end

  def init(language) do
    data = load_data(language)

    {:ok, data}
  end

  def load_data(language) do
    %{heng: "hahaha"}
  end

  def handle_call({:lookup, word}, _from, data) do
    {:reply, data[word], data}
  end
end
