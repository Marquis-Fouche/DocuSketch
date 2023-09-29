# импортируем необходимые библиотеки
import pandas as pd
import matplotlib.pyplot as plt
import os

# определяем класс Plotter
class Plotter:
    # конструктор класса
    def __init__(self, json_file):
        # загружаем данные из JSON-файла в кадр данных pandas
        self.df = pd.read_json(json_file)
        # инициализируем список путей к графикам как пустой список
        self.plots = []

    # метод для рисования графиков
    def draw_plots(self):
        # создаем папку "Графики" в корневом каталоге проекта, если ее еще нет
        if not os.path.exists("Graphics"):
            os.mkdir("Graphics")
        # рисуем график для сравнения истинного и найденного количества углов в комнате
        plt.figure(figsize=(10, 6))
        plt.scatter(self.df["gt_corners"], self.df["rb_corners"])
        plt.xlabel("True number of corners")
        plt.ylabel("Found number of corners")
        plt.title("Comparison of true and found number of corners in a room")
        # сохраняем график в папке "Графики" с именем "corners.png"
        plt.savefig("Graphics/corners.png")
        # добавляем путь к графику в список путей к графикам
        self.plots.append("Graphics/corners.png")
        # рисуем график для сравнения разных столбцов отклонения в градусах
        plt.figure(figsize=(10, 6))
        plt.boxplot([self.df["floor_mean"], self.df["floor_max"], self.df["floor_min"], self.df["ceiling_mean"], self.df["ceiling_max"], self.df["ceiling_min"]], labels=["floor_mean", "floor_max", "floor_min", "ceiling_mean", "ceiling_max", "ceiling_min"])
        plt.xlabel("Deviation columns")
        plt.ylabel("Deviation in degrees")
        plt.title("Comparison of different degree deviation columns")
        # сохраняем график в папке "Графики" с именем "deviation.png"
        plt.savefig("Graphics/deviation.png")
        # добавляем путь к графику в список путей к графикам
        self.plots.append("Graphics/deviation.png")
        # возвращаем список путей к графикам
        return self.plots