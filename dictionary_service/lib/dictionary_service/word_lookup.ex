defmodule DictionaryService.ChineseLookup do
  use GenServer

  def lookup(word) do
    GenServer.call(:chineselookup, {:lookup, word})
  end

  def start_link(language) do
    GenServer.start_link(__MODULE__, language, name: :chineselookup)
  end

  def init(_language) do
    {:ok, raw} = File.read("cedict.json")
    {:ok, data} = Poison.decode(raw)
    {:ok, data}
  end

  def handle_call({:lookup, word}, _from, data) do
    response =
      data
      |> Enum.filter(fn entry -> character_matches(entry, word) end)
      |> Enum.sort(&sort_by_hsk/2)

    {:reply, response, data}
  end

  defp character_matches(entry, character) do
    Map.get(entry, "traditional") == character or Map.get(entry, "simplified") == character
  end

  defp sort_by_hsk(a, b) do
    Map.get(a, "hsk", 7) >= Map.get(b, "hsk", 7)
  end
end
