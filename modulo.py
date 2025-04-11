import numpy as np
import matplotlib.pyplot as plt
import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Marca el tiempo de inicio
        result = func(*args, **kwargs)  # Llama a la función original
        end_time = time.time()  # Marca el tiempo de fin
        print(f"Tiempo de ejecución: {end_time - start_time} segundos")
        return result
    return wrapper



class Punto2D:
  def __init__(self,x,y):
    self.x=x
    self.y=y

  def __str__(self):
    return f"({self.x},{self.y})"

# 
  def __add__(self, otro):
    return Punto2D(self.x + otro.x, self.y + otro.y)

  def __mul__(self, otro):
    return Punto2D(self.x * otro.x, self.y * otro.y)

  def __call__(self, otro):
    return Punto2D(self.x*otro,self.y*otro)

  def __sub__(self, otro):
      return Punto2D(self.x - otro.x, self.y - otro.y)
        
  def __rmul__(self, otro):
        # Sobrecarga del operador * para multiplicar por un escalar (para 3 * A)
      return self.__mul__(otro)

#  def __call__(self, escalar):
#        # Sobrecarga del operador () para multiplicar las coordenadas por un escalar
#        if isinstance(escalar, (int, float)):
#            return Punto2D(self.x * escalar, self.y * escalar)    

  def grafica(self):
        # Método para graficar el punto
        plt.figure(figsize=(6, 6))  # Tamaño de la figura
        plt.scatter(self.x, self.y, color='red', label=f'Punto ({self.x}, {self.y})')  # Graficar el punto

        # Etiquetas de los ejes
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')

        # Título de la gráfica
        plt.title('Gráfica del Punto')

        # Etiqueta del punto
        plt.text(self.x + 0.1, self.y + 0.1, f'({self.x}, {self.y})', fontsize=12)

        # Líneas para los ejes
        plt.axhline(0, color='black',linewidth=1)
        plt.axvline(0, color='black',linewidth=1)

        # Mostrar la cuadrícula
        plt.grid(True)

        # Mostrar la gráfica
        plt.legend()
        plt.show()

   # @medir_tiempo  # Aplica el decorador para medir el tiempo
       
  def distancia(self, otro):
        # Verificar que el otro punto sea una instancia de la clase Punto2D
        if isinstance(otro, Punto2D):
            # Calcula la distancia utilizando numpy
            dx = self.x - otro.x
            dy = self.y - otro.y
            return np.sqrt(dx ** 2 + dy ** 2)  # Devuelve la distancia
        else:
            raise TypeError("El argumento debe ser un objeto de la clase Punto2D.")


  def __abs__(self):
        # Calcula la distancia al origen (0, 0) usando la fórmula de distancia euclidiana
        return np.sqrt(self.x**2 + self.y**2)






