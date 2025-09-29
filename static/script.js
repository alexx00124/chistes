// Elementos del DOM
const jokeContainer = document.getElementById('joke-container');
const newJokeBtn = document.getElementById('new-joke-btn');
const loadingSpinner = document.getElementById('loading-spinner');

// Estado de la aplicación
let isLoading = false;

// Función principal para obtener chistes
async function getNewJoke() {
    // Evitar múltiples peticiones simultáneas
    if (isLoading) return;
    
    try {
        // Activar estado de carga
        setLoadingState(true);
        
        // Hacer petición al servidor Flask
        const response = await fetch('/joke', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
            // Timeout de 10 segundos
            signal: AbortSignal.timeout(10000)
        });
        
        // Verificar que la respuesta sea exitosa
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        // Parsear respuesta JSON
        const data = await response.json();
        
        // Mostrar el chiste
        displayJoke(data.joke, data.success);
        
    } catch (error) {
        console.error('Error al obtener chiste:', error);
        
        // Mostrar mensaje de error apropiado
        let errorMessage = 'Chuck Norris está ocupado salvando el mundo... ¡Inténtalo más tarde!';
        
        if (error.name === 'AbortError') {
            errorMessage = 'La petición tardó demasiado...';
        } else if (error.message.includes('Failed to fetch')) {
            errorMessage = 'Error de conexión...';
        }
        
        displayJoke(errorMessage, false);
        
    } finally {
        // Desactivar estado de carga
        setLoadingState(false);
    }
}

// Función para mostrar el chiste en el DOM
function displayJoke(joke, isSuccess = true) {
    // Crear elemento para el chiste
    const jokeElement = document.createElement('div');
    jokeElement.className = isSuccess ? 'joke-text' : 'joke-text error-message';
    jokeElement.textContent = joke;
    
    // Limpiar contenedor y añadir nuevo chiste
    jokeContainer.innerHTML = '';
    jokeContainer.appendChild(jokeElement);
    
    // Agregar animación de entrada
    jokeElement.style.opacity = '0';
    jokeElement.style.transform = 'translateY(20px)';
    
    // Aplicar animación con un pequeño delay
    setTimeout(() => {
        jokeElement.style.transition = 'all 0.5s ease';
        jokeElement.style.opacity = '1';
        jokeElement.style.transform = 'translateY(0)';
    }, 50);
}

// Función para manejar el estado de carga
function setLoadingState(loading) {
    isLoading = loading;
    
    if (loading) {
        // Activar estado de carga
        newJokeBtn.classList.add('loading');
        newJokeBtn.disabled = true;
        loadingSpinner.style.display = 'block';
        newJokeBtn.querySelector('.button-text').textContent = 'Cargando sabiduría...';
    } else {
        // Desactivar estado de carga
        newJokeBtn.classList.remove('loading');
        newJokeBtn.disabled = false;
        loadingSpinner.style.display = 'none';
        newJokeBtn.querySelector('.button-text').textContent = '¡Dame un chiste épico!';
    }
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    console.log('Aplicación de Chuck Norris iniciada 🥋');
    
    // Agregar evento al botón
    newJokeBtn.addEventListener('click', getNewJoke);
    
    // Permitir usar Enter para obtener chistes
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Enter' && !isLoading) {
            getNewJoke();
        }
    });
    
    // Cargar un chiste automáticamente al iniciar
    setTimeout(() => {
        getNewJoke();
    }, 1000);
});

// Función de utilidad para mostrar notificaciones
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    // Estilos inline para la notificación
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 2rem;
        border-radius: 10px;
        color: white;
        font-weight: bold;
        z-index: 1000;
        animation: slideIn 0.3s ease;
        background: ${type === 'error' ? '#ff6b6b' : '#4ecdc4'};
    `;
    
    document.body.appendChild(notification);
    
    // Remover notificación después de 3 segundos
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Manejo de errores globales
window.addEventListener('error', function(event) {
    console.error('Error global capturado:', event.error);
    showNotification('Algo salió mal... ¡Pero Chuck Norris lo arreglará!', 'error');
});

// Manejo de promesas rechazadas
window.addEventListener('unhandledrejection', function(event) {
    console.error('Promesa rechazada:', event.reason);
    event.preventDefault(); // Evitar que se muestre en consola
});