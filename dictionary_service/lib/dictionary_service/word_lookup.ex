defmodule DictionaryService.WordLookup do
  use GenServer

  def lookup(word) do
    GenServer.call(:lookup, {:lookup, word})
  end

  def start_link(language) do
    GenServer.start_link(__MODULE__, language, name: :lookup)
  end

  def init(language) do
    {:ok, load_data(language)}
  end

  def load_data(language) do
    %{"heng" => "hahaha"}
  end

  def handle_call({:lookup, word}, _from, data) do
    response = Map.get(data, word, "not found")
    {:reply, response, data}
  end
end
