
##JUANROAS4G
import csv
import math

RutaArchivo = r'C:\Users\salasistemas\Downloads\Estudiantes_Graduados_UNAL_20250227.csv'

DatosAño = {}


with open(RutaArchivo, mode='r', encoding='utf-8-sig') as archivo:
    LeerCSV = csv.DictReader(archivo)  
    
    
    for fila in LeerCSV:
        
        anio = fila.get('YEAR')
        semestre = fila.get('SEMESTRE')
        edad = fila.get('EDAD')
        sexo = fila.get('SEXO')
        
        try:
            anio = int(anio)          
            semestre = int(semestre)  
            edad = int(edad)          
        except:
            continue  
        
        if anio and semestre and edad > 0 and edad < 100 and sexo:
            
            if anio not in DatosAño:
                DatosAño[anio] = {
                    'edades': [],
                    'hombres1': 0,
                    'hombres2': 0,
                    'mujeres1': 0,
                    'mujeres2': 0
                }
            
            
            DatosAño[anio]['edades'].append(edad)
            
            
            sexo = sexo.strip().upper()  
            if semestre == 1:
                if sexo in ['MASCULINO', 'HOMBRE', 'M', 'HOMBRES']:
                    DatosAño[anio]['hombres1'] += 1
                elif sexo in ['FEMENINO', 'MUJER', 'F', 'MUJERES']:
                    DatosAño[anio]['mujeres1'] += 1
            elif semestre == 2:
                if sexo in ['MASCULINO', 'HOMBRE', 'M', 'HOMBRES']:
                    DatosAño[anio]['hombres2'] += 1
                elif sexo in ['FEMENINO', 'MUJER', 'F', 'MUJERES']:
                    DatosAño[anio]['mujeres2'] += 1


for anio in sorted(DatosAño.keys()):
    edades = DatosAño[anio]['edades']
    
    if len(edades) > 0:
        
        promedio = sum(edades) / len(edades)
        
       
        SumaDesv = sum((edad - promedio) ** 2 for edad in edades)
        if len(edades) > 1:
            Desviacion = math.sqrt(SumaDesv / (len(edades) - 1))
        else:
            Desviacion = 0
        
        
        MaxEdad = max(edades)
        MinEdad = min(edades)
        
       
        print(f"\nAño {anio}:")
        print(f"  Promedio: {promedio:.2f}")
        print(f"  Desv. Estandar: {Desviacion:.2f}")
        print(f"  Max: {MaxEdad}")
        print(f"  Min: {MinEdad}")
        
        print(f"  Numero total de hombres semestre I: {DatosAño[anio]['hombres1']}")
        print(f"  Numero total de hombres semestre II: {DatosAño[anio]['hombres2']}")
        print(f"  Numero total de mujeres semestre I: {DatosAño[anio]['mujeres1']}")
        print(f"  Numero total de mujeres semestre II: {DatosAño[anio]['mujeres2']}")