#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math, copy

class OTM(object):

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

                # Verifica se a lista ja foi iniciada
                if len(frames) == frames_available:
                    # Copia de 'inputs' para nao modificar a lista original
                    aux = copy.deepcopy(inputs)
                    # Retorna apenas as paginas que ainda nao foram atendidas
                    aux = aux[1:]

                    # Copia de 'frames' para nao modificar a lista original
                    identify_number = copy.deepcopy(frames)

                    # Contador auxiliar para calcular o numero de identificacao de cada pagina que se encontra nas molduras
                    i = 0
                    # Percorre todos as paginas que estao nas molduras
                    while i < frames_available:
                        for j,a in enumerate(aux):
                            # Salva a posicao da proxima requisicao de cada pagina que se encontra nas molduras
                            if a == identify_number[i]:
                                identify_number[i] = j
                                i += 1
                                break


                    index = frames.index(max(identify_number))
                    frames.pop(index)

                # Adiciona a pagina a ultima que chegou
                frames.append(inputs[0])
            inputs.pop(0)
