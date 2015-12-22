#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math, copy

class FIFO(object):

    def __init__(self, lines):
        # Copia de 'lines' para nao modificar o arquivo original
        inputs = copy.deepcopy(lines)

        # Valor com a quantidade total de faltas de paginas
        self.output = 0

        # Converte todos os valores de entrada para inteiros
        for i,line in enumerate(inputs):
            inputs[i] = int(line.split()[0])

        # Quantidade de molduras disponiveis na RAM
        frames_available = inputs.pop(0)
        # Lista de molduras presentes na RAM
        frames = []

        i = 0
        while len(inputs) > 0:
            # Verifica se a pagina ja esta em uma das molduras
            if not (inputs[i] in frames):
                # Soma uma falta de pagina
                self.output += 1

                # Verifica se a lista ja foi iniciada
                if len(frames) == frames_available:
                    # Retira a primeira pagina que chegou
                    frames.pop(0)

                # Adiciona a pagina a ultima que chegou
                frames.append(inputs[i])
            inputs.pop(i)
