#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

class LRU(object):

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

        # Lista com as paginas que ja foram utilizadas
        pages_used = []

        while len(inputs) > 0:
            # Verifica se a pagina ja esta em uma das molduras
            if not (inputs[0] in frames):
                # Soma uma falta de pagina
                self.output += 1

                # Verifica se a lista esta cheia
                if len(frames) == frames_available:
                    # Copia de 'frames' para nao modificar a lista original
                    identify_number = copy.deepcopy(frames)

                    # Contador auxiliar para calcular o numero de identificacao de cada pagina que se encontra nas molduras
                    i = 0

                    # Percorre todos as paginas que estao nas molduras
                    while i < frames_available:

                        # Contador auxiliar para encontrar a pagina usada a mais tempo
                        j = len(pages_used) - 1

                        while j >= 0:
                            # Procura pagina atual na lista das paginas antigas
                            if pages_used[j] == identify_number[i]:
                                identify_number[i] = j
                                break
                            # Pagina nao foi referenciada anteriormente
                            elif j == 0:
                                identify_number[i] = 9999999

                            j -= 1

                        i += 1

                    # Retorna pagina utilizada a mais tempo
                    page_remove = pages_used[min(identify_number)]

                    # Remove pagina utilizada a mais tempo
                    frames.remove(page_remove)

                # Adiciona a pagina a ultima que chegou
                frames.append(inputs[0])

            # Adiciona as paginas utilizadas
            pages_used.append(inputs[0])
            inputs.pop(0)
