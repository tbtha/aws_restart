# APUNTES

## IDE
#### Entorno de desarrollo integrado / Integrated Development Environment
#### Es una aplicación informática (Software) que proporciona servicios integrales para facilitarle al desarrollador o programador el desarrollo de software  
#### IDE de AWS  es Cloud9
_____

_____
___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 

https://pdx.scorm.canvaslms.com/RusticiEngine/defaultui/player/modern.html?configuration=sconeID&preventRightClick=false&cc=es_ES&ieCompatibilityMode=none&cache=20.1.9.169&playerConfUrl=https%3A%2F%2Fpdx.scorm.canvaslms.com%2FRusticiEngine%2FPlayerConfiguration.jsp&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZWRpcmVjdE9uRXhpdFVybCI6Imh0dHBzOi8vc2NvbmUtcHJvZC51cy13ZXN0LTIuaW5zY2xvdWRnYXRlLm5ldC9wYWNrYWdlcy8xMDkwL2xhdW5jaF9jb21wbGV0ZT9sb2NhbGU9ZXMiLCJwYWNrYWdlIjoiQXBpQ291cnNlSWR8c2NvbmVfcHJvZC5zaGEyNTZfMWI0ZTgyNzFiOWY4ODZlNzcxMWJlYjNkYWE4OWI1YjNiZGRmN2VjZmVhYjJlYjU1ZmVhZjVlM2VkZmE4NTcyOSFWZXJzaW9uSWR8MCIsImNvbmZpZ3VyYXRpb24iOiJzY29uZUlEIiwicmVnaXN0cmF0aW9uIjoiQXBpUmVnaXN0cmF0aW9uSWR8c2NvbmVfcHJvZC5hc3NpZ25tZW50LjI3NjU2NiFJbnN0YW5jZUlkfDAiLCJleHAiOjE2NjI1ODU4NjB9.YbsIwW21VpN9oqJ81139i0c-ZkNBbGrGezGBAavAj74&tracking=true&forceReview=false

## ¿Qué es la computación en la nube? 
#### La computación en la nube es la entrega  bajo demanda de recursos de TI en línea, con precios de pago por uso

## Tres modelos de computación en la nube
#### Infraestructura como servicio (IaaS) : el proveedor de la nube ejecuta el  hardware  y el software de virtualización . Usted aprovisiona y administra sus servidores virtuales y todo el software que está instalado en ellos.

#### Plataforma como servicio (PaaS) : el proveedor de la nube ejecuta y administra el hardware , el software de virtualización y los servidores virtuales . Solo necesita implementar su aplicación y sus datos.

#### Software como servicio (SaaS ): el proveedor de la nube  ejecuta y administra todo , desde el hardware hasta la aplicación. Solo necesita suscribirse a la aplicación para usarla

## Tres modelos de implementación en la nube
#### All-in cloud :Todo en la nube : todas sus aplicaciones se implementan completamente en la nube.
#### Hybrid : Híbrido : algunas de sus aplicaciones se implementan en la nube, pero otras permanecen en las instalaciones. Las aplicaciones aún pueden conectarse entre sí.
#### Privete cloud : (on-premises) : Nube privada ( instalaciones) : todas sus aplicaciones se implementan completamente en una infraestructura de nube que se ejecuta en su propio centro de datos.

## Ventajas:
+ Gasto de capital a gasto variable : no es necesario pagar por adelantado los activos físicos que necesita. En su lugar, paga sobre la marcha por los recursos que utiliza.
+ Economías de escala : obtenga un costo variable más bajo para los recursos que el que puede obtener por su cuenta. Por ejemplo, como proveedor de servicios en la nube, AWS le transfiere ahorros a medida que crece.
+ Planificación de la capacidad : reduzca las conjeturas sobre sus necesidades de capacidad.
+ Velocidad y agilidad : aprovisione recursos de forma rápida y bajo demanda.
+ Gaste estratégicamente : gaste dinero en sus proyectos comerciales en lugar de administrar centros de datos
+ Facilidad de implementación : Globalícese en minutos.

### El modelo de precios de AWS se basa en el principio de que paga por lo que usa .

## Acceso a los servicios:
##### Consola de administración de AWS : una aplicación basada en web o móvil para administrar sus servicios de AWS
##### Interfaz de línea de comandos de AWS (AWS CLI) : una herramienta de línea de comandos para administrar sus servicios de AWS
##### Kits de desarrollo de software (SDK) : un conjunto de herramientas de software (como bibliotecas, recursos y muestras) que un desarrollador puede usar en un programa para acceder a los servicios de AWS.

## Términos clave de la infraestructura de AWS

- Región : un área geográfica que se compone de dos o más zonas de disponibilidad
- Zona de disponibilidad : uno o más centros de datos discretos que están diseñados para el aislamiento de fallas
- Ubicación de borde  :  donde los usuarios finales pueden acceder a los servicios de AWS


# AMAZON EC2
#### Amazon EC2 proporciona servidores virtuales, también llamados instancias , que pueden hacer casi todo lo que puede hacer un servidor local. Cuando lanza una instancia EC2, dos parámetros que debe especificar son:
1. Un tipo de instancia : este parámetro especifica las características de rendimiento de la CPU, la memoria, el almacenamiento y la red de la instancia. El tipo de instancia a menudo se denomina tamaño  de la instancia.
2. Una imagen de máquina de Amazon (AMI) : este parámetro define el software inicial y el sistema operativo (SO) para la instancia. Hay muchas opciones disponibles para sistemas operativos y software preinstalado.
** Si inicialmente elige un tipo de instancia que tiene poca o demasiada potencia para su aplicación, puede cambiar el tipo de instancia más fácilmente que cambiar un servidor local.
###### Una instancia EC2 se puede comprar de cuatro maneras:
1. Instancias bajo demanda : pague solo por lo que usa, sin compromisos.
2. Instancias al contado: puje por instancias EC2 no utilizadas, sin compromisos. Puede ahorrar hasta un 90 por ciento en costos en comparación con las instancias bajo demanda.
3. Instancias reservadas : Reserve una instancia EC2 por 1 año o 3 años, con varios niveles de ahorro. (Nota: si planea usar un servidor durante mucho tiempo, es decir, más de 1 año, este tipo de compra es la mejor opción).
4. Host dedicado : ejecute instancias EC2 en hardware dedicado a un solo cliente
