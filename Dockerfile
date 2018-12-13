FROM elixir:1.7.4-alpine
RUN mix local.hex --force && mix archive.install hex phx_new 1.4.0 && mix local.rebar --force

EXPOSE 8000
ENV PORT=8000 MIX_ENV=prod

COPY . /app/
WORKDIR /app
RUN mix deps.get && mix compile
CMD ["mix", "phx.server"]
