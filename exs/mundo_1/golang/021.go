/*
Desafio 021

Problema: Faça um programa que abra e reproduza o áudio de um arquivo MP3.

Resolução do problema:
*/

package main

import (
	"fmt"
	"io"
	"log"
	"os"


	//para rodar este codigo, e necessario ter estas duas bibliotecas.
	//voce pode instala-las usando o comando (go get)
	"github.com/hajimehoshi/oto" 

	"github.com/hajimehoshi/go-mp3"
)

func run() error {
	f, err := os.Open("../assets/audio/021.mp3")
	if err != nil {
		return err
	}
	defer f.Close()

	d, err := mp3.NewDecoder(f)
	if err != nil {
		return err
	}

	c, err := oto.NewContext(d.SampleRate(), 2, 2, 8192)
	if err != nil {
		return err
	}
	defer c.Close()

	p := c.NewPlayer()
	defer p.Close()

	fmt.Printf("Length: %d[bytes]\n", d.Length())

	if _, err := io.Copy(p, d); err != nil {
		return err
	}
	return nil
}

func main() {
	if err := run(); err != nil {
		log.Fatal(err)
	}
}
