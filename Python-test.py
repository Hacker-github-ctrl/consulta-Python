#!/usr/bin/env python3
# coding -utc- 8#
import time

def consulta():
  print("### consulta ###")
  print()

  nome = input("Digite o seu nome: ")
  if nome == "":
    print("\nOlá", nome)
    exit()
  else:
    print("\nDigite novamente")
    exit()
