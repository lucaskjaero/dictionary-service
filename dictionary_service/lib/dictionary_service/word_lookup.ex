defmodule DictionaryService.WordLookup do
  use GenServer

  def lookup(pid, word) do
    GenServer.call(pid, {:lookup, word})
  end

  def start_link(data) do
    GenServer.start_link(__MODULE__, data)
  end

  def init(data) do
    {:ok, data}
  end

  def load_data(path) do
    %{heng: "hahaha"}
  end

  def handle_call({:lookup, word}, _from, data) do
    {:reply, data[word], data}
  end
end
