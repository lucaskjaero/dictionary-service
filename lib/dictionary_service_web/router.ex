defmodule DictionaryServiceWeb.Router do
  use DictionaryServiceWeb, :router

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/", DictionaryServiceWeb do
    pipe_through(:api)

    get("/", HealthController, :request)
  end

  scope "/dictionary/v1/", DictionaryServiceWeb do
    pipe_through(:api)

    # Vocab lookup
    get("/:language/definition/:word", VocabularyController, :request)

    # Level lists by language
    get("/chinese/hsk/:level", HSKController, :request)
  end

  scope "/stemming/v1/", DictionaryServiceWeb do
    pipe_through(:api)

    # Vocab lookup
    post("/:language/document", StemmingController, :request)
  end
end
