# Социометрическое моделирование

Этот проект включает в себя программу для анализа и визуализации социометрических данных. Она позволяет прочитать данные из файла, рассчитать различные социальные индексы, такие как социометрический статус, эмоциональная экспансивность, индекс сплоченности и другие, а также построить социограмму.

## Основные возможности

- Чтение и обработка социометрических данных из текстового файла.
- Расчёт социометрического статуса участников группы.
- Расчёт индекса эмоциональной экспансивности и других социальных индексов.
- Построение социограммы с различными визуальными улучшениями.
- Визуализация графа социальных связей с использованием NetworkX и Matplotlib.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/EgorZybin/Sociometric_app.git
    cd Sociometric_app
    ```

2. Установите необходимые зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Запуск программы

1. Создайте файл данных в формате `data.txt`, в котором будет информация о социометрических связях между участниками. Пример файла:
    ```data.txt
    # Участники (номер) | 1  2  3  ...
    1  +  -  +  ...
    2  -  +  +  ...
    3  +  -  +  ...
    ```

2. Запустите программу:
    ```bash
    python main.py {file_path} # file_path - путь к файлу с данными
    ```

### Важные функции:

- `read_data(file_path)`: Читает данные из файла и формирует социометрическую матрицу.
- `sociometric_status()`: Рассчитывает социометрический статус каждого участника.
- `emotional_expanse()`: Рассчитывает индекс эмоциональной экспансивности.
- `cohesion_index()`: Рассчитывает индекс сплоченности.
- `plot_socionetwork()`: Строит социограмму на основе данных.

### Тестовая социограмма:

Входные данные:

```data.txt
# Участники (номер) | 1  2  3  4
1  +  -  0  +
2  -  +  +  -
3  0  0  +  +
4  +  0  -  +
```
![Test Socionetwork](https://github.com/EgorZybin/Sociometric_app/blob/main/tests/test_sociometric.png)

## Автор

GitHub: [EgorZybin](https://github.com/EgorZybin)
Telegram: [EgorZybin](https://t.me/raizzep)