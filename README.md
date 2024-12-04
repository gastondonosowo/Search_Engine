# Search Engine

**Search Engine** es un motor de búsqueda básico que utiliza gRPC para realizar consultas de búsqueda sobre una base de datos PostgreSQL. Este proyecto incluye un backend que se comunica con un cliente Flask y utiliza Redis como caché para mejorar el rendimiento en búsquedas repetidas. El sistema permite realizar búsquedas de metadatos de páginas web, como título, descripción y palabras clave, y devuelve los resultados de manera eficiente y rápida.

## Características principales:
- **Backend gRPC**: Implementa un servicio gRPC que recibe solicitudes de búsqueda, consulta una base de datos PostgreSQL y devuelve los resultados en formato JSON.
- **Base de datos PostgreSQL**: Almacena los metadatos extraídos de páginas web, como títulos, descripciones y palabras clave.
- **Caché con Redis**: Almacena los resultados de búsqueda en Redis para mejorar la velocidad de las consultas repetidas y reducir la carga en el backend.
- **Interfaz web con Flask**: Utiliza Flask para proporcionar una interfaz de búsqueda donde los usuarios pueden ingresar términos de búsqueda y obtener resultados al instante.
- **Optimización de rendimiento**: Utiliza políticas de memoria en Redis (LRU) para garantizar que solo se almacenen las búsquedas más recientes y relevantes.

## Cómo funciona:
1. **Extracción de metadatos**: El proyecto incluye un script (`lectura.py`) que extrae metadatos (título, descripción y palabras clave) de páginas web y los almacena en la base de datos PostgreSQL.
2. **Consulta y caché**: El cliente Flask realiza una consulta al servidor gRPC con el término de búsqueda. Si el término ya ha sido buscado previamente, los resultados se recuperan de Redis; de lo contrario, se realiza una consulta en la base de datos PostgreSQL.
3. **Interfaz web**: Los resultados se presentan al usuario a través de una interfaz web, mostrando los títulos, descripciones y enlaces a las páginas web correspondientes.

## Tecnologías utilizadas:
- **gRPC**: Para la comunicación eficiente entre el cliente y el servidor.
- **PostgreSQL**: Base de datos relacional para almacenar los metadatos de las páginas web.
- **Redis**: Sistema de almacenamiento en caché para mejorar el rendimiento de las búsquedas.
- **Flask**: Framework web para crear la interfaz de usuario.

## Requisitos:
- Docker (para ejecutar los contenedores)
- Python 3.7+
- Dependencias de Python:
  - grpcio
  - psycopg2
  - redis
  - flask
  - beautifulsoup4
  - requests
