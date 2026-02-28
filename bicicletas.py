from funcionUno import crear_lista_estudiantes
from funcionDos import crear_lista_notas
from funcionTres import calcular_promedio
from funcionCuatro import evaluar_bicicleta

#Paso 1. Creo el equipo
equipoUno=crear_lista_estudiantes(4)

#Paso 2. Evaluar los componentes de eficiencia, estabilidad y parecido de la bicicleta
notasEficiencia=crear_lista_notas(20)
notasEstabilidad=crear_lista_notas(20)
notasParecido=crear_lista_notas(20)

#Paso 3. Calcular la nota promedio de cada componente
eficiencia=calcular_promedio(notasEficiencia)
estabilidad=calcular_promedio(notasEstabilidad)
parecido=calcular_promedio(notasParecido)

#Paso 4. Evaluo la bicicleta
evalucacionFinal=evaluar_bicicleta(eficiencia,estabilidad,parecido)

#Paso 5. Imprimo el resultado
print(f"El resultado del equipo 1 fue: {evalucacionFinal}")
