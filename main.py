import PySimpleGUI as sg
import numpy as np

from fuctions import getMatrices, convertToPolar

sg.theme('DarkBlue1')
layout = [
    [sg.Text('Matriz de intensidades'), sg.Text('I1    '), sg.Text('I2      '), sg.Text(' I3     '), sg.Text('V')],
    [sg.Text('Valores ecuacion 1'), (sg.Input(size=5)), sg.Input(size=5), sg.Input(size=5), sg.Input(size=10)],
    [sg.Text('Valores ecuacion 2'), sg.Input(size=5), sg.Input(size=5), sg.Input(size=5), sg.Input(size=10)],
    [sg.Text('Valores ecuacion 3'), sg.Input(size=5), sg.Input(size=5), sg.Input(size=5), sg.Input(size=10)],
    [sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('Calculadora Matriz 3x3 de Corrientes', layout)

while True:
    event, values = window.read()

    if event == 'Ok':
        Eq1 = {"Intensity_1_1": complex(values[0]), "Intensity_2_1": complex(values[1]),
               "Intensity_3_1": complex(values[2]),
               "Voltaje_1": complex(values[3])}
        Eq2 = {"Intensity_1_2": complex(values[4]), "Intensity_2_2": complex(values[5]),
               "Intensity_3_2": complex(values[6]),
               "Voltaje_2": complex(values[7])}
        Eq3 = {"Intensity_1_3": complex(values[8]), "Intensity_2_3": complex(values[9]),
               "Intensity_3_3": complex(values[10]),
               "Voltaje_3": complex(values[11])}
        Matrices = getMatrices(Eq1, Eq2, Eq3)
        Principal_Matriz = Matrices[0]
        Matriz_Intensidad_1 = Matrices[1]
        Matriz_Intensidad_2 = Matrices[2]
        Matriz_Intensidad_3 = Matrices[3]
        Determinant_Principal_Matriz = np.linalg.det(Principal_Matriz)
        Determinant_Matriz_Intensidad_1 = np.linalg.det(Matriz_Intensidad_1)
        Determinant_Matriz_Intensidad_2 = np.linalg.det(Matriz_Intensidad_2)
        Determinant_Matriz_Intensidad_3 = np.linalg.det(Matriz_Intensidad_3)
        print(Determinant_Principal_Matriz)
        print(Determinant_Matriz_Intensidad_1)
        print(Determinant_Matriz_Intensidad_2)
        print(Determinant_Matriz_Intensidad_3)
        Intensity_1 = Determinant_Matriz_Intensidad_1 / Determinant_Principal_Matriz
        Intensity_2 = Determinant_Matriz_Intensidad_2 / Determinant_Principal_Matriz
        Intensity_3 = Determinant_Matriz_Intensidad_3 / Determinant_Principal_Matriz
        Intenssity_polar_1 = (convertToPolar(Intensity_1))
        Intenssity_polar_2 = (convertToPolar(Intensity_2))
        Intenssity_polar_3 = (convertToPolar(Intensity_3))

        modal = sg.Window("Resultados", auto_size_text=True, auto_size_buttons=True,
                          default_element_size=(40, 1)).Layout(
            [[sg.Text("La intensidad 1 compleja es: "), sg.Text(Intensity_1)],
             [sg.Text("La intensidad 2 compleja es: "), sg.Text(Intensity_2)],
             [sg.Text("La intensidad 3 compleja es: "), sg.Text(Intensity_3)],
             [sg.Text("La intensidad 1 polar es: "), sg.Text(Intenssity_polar_1[0]), sg.Text("A"),
              sg.Text("el angulo es: "), sg.Text(Intenssity_polar_1[1]), sg.Text("°")],
             [sg.Text("La intensidad 2 polar es: "), sg.Text(Intenssity_polar_2[0]), sg.Text("A"),
              sg.Text("el angulo es: "), sg.Text(Intenssity_polar_2[1]), sg.Text("°")],
             [sg.Text("La intensidad 3 polar es: "), sg.Text(Intenssity_polar_3[0]), sg.Text("A"),
              sg.Text("el angulo es: "), sg.Text(Intenssity_polar_3[1]), sg.Text("°")],

             [sg.Button("Ok")]])
        modal.Read()
        if event == 'Ok':
            modal.close()

    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

window.close()
