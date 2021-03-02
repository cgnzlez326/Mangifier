import os
from imports import mangifier


def load_images():
    i = 0
    path = os.path.abspath(os.getcwd())
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
    with os.scandir(path + '\\imports\\manga') as entries:
        for entry in entries:
            if i == 0:
                arr1.append(path + '\\imports\\manga\\' + entry.name)
                i += 1
            elif i == 1:
                arr2.append(path + '\\imports\\manga\\' + entry.name)
                i += 1
            elif i == 2:
                arr3.append(path + '\\imports\\manga\\' + entry.name)
                i += 1
            elif i == 3:
                arr4.append(path + '\\imports\\manga\\' + entry.name)
                i = 0
    f_array = mangifier.magic_manga(arr1, arr3)
    s_array = mangifier.magic_manga(arr4, arr2)
    return f_array, s_array, path
