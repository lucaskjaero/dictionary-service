defmodule DictionaryService.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false

  use Application

  def start(_type, _args) do
    import Supervisor.Spec, warn: false
    # List all child processes to be supervised
    children = [
      # Start the endpoint when the application starts
      DictionaryServiceWeb.Endpoint,
      # Starts a worker by calling: DictionaryService.Worker.start_link(arg)
      # {DictionaryService.Worker, arg},
      DictionaryService.ChineseLookup
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: DictionaryService.Supervisor]
    Supervisor.start_link(children, opts)
  end

  # Tell Phoenix to update the endpoint configuration
  # whenever the application is updated.
  def config_change(changed, _new, removed) do
    DictionaryServiceWeb.Endpoint.config_change(changed, removed)
    :ok
  end
end
