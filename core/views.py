from random import randint

from chartjs.views.lines import BaseLineChartView
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

class DadosJSONView(BaseLineChartView):

    def get_labels(self):
        #Representa o eixo x
        labels = [
            'Janeiro',
            'Fevereiro',
            'Março',
            'Abril',
            'Maio',
            'Junho',
            'Julho',
            'Agosto',
            'Setembro',
            'Outubro',
            'Novembro',
            'Dezembro',
        ]

        return labels

    def get_providers(self):
        #Returna nome dos datasets
        datasets = [
            "Programação para Leigos",
            "Algoritmo e Lógica de Programação",
            "Programação em C",
            "Programação em Java",
            "Programação em Python",
            "Banco de Dados"        
        ]

        return datasets

    def get_data(self):
        '''
        Retorna os datasets para plotagem dos gráficos
        - Cada linha representa um dataset
        - Cada coluna representa um label

        A quantidade de dados devem ser iguais ao datasets/labels
        12 labels = 12 colunas
        06 datasets = 06 linhas
        
        '''
        dados = []
        for i in range(6):
            for j in range(12):
                dado = [
                    randint(1, 100), #jan
                    randint(1, 100), #fev
                    randint(1, 100), #mar
                    randint(1, 100), #abr
                    randint(1, 100), #mai
                    randint(1, 100), #jun
                    randint(1, 100), #jul
                    randint(1, 100), #ago
                    randint(1, 100), #set
                    randint(1, 100), #out
                    randint(1, 100), #nov
                    randint(1, 100), #dez
                ]
            dados.append(dado)
        return dados
