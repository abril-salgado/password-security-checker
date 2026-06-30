# Password Security Checker & Generator 🔐

Una herramienta interactiva desarrollada en Python orientada a la concienciación y aplicación de buenas prácticas en ciberseguridad. El sistema analiza la robustez de las credenciales de los usuarios basándose en criterios de entropía y genera claves aleatorias altamente seguras.

## 📌 Características Principales
* **Análisis por Patrones (Regex):** Utiliza expresiones regulares (`re`) para verificar de forma exacta la presencia de estructuras complejas (mayúsculas, minúsculas, dígitos y caracteres especiales).
* **Evaluación de Longitud Crítica:** Clasifica la robustez según los estándares actuales de la industria (mínimo 8 caracteres, óptimo 12+).
* **Generación Criptográfica Segura:** A diferencia de la librería estándar `random` (que es predecible), este sistema implementa el módulo `secrets`, diseñado específicamente para generar tokens y secretos criptográficos aptos para contraseñas de producción.
* **Feedback Dinámico (UX):** Devuelve un diagnóstico preciso con sugerencias específicas en caso de detectar vulnerabilidades.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.13
* **Librerías Nativas:** `re`, `secrets`, `string`
* **Librerías Externas:** `colorama` (Interfaz de usuario)

## 🚀 Instalación y Uso
1. Clonar el repositorio.
2. Instalar la dependencia de diseño:
   ```bash
   py -m pip install colorama
