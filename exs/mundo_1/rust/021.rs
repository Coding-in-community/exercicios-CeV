/*
Desafio 021

Problema: Faça um programa que abra e reproduza o áudio de um arquivo MP3.
*/

/*
AVISO: Esse código, assim como todos os outros que utilizam bibliotecas externas,
incluindo rand, só pode ser executado dentro de um ambiente completo Rust. O
caminho "src/sample.mp3" se refere exclusivamente a esse cenário. Uma vez que não
é viável executar este código em outro lugar que não seja com o Cargo, e o caminho
de todo projeto é relativo ao arquivo Cargo.toml, NÂO ALTERE o caminhodo arquivo.
Além de não fazer sentido, deixa a reprodução do conteúdo ainda mais complicada.
*/

use rodio::{Decoder, OutputStream, Sink};
use std::fs::File;
use std::io::BufReader;

fn main() {
    let file_path = "src/sample.mp3";

    let (_stream, stream_handle) = OutputStream::try_default().unwrap();

    let sink = Sink::try_new(&stream_handle).unwrap();

    let afile = File::open(file_path).expect("Erro ao abrir arquivo");
    let buffer = BufReader::new(afile);

    let source = Decoder::new(buffer).unwrap();

    sink.append(source);
    sink.sleep_until_end();
}
