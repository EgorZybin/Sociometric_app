import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


class Sociometric:
    def __init__(self, file_path):
        """
        Инициализация класса.
        :param file_path: Путь к файлу с данными.
        """
        self.file_path = file_path
        self.matrix = self.read_data(file_path)
        self.num_people = self.matrix.shape[0]

    def read_data(self, file_path):
        """
        Чтение данных из файла и создание социометрической матрицы.
        :param file_path: Путь к файлу с данными.
        :return: Социометрическая матрица.
        """
        with open(file_path, 'r') as file:
            lines = file.readlines()

        matrix = []
        for line in lines[1:]:  # Пропускаем заголовок
            row = []
            for value in line.strip().split()[1:]:  # Пропускаем индекс участника
                if value == '+':
                    row.append(1)  # Положительный выбор
                elif value == '-':
                    row.append(-1)  # Отрицательный выбор
                else:
                    row.append(0)  # Нет выбора
            matrix.append(row)

        return np.array(matrix)

    def sociometric_status(self):
        """
        Расчет социометрического статуса
        C = (R+ + R-) / (N - 1)
        """
        matrix = self.matrix
        num_people = matrix.shape[0]
        statuses = []

        for i in range(num_people):
            positive_choices = np.sum(matrix[i] == 1)
            negative_choices = np.sum(matrix[i] == -1)

            status = (positive_choices + negative_choices) / (num_people - 1)
            statuses.append(int(status))

        return statuses

    def emotional_expanse(self):
        """
        Расчёт индекса эмоциональной экспансивности.
        :return: Индекс эмоциональной экспансивности.
        """
        B_plus = np.sum(self.matrix == 1)
        B_minus = np.sum(self.matrix == -1)
        E = (B_plus + B_minus) / (self.num_people - 1)
        return round(E, 2)

    def expansiveness_index(self):
        """
        Расчёт индекса экспансивности.
        :return: Индекс экспансивности.
        """
        R_o_plus = np.sum(self.matrix == 1)
        R_o_minus = np.sum(self.matrix == -1)
        Ag = (R_o_plus + R_o_minus) / self.num_people
        return round(Ag, 2)

    def cohesion_index(self, k):
        """
        Расчёт индекса сплоченности.
        :param k: Лимит выборов.
        :return: Индекс сплоченности.
        """
        mutual_positive = 0

        for i in range(self.num_people):
            for j in range(self.num_people):
                if self.matrix[i, j] == 1 and self.matrix[j, i] == 1:
                    mutual_positive += 1

        Gq = mutual_positive / (0.5 * self.num_people * k)
        return round(Gq, 2)

    def antipathy_index(self, k):
        """
        Расчёт индекса антипатии.
        :param k: Лимит выборов.
        :return: Индекс антипатии.
        """
        mutual_negative = 0

        for i in range(self.num_people):
            for j in range(self.num_people):
                if self.matrix[i, j] == -1 and self.matrix[j, i] == -1:
                    mutual_negative += 1

        Ga = mutual_negative / (0.5 * self.num_people * k)
        return round(Ga, 2)

    def tension_index(self, k):
        """
        Расчёт индекса напряженности.
        :param k: Лимит выборов.
        :return: Индекс напряженности.
        """
        disagreement_count = 0

        for i in range(self.num_people):
            for j in range(self.num_people):
                if self.matrix[i, j] != self.matrix[j, i]:
                    disagreement_count += 1

        Gn = disagreement_count / (self.num_people * k)
        return round(Gn, 2)

    def plot_socionetwork(self, file_name='sociometric.png'):
        """
        Построение социограммы.
        """
        G = nx.Graph()

        # Добавление узлов
        for i in range(self.num_people):
            G.add_node(i)

        # Добавление рёбер (положительные и отрицательные выборы)
        for i in range(self.num_people):
            for j in range(self.num_people):
                if self.matrix[i, j] == 1:
                    G.add_edge(i, j, color='green', weight=2)  # Положительные связи
                elif self.matrix[i, j] == -1:
                    G.add_edge(i, j, color='red', weight=2)  # Отрицательные связи

        # Рисуем граф
        edge_colors = [G[u][v]['color'] for u, v in G.edges()]
        edge_weights = [G[u][v]['weight'] for u, v in G.edges()]

        # Используем более сложное расположение для более группового отображения
        pos = nx.spring_layout(G, k=0.5, iterations=50)  # Альтернатива для более плотного группирования

        # Цвета и размеры узлов зависят от статуса
        statuses = self.sociometric_status()
        node_colors = ['lightgreen' if status >= 0 else 'salmon' for status in statuses]
        node_sizes = [500 + 200 * abs(status) for status in statuses]  # Размеры узлов пропорциональны статусу

        # Рисуем граф с улучшениями
        nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color=node_colors, font_size=12,
                font_weight="bold",
                edge_color=edge_colors, width=edge_weights, alpha=0.7)

        plt.title("Социограмма")
        # Сохраняем граф в файл (в формате PNG, JPG или SVG)
        plt.savefig(file_name, format=file_name.split('.')[-1].upper())  # Сохранение в формате файла
        plt.show()


if __name__ == "__main__":
    file_path = "data.txt"  # Путь к текстовому файлу с данными
    socio_metric = Sociometric(file_path)
    k = 2  # Лимит выборов

    # Получаем социометрический статус участников
    statuses = socio_metric.sociometric_status()
    print("Социометрический статус участников: ", statuses)

    # Рассчитываем индекс эмоциональной экспансивности
    expanse = socio_metric.emotional_expanse()
    print("Индекс эмоциональной экспансивности: ", expanse)

    # Рассчитываем индекс экспансивности
    expansiveness = socio_metric.expansiveness_index()
    print("Индекс экспансивности: ", expansiveness)

    # Рассчитываем индекс сплоченности
    cohesion = socio_metric.cohesion_index(k)
    print("Индекс сплоченности: ", cohesion)

    # Рассчитываем индекс антипатии
    antipathy = socio_metric.antipathy_index(k)
    print("Индекс антипатии: ", antipathy)

    # Рассчитываем индекс напряженности
    tension = socio_metric.tension_index(k)
    print("Индекс напряженности: ", tension)

    # Строим социограмму
    socio_metric.plot_socionetwork()
