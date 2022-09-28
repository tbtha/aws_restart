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
#### 

- Región : un área geográfica que se compone de dos o más zonas de disponibilidad (26 por ahora )
- Zona de disponibilidad : uno o más centros de datos discretos que están diseñados para el aislamiento de fallas
- Ubicación de borde  :  donde los usuarios finales pueden acceder a los servicios de AWS

### Que tomar en cuenta para elegir una region ? 
#### requirimientos legales/Restriciones geograficas para almacenas datos, impedimentos que requiera desplegar los recursos en cierta region (si los datos requieren estar en latinoamerica, lo mejor seria la region de sao paulo)
#### cercania con tus clientes : donde estan tus bases de cliente ? conviene estar en una region cercana a los clientes para reducir la latencia que existiria entre las peticiones y los recursos 
#### servicios disponibles : no hay los mismo servicios en todas las regiones al mismo tiempo, los servios nuevo generalmente estan disponibles en la region de virginia (para pruebas virginia es la region que selccionaria )
#### precios : por la forma de estuctura fiscal en brasil por ej. es mas caro, 

##### *latencia -> si


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


#### Cloud adoption framework (AWS CAF)ayuda a las organizaciones a desarollar planes eficiente  y eficaces,tambien orientar y dar buena practicas para crear un buen enfoque en la nube y su proceso de 
##### actores para definir los objetivos 
**se organiza en 6 perspectivas y son capacidades /
##### enfoque empresarial(orientado a la e/arquitectos empresariales )1.empresa -> con que contamos para soportar la tecnologia de la e 2.personas-> priorizar capacitacion para desarrollar organizacion agil  3.gobernanza -> darle continuidad a cualquir proyecto / riesgos empresariales (prince2, SaFe, OKRs)
##### enfoque tecnico(arquitectos y administradores TI) 1.plataforma -> entender y comunicar las naturaleza de los sitemas informaticos 2.seguridad -> como aseguramos las platafoormas/asegurarque la org cumpla obj de seguridad  3.operaciones -> cuales son la operaciones/acciones que se ejecutan para que las plataformas/negocio puedan seguir funcionando, definimos como se llevaran a cabo os negocios diarios 

#### AWS Well-Architected Framework



 aws iam list-policies --scope Local 

Putty
ip publica cuando te conectas desde afuera 
ingresar con ec2-user


#### AWS systems Manager:  
##### session manager: administracion/gestion de instancias, queda registrado en cloud trail, no hay que establecer puerto ni concecciones de grupos 
#### patch manager: 
#### maintenance windows : programar periodos para ejecutar tareas administrativas y de mantenimiento en las instancias
#### state manager : administrador de estados -> mantener una configuracion uniforme d elas instacias de amazon EC2 (documento json con acciones que esten definidas para controlar las inslacias , pasos y parametros definidos )
##### inventory : recopila informacion acerca de las instancias y del software instalado en ellas 
##### insights : panel de informacion es una muestra de datosoperativos para cada recurso (Cloudwatch Dashboard)





AÑADIR Que tomar en cuenta para elegir una region ?
requirimientos legales/Restriciones geograficas para almacenas datos, impedimentos que requiera desplegar los recursos en cierta region (si los datos requieren estar en latinoamerica, lo mejor seria la region de sao paulo)
cercania con tus clientes : donde estan tus bases de cliente ? conviene estar en una region cercana a los clientes para reducir la latencia que existiria entre las peticiones y los recursos
servicios disponibles : no hay los mismo servicios en todas las regiones al mismo tiempo, los servios nuevo generalmente estan disponibles en la region de virginia (para pruebas virginia es la region que selccionaria )
precios : por la forma de estuctura fiscal en brasil por ej. es mas caro,

*regiones : areas geograficas aisladas,atraves de las regiones podemos acceder a los servicios de aws, una region  se compone de dos o más zonas de disponibilidad

#### zonas de disponibilidad: uno o mas centros de datos discretos que que están diseñados para el aislamiento de fallas suficientemente cerca para una latencia baja( tiempo de solicitud y recepcion del contenido) y suficientemente lejos para reducir los riegos de desastres en un conjunto de zonas de disponibilidad,
se recomienda dejar nuestros recursos en dos zonas de disponibilidad, para garantizar la alta disponibilidad 

#### Ubicacion de borde / ubicacion periferica : para poder crear copias de la informacion para tenerlas mas cercnas a os clientes y asi reducir la latencia, aws para no crear regiones en absolutamente todo elmunod, crea pequeñas
infraestructuras, las "ubicaciones pefirericas" (cloudfront, red de entrega de contenido que permite hacer la copia de la info que esta en una region hacia estas ubicaciones perifericas ) 

 

### Redes :
##### Direccione IP : direccion unica que identifica un dispositivo o rcurso en internet o dentro de una red local (identificador que permite enviar info entre dispositivos en una red) 
##### CIDR   
