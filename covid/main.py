# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

general_df = pd.read_csv("general.csv")
timeseries_df = pd.read_csv("timeseries.csv")

# Zwiększenie rozmiaru wykresu
plt.figure(figsize=(12, 6))

general_df['Timestamp'] = pd.to_datetime(general_df['Timestamp'])

# Zmiana kolorów, styli linii i markerów
plt.plot(general_df['Timestamp'], general_df['Confirmed'], linestyle='-', marker='o', markersize=5, label='Chorzy', color='blue')
plt.plot(general_df['Timestamp'], general_df['Deaths'], linestyle='-', marker='o', markersize=5, label='Zgony', color='red')
plt.plot(general_df['Timestamp'], general_df['Recovered'], linestyle='-', marker='o', markersize=5, label='Wyzdrowienia', color='green')

plt.xlabel("Data")
plt.ylabel("Liczba przypadków")
plt.title("Całkowita liczba chorych, zgonów i wyzdrowień w czasie")
plt.legend()
plt.show()


cases_by_province = timeseries_df[timeseries_df["Infection/Death/Recovery"] == "I"]["Province"].value_counts()
plt.bar(cases_by_province.index, cases_by_province.values)
plt.xlabel("Województwo")
plt.ylabel("Liczba przypadków")
plt.title("Całkowita liczba chorych w poszczególnych województwach")
plt.xticks(rotation=90)
plt.show()


deaths_by_gender = timeseries_df[timeseries_df["Infection/Death/Recovery"] == "D"]["Sex"].value_counts()
plt.pie(deaths_by_gender.values, labels=deaths_by_gender.index, autopct="%1.1f%%")
plt.title("Procentowa zawartość mężczyzn i kobiet wśród zgonów")
plt.show()


deaths_age_data = timeseries_df[(timeseries_df["Infection/Death/Recovery"] == "D") & (timeseries_df["Age"].notna())]["Age"]

# Wybierz przedziały wiekowe
bins = [0, 18, 40, 65, 100]

# Przypisz przedziały wiekowe do danych
age_categories = pd.cut(deaths_age_data, bins)

# Podsumuj liczbę zgonów według kategorii wiekowych
deaths_by_age = age_categories.value_counts().sort_index()

# Stwórz wykres kołowy
plt.pie(deaths_by_age.values, labels=deaths_by_age.index, autopct="%1.1f%%")
plt.title("Procentowa zawartość osób w danym wieku wśród zgonów")
plt.show()
