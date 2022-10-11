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

**169.254.169.254 -> para cada instancia se brinda un servicio de matadas en la sig direccion ip  169.254.169.254
aws e2 decribe-instances  --instances-id $INSTANCE_ID
ej. curl http://169.254.169.254/latest/mata-data/public-hostname

#### si la intsnacia se reincia no cambia la ip, cuando apagamos y prendemos si 
#### tipos de almacenamiento 
##### EBS -> persiste esta info , si se apaga y prende una instancia 
##### intance store -> se pierde la info si se apaga y prende una instancia 

##### las ip siempre son dinamicas 
##### cuando ocupamos una ip elastica(estatica)?, cuando queremos apagar y prender una instancia y no queremos que se cambie la ip 

#### hibernacion de una instancia, el sistema op guarda toda la info en memoria (asignamos ip elastica), por la instanci ahibernada no pagamos pero todo lo que almacena en el disco ebs si se cobra, requisistos para hibernar una instancia, 1.habilitar la hibernacion en el moemnto del lanzamiento / tipo de instancia compatible3.

### RE LANZAMIENTO DE UNA INSTANCIA
#### cuando hay muhco trafico en la red, cuando necesitamos una instancia mas pequeña, cuando el hadware necesita algun cambio,(para tamaño/ parches) vamos a necesitar lanzar una instancia desde 0, es imaportante diseñar instancias, todo lo que ira dentro en los user-script y la ami y asi no se pierde nignuna configuracion

#### cuando transicionamos a un nuevo tamaño de instancia , primero tenemos que apagarla para cambiar el tamaño

### AMI, y su obsolencia, amazon mantiene las que ya estan activas, pero ya no se puede crear mas instancias con esta ami (como buena practica se recomienda tener una misma ami para todas la instancias y asi tener la misma configuracion )

### actualizacion de ejecuacion de EC2, Sistem manager permite manejar muchas instancias a la vez, ocupamos un solo comando para podr actualizar todas la instancias  


###bastion host, como medida de "seguridad", sirve para que por ahi pase la info, y tenga salida a internet 


Qué método debería usar?

Lanzar desde la Management Console cuando necesite lanzar con rapidez una instancia temporal o única.
Lanzar con un script cuando deba automatizar la creación de una instancia de forma repetida y confiable.
Lanzar con CloudFormation cuando desee lanzar recursos relacionados en conjunto.



#### ** CONEXIONES, si no puede hacer la conexion por ssh verfique que el grupo de seguridad tenga habilitada una regla de entrada el puerto 22 , lo mismo si quiere sacarlo a la web, debe habilitar el puerto 80 


#### Cloud adoption framework (AWS CAF)ayuda a las organizaciones a desarollar planes eficiente  y eficaces,tambien orientar y dar buena practicas para crear un buen enfoque en la nube y su proceso de 
##### actores para definir los objetivos 
**se organiza en 6 perspectivas y son capacidades /
##### enfoque empresarial(orientado a la e/arquitectos empresariales )1.empresa -> con que contamos para soportar la tecnologia de la e 2.personas-> priorizar capacitacion para desarrollar organizacion agil  3.gobernanza -> darle continuidad a cualquir proyecto / riesgos empresariales (prince2, SaFe, OKRs)
##### enfoque tecnico(arquitectos y administradores TI) 1.plataforma -> entender y comunicar las naturaleza de los sitemas informaticos 2.seguridad -> como aseguramos las platafoormas/asegurarque la org cumpla obj de seguridad  3.operaciones -> cuales son la operaciones/acciones que se ejecutan para que las plataformas/negocio puedan seguir funcionando, definimos como se llevaran a cabo os negocios diarios 











#### AWS Well-Architected Framework




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

CLI comandos 
https://docs.aws.amazon.com/cli/latest/reference/index.html

cafe S3 y sitio webe statico http://tgamboa987.s3-website-us-west-2.amazonaws.com/


curl 169.254.169.254/latest/user-data






#### Elastic Beanstalk Servicio de computo (PaaS)
##### permite implemetar, escalar y administrar aplicaciones web con rapidez, tomar codigo, cargarlo y elastic se encarga de desplegar el codigo, mantiene el control de todos los recursos de mi app
#### compatible con go, java SE, node js, php, python y demases
#### elastic es gratuito, solo se paga por lo servicios subyacentes como ec2, rds, balanceador de carga, etc



