#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

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

        while len(inputs) > 0:
            # Verifica se a pagina ja esta em uma das molduras
            if not (inputs[0] in frames):
                # Soma uma falta de pagina
                self.output += 1

                # Verifica se a lista esta cheia
                if len(frames) == frames_available:
                    # Retira a primeira pagina que chegou
                    frames.pop(0)

                # Adiciona a pagina a ultima que chegou
                frames.append(inputs[0])
            inputs.pop(0)
