import calendar

class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        """
        Cuenta cuántas veces ocurre un día de la semana específico en un año.
        0 = Lunes, 6 = Domingo.
        """
        if not (0 <= weekday <= 6):
            raise ValueError("El día de la semana debe estar entre 0 (lunes) y 6 (domingo).")
            
        total_occurrences = 0
        
        # Iteramos por cada mes del año (de 1 a 12)
        for month in range(1, 13):
            # monthdays2calendar devuelve una lista de semanas (listas de tuplas)
            month_plan = self.monthdays2calendar(year, month)
            
            for week in month_plan:
                for day_number, day_of_week in week:
                    # Si day_number es 0, el día no pertenece a este mes
                    if day_number != 0 and day_of_week == weekday:
                        total_occurrences += 1
                        
        return total_occurrences

# --- Ejemplo de uso ---
my_cal = MyCalendar()

# Vamos a contar cuántos lunes (0) hubo en el año 2019
year = 2000
target_day = 6 
result = my_cal.count_weekday_in_year(year, target_day)

print(f"En el año {year}, el día de la semana {target_day} ocurrió {result} veces.")