#### Escalamiento VERTICAL/HORIZONTAL
##### vetical, aumento de hadware / horizontal, misma caracteristicas mas aumento de instancia 
#### Grupo de Amazon EC2 auto scaling, (escalamiento horizontal)permite crecer o aumentar la cantidad de instancias, y cuando no se necesite (cuando no hay tanta demanda quiero 2 instancias pero para un cyber necesito 15 instancias, cuando una instancia esta cargada, automaticamente se crean mas instancias ), si no ocupo auto scaling tendria que hacerlo manual , (en base a reglas por ej si se esta al 70% de la instancia, se crea otra instancia y asi sucesivamente )
##### como sabemos cuando hay que aumentar?, de eso se ocupa el elastic load balancing, puedo distribuir el trafico por paginas/tags(? en diferentes intancias /home / contacts /orders (se paga por el balanceador de carga dependiendo el tipo y por las instancias ocupadas )
#### AMAZON ROUTE 53, convierte tu ip(del balanceador) en un "nombre"/endpoint (elb-mybalancer.aws.com), el balanceador de carga pongo la ip publica y se conecta a las instacias que deben estar privadas(route53 envia una peticion a "elb-mybalancer.aws.com" a elastic load y asi se conecta a las intancias y envia la peticion a la instancias que corresponda )

** ELB (elastic load balancing/Balanceador de carga) distribuye solicitudes entre intancias y aumenta la disponibilidad 
#### casos de uso ? SEGURO, DESACOPLE , TOLERANCIA A ERRORES trabaja a nivel de la app en general( se encarga que las instancias estan "bien", si hay algun error en la instancias la elimina y crea otra igual, que me permite trabajar), EXPANSIVO aumenta la elasticidad y escalabilidad 
#### Elastic Load Balancing distribuye automáticamente el tráfico entrante de aplicaciones entre varias instancias de Amazon EC2. Le permite lograr tolerancia a fallos en sus aplicaciones al proporcionar sin problemas la cantidad necesaria de capacidad de equilibrio de carga necesaria para enrutar el tráfico de aplicaciones.

#### balanceador de carga de red, protocolo tcp, en los dispositivio IOT, sensores que trasmiten informacion 
** si necesito un app que tenga un rendimiento extremo, maneja solucitudes repentinas a gran velocidad 

