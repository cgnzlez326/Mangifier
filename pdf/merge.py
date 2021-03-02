import PyPDF2
import os
from PIL import Image
from load import img_loader


def merge(f_arr, s_arr, path):
    path_array = f_arr[0].split('\\')
    filename = str(path_array[-2])
    times = len(f_arr)
    merge_pdf = PyPDF2.PdfFileMerger()
    i = 0
    try:
        os.mkdir(path + '\\export')
    except FileExistsError:
        print('Carpeta ya creada, se omitirá el error')
    except:
        print('Ups, algo ha salido mal')
    for i in range(times):
        tmp_file1 = img_loader.img_loader(f_arr[i], s_arr[i])
        tmp_file1.save(f'temporary{i}.pdf', quality=100, subsampling=0)
        merge_pdf.append(f'temporary{i}.pdf')
        if (i % 2) == 0:
            print('Modelo 1-4 creado y unido al pdf principal')
        else:
            print('Modelo 3-2 creado y unido al pdf principal')
    try:
        merge_pdf.write(path + '\\export\\' + filename + '.pdf')
        merge_pdf.close()
        print('Finalizado y guardado el pdf principal, limpiando restos...')
    except:
        print('Algo ha salido mal guardando xdxd')
    for i in range(times):
        os.remove(f'temporary{i}.pdf')
    print('Restos limpios, manga ubicado en export!')
