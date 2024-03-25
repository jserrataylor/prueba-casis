import streamlit as st
import joblib
import numpy as np

# Cargar el modelo (Asegúrate de tener el modelo en el mismo directorio que este script)
model = joblib.load('casis_logistic_regression_model.pkl')

st.title('Cuestionario de Evaluación de Riesgo de CASIS')

# Definir las preguntas
questions = [
    "¿Tiene preocupaciones sobre su alimentación?",
    "¿Tiene dificultades con el sueño?",
    "¿Ha asistido a consejería o psicoterapia por preocupaciones con su salud mental?",
    "¿Ha sentido necesidad de reducir el uso de bebidas alcohólicas u otras drogas?",
    "¿Ha tenido ataques de pánico o episodios de ansiedad severa?",
    "¿Ha considerado seriamente lastimar a otra persona?",
    "¿Ha tenido contactos sexuales u otras experiencias sexuales sin desearlo?"
]

# Crear un formulario para las preguntas
form = st.form(key='casis_form')
answers = []
for question in questions:
    answer = form.radio(question, ('Si', 'No'), key=question)
    answers.append(answer)

submit_button = form.form_submit_button(label='Enviar')

if submit_button:
    # Convertir respuestas a valores numéricos y hacer predicción
    numerical_answers = [1 if a == 'Si' else 0 for a in answers]
    prediction = model.predict([numerical_answers])
    result = "Tiene alta posibilidad de tener CASIS." if prediction[0] == 1 else "Tiene una alta posibilidad de NO tener CASIS."
    st.write(result)