#### balanceador de carga de aplicaciones, protocolo HTTP permite trabaja a nivel de app web, tiene la capacidad de recepcion mas lenta(? que el de red 
** direccionamiento basado en rutas y host /home / contact ( en un balanceador de carga hay agentes de escucha que clasifica grupos de destino  y  en esos grupos hay comprobacion de status  )
#### balancador de carga clasico, esta deprecado 
** habilitamos sesiones pegajosas(? para que el usuario que se le cayo en net, y queremos que vulva a conectarse a la misma instancia para que su carrito vuelva a tener la misma info

#### Receptores/AGENTES DE ESCUCHA/listener dentro del balanceador de carga 
##### proceso que define el puerto y protocolo con el que escucha el balanceador de carga 
##### cada balanceador necesita al menos un agente de escucha para aceptar el trafico y hasta 50 
##### las REGLAS de direccionamiento se definen en los agentes de escucha (una regla como minimo)

##### crear balanceador de carga CLI :aws elbv2 create-load-balancer 
##### crear grupo de destino para el balanceador de carga: aws elbv2 create-target-group
##### registrar las instancias en el grupo de destino : aws elbv2 registre-target
##### crear un agente de escucha y sus reglas: aws elbv2 create-listener 
##### comprobar el estado : aws elbv2 describe-target-health


#### AMAZON EC2 Auto Scaling
##### lanza o termina las inatncias de amazon Elastic Compute CLoud (amazon EC2) automaticamente, necesita una plantilla de lanzamiento(AMI, tipo de intancia,VPC, grupo de seguridad,almacenamiento, par de claves,datos de usuario ,tags), permite la configuracion de las politicas de escalado y tamao del grupo de instancias Ec2, no escala de forma infinita, hay que establecer el limite 
##### Auto Scaling le ayuda a mantener la disponibilidad de las aplicaciones y le permite escalar su capacidad de Amazon EC2 hacia fuera o en función de las condiciones que defina. Puede utilizar Auto Scaling para asegurarse de que está ejecutando el número deseado de instancias de Amazon EC2. Auto Scaling también puede aumentar automáticamente el número de instancias de Amazon EC2 durante los picos de demanda para mantener el rendimiento y disminuir la capacidad durante las paradas para reducir los costes. Auto Scaling es adecuado para aplicaciones que tienen patrones de demanda estables o que experimentan variabilidad horaria, diaria o semanal en el uso.
** Hay que establecer la misma VPC par autoScaling y las intancias 
**Integracion con Elastic Load Balancing 
##### politicas: como activar politicas? puedo configurar alarmas en CLoudWatch 
##### como validamos que las instancias esten sanas ?, es saber si las intancias funcionan como corresponde  aws autoscaling set-intance-health 
##### politicas de terminacion : define qe instancia se termina con el escalado descendentes /1.valancear las zonas de disponibilidad y lugo ya hay diferentes opciones 
##### Creacion de un grupo de estado estable : configurar unn grupo de amazon Ec2 autoscaling con los mismos valores minimos, maximos y deseados 
##### ** Escalado dinamico : Amazon EC2 /escalado de siguimiento de objetivo(aumenta o reduxca la capacidad en funcion de un valor en base a una metrica )/ escalado por pasos(aumenta o reduce la capacidad segun ciertos pasos if/else)/ escalado simple(aumente o reduzca la capacidad en funcion de un unico ajuste de escalado) 
##### ** Escalado predictivo : Amazon EC2 / escala de forma automatica en base a predicciones de Ec2, tambien se establece un maximo de escalamiento 
****** ALGO QUE FALLA UNICAMENTE AL CREAR UNA INTANCIA ES LA AMI, SI SE CREA Y FALLA DEBE SER OTRA COSA ******


**region :curl http://169.254.169.254/latest/dynamic/instance-identity/document |     grep region
**


##### AMAZON ROUTE 53 (SERVICIO GLOBAL(AL IGUAL QUE IAM))
###### convertir el ip a un nombre de dominio ,route 53 cobra por el 
###### cree un registro CNAME que apunto al balanceador de carga 
###### Politicas de direccionamiento ->  es el primer punto de contacto/entrada cuando queramos acceder a un recurso  / direccionamiento ponderado / de latencia / conmutaccion de error 
**** LOAD BBALANCER balancea las cargas operativas de la instancias 
**** ROUTE 53 balancea en funcion a politicas muhco mas amplias
#### blue/green deploy : cuando tenemos 2 versiones de un sistema que queremos probar que la segunda version funcione bien , debemos implementar blue(version1) y green(version2) / ROUTE 53 balancea de apoco, enviando el 100% del trafico al sistema blue y gradualmente empieza a enviarlo al sistema greend
#### Pruebas 

##### Docker contenedores / administrar infrestructura, https://kodekloud.com/courses/docker-for-the-absolute-beginner/
###### ECS, EKS, Fargate -> contenedores en AWS
#### Como crear contenedores: 
#### Docker es  una plataforma que nos permite crear , orbar, implementar,ejecutar contenedores
#### como se ve docker en AWS Amazon:
#### Elastic Container Registry (Amazon  ECR) : registro de contenedores administrado que facilita (creacion de imagenes)
#### Elasticc Container Service (Amazon ECS) : servicio de contenedores altamanete escalable y de gra rendimiento (es compatible con los contenedores de docker, puedo ocupar una imagen alojada ahi )
#### kubernetes : software de codigo abierto para el aprovisionamiento y la administracion de contenedores  
#### Amazon Elastic Kubernetes (amazon EKS) : (orquestador que contenedores) aprovisiona un cluster, tiene nodos de trabajo,
#### AWS Farget : tecnologia que permite ejecutar contenedores sin tener que administrar servidores ni cluster (no hay que administrar infraestuctura)(administrador de contenedores serverless) 


** cluster : conjunto de contendores


##### Lambda AWS(para tareas especificas que no requiere estar activa todo el timepo, cada vez que se invoca una funcion es que se ejecuta )/ servicio administrado de AWS / invocacion basada en eventos / el timepo de ejecucion de una funcion se limita a un maximo de 15min / admite varios lenguajes 
#### Lambda le permite al codigo ejecutarse sin approvisionamiento (tiene  de invocaciones gratuitas)
*** TODO LO SERVERLESS SE PAGA POR LO QUE SE USA SOLAMENTE
#### Capas d elamba son bibliotecas que permiten 

#### APIS

