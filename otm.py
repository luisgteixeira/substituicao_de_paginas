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

                # Verifica se a lista esta cheia
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
                            if a == identify_number[i]:
                                # Salva a posicao da proxima requisicao de cada pagina que se encontra nas molduras
                                identify_number[i] = j
                                break
                            elif j == (len(aux) - 1):
                                # Pagina nao sera referenciada futuramente
                                identify_number[i] = -1
                        i += 1

                    if aux:

                        if -1 in identify_number:
                            # Apaga pagina que nao vai ser referenciada futuramente
                            value = frames[identify_number.index(-1)]
                        else:
                            # Retorna pagina que demorara mais execucoes para sera referenciada
                            value = aux[max(identify_number)]

                        # Apaga pagina que sera referenciada com maior numero de execucoes a frente
                        frames.remove(value)

                # Adiciona a ultima pagina que chegou
                frames.append(inputs[0])
            inputs.pop(0)
