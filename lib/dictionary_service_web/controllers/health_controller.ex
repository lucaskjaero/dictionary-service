defmodule DictionaryServiceWeb.HealthController do
  use DictionaryServiceWeb, :controller

  def request(conn, _data) do
    json(conn, %{health: "ok"})
  end
end
