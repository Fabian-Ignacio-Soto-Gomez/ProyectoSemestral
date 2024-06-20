import csv
from .api.models import FormMonthly,FormFinal

def import_form_monthly(path):
    with open(path, 'r') as file:
        try:
            reader = csv.DictReader(file)
            for row in reader:
                FormMonthly.objects.create(
                    rut_student= row['Rut del estudiante'],
                    rut_empresa = row['Rut de la empresa'],
                    nota = row['Nota de evaluación'],
                    comentarios = row['Comentarios generales']
                )
        except:
            print('Error de subida')

def import_form_final(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        try:
            for row in reader:
                FormMonthly.objects.create(
                    rut_student= row['Rut del estudiante'],
                    rut_empresa = row['Rut Empresa'],
                    rut_evaluador = row['Rut Evaluador'],
                    nota = row['Nota'],
                    comentarios = row['Comentarios Generales']
                )
        except:
            print('Error de subida')

if __name__ == '__main__':
    csv_file_path_form_monthly = './data/formularios/'
    csv_file_path_form_final = './data/formularios/'

    import_form_monthly(csv_file_path_form_monthly)
    import_form_final(csv_file_path_form_final)