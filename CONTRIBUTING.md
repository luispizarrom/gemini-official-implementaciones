# Guía de Contribución

¡Gracias por su interés en contribuir a `gemini-official-implementations`! Este documento proporciona directrices para contribuir a este repositorio, que funciona como un centro de recursos académico y técnico sobre las implementaciones oficiales de Gemini.

## Índice

1. [Código de Conducta](#código-de-conducta)
2. [¿Cómo Puedo Contribuir?](#¿cómo-puedo-contribuir)
3. [Proceso de Contribución](#proceso-de-contribución)
4. [Estándares de Codificación](#estándares-de-codificación)
5. [Estándares de Documentación](#estándares-de-documentación)
6. [Mantenimiento del Repositorio](#mantenimiento-del-repositorio)

## Código de Conducta

Este proyecto y todos sus participantes están gobernados por nuestro [Código de Conducta](CODE_OF_CONDUCT.md). Al participar, se espera que respete este código. Por favor, reporte comportamientos inaceptables a [luispizarrom@example.com](mailto:luispizarrom@example.com).

## ¿Cómo Puedo Contribuir?

Existen varias maneras de contribuir a este repositorio:

### 1. Reportar Problemas

Si encuentra información desactualizada, enlaces rotos, o errores en los ejemplos de código:

- Utilice la sección de Issues de GitHub
- Utilice la plantilla de issue proporcionada
- Incluya pasos detallados para reproducir el problema
- Proporcione capturas de pantalla si es posible

### 2. Sugerir Mejoras

Para proponer nuevas funcionalidades o mejoras:

- Revise primero las issues existentes para evitar duplicados
- Utilice la plantilla de "Feature Request"
- Describa claramente el problema que resolvería su propuesta
- Explique cómo beneficiaría a los usuarios del repositorio

### 3. Contribuir con Código o Documentación

Puede contribuir con:

- Nuevos ejemplos de implementación
- Mejoras a la documentación existente
- Correcciones a problemas identificados
- Nuevos casos de uso con ejemplos prácticos

### 4. Revisión de Pull Requests

La revisión de contribuciones de otros es una forma valiosa de participar:

- Proporcione comentarios constructivos
- Verifique que el código cumple con los estándares
- Pruebe las implementaciones cuando sea posible
- Valide la precisión de la documentación técnica

## Proceso de Contribución

### Para Contribuciones Menores

Para correcciones tipográficas, actualizaciones de enlaces, o pequeñas mejoras:

1. Haga fork del repositorio
2. Realice sus cambios en su fork
3. Envíe un pull request al repositorio principal
4. Los mantenedores revisarán su PR lo antes posible

### Para Contribuciones Mayores

Para nuevas funcionalidades, ejemplos complejos, o documentación extensa:

1. Abra primero una issue describiendo su propuesta
2. Espere comentarios de los mantenedores
3. Una vez que se apruebe el concepto, proceda a implementarlo
4. Haga fork del repositorio y cree una rama para su contribución
5. Implemente los cambios acordados
6. Envíe un pull request con referencia a la issue original

## Estándares de Codificación

### Python

- Siga la guía de estilo [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Utilice docstrings para documentar funciones y clases
- Incluya typing hints cuando sea posible
- Mantenga los ejemplos simples y centrados en Gemini
- Verifique que el código se ejecuta correctamente con las versiones actuales de la API

```python
# Ejemplo de estilo de código esperado
def process_multimodal_input(
    text: str, 
    image_path: Optional[str] = None, 
    model: str = "gemini-1.5-pro"
) -> dict:
    """
    Procesa entrada multimodal con Gemini.
    
    Args:
        text: Texto para procesar
        image_path: Ruta opcional a una imagen
        model: Modelo de Gemini a utilizar
        
    Returns:
        dict: Respuesta estructurada del modelo
    """
    # Implementación
    pass
```

### JavaScript

- Siga las convenciones de [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
- Utilice JSDoc para documentar funciones
- Prefiera sintaxis moderna (ES6+)
- Incluya comentarios explicativos cuando sea necesario

### Markdown

- Utilice títulos jerárquicos (#, ##, ###)
- Incluya índices para documentos extensos
- Utilice bloques de código con especificación de lenguaje
- Mantenga párrafos concisos y enfocados

## Estándares de Documentación

### Contenido Técnico

- Sea preciso y específico
- Incluya ejemplos prácticos
- Cite fuentes oficiales cuando sea posible
- Mantenga la documentación actualizada con la última API

### Estructura

- Organice el contenido de manera lógica
- Utilice títulos descriptivos
- Incluya una introducción que explique el propósito
- Termine con recursos adicionales cuando sea apropiado

### Imágenes y Diagramas

- Utilice diagramas claros y legibles
- Incluya texto alternativo para accesibilidad
- Optimice imágenes para rendimiento web
- Mantenga diagramas técnicamente precisos

## Mantenimiento del Repositorio

Este repositorio es mantenido principalmente por [@luispizarrom](https://github.com/luispizarrom) con el apoyo de la comunidad. Los mantenedores se comprometen a:

- Revisar issues y pull requests regularmente
- Mantener la documentación actualizada
- Verificar la precisión técnica del contenido
- Facilitar discusiones constructivas

### Proceso de Revisión

El proceso de revisión para las contribuciones incluye:

1. Revisión inicial de formato y estructura
2. Validación técnica del contenido
3. Verificación de coherencia con el resto del repositorio
4. Pruebas de funcionamiento para ejemplos de código

### Comunicación

La comunicación sobre este repositorio se realiza principalmente a través de:

- Issues y pull requests de GitHub
- Comentarios dentro del código
- Documentación actualizada

---

*Gracias por contribuir a hacer de este repositorio un recurso valioso para la comunidad de Gemini.*
