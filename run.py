from app import create_app
from dotenv import load_dotenv
from joblib import load

import os


app = create_app()


load_dotenv()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

 
## py -m venv venv (Creamos el entorno)
## pip install --upgrade pip (Instalamos dependencias de gestor de paquetes)
## pip install flask scikit-learn joblib flask-cors (Instalamos los paquetes de scikit-learn)







