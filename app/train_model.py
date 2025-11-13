# train_model.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
#  Datos de ejemplo
# Un dataset muy pequeño para una demo en la clase.
# Podemos usar un CSV con más filas si queremos hacerlo escalable.
# Cada texto tiene una etiqueta: "positivo" o "negativo"
texts = [
    "el sistema funciona perfectamente",
    "la aplicación tiene muchos errores",
    "me encanta la nueva funcionalidad",
    "el diseño de la interfaz es confuso",
    "excelente soporte técnico",
    "la documentación no es clara",
    "el rendimiento de la aplicación es lento",
    "gran experiencia de usuario",
    "la integración con otras herramientas es perfecta",
    "no pude completar mi tarea debido a fallos",
    "la aplicación es muy intuitiva",
    "el sistema se cae constantemente",
    "la velocidad de respuesta es impresionante",
    "no entiendo cómo usar esta funcionalidad",
    "el equipo de soporte resolvió mi problema rápidamente",
    "la actualización introdujo más errores",
    "la interfaz es moderna y atractiva",
    "la funcionalidad prometida no está disponible",
    "el sistema cumple con todas mis expectativas",
    "la aplicación consume demasiados recursos",
    "la experiencia general es muy positiva",
    "no puedo acceder a mi cuenta",
    "el diseño es simple y efectivo",
    "los tiempos de carga son demasiado largos",
    "la aplicación es muy útil para mi trabajo",
    "el sistema no guarda mis cambios",
    "la documentación es muy completa y clara",
    "el soporte técnico no responde a tiempo",
    "la funcionalidad de búsqueda es excelente",
    "la aplicación no es compatible con mi dispositivo"
]
labels = [
    "positivo", "negativo", "positivo", "negativo", "positivo",
    "negativo", "negativo", "positivo", "positivo", "negativo",
    "positivo", "negativo", "positivo", "negativo", "positivo",
    "negativo", "positivo", "negativo", "positivo", "negativo",
    "positivo", "negativo", "positivo", "negativo", "positivo",
    "negativo", "positivo", "negativo", "positivo", "negativo"
]


#  2. Split entrenamiento / prueba
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.25, random_state=42, stratify=labels
)


#  3. Pipeline: CountVectorizer + MultinomialNB
pipeline = Pipeline([
    ("vect", CountVectorizer()),        # convierte texto a conteos (Bag of Words)
    ("clf", MultinomialNB())            # clasificador Naive Bayes multinomial
])


# 4. Entrenar
pipeline.fit(X_train, y_train)


#  5. Evaluar (rápido)
y_pred = pipeline.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Reporte:\n", classification_report(y_test, y_pred))


#  6. Guardar el pipeline entrenado
dump(pipeline, "sentiment_model.joblib")
print("Modelo guardado en sentiment_model.joblib")





