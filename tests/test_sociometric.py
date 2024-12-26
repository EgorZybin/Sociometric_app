import unittest
import numpy as np
from unittest.mock import patch
from main import Sociometric


class TestSocioNetwork(unittest.TestCase):

    def setUp(self):
        """
        Подготовка тестового окружения.
        """
        self.test_file_content = """# Участники, Участник 1, Участник 2, Участник 3, Участник 4
1  +  -  0  +
2  -  +  +  -
3  0  0  +  +
4  +  0  -  +
"""
        # Сохраним временный файл для чтения
        self.test_file = 'test_data.txt'

    def test_read_data(self):
        """
        Тестирование функции чтения данных из файла.
        """
        # Пишем тестовый файл
        with open(self.test_file, 'w') as file:
            file.write(self.test_file_content)

        # Создаем объект сети и читаем данные
        socio_network = Sociometric(file_path=self.test_file)
        matrix = socio_network.matrix

        # Ожидаем, что матрица будет соответствовать данным
        expected_matrix = np.array([
            [1, -1, 0, 1],
            [-1, 1, 1, -1],
            [0, 0, 1, 1],
            [1, 0, -1, 1]
        ])

        np.testing.assert_array_equal(matrix, expected_matrix)

    def test_sociometric_status(self):
        """
        Тестирование расчёта социометрического статуса.
        """
        with open(self.test_file, 'w') as file:
            file.write(self.test_file_content)

        socio_network = Sociometric(file_path=self.test_file)
        statuses = socio_network.sociometric_status()

        # Ожидаемые социометрические статусы для участников
        expected_statuses = [0.5, 0.5, 0.5, 0.5]
        self.assertEqual(statuses, expected_statuses)

    def test_emotional_expanse(self):
        """
        Тестирование расчёта эмоциональной экспансивности.
        """
        with open(self.test_file, 'w') as file:
            file.write(self.test_file_content)

        socio_network = Sociometric(file_path=self.test_file)
        expanse = socio_network.emotional_expanse()

        # Ожидаемый индекс эмоциональной экспансивности
        expected_expanse = 0.5  # В данном примере это 6 положительных выборов / 12 всего выборов
        self.assertAlmostEqual(expanse, expected_expanse, places=2)

    @patch("matplotlib.pyplot.show")
    def test_plot_socionetwork(self, mock_show):
        """
        Тестирование построения социограммы (с использованием mock для plt.show()).
        """
        with open(self.test_file, 'w') as file:
            file.write(self.test_file_content)

        socio_network = Sociometric(file_path=self.test_file)

        # Проверяем, что построение графа не вызывает ошибок
        socio_network.plot_socionetwork()

        # Проверяем, что matplotlib.show() был вызван
        mock_show.assert_called_once()


if __name__ == "__main__":
    unittest.main()
