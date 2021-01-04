defmodule Calc do

  def main do
  a = IO.gets("Digite um numero: ")
      |> String.trim()
      |> String.to_integer()
  b = IO.gets("Digite um numero: ")
      |> String.trim()
      |> String.to_integer()

  a
  |> sum(b)
  end

  def sum(a, b) do
    IO.puts "A soma e #{a+b}"
  end
end

Calc.main()
