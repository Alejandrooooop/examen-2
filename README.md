# Sistema de Gestión de Notas

Proyecto básico en Python para calcular promedios, clasificar notas y verificar si un estudiante aprueba o no.

## 📌 Características

* Calcular promedio de notas.
* Clasificar una nota según su desempeño.
* Verificar si una nota está aprobada.
* Configuración mediante variables de entorno.

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/proyecto-notas.git
cd proyecto-notas
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

### 3. Activar entorno virtual

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ⚙️ Variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
APP_NAME=MiAplicacion
VERSION=1.0.0
MAX_NOTA=5.0
MIN_APROBACION=3.0
```

### Descripción

| Variable       | Descripción              |
| -------------- | ------------------------ |
| APP_NAME       | Nombre de la aplicación  |
| VERSION        | Versión del proyecto     |
| MAX_NOTA       | Nota máxima permitida    |
| MIN_APROBACION | Nota mínima para aprobar |

---

## 📂 Estructura del proyecto

```bash
.
├── notas.py
├── .env
├── .gitignore
└── README.md
```

---

## 💻 Ejemplo de uso

```python
from notas import (
    calcular_promedio,
    clasificar_nota,
    esta_aprobado
)

notas = [4.5, 3.8, 5.0]

promedio = calcular_promedio(notas)

print("Promedio:", promedio)
print("Clasificación:", clasificar_nota(promedio))
print("¿Aprobó?:", esta_aprobado(promedio))
```

### Salida esperada

```bash
Promedio: 4.433333333333334
Clasificación: Bueno
¿Aprobó?: True
```

---

## 📄 Licencia

Proyecto educativo de ejemplo.


mi tercer commit