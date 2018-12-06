scope "/api/v1/", DictionaryServiceWeb do
    pipe_through(:api)

    # Vocab lookup
    get("/:language/definition/:word", VocabularyController, :request)

    # Level lists by language
    get("/chinese/hsk/:level", HSKController, :request)
  end
