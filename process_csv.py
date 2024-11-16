import pandas as pd

# Укажите полный путь к вашему файлу
file_path = r"C:\Users\Azerty\Desktop\ДАННЫЕ О ПОГОДЕ\weather_data.csv"

# Чтение CSV-файла
df = pd.read_csv(file_path)

# Вывод первых 5 строк
print(df.head())

# Сохранение обработанных данных (при необходимости)
output_path = r"C:\Users\Azerty\Desktop\ДАННЫЕ О ПОГОДЕ\processed_weather_data.csv"
df.to_csv(output_path, index=False)
