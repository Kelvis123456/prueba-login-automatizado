# prueba-login-automatizado

Un ejercicio de automatización de pruebas: una prueba de Selenium con Pytest que inicia sesión en la demo pública de OrangeHRM y comprueba que llega al dashboard. Guarda una captura antes y otra después del login y deja un reporte HTML.

**Stack:** Python · Selenium · Pytest

## Qué hay

- `test_login.py`: la prueba `test_login_exitoso`. Abre `https://opensource-demo.orangehrmlive.com/`, entra con las credenciales públicas de la demo y verifica que la URL contiene `dashboard`.
- `historias_usuario.txt`: las historias de usuario con sus criterios de aceptación y de rechazo.
- `evidencias/capturas/`: las dos capturas que genera la prueba.
- `reportes/reporte.html`: el reporte de una corrida.

## Cómo correrla

Necesitas Chrome. Selenium 4 baja el driver por su cuenta.

```bash
pip install selenium pytest pytest-html
pytest test_login.py --html=reportes/reporte.html
```

## Lo que no cubre

- Solo está el caso de login exitoso. Los criterios de rechazo de las historias (usuario o contraseña incorrectos, campos vacíos) no tienen prueba todavía.
- Usa `time.sleep` en vez de esperas explícitas, así que es más lenta y más frágil de lo necesario.
- Depende de que la demo pública de OrangeHRM esté en línea y no cambie sus credenciales ni su formulario.
