import re
import secrets
import string
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

def evaluar_contrasena(password):
    """Evalúa la fortaleza de una contraseña y devuelve el nivel y sugerencias."""
    puntaje = 0
    sugerencias = []

    # 1. Validar longitud
    if len(password) >= 12:
        puntaje += 2
    elif len(password) >= 8:
        puntaje += 1
    else:
        sugerencias.append("• Tener al menos 8 caracteres (idealmente 12 o más).")

    # 2. Validar mayúsculas y minúsculas
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        puntaje += 1
    else:
        sugerencias.append("• Combinar letras mayúsculas y minúsculas.")

    # 3. Validar números
    if re.search(r"\d", password):
        puntaje += 1
    else:
        sugerencias.append("• Incluir al menos un número.")

    # 4. Validar caracteres especiales
    if re.search(r"[ !@#$%^&*(),.?\":{}|<>_+-]", password):
        puntaje += 1
    else:
        sugerencias.append("• Incluir caracteres especiales (ej: @, #, $, _).")

    # Determinar resultado basado en el puntaje (Máximo 5)
    if puntaje >= 5:
        return Fore.GREEN + "ALTA (Segura) 💪", sugerencias
    elif puntaje >= 3:
        return Fore.YELLOW + "MEDIA (Aceptable) ⚠️", sugerencias
    else:
        return Fore.RED + "BABAJA (Vulnerable) ❌", sugerencias


def generar_contrasena_segura(longitud=16):
    """Genera una contraseña aleatoria criptográficamente segura."""
    caracteres = string.ascii_letters + string.digits + "!@#$%^*_+-="
    while True:
        password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        # Asegurar que cumpla con los requisitos mínimos
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in "!@#$%^*_+-=" for c in password)):
            return password


def menu():
    while True:
        print(Fore.CYAN + "\n=========================================")
        print(Fore.CYAN + "    ANALIZADOR DE SEGURIDAD HACK-CHECK   ")
        print(Fore.CYAN + "=========================================")
        print("1. Evaluar robustez de una contraseña")
        print("2. Generar una contraseña segura aleatoria")
        print(Fore.RED + "3. Salir")
        print(Fore.CYAN + "-----------------------------------------")
        
        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == '1':
            pswd = input("\nIngrese la contraseña a analizar: ")
            nivel, consejos = evaluar_contrasena(pswd)
            print(f"\nFortaleza de la contraseña: {nivel}")
            if consejos:
                print(Fore.LIGHTBLACK_EX + "\nRecomendaciones para mejorarla:")
                for consejo in consejos:
                    print(Fore.LIGHTBLACK_EX + consejo)
        elif opcion == '2':
            try:
                lon = int(input("\nIngrese la longitud deseada (mínimo 8, recomendado 12+): "))
                if lon < 8:
                    print(Fore.YELLOW + "Por seguridad, la longitud mínima es 8. Ajustado a 8.")
                    lon = 8
            except ValueError:
                lon = 16
            
            nueva_pswd = generar_contrasena_segura(lon)
            print(Fore.GREEN + f"\n[✔] Contraseña generada con éxito:")
            print(Fore.LIGHTMAGENTA_EX + f"👉  {nueva_pswd}  👈")
        elif opcion == '3':
            print(Fore.GREEN + "\n¡Mantente seguro! Saliendo del sistema...")
            break
        else:
            print(Fore.RED + "\n[!] Opción inválida.")

if __name__ == "__main__":
    menu()