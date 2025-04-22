comandos para correr el programa en un nuevo dispositivo:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser "cambiar PATH por si no reconoce env"
venv\Scripts\activate "activar el entorno virtual"
python .\src\app.py  ""correr el programa"

""cosas a instalar para correr el programa""
-pip install virtualenv  
-pip install flask-login flask-mysqldb flask-WTF
-pip install mysql-connector-python
-pip install Flask-Session

🧠 Guía Rápida de Comandos Git desde Terminal

📁 Inicializar un repositorio
    git init

📄 Ver el estado del repositorio
    git status

➕ Agregar archivos al área de preparación (staging)
    git add nombre-del-archivo     # Agrega un archivo específico
    git add .                      # Agrega todos los cambios

💾 Guardar los cambios (commit)
    git commit -m "Mensaje descriptivo del cambio"

🚀 Subir los cambios al repositorio remoto en GitHub
    git push origin main           # O 'master', según el nombre de tu rama

🔎 Ver el historial de cambios (commits)
    git log                        # Muestra el historial completo
    git log --oneline              # Historial compacto

❌ Borrar y deshacer cambios

🧹 Borrar un archivo del proyecto y de Git
    git rm nombre-del-archivo
    git commit -m "Elimino archivo innecesario"

🗑️ Borrar archivo manualmente y registrar el cambio
    rm nombre-del-archivo
    git add .
    git commit -m "Borro archivo manualmente"

🔄 Deshacer cambios en archivo antes del commit
    git restore nombre-del-archivo

⏪ Deshacer el último commit (sin borrar archivos)
    git reset --soft HEAD~1

🔁 Revertir un commit ya subido a GitHub
    git revert HEAD

📦 Ignorar archivos y carpetas (como `env/`)

1. Crear o editar el archivo `.gitignore` con el siguiente contenido:
    env/
    *.pyc
    __pycache__/

2. Eliminar del control de versiones pero mantener en disco:
    git rm -r --cached env/
    git add .gitignore
    git commit -m "Ignoro carpeta env y archivos innecesarios"

