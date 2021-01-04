defmodule Return do
  def msg() do
  IO.gets("What your name ? \n")
  |> name

  end
  defp name(name) do
    "Welcome #{name}"
    |> IO.puts
  end
end

Return.msg()
