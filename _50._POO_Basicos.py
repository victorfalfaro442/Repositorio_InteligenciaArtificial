class ResumenPOO:
    """Clase informativa sobre los fundamentos de la POO en Cisco"""
    
    def __init__(self):
        self.seccion = "3.1 - Fundamentos de la POO"
        self.conceptos_clave = [
            "Clase: El plano o molde (ej. Molde de galletas)",
            "Objeto: La instancia real (ej. La galleta)",
            "Herencia: Crear nuevas clases basadas en otras",
            "Propiedades: Lo que el objeto TIENE (variables)",
            "Métodos: Lo que el objeto HACE (funciones)"
        ]

    def mostrar_info(self):
        print(f"--- {self.seccion} ---")
        print("Puntos vitales para el concurso de sección:")
        for concepto in self.conceptos_clave:
            print(f"-> {concepto}")
        
        print("\nNota técnica:")
        print("La POO ayuda a organizar códigos grandes y complejos.")

# Crear el primer objeto (instancia)
mi_resumen = ResumenPOO()
mi_resumen.mostrar_info()
