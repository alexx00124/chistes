from flask import Flask, render_template, jsonify
import random
import logging

# Configurar logging para debug
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
# base de datos de los chistes 
SPANISH_JOKES = [
    # Animales
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
    "¿Cuál es el animal más antiguo? La cebra, porque está en blanco y negro.",
    "¿Qué le dice un pez a otro pez? ¡Nada, nada!",
    "¿Qué le dice un gusano a otro gusano? Voy a dar una vuelta a la manzana.",
    "¿Por qué los pájaros no usan WhatsApp? Porque ya tienen Twitter.",
    "¿Qué hace una vaca en un terremoto? ¡Leche batida!",
    "¿Por qué el perro se sentó en la sombra? Porque no quería ser perro caliente.",
    "¿Qué hacen dos pulpos al chocar? Se dan ocho abrazos.",

    # Tecnología
    "¿Qué le dice una impresora a otra? ¿Ese papel es tuyo o es una impresión mía?",
    "¿Por qué los peces no usan celular? Porque ya tienen línea fija.",
    "El WiFi de mi casa es como un mago: aparece y desaparece cuando quiere.",
    "—¿Cuál es tu red social favorita? —La red eléctrica, sin ella no soy nada.",
    "¿Qué hace un programador en la playa? Nada, porque el sol le da error.",
    "Mi contraseña es como mi cepillo de dientes: no la comparto con nadie.",

    # Escuela
    "¿Por qué los libros de matemáticas están siempre tristes? Porque tienen muchos problemas.",
    "Profesor: 'Si tengo cinco manzanas en una mano y cuatro en la otra, ¿qué tengo?' Alumno: 'Unas manos enormes'.",
    "¿Cuál es el colmo de un electricista? No encontrar su corriente de estudio.",
    "—Profesor, ¿me puede castigar por algo que no he hecho? —Claro que no. —Menos mal, porque no hice la tarea.",
    "Examen de historia: Defina Napoleón. Respuesta: Un hombre con un sombrero.",
    "¿Por qué la escoba llega tarde al colegio? Porque se quedó barriendo.",

    # Vida cotidiana
    "—Oye, ¿cuál es tu plato favorito? —El hondo, porque cabe más comida.",
    "—Doctor, cada vez que tomo café me duele el ojo. —Pues saque la cuchara de la taza.",
    "Camarero, este filete tiene muchos nervios. —Normal, es la primera vez que se lo comen.",
    "—Doctor, me duele aquí, aquí y aquí. —Usted lo que tiene es el dedo roto.",
    "Estás obsesionado con la comida. —¿A qué te refieres croquetamente?",
    "¿Cómo se despiden los químicos? Ácido un placer.",
    "¿Qué le dice un techo a otro? Techo de menos.",
    "¿Por qué la cama fue a la escuela? Para hacerse más inteligente.",

    # Cortos y juegos de palabras
    "¿Qué hace una taza en la escuela? Taza-mates.",
    "¿Qué hace una señal de tránsito en el gimnasio? Levanta pesas.",
    "¿Por qué la computadora fue al médico? Tenía un virus.",
    "¿Qué le dijo el semáforo al coche? ¡No me mires, me estoy cambiando!",
    "¿Por qué la bicicleta no se mantenía en pie sola? Porque estaba cansada.",
    "¿Qué le dice un semáforo a otro? No me mires que me estoy cambiando.",
    "¿Qué hace una naranja corriendo? ¡Jugo rápido!",
    "¿Por qué el tomate se sonrojó? Porque vio la ensalada desnuda."
]

# Ruta principal que renderiza el HTML
@app.route('/')
def index():
    return render_template('index.html')

# Ruta API que devuelve chistes en español
@app.route('/joke')
def get_joke():
    try:
        # Seleccionar un chiste aleatorio de la lista
        random_joke = random.choice(SPANISH_JOKES)
        
        return jsonify({
            'joke': random_joke,
            'success': True,
            'language': 'es',
            'total_jokes': len(SPANISH_JOKES)
        })
        
    except Exception as e:
        # Manejar cualquier error
        app.logger.error(f"Error inesperado: {e}")
        return jsonify({
            'joke': '¡Algo salió mal... Pero Chuck Norris lo arreglará pronto!',
            'success': False
        }), 500

# Ruta adicional para obtener chistes por categoría
@app.route('/joke/random')
def get_random_joke():
    return get_joke()

# Ruta para estadísticas
@app.route('/stats')
def get_stats():
    return jsonify({
        'total_jokes': len(SPANISH_JOKES),
        'language': 'español',
        'version': '2.0',
        'powered_by': 'Chuck Norris Español Edition'
    })

if __name__ == '__main__':
    print("Servidor de Chuck Norris en Español iniciado!")
    print(f"Base de datos: {len(SPANISH_JOKES)} chistes en español")
    print("Accede en: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)