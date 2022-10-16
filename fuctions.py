import cmath
import math
import numpy as np


def convertToPolar(complexNumber):
    module, angleRad = cmath.polar(complexNumber)
    angle = math.degrees(angleRad)
    return module, angle


def getMatrices(Ecuation1, Ecuation2, Ecuation3):
    Principal_Matriz = np.array([[Ecuation1["Intensity_1_1"], Ecuation1["Intensity_2_1"], Ecuation1["Intensity_3_1"]],
                                 [Ecuation2["Intensity_1_2"], Ecuation2["Intensity_2_2"], Ecuation2["Intensity_3_2"]],
                                 [Ecuation3["Intensity_1_3"], Ecuation3["Intensity_2_3"], Ecuation3["Intensity_3_3"]]])
    Matriz_Intensiad_1 = np.array([[Ecuation1["Voltaje_1"], Ecuation1["Intensity_2_1"], Ecuation1["Intensity_3_1"]],
                                   [Ecuation2["Voltaje_2"], Ecuation2["Intensity_2_2"], Ecuation2["Intensity_3_2"]],
                                   [Ecuation3["Voltaje_3"], Ecuation3["Intensity_2_3"], Ecuation3["Intensity_3_3"]]])
    Matriz_Intensiad_2 = np.array([[Ecuation1["Intensity_1_1"], Ecuation1["Voltaje_1"], Ecuation1["Intensity_3_1"]],
                                   [Ecuation2["Intensity_1_2"], Ecuation2["Voltaje_2"], Ecuation2["Intensity_3_2"]],
                                   [Ecuation3["Intensity_1_3"], Ecuation3["Voltaje_3"], Ecuation3["Intensity_3_3"]]])
    Matriz_Intensiad_3 = np.array([[Ecuation1["Intensity_1_1"], Ecuation1["Intensity_2_1"], Ecuation1["Voltaje_1"]],
                                   [Ecuation2["Intensity_1_2"], Ecuation2["Intensity_2_2"], Ecuation2["Voltaje_2"]],
                                   [Ecuation3["Intensity_1_3"], Ecuation3["Intensity_2_3"], Ecuation3["Voltaje_3"]]])
    return Principal_Matriz, Matriz_Intensiad_1, Matriz_Intensiad_2, Matriz_Intensiad_3
