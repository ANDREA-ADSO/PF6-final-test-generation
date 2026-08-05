def dish_fetch(num):
    return {
        "id": num,
        "name": f"Plato típico {num}"
    }
import requests

def dish_fetch(num):
    # Conectarse a la API
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={num}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        meal = data["meals"][0] if data["meals"] else None
        if meal:
            return {
                "id": num,
                "name": meal["strMeal"]
            }
    # Si no encuentra nada, devuelve un diccionario genérico
    return {
        "id": num,
        "name": f"Plato típico {num}"
    }

def main():
    print("=== Menú de Platos Típicos ===")
    numero = int(input("Escribe un número de plato (ejemplo 52772): "))
    plato = dish_fetch(numero)
    print("ID:", plato["id"])
    print("Nombre:", plato["name"])

if __name__ == "__main__":
    main()
