
* apuntes pablo 
* https://pablo-dev.notion.site/pablo-dev/c483bcdd69194cec9b7619596844be98?v=cad8574c8ae3499286c9d27097b038f5

# MIS APUNTES 
#### IDE
~~~
Entorno de desarrollo integrado / Integrated Development Environment
Es una aplicación informática (Software) que proporciona servicios integrales para facilitarle al desarrollador o programador el desarrollo de software  
IDE de AWS  es Cloud9
~~~

### MODULO 1 : INTRODUCCION A AWS 

#### CLIENTE-SERVIDOR
~~~
Un CLIENTE puede ser un navegador web o una app de escritorio, con la que interactua una persona para realizar
	solicitudes a los servidores de computo un cliente solicita un articulo de noticias, puntuacion de un juego,etc
Un SERVIDOR puede ser un servicio como Amazon Elastic Compute Cloud (Amazon EC2), un tipo de servidor virtual.
	el servidor evalua los detalles de la solicitud y la cumple al devolver la informacion del cliente
		*Es un aparato informático que almacena, distribuye y suministra información
~~~

#### CLOUD 
~~~
***Recursos TI : software y hadware utilizados para : almacenamiento, cómputo, redes,
bases de datos, analítica, machine learning, Internet de las cosas, seguridad,
desarrollo, entre otras
	
*Como usuario podemos acceder a AWS x :
	-AWS Management Console (protected by password + MFA)
	-AWS Command Line Intefaces (CLI): protected by access keys (herramienta que permite interactuar con los servicios de AWs mediante comandos en una shell de linea de comandos )
	-AWS Software Developer Kit (SDK): for code : protected by acces keys (para llamar a las API de AWS desde el cod de su app)
	Estos estan protegidos por la misma clave de acceso, generamos las claves de acceso en la consola de administracion recordar mantener secreta su 
		-Access Key ID
		-Secret Access Key 
		
Para utilizar la CLI b: "install AWS CLI in windows" descargar de la pag, aceptar los terminos y verificar si se instalo correctamente revisando la version con aws --version 
*Para actualizar es necesario volver a descargar el AWS CLI MSI y volver a ejecutar 
	-indicaciones de configuracion y de uso en el modulo 6 IAM
	

IMPLEMENTACION CLOUD

>Basada en la nube / All-in cloud
	Todas sus aplicaciones se implementan completamente en la nube.
	Puede crear esas aplicaciones en una infraestructura de bajo nivel que requiere que el personal de TI las administre.
	De forma alternativa, puede crearlas mediante servicios de nivel superior que reducen los requisitos de administración,
		 arquitectura y escalado de la infraestructura principal.
	*Por ejemplo, una empresa podría crear una aplicación compuesta por servidores virtuales, bases de datos
		 y componentes de red totalmente basados en la nube.
>En las instalaciones / nube privada / on premises 
	Los recursos se implementan en las instalaciones locales mediante herramientas de virtualización y administración de recursos.
	*Por ejemplo, es posible que tenga aplicaciones que se ejecutan con tecnología que se almacena por completo 
		en su centro de datos local.
>Hibrida 
	Algunas de sus aplicaciones se implementan en la nube, pero otras permanecen en las instalaciones. Las aplicaciones aún pueden conectarse entre sí.
	Conecte los recursos basados en la nube a la infraestructura en las instalaciones locales.
	*Por ejemplo con una implementación híbrida, la empresa podría mantener las aplicaciones heredadas en las 
		instalaciones y beneficiarse de los servicios de datos y análisis que se ejecutan en la nube.

BENEFICIOS / VENTAJAS 
>Cambiar gastos iniciales por gastos variables 
	gastos iniciales = centro de datos, servidores fisicos y otros recursos en los que tendria que invertir antes de utilizarlos 
	gatos variables = solo paga por los recurso de computo que consume 

>Gaste estratégicamente / Deja de gastar dinero en la ejecucion y el mantenimiento de centro de datos
	Los centro de datos requieren mas gasto y tiempo en administrar la infraestructura y los servidores
		la idea es centrarse mas en las aplicaciones y los clientes 

>Planificación de la capacidad /Deja de adivinar la capacidad 
	No tiene que predecir cuánta capacidad de infraestructura necesitará antes de implementar una aplicación, 
		puede aumentar o disminuir la capacidad de computo en minutos de acuerdo a la demanda 

>Economias de escala 
	El uso agregado de la nube por parte de un gran número de clientes se traduce en menores precios de pago por uso.
	 AWS le transfiere ahorros a medida que los clientes aumentan.

>Aumentar la velocidad y la agilidad
	Aprovisione recursos de forma rápida y bajo demanda.
	El cómputo en la nube le permite acceder a nuevos recursos y disponibilidad en cuestión de minutos
		 en un centro de datos fisico esto seria en cuestion de semanas 
	La flexibilidad facilita el desarrolo y la implementacion de app

> Globalizarse en minutos 
	Le permite implementar rápidamente aplicaciones a clientes de todo el mundo, a la vez que les proporciona una
		 latencia baja utilizando la infraestructura global 
~~~

### MODULO 2 : COMPUTO EN LA NUBE
#### EC2 / AutoScaling / Elastic Load Balancing / Lambda / Elastic Container Registry (Amazon ECR) / 
Elasticc Container Service (Amazon ECS) / Amazon Elastic Kubernetes (amazon EKS) / AWS Farget
####  Amazon Simple Notification Service (AMAZON SNS Amazon Simple Queue Service (AMAZON SQS)
~~~
>>>>>>>>>> AWS Elastic Compute Cloud EC2 (Computo como servicio)
Proporciona capacidad de cómputo segura y de tamaño modificable en la nube como instancias de Amazon EC2. 
Servicio de computo de Servidores Virtuales
AWS maneja una gran cantidad de computo

muy flexible, rentable,rapido en comparacion de un datacenter local

EC2 se ejecuta en los equipos HOST administrados por AWS mediante tecnologia de virtualizacion, cuando se pone
	en marcha una maquina virtual comparte el host con varias instancias , el hypervisor es el resposable de
	compartir los recursos fisicos y de aislar dichas instancias, esto significa que son seguras e independiente 
	aunque compartan recursos, no  tiene conocimiento entre si 
	Multitenancy: compartir el hadware subyacente entre maquinas virtuales 

Son muy flexibles 
Tiene completo control de la instancias
Escalamiento vertical -> puede dar mas memoria y CPU, puede ampliar o disminuir las instancias cuanto lo necesite 
Usted controla el aspecto de red de EC2, que tipo de solicitudes pueden llegar al servidor y si se puede acceder de
	 manera publica o privada 
/Solo paga por lo que utiliza, instancias que estan en ejecucion
*Al lanzar una instancias de EC2, se lanza una maquina virtual en un hadware fisico instalado en una zona de disponibilidad 
****** ALGO QUE FALLA UNICAMENTE AL CREAR UNA INTANCIA ES LA AMI, SI SE CREA Y FALLA DEBE SER OTRA COSA ******
*Los datos de usuario están limitados a 16 KB.
*Los datos de usuario y los metadatos no están encriptados.
*Los metadatos de la instancia están disponibles en http://169.254.169.254/latest/meta-data.

TIPOS DE INSTANCIAS
(Analogia de la cafeteria: asi como cada empleado tiene habilidades diferente cada instancias tiene caracteristicas diferente)
Los tipos de instancias se agrupan bajo una familia de instancias que estan optimizadas para distintas tareas 
Ofrecen diferentes capacidad de procesamiento, memoria ram, alamcenamiento y red

>Uso general : Equilibran los recursos informaticos de memoria, procesamiento y de redes 
		Adecuadas para diversas cargas de trabajo 
		*servidore web,servidores de app, repositorios, base de datos pequeñas y medianas 

>Optimizadas para procesamientos/informaticas/computacion: 
		Procesadore de alto rendimiento 
		Adecuadas para app que requieren gran cantidad de recursos informaticos 
		*servidores web de alto rendimiento, servidores de juegos, High performance computing(HPC), modelador de datos cientificos 
		*para cargas de trabajo de procesamiento por lotes que requieren procesar muchas transacciones en un solo grupo.
		*para una carga de trabajo de procesamiento por lotes.

>Optimizadas para memoria :
		Para cargas de trabajo de uso intensivo de memoria 
		Adecuadas para las base de datos de alto rendimiento
		*para carga de trabajo que requiere que se carguen previamente grandes cantidades de datos antes de ejecutar una aplicación.

>Informatica acelerada / computo acelerado: 
		Utilizan aceleradores de hadware para agilizar el procesamiento de datos 		
		Ideales para calculos numericos de punto flotante, procesamiento de graficos y motores de busqueda 

>Optimizadas para almacenamiento :
		 Alto rendimiento para los datos almacenados localmente
		Ofrecen baja latencia y gran cantidad de operaciones dde entrada y salida por segundo (IOPS,metrica
			que mide el rendimiento de almacenamiento, indica cuantas operaciones de salida/entrada puede realizar
			un dispositivo en un segundo )
		Adecuadas para cargas d etrabajo como sistemas de archivos distribuidos y las aplicaciones de almacenamineto de datos 

**analogia-> cajero/optimizada para memoria baristas/optimizadas para procesamientos dibujosenelcafe/ informatica acelerada

PRECIOS

>>>Bajo demanda/ on demand :
	Solo se paga por el tiempo que exista la instancia 
	LINUX x segundos / WINDOWS x hora 
	No se aplican cosotos iniciales ni contratos minimos 
	*Ideales para cargas de trabajo irregulares de corto plazo 
		
>>>Planes de ahorro/Savings Plans:
	Precios bajos a cambio de un compromiso de una cantidad constante de recursos USD x hora 
	Require compromiso de 1 a 3 años 
	ahorros del 72%, sin importar la familia,el tamaño, la region

>>>Intancias Reservada:
	Para cargas de trabajo estables y de uso predecible 
	descuentos por compromiso de 1 a 3 años (pago total, pago inicial o sin pago inicial)
		Instancias reservadas standar (RI) :
			75% de dcto frente a precio bajo demanda 
		Instancias reversvadas convertible 
			hasta un 54 % de descuento en el precio bajo demanda
			 ofrece la capacidad de cambiar los atributos de la instancia reservada si el intercambio da como resultado instancias igual o mayor valor.
		Instancias reservadas programadas
			Las instancias reservadas programadas están disponibles para iniciarse dentro del período de tiempo que reserve, hacen coincidir con un cronograma que solo requiere una fraccion de dia, una semana o un mes 
			
>>>Instancias Spot:
	Aws puede recuperar estas instancias, da 2 minutos de advertencias para recuperar el trabajo y guardar el estado
	Ideal para cargas de trabajo que puedan ser INTERRUMPIDAS o que tengan tiempo de inicio y finalizacion flexibles 
	90%dcto frente bajo demanda 
	
>>>Host Dedicado:
	Servidores fisico dedicados solo a tus instancias 
	Disponible como On-Demand o con reserva de host dedicado.
	Utilizados para cumplir requisitos de conformidad
	Opcion mas costosa
	La facturacion es por host
	
>>> Instancias dedicadas 
	Instancias virtualizadas en hardware solo para usted.
	Puede compartir hardware con otras instancias no dedicadas en la misma cuenta.
	La facturacion es por instancias, Costo adicional de $2 por hora por región.
	

>>>>>>>>>Escalabilidad / scalability
Implica comenzar solo con los recursos necesario y diseñar una arquitectura para responder
automaticamente a la DEMANDA cambiante mediante el escalado o reduccion horizontal

ESCALABILIDAD HORIZONTAL : la capacidad de un sistema para crecer agregando computadoras adicionales con las mismas caracteristicas

	para que el proceso de escalado se realice automaticamente utilizamos :
>>>>>>>>>> Amazon EC2 Auto Scaling <<<<<<<<<<
(si accede a un sitio web que no carga o se agota el tiempo de espera, es probable que haya recibido mas solicitudes
de las que puede gestionar )
(analogia -> larga fila en la cafeteria y hay solo una cajera para recibir pedidos, gracias a autoscaling podemos aumentar
el n de cajeras para que disminuya las solicitudes a la cajera original )

Amazon EC2 Auto Scaling le permite AÑADIR o ELIMINAR AUTOMATICAMENTE instancias en respuesta a la DEMANDA
cambiante de las aplicaciones y asi tener una mayor DISPONIBILIDAD de las apps
	El escalado DINAMICO responde a la demanda cambiante.
	El escalado PREDICTIVO programa automáticamente el número correcto de instancias de Amazon EC2 en
		función de la demanda prevista.


GRUPO DE AUTOSCALING
	Establecer la capacidad MIN, que quiere decir que en todo momento debe habel al menos una instancia en ejecucion 
	Establecer la capacidad DESEADA, 
		*si no la establece, de forma predeterminada tomara el valor del min
	Establecer la capacidad MAX, 

**Arquitectura rentable y automatica, solo paga por las instancias que utliza asi reduce gastos y proporciona
	 la mejor experiencia al cliente  
**Necesita una plantilla de lanzamiento(AMI, tipo de intancia,VPC, grupo de seguridad,almacenamiento, par de claves,datos de usuario ,tags)


>>>>>>>>>> Elastic Load Balancing ELB <<<<<<< 
Dirigiendo el trafico de red para mejorar la escalabilidad de las app, con el balanceador de carga (servicio administrado )
(analogia -> en el cafe integramos a un anfitrion que recibe en la puerta a las personas y las distribuye en las
	diferentes filas de cajeras, asi no se acoplan en una sola fila y el trafico fluye bien )
Misma idea con las instancias, cuando ingresa una solicitud y hay varias instancias con el mismo software, como
sabe esa solicitud a que instancia debe dirigirse, para eso ocupamos el balanceador de carga, es quien RECIBE las
solicitudes y las distribuye a las instancias 

Un equilibrador de carga DISTRIBUYE AUTOMATICAMENTE EL TRAFICO entrante de aplicaciones entre varias instancias de Amazon EC2
	Actúa como un único punto de contacto para todo el tráfico web entrante de su grupo de Auto Scaling.
	Funciona para el trafico externo e interno (comunicacion de instancias frontend y backend)
	Aunque Elastic Load Balancing y Amazon EC2 Auto Scaling son servicios independientes, funcionan conjuntamente
		para garantizar que las aplicaciones que se ejecutan en Amazon EC2 puedan ofrecer un 
		ALTO RENDIMIENTO y DISPONIBILIDAD .

Beneficios:
	SEGURO
	DESACOPLE distribuye el trafico 
	TOLERANCIA A ERRORES si hay algun error en la instancias la elimina y crea otra, que permita trabajar
	EXPANSIVO aumenta la elasticidad y escalabilidad

TIPOS:  ??????????????????????????????????????????????
	Balanceador de carga de RED, capa 4, protocolo tcp, en los dispositivio IOT, sensores que trasmiten informacion 
		si necesito un app que tenga un rendimiento extremo, maneja solucitudes repentinas a gran velocidad 
	Balanceador de carga de APLICACIONES, capa 7 protocolo HTTP permite trabaja a nivel de app web, tiene la capacidad de recepcion mas lenta que el de red 
		direccionamiento basado en rutas y host /home / contact
	Balancador de carga clasico, esta deprecado 
		habilitamos sesiones pegajosas(? para que el usuario que se le cayo en net, y queremos que vulva a conectarse a la misma instancia para que su carrito vuelva a tener la misma info

<img width="542" alt="Elastic Load Balancing" src="https://user-images.githubusercontent.com/89615984/198515176-28d980fd-64db-4eec-801c-ecd144a3557a.png">

 **en un balanceador de carga hay agentes de escucha que clasifica grupos de destino y  en esos grupos hay comprobacion de status
Receptores/AGENTES DE ESCUCHA/listener dentro del balanceador de carga 
proceso que define el puerto y protocolo con el que escucha el balanceador de carga 
cada balanceador necesita al menos un agente de escucha para aceptar el trafico y hasta 50 
las REGLAS de direccionamiento se definen en los agentes de escucha (una regla como minimo)

MENSAJERIA Y COLAS/BUFFER
(analogia -> buffer para la comunicacion entre la cajera y el barista  )
xxArquitectura estrechamente acopladasxx
	*si un componente falla/cambia genera problema a otro componentes 
	*appA envia msje a appB, si appB falla deja de recibir los msjes, se van perdiendo y appA tambien 
		empieza a fallar 

!!Arquitectura con bajo/debil acoplamiento / LLOSELY COUPLED -> ARQUITECTURA CONFIABLE (DISPONIBILIDAD)
	*si un componente falla, esta aislado y un solo error no causara errores en cascada en todo el sistema
	* Entre la appA y la appB establecemos un buffer(cola de mensajes) para que en caso de que appB falle ,
		los mensajes sigan llegando a ese buffer y no interrumpa a la appA y cuando se restablezca la 
		appB los procese  

>>>>>>>>>> Amazon Simple Queue Service (AMAZON SQS)<<<<<<<<<< aws administra la insfraestructura
Permite a los componentes de software enviar, almacenaar y recibir mensajes en cualquier volumen, esto elimina
el riegos de perder msjes y no necesita que otro servicio este disponible 
	CARGAS: Datos contenido en un mensaje
	COLAS DE SQS : donde estan los mensjes hasta que se procesan 


>>>>>>>>>> Amazon Simple Notification Service (AMAZON SNS)<<<<<<<<<<
Canal para enviar mensajes entre servicios y tambien a los usuario finales
Modelo de publicacion y suscripcion (los msje se publican en topicos y usuarios suscritos reciben en msje)
	TEMA/TOPIC DE SNS: canal para la entrega de msjes
	SUSCRIPTORES DE ESE TEMA/TOPIC: pueden ser servicios como colas de SQS, funciones lambda, enlaces
		web HTTP/HTTPS y correos electronicos 

Tambien podemos utilizarlo para distribuir notificaciones a los usuarios finales mediantes msjes de texto
o correo electronico 

>>>SERVICIOS INFORMATICO ADICIONALES
EC2 flexible/confiable/escalable
Require que configure y administre su flota de instancias, el cliente es responsable de aplicar parches
a las instancias cuando se lanzan nuevos paquetes de software, configurar el escalamiento y asegurar disponibilidad 

SERVERLES : No se puede ver ni acceder a la infraestructura, ni a a las intancias que estan alojando la aplicacion
*AWS es responsable de la administracion, provisionamiento, escalamiento, alta disponibilidad y mantenimiento 

	COMPUTO SERVERLES 
>>>>>>>>>> AWS Lambda <<<<<<<<<< 
Servicio que permite ejecutar código sin necesidad de aprovisionar ni administrar servidores. 
Permite cargar codigo en una FUNCIONA LAMBDA, se configura un desencadenador, el servicio espera ese
aviso y ejecuta el codigo  
*tiempo de ejecucion de 15min 
*solo paga por el timepo de computo que consume/ejecutan
EJ: una función Lambda sencilla podría implicar cambiar automáticamente el tamaño de las imágenes
cargadas en la nube de AWS. En este caso, la función se activa cuando se carga una nueva imagen.
*AWS LAMBDA PERMITE 1 MILLON DE INVOCACIONES GRATUITAS POR MES 

>>>>>>>>>> AWS Batch <<<<<<<<<<
Administra toda la  configuracion por usted, evitando el aprovisionamineto , la administracion y el escalado de los trabajos informaticos por LOTES 

>>>>>>>>>> AWS Lightsail <<<<<<<<<<
Proporciona aplicaciones o servidores privado virtuales preconfigurados que incluye todo lo necesario para comenzar su sitio web
Ideal para personas que no manejan aws


>>>CONTENEDORES 
eficacia y portabilidad 

CONTENEDORES :Proporcionan una forma estándar de empaquetar el código y las dependencias de su aplicación en un solo objeto. 
	Los contenedores solo necesitan de la unidad logica y por debajo un orquestador que nos manejan estos conetenedores
Contenedor de Docker -> plataforma que utiliza la virtualizacion a nivel operativo 
	para entregar software en contenedores
	CONTENEDOR: paquete para su codigo donde pone codigo y dependencias o cualquier configuracion
	Estos contenedores se ejecutan en instancias y funcionan independientes
	Cuando se utiliza contenedores necesita procesos para inicializar/deternerlos/reinciciarlo y 
		monitorearlo 
	CLUSTER: conjunto de contendores/nodos
	Proceso de realizar estas tareas se denomina ORQUESTACION

	Herramientas de orquestacion de contenedores 
>>>>>>>>>> Amazon Amazon Elastic Container Service (Amazon ECS)<<<<<<<<<<
Es un sistema de administración de contenedores altamente escalable y de alto rendimiento que le permite
	ejecutar y escalar aplicaciones en un cluster administrado de instancias amazon ec2 o fargate 
Con Amazon ECS, puede utilizar las llamadas a la API para lanzar y detener aplicaciones habilitadas para Docker.
*servicio altamente escalable y de gra rendimiento (es compatible con los contenedores de docker, puedo ocupar una imagen alojada ahi )
*contenedores en instacias
*no hay cargo adicional, solo paga por los recursos que utilice como instanicas o volumenes de EBS
ECR esta integrado con ECS
>>>>>>>>>>Amazon Elastic Container Registry (Amazon ECR) <<<<<<<<<<
Registro de contenedores ADMINISTRADO para almacenar, administrar e implementar imagenes docker
*no hay tarifas ni compromisos inicuale, paga por la cantidad de datos que alamcena y los datos tranferidos a internet 


>>>>>>>>>> Amazon Elastic Kubernetes Service (Amazon EKS)
Es un servicio totalmente administrado que puede utilizar para ejecutar Kubernetes en AWS. 
Kubernetes es un software de código abierto que le permite implementar y administrar aplicaciones en contenedores 
*(orquestador de contenedores) aprovisiona un cluster, tiene nodos de trabajo
*contenedores en instacias

>>>>>>>>>> AWS Fargate <<<<<<<<<<<<
Motor de computo serverless para contenedores.Funciona con ECS o EKS
Tecnologia que permite EJECUTAR contenedores sin tener que administrar servidores ni cluster 
*solo necesitamos saber que imagen queremos lanzar 




***dentro de una intancia pueden haber varios contenedores***

~~~



### MODULO 3 : INFRAESTRUCTURA GLOBAL 
#### Region / zona de disponibilidad / ubicacion de borde 
#### Amazon CloudFront , Amazon Route 53, Amazon Outposts, Amazon Cloud Formation, AWS Elastic Beanstalk
~~~
(analogia -> desfile por fuera del local de comida, creacion demultiples tiendas )
(no es conveniente  correr una app en un solo edificio, ya que el edificio puede fallar por motivos inevitables,
si mi negocio tiene que se aprueba de desastres no puede funcionar en una sola ubicacion)
ALTA DISPONIBILIDAD y TOLERANCIA A FALLOS 

>REGIONES: Cada region se puede comunicar con otra region mediantes una red de fibra de alta velocidad 
us-west-1	controlada por aws
	Cada region estan aisaladas geograficamente, ningun dato entra o sale de su entorno sin que usted conceda
		permisos, para cumplir con REQUISITOS DE CONFORMIDAD GUBERNAMENTAL que indiquen que los datos
		no pueden salir de esa region
	Una region  se compone de dos o más zonas de disponibilidad
	Factores para elegir una REGION :
	1 Conformidad/Compliance -> observar requisitos de conformidad
	2 Proximidad -> cercania de sus clientes,ayudará a enviarles contenido más rápido 
	3 Disponibilidad de caracteristicas -> puede ser que la region mas cercano no tenga las caracteristicas
		 que se necesitan para el negocio
	4 Precios -> algunos lugares los precios son mas caros 

>ZONAS DE DISPONIBILIDAD : 1 o mas centros de datos discretos, con fuentes de energia, redes y conectividad redundante
us-west-1a / us-west-1b / us-west-1c	 
	Sirve para un plan de recuperacion antes desastre, 
	Ejecutar las aplicaciones en almenos dos zonas de disponibilidad en una region
	
>UBICACIONES DE BORDE/ EDGE LOCATION /UBICACION PERIFERICA: 
*Egde location tambien ejecutan otros servicio 
	Redes de entrega de contenido / content delivery network CDN -> Amazon CloudFront
>>>>>>>>>> Amazon CloudFront <<<<<<<<<<
Servicio que ayuda a entregar datos, videos, app, API a los clientes en todo el mundo con baja latencia y 
alta velocidad de transporte 
Amazon CloudFront utiliza ubicaciones de borde para ayudar acelerar la comunicacion, almacena copias en caché
del contenido mas cerca de los clientes para una entrega mas rapida 
CDN : Una red que ayuda a ofrecer contenido estatico a los usuarios segun su ubicacion geografica 

	Resolucion de nombre de dominio DNS
>>>>>>>>>> Amazon Route 53 <<<<<<<<<<<
Ayuda a dirigir a lo cliente a la direcciones IP correctas con una latencia baja y confiable 
Sistema de nombres de dominio DNS: sistema de traduccion de nombres de sitios web a IP
Con Route 53 podemos registrar nombres de dominio, podemos comprar y administar los mismos


	Si el cliente quiere ocupar los servicios de AWS dentro de su edificio 
>>>>>>>>>> AWS Outposts <<<<<<<<<<
Aws aisla una region operativa dentro de tu centro de datos, aws es el propietario y opera 100% de la 
infraestructura
Ampliar la infraestructura y los servicios de AWS a su centro de datos en las instalaciones locales.

>>> COMO APROVISIONAR RECURSOS
Interactuamos con aws atraves de APIs, todo es una llamada a la API (Interfaz de programacion de aplicaciones)
Consola de administracion AWS -> navegacion visual acceder y administrar los servicios
Interfaz de comando AWS (CLI) -> realizar llamadas a la API mediante el uso del teminal de su maquina 
Kits de dasarrollo de software de AWS (SDKs) -> permiten interactura con recursos de aws en lenguajes de programacion
Otras herramientas como : Cloud Formation /Elastic Beanstalk/ Terraform(no aws)
		para crear y administrar recursos de aws 


>>>>>>>>>> Elastic Beanstalk <<<<<<<<<< PaaS
Servicio que ayuda aprovisionar entorno basados en EC2
Hay que proporcionarle el codigo  de la app web con las configuracione y Elastik Beanstalk toma esa info y contruye 
el ambiente por usted
Mantiene el control de todos los recursos de mi app
Compatible con go, java SE, node js, php, python y demases
Elastic Beanstalk es gratuito, solo se paga por lo servicios subyacentes como ec2, rds, balanceador de carga, etc

>>>>>>>>>>> Cloud Formation <<<<<<<<<<<
Infraestructura como herramienta de codigo que le permite definir una amplia variedad de recursos de forma 
	declarativa en formato texto JSON o YAML llamados TEMPLATE de CLoud Formation
Permite definir lo que desea crear sin especificar los detalles de como construirlo
Admite muchos recuros como alacenamiento, bases de datos y demases 
Una vez que defina sus recursos en el template de cloud formation, cloud formation analizara ese template 
	y comenzara aprovisionar  todos los recursos que definio, en paralelo cloud formation administra 
	todas las llamadas a las APIs del backend
Puede ejecutar la misma plantilla en multiples cuentas y/o regiones y creara ambientes identicos en todos 
	estos, deja menos espacio para el error y todo es automatizado 

>>Dos terminos importantes para AWS CloudFormation son :
Una PLANTILLA/TEMPLATE es una especificacion de los recursos de AWS que se aprovisionarán 
Una STACK/PILA es una conjunto de recursos de AWS que se crearo a partir de una plantilla, puede aprovisionar(crear una plantilla muchas veces)
*Al eliminar una PILA, se eliminan los recursos que estan asociado con esa pila. CloudFormation determina
	el orden de eliminacion, usted no tiene control sobre el orden de eliminacion
*Puede editar los recursos directamente en la consola pero los cambios realizados fuera de Cloud Fromation pueden
	complicar las operaciones de eliminacion o de actualizacion dela pila
>>>Estructura de plantilla
>Parameters : (opcional) incluyen nombre/valor, que podemos hacer referencia mas adelante
>Mappings:(opcional) suelen utilizarse para hacer referencia a los valores de AMI
>Resources /Recursos :(obligatoria) contiene los objetos de AWS que se crearan, puede especificar relaciones
	y dependencias entre los recursos para que se creen en el orden correcto
>CloudFormation::Init permite implementar aplicaciones, archivos y otros recursos en las inctancias EC2
	 como parte del proceso de implementacion 
>CloudFormatio::WaitCondition se usa para coordinar la creacion de recursos, por ej si un recurso depende de otro,
	cloudFormation esperara que se completen otras actividades de creacion de recursos antes de intentar crear
	el recurso dependiente. WaitCondition envia una señal a aws cuando los comando de Init teminen de ejecutarse 
>Outputs/Resultados : (opcinal) devuelve valores que se crean en la plantilla, id-instances, VPCid





~~~

### MODULO 4 : REDES / NETWORKING
#### Amazon VPC / AWS Direct Connect 
#### Puerta de enlace de Internet(Internet Gateway) / Puerta de enlace privada virtual (Virtual Private Gateway) /ACL (Listas de control de acceso) / Grupos de seguridad 
~~~
>>>>>>>>>> Amazon Virtual Private CLoud (Amazon VPC)<<<<<<<<<<
Es un servicio de red que puede utilizar para establecer límites en torno a sus recursos de AWS 
Permite aprovisionar un segmento de red, logicamente aislado, donde podemos lanzar recurso de aws en una red 
virtual definida. Estos recursos pueden estar privados o publicos , con o sin acceso a internet 
Permite definir su rango de IP para los recursos de AWS
Una VPC:
	Está dedicada a una cuenta de AWS
	Pertenece a una sola región de AWS
	Puede abarcan varias zonas de disponibilidad
	Está aislada lógicamente de otras VPC
Puede crear varias VPC en una cuenta de AWS para separar los entornos de redes
*VPC predetermina de la cuenta, no es recomendada para gestionar nuestras app
Cuando creamos VPC definimos un bloque de IP con notacion CIDR(podemos tener un bloque de direcciones IP primario y 4 segundario )
Cuando utilizamo IPV6, amazon proporciona las direcciones IP
*5 VPC limite regional 

Direccione IP : direccion unica que identifica un dispositivo o rcurso en internet o dentro de una red
	local (identificador que permite enviar info entre dispositivos en una red) 


Direcciones IP reservadas de amazon VPC: (10.0.0.0/16)
10.0.0.0 -> direccionamiento 
10.0.0.1 -> reservada por aws para direccion de enrutador de VPC
10.0.0.2->
10.0.0-3 -> reservada para futura utilizacionn de aws
10.0.0.255 -> direccion de difusion de red 

******curl 169.254.169.254/latest/user-data******
 
>>>SUBREDES
	Rangos de direcciones IP dentro de la VPC 
	Subred Publica (analogia-> cajera)
	Subred Privada (analogia-> barista)
	*Hasta 200subredes por VPC 

Formas de controlar el acceso 
>>>>>Internet Gateway<<<<<
Recursos de acceso publico: Con el fin de permiter que el trafico de internet fluya desde y hacia la VPC,
asociamos Internet Gateway : puerta abierta al publico
*Para permitir que el tráfico público de Internet acceda a su VPC, debe conectar una puerta de enlace de Internet a la VPC.
<img width="840" alt="Intert Gateway" src="https://user-images.githubusercontent.com/89615984/198515174-02d87ff6-c91b-4490-8c1c-4904accb4c80.png">
**Subnet publica sale a internet atraves de Internet Gateway

>>>>>Virtual Private Gateway<<<<<
Recursos privados internos : No queremos que nadie que no corresponda pueda llegar a estos recursos, para
eso tenemos a Virtual Private Gateway : solo permite el ingreso de una red aprobada y no del internet publico 
Permite crear una conexion de VPN cifrada entre una red privada como datacenter on-oremiss
*Para acceder a los recursos privados de una VPC, hay utilizar una puerta de enlace privada virtual y un enrutador de aws . 
<img width="840" alt="Virtual Private Gateway" src="https://user-images.githubusercontent.com/89615984/198515167-eddd21bc-6615-4ce6-83e8-f77404851e9d.png">


>>>>>>>>>> AWS Direct Connect <<<<<<<<
Es un servicio que le permite establecer una conexión privada dedicada entre su centro de datos y una VPC.  
Puede establecer una conexion privada de fibra optica desde su centro de datos on-premiss a aws 
Se trabaja con un partern (Movistar/claro/etc) para poder establecer esta conexion
Direct Conect proporciona una linea fisica que conecta su red a su VPC de AWS 
*Tambien necesita de Virtual private Gateway para hacer la conexion a la VPC 

#SEGURIDAD
**La unica razon tecnica para usar subredes de una VPC es controlar el acceso a los gateway, pero las subredes
tambien pueden controlar los permisos de trafico con las listas de control de acceso a la red

*Red reforzadas 
>>>>>Listas de control de acceso a redes y subredes  ACL (stateless)
Es un firewall virtual que controla el paquete/trafico que entra y sale de la VPC(subred)
El hecho que lo deje entrar no precisamente lo deja salir :sin estado
(analogia-> agente de control depasaporte de aeropuerto)
*De forma predeterminada permite todo el tráfico entrante y saliente.

>>>>>Grupos de seguridad (stateful)
Seguridad nivel de instancia
Si lo deja entrar lo deja salir :con estado
*La ACL preterminada deniega todo el trafico entrante y saliente.
*Las ACL personalizadas de forma predeterminada se deniega todo el tráfico entrante y saliente



~~~

### MODULO 5: Storage and Database 
#### Instance Store / Amazon Elastic Block Store (Amazon EBS)/ Amazon Simple Storage Solution (Amazon S3) / Amazons Elastic Fyle Sistem(Amazon EFS)
####  Amazon Relational Database Service (RDS) /  Amazon DynamoDB./ ElastiCache/ Neptune/ Aurora/ Redshift
##### https://aws.amazon.com/es/products/storage/
~~~
*hay que asegurarnos que elegimos el almacenamiento adecuado

>>>>> Instance Store / Almacenes de instancias<<<<< almacenaiento de bloque, se actualiza las partes que se modifica 
Almacenamiento temporal de una instancias de EC2 (disco duro/almacenamiento local)
Es un almacenamiento en disco que está conectado físicamente a la computadora host para una instancia de EC2 y, por
	 lo tanto, tiene la misma vida útil que la instancia.
Si se detiene la instancia , todos los datos escritos se eliminan 
*Instance Stores es util cuando podemos perder los datos, arhivos emporales, datos de pruebas , etc 

>>>>>Amazon Elastic Block Store (Amazon EBS)<<<<<  almacenaiento de bloque, se actualiza las partes que se modifica 
Podemos crear discos duros virtuales, volumenes EBS, que podemos asociar a instancia EC2
EBS para que los datos persistan fuera del ciclo de vida de la instancias 
Permite tomar copias de seguridad incrementales de los datos, llamados Snapchots/Instantaneas,
	es importante tomar snapshot a menudo ya que si la unidad se daña podemos restaurar los
	datos la snapshot, estas snapshot pueden ser almacenadas en S3
Tamaños  de volumenes desde 1GB hasta 16TiB
Volumen de EBS almacena los datos en una unica zona de disponibilidad, tiene redundancia sobre la misma 
Para asociar un instancia y volumn EBS deben estar en la misma ZA
* Necesitamos almacenamiento ebs para hibernar las instancias
*Almacenan los datos en una sola zona de disponibilidad 

>>>>> Amazon Simple Storage Service (Amazon S3) <<<<< almacenamiento como objetos
Almacenamiento y recuperacion de una cantidad ilimitada de datos
Almacenamiento de los datos como objetos en buckets
Caracteristicas: 
	tamaño maximo de objeto de 5TB
	opcion de configuracion de versionamiento de objetos
	11 9 de durabilidad
	cada objeto tiene su URL 
	Sin Srvidor(no necesita instancias )
	Opcion de habilitar el control de versiones , en caso de sobreescritura o eliminaciones accidentales 

Costos dependen de:
	tipo de clase de almacenamiento
	cantidad de almacenamiento (cantidad y tamaño de los objetos)
	solicitudes (numero y tipo de solicitudes )
	transferencia de datos (se cobran cargos por los datos salientes )	
*AMAZON S3 ES GRATIS 1 AÑO PARA HASTA 5GB DE ALMACENAMINEOT 

Capas de datos / clases
	>>>Ammazon S3 Standard
	Diseñado para los datos a los que se accede con frecuencia 
	Los datos se almacenenan en almenos 3 zonas de disponibilidad 
	*S3 Standard tiene un costo superior al de otras clases de almacenamiento

	>>>Amazon S3 Standar-IA Infrequent Access o acceso poco frecuente 
	Para datos que se acceden con menos frecuencia pero qeu requieren acceso rapido
	Preciso para copias de seguridad, archivos de recuperacion,etc
	Los datos se almacenenan en almenos 3 zonas de disponibilidad 	
	*Tiene un precio de almacenamiento más bajo y un precio de obtención más alto
	
	>>>Amazon S3 One Zone-IA Infrequent Acccess
	Almacena datos en una única zona de disponibilidad
	Recomendado para ahorrar costos y para datos que se pueden reproducir facilmente en caso de error en la ZD
	*Tiene un precio de almacenamiento inferior al de S3 Standard-IA

	>>>>Amazon S3 Intelligen-Tiering
	Ideal para datos con patrones de acceso desconocidos o cambiantes
	Requiere una pequeña tarifa mensual de monitoreo y automatización por objeto
	S3 supervisa los patrones de acceso de los objetos. Si no ha accedido a un objeto durante 30 días consecutivos,
		Amazon S3 lo traslada automáticamente al nivel de acceso poco frecuente, S3 Standard-IA. Si accede a un
		objeto frecuentemente , Amazon S3 lo traslada automáticamente al nivel de acceso frecuente, S3 Standard.
	**se almacena los obj en dos capas, una de acceso fecuente y otra capa para los datos en reposo

	>>>Amazon S3 Glacier
	*En caso de requisito de conformidad que exijan la retencion de datos por un cierto periodo de tiempo,
		podemos utilizar una politica de bloqueo de almacenes, podemos especificar politicas
		WORM (escritura unica/lectura multiple)
	Podemos cargar archivos directo en glacer o mediante policas de vida de S3
	*de bajo costo pero demora en recuperar la info
	 3 Opciones de traer/recuperar archivos
		urgente 1-5min
		estandar 2-5 horas
		masiva 5-12 horas 
		*costos diferentes , mientras mas urgente mas alto el valor 
	* si se quiere traer archivos mas seguido es mejor ocupar otro servicio que sea mas economico	

	>>>>Amazon S3 Deep Archive
	Puede obtener objetos en 12 horas
	*de menor costo ideal para archivar

*Amazon S3 Politicas de ciclo de vida: politicas para transferir datos entre capas automaticamente  
	ej: podemos establecer que queremos un objeto en S3 standar por 30 dias, luego que se transfiera
	 a S3 Standar-IA por los proximos 60 dias , y finalmente que se tranfiera a S3 glacer por 180 dias
	 y que luego sea eliminado
*podemos crear permisos para limitar quien puede subir o descargar los objetos 
*Paga por lo que utiliza 

>>>>>>>>>> Amazon Elastic File System (Amazon EFS) <<<<<<<<<< almacenamiento de archivos 
Sistema de archivos adminsitrado 
Permite tener multiples instacias que puedan acceder a los datos de EFS al mismo tiempo 
Escala automaticamente ascendiente y descentiendo, sin que nosotros hagamos algo
Sistema de archivos para linux
Servicio regional, almacena datos en varias zonas de disponibilidad 
El alamcenamiento duplicado permite acceder a los datos simultaneamente desde todas las ZA (almacena datos en mas de una zona de disponibilidad )
*Servidores locales pueden acceder a EFS mediante direct connect 



			DATABASE
RDBMS : Sistema de base de datos relacional 
Las bases de datos relacionales utilizan un lenguaje de consulta estructurada (SQL)
	 para almacenar y consultar datos.
https://aws.amazon.com/es/products/databases/
Lift-and-shift migration : migrar la base de datos para que se ejecute en la nube 

>>>>>>>>>> Amazon Relational Database Service (Amazon RDS)<<<<<<<<<<<
Servicio administrado que permite ejecutar bases de datos relacionales 
Motores de DB disponibles en RDS : Amazon Aurora, MySQL, PostgreSQL, Oracle, Microsoft SQL server, MariaDB 
Beneficios: 
	Parches automatizados 
	Copias de seguridad (backup)
	Redundacia 
	Conmutacion por error
	Recuperacion ante desastre 
	Tu controlas la red 
	Analisis complejo de consultas JOIN

>>>>>>>>>>>> Amazon Aurora <<<<<<<<<<
Es una base de datos realcional compatible con MySQL y PostgreSQL
Beneficios 
	DB rentable 
	Replicacion de datos (6 copias en tres zonas de disponibilidad )
	Copias de seguridad continuas en S3
	

>>>>>>>>>>>> Amazon DynamoDB <<<<<<<<<<<<<
Una base de datos serverless, no relacional
Con dynamoDB creamos tablas, en esas "tablas" almacenamos y consultamos datos que se organizan en elementos y atributos 
Dynamo tiene un esquema flexible simple con CLAVE/VALOR, podemos agregar y eliminar elementos de una "tabla" en cualquier momento, 
	no todos lo elementos(clave) tienen la misma cantidad de atributos(valor) 
No se pueden hacer consulta de datos complejas, hay que escribir las querys de acuerdo a un pequeño
	 subconjunto de atributos llamados CLAVES, son consultas simples 
DynamoDB se encarga de administar el almacenamiento y no hay que preocuparse por el escalamiento del sistema 
Beneficios
	Almacena de forma redundante en todas las ZA 
	Es de alto rendimiento (tiempo de respuesta de milisegundos)
	Altamente escalable automatico
	
****Amazon DynamoDB Accelerator (DAX) es una caché en memoria para DynamoDB. 
	Ayuda a mejorar los tiempos de respuesta de milisegundos de un solo dígito a microsegundos.
	https://aws.amazon.com/es/dynamodb/dax/

>>>>>>>>>>> Amazon Redshift <<<<<<<<<<<
Servicio de almacenamiento de datos que puede utilizar para el ANALIS DE BIG DATA, en situaciones empresariales .
Ofrece la capacidad de recopilar datos de muchas fuentes y le ayuda a comprender las relaciones
	y las tendencias de los datos.
La arquitetcura esta compuesta por 3 niveles base de datos en si, analisis, y frontend que presenta los resultados
Nos permite hacer analisis de grandes voluemntes de info, es administrado por aws

>>>>>>>>>>>> Amazon Neptune <<<<<<<<<<<<<
Servicio de base de datos DE GRAFICOS
Puede utilizar Amazon Neptune para crear y ejecutar aplicaciones que funcionan con conjuntos de datos 
	altamente conectados, como motores de recomendación, detección de fraudes y gráficos de conocimiento.
https://aws.amazon.com/es/neptune/

>>>>>>>>>>>Amazon ElasticCache <<<<<<<<<<<<<
Servicio que añade capas de almacenamiento en caché a las bases de datos para ayudar a mejorar los tiempos
	de lectura de las solicitudes comunes. 
https://aws.amazon.com/es/elasticache/


>>>>>>>>>>>>AWS Database Migration Service DMS<<<<<<<<<<<
Servicio que permite migrar bases de datos a la nube de una manera segura y facil
*La base de datos de origen continua en operacion durante el proceso de migracion 
*Minimiza el tiempo de inactividad de las app qeu utilizan esa base de datos 
*Las DB de origen y destino no tiene que ser necesariamente del mismo tipo

>>HOMOGENEAS 
	Proceso de 1 solo paso 
	*La estructura , tipos de datos y codigo de la DB son compatibles 
	MySQL > RDS(MySQL)
	Microsoft SQL Server > RDS(SQL Server )
	Oracle > RDS(Oracle)
	*La DB puede estar en on premiss

>>HETEROGENEAS
	Proceso en 2 pasos 
	*La estructura , tipos de datos y codigo de la DB NO compatibles 
	Es necesario la convertir el esquema y el codigo con AWS Schema Conversion Tool para que 
		coincidan con los de destino  
	*Luego DMS para la migracion  
	
>>>Migraciones de bases de datos de desarrollo y pruebas
	Cuando se necesita hacer pruebas sobre los datos de produccion pero sin afectar a los usuarios 
	Se utiliza DMS para migrar los datos a los entornos de desarrollo o pruebas
>>>Consolidacion de bases de datos
	Cuando tenermos varias bases de datos y queremos consolidarla solo en 1 motor central
>>>Replicacion continua de bases de datos 
	Cuando necesitamos replicar continuamento los datos de una lugar a otro 

https://aws.amazon.com/es/dms/


~~~

### MODULO 6: SEGURIDAD
#### AWS Identify and Access Management AWS IAM (Politicas de IAM)/ AWS Organizations ( Politicas de control de servicios (SCPs) )/ AWS Artifact 
#### AWS SHIELD / AWS WAF / AWS Key Management Services (AWS KMS)  / Amazon Inspector / Amazon GuardDuty 
~~~
>>>Modelo de responsabilidad compartida 

CLIENTE, responsable de la seguridad EN la nube 
	Son responsable de todo lo que crean y almacenan en la nube 
		controla cómo se conceden, administran y revocan los derechos de acceso.
	Capas a cargo : SISTEMA OPERATIVO / APLICACIONES / DATOS

AWS, responsable de la seguridad DE la nube
	Aws opera, administra y controla los componentes en todos los niveles de la infraestructura.
	Capas a cargo : FISICO / RED / HIPERVISOR 
	

Al crear una cuenta en AWs, se recibe el usuario ROOT/RAIZ de la cuenta, quien es el propietario y tiene acceso 
	y control de cualquier recurso de la cuenta 
*Se recomienda activar la autenticacion multi-factor (MFA) para que al iniciar sesion deba ingresar
	correo, contraseña y un token aleatorio
*No utilice el usuario raíz para las tareas cotidianas. 
Tareas que requieren el uso de credenciales de usuario ROOT 
	Cambiar el plan de soporte de AWS
	Eliminar cuentas de AWs 

		Para controlar el acceso a la cuenta:
>>>>>>>>>> AWS Identify and Access Management AWS IAM <<<<<<<<<<< SERVICIO GLOBAL
IAM -> Autenticacion y autorizacion como servicio, permite administrar el acceso a los servicios y recursos de AWS de forma segura.

*Root , se crea por defecto, debe ocupar root solo para fines especificos 
*Users, son personas parte de la organizacion , estas se pueden organizar en grupos
*Gruops, conjunto de usuarios, solo contiene users , no otros grupos(sirve para facilitar la administracion)
POR QUE CREAMOS USUARIOS/GRUPOS? 
A los usuarios o grupos podemos asignarles documentos JSON que son "politicas", estas politicas definen los permisosque tendran esos users, de forma predeterminada se deniegan todos los permiso, explicitamente hay que
	darle permisos para que puedan acceder a los recursos (PRINCIPIO DE MENOR PRIVILEGIO: un usuario solo tiene acceso a lo que realmente necesita)

>>> Politicas de IAM -> es un documento JSON que describe que llamadas a la API un usuario puede o no hacer 
			documento que permite o deniega permisos para los servicios y recursos de AWS 
	ej1:
	"Version": "2012-10-17", (version de la politica)
	"Id": "S3-Account-Permissions", (identificador de la politica)
	"Statement":[  (declaraciones)
		"Sid": "1" (id),
		"Effect" :"Allow" / "Deny"  (le da acceso o deniega el permiso)
	]	"Principal":{
			"AWS": ["arn:aws:iam::123456789012:root/*"] (  a que cuenta, usuario o rol se aplicara esta politica )
			}
		"Action":[   (lista de llamadas a la APi que se denegaran o permitiran segun el efecto )
			"s3:GetObject",
			"s3:PutObject"
		],
		"Resource":  (lista de recursos a los que se aplicaran las acciones )
			["arn:aws:s3:::mybucket/*"]
		
	

	ej2:
	Effect : "Allow"
	Action : "s3:ListObject"
	Resource : "arn:aws:s3:::coffee_shop_reports" 
	*En este ejemplo de política de IAM se concede permiso para acceder a los objetos del bucket

*Podemos asociar una politica a un grupo y asi todos los usuarios de ese grupo tienen los mismo permisos 
*Roles : Podemos crear ROLES que tienen permisos asociados que permiten o deniegan acciones especificas, estos
 	los asumen durante un periodo te tiempo limitado, no tienen nombre de usuario ni contraseña 

protejamos a los user y groups IAM 
1-> PASSWORD POLICY
	strong password = mas seguridad tendra la cuenta 
	la politica de password puede tener diferetenes opciones
		un largo minimo, especificacion de caracters , que cambien sus contraseñas cada cierto tiempo determinado , tambien puede evitar la reutilizacion de las constraseñas 

2-> Multi Factor Authenticatio - MFA
	Deseamos proteger lo mas posibles nuestras cuentas ya que tienen autorizacion para acceder a los recursos/servicios, como lo protejemos ? con un dispositivo  MFA 
	MFA utiliza la combinacion de una constraseña que uested conoce y un dispositivo de segurirdad que usted posea, si pierde su ontraseña o es hackeada, tendra que tener si o si el dispositivo fisico para entrar a la cuenta 
	cuales son estos dispositivos ? 
	1.Dispositivo Virtual MFA (google authenticator-solo telefono /Authy-multidispositivo) .Soporte para multiples tokens en un solo dispositivo
	2.Universal 2nd Factor (U2F) Security Key , es un dispositivo fisico usb? Yubikey by Yubokey, admite multiples users root y iam que usen una sola security key  
	3.Hardware key Fob MFA Device  , Provided by Gemalto
	4.Hadware key fob MFA Device for AWS GovCloud(US), Provided by surepassId
	
USERS: 
(una vez instalamos la AWS CLI)
Para poder acceder a la AWS CLI necestamos nuestras claves de acceso (Access key Id / Secret access key)
	-las claves de acceso se pueden crear al momento de crear el usuario 
	-tambien podemos crearlas despues de creado el user 
1ER PASO es configurar el uso de aws, ingresar en la linea de comando 
	aws configure
en el que hay que ingresar los sig datos 
	Access key ID
	Secret access key
	Default region name 
	Default out format 
Probamos funcionamiento con "aws iam list-users"

>>>>>>>>>> AWS Organizations <<<<<<<<<<
AWS Organizations crea automáticamente una raíz, que es el contenedor principal de todas las cuentas de su organización. 
Una forma de tener orden y hacer cumplir permisos para ciertas funciones en determinadas cuentas 
Es como una ubicacion central para administrar varias cuentas de AWS (la facturación, el acceso, la conformidad y la seguridad)
Caracteristicas:
	Administracion centralizadas de todas las cuentas de la organizacion
	Facturacion unificada de todas las cuentas (descuentos por volumen)
	Administrar cuentas de manera jerarquicas(agrupamos cuentas en unidades organizativas
		 puede aislar con mayor facilidad las cargas de trabajo o las aplicaciones que tienen requisitos de seguridad específicos.)
	Control sobre los servicios aws y acciones API que puede acceder cada cuenta (Podemos utilizar las 
		Politicas de control de servicios (SCPs), para restringir a que servicio, recurso  o acciones
		pueden acceder los usuarios o roles en cada cuenta de la organizacion )
	*Las politicas decontrol de servicios se aplican a una cuenta miembro individual o a una unidad organizativa 
**está disponible para todos los clientes de AWS sin cargo adicional.
** El número máximo predeterminado de cuentas permitidas para una organización es de 4, pero puede ponerse en contacto
	con AWS Support para aumentar la cuota, si es necesario.

>>>>> Conformidad
Cada industria tiene estandares que deben cumplirse, se realizan auditorias para validar que se cumplieron los estandes 
EJEMPLO:
	Si utilizamos sofwate que trata con datos  de consumidores de la union europea debemos asegurarnos de que cumplimos con el
		Reglamento General de Proteccion de Datos (GDPR)
	Si utilizamos app del sector de sanidad de eeuu, hay que diseñar la arquitetcura para que cumpla con los requisitos de HIPAA
		Health Insurance Portability and Accountability Act

AWS ya creo la infraestructura de centros de datos y de redes con las practicas recomendadas de seguridad de la industria
Como cliente heredamos todas las practicas recomendadas de aws 

La region puede ayudarnos a cumplir con normas de conformidad 
Ej:si solo puede almacenar datos en su pais, puede elegir una region apropiada y aws no replicara automaticamente en otras regiones 
*El cliente es propietario de los datos y es SU reponsabilidad proteger los datos , hay varios mecanismos de seguridad 
Para habilitar la proteccion de datos en muchos servicios es parte de la configuracion que tiene que gestionar en el recurso

AWS puede proporcionales documentacion que demuestre que sigue las practicas recomendadas de seguridad y conformidad
	podemos acceder a estos documentos en el servicio AWS Artifact, aqui puede tener acceso a informes de conformidad
	realizados por terceros que han validado una amplia gama de estandares de conformidad "Centro de Conformidad de AWS" para info 

>>>>>>>>>>> AWS Artifact <<<<<<<<<<
Es posible que tenga que cumplir estándares específicos. Una auditoría o inspección garantizará que
	la empresa cumple con esos estándares.
AWS Artifact es un servicio que proporciona ACCESO BAJO DEMANDA DE INFORMES DE SEGURIDAD Y CONFORMIDAD de AWS y a determinados acuerdos en línea. 
Consta de dos secciones principales: AWS Artifact Agreements y AWS Artifact Reports.

>>AWS Artifact Agreements:Acuerdos 
	Supongamos que su empresa necesita firmar un acuerdo con AWS en relación con el uso de determinados tipos de información en los servicios
		de AWS. Puede hacerlo a través de AWS Artifact Agreements.

>>>AWS Artifact Reports 
	Proporciona informes de conformidad de auditores externos. Estos auditores han probado y verificado que AWS cumple con una variedad de estándares
		y normativas de seguridad globales, regionales y específicas del sector. 
https://aws.amazon.com/es/artifact/

>>>>>Centro de conformidad del cliente / Customer Compliance Center
Contiene recursos que le ayudarán a obtener más información sobre la conformidad de AWS. 
En el centro de conformidad del cliente, puede leer las historias de conformidad de los clientes para descubrir cómo las empresas de sectores regulados
han resuelto diversos desafíos de conformidad, gobernanza y auditoría.


>>>>> Ataques de denegacion de servicios distribuido DDoS / Disttributed denial-of-service
Es un intento deliberado de hacer que un sitio web o una aplicación no estén disponibles para los usuarios.
El objetivo del ataque es anular la capacidad de funcionar de su aplicacion por medio de saturar el sistema
	al punto que no pueda operar mas 
El atacante intenta saturar la capacidad de sua app para denegar sus serviciosa cualquier person, el ataque
 desde una maquina no es suficiente, el atacante aprovecha otras maquinas en internet para tocar a su infraestructura
 La idea principal es que el comandante del ataque haga el menor trabajo posible, y que la victima sea
 objeto de una carga de trabajo insoportable de procesar 

Ataques especificos
>>> Inundacion UDP
EJ:	Cualquiera que pueda enviar una solicitud al sistema meteorologico recibira como respuesta una cantidad
	grande de datos, aqui el ataque es simple el atacante envia una solicitud como el pronostico del tiempo
	pero da una direccion de retorno falsa como una nuestra, entonces todas la respuestas/info/datos inunda
	nuestro servidor y paraliza el sistema al tratar de recibir una info que nunca solicito 
	*Ataque de bajo nivel diseñado para agotar la red
**Solucion: Los grupos de seguridad solo permiten el trafico entrarte de solicitudes autorizadas, el protocolo
	meteorologico es distinto al habitual, entonces si no esta en la lista de entrada no se puede comunicar con el servidor 

>>> Ataques a nivel HTTP
	Parecen cliente normales con solicitudes normales, todas proenientes de un ejercito de quipos, demandan tanta
	atencion que los clientes habituales no pueden entrar, intentan trucos como el siguiente ataque:
>>> Ataque Slowloris
	El atacante finge tener una conexion lenta y la  solicitud al servidor se hace larguisima y la fila no puede avanzar 
	Pueden agotar la capacidad de todo un frontend sin esfuerzo
**Solucion: Elastic Load Balancer espera recibir la solicitud completa antes de hacerla llegar al servidor, puede interntar
	saturarlo pero es escalable 

***Para ataques mas audaces/sofisticado:
Aws tiene herramientas de defensa 

>>>>>>>>>>> AWS WAF <<<<<<<<<< ????????????????????????????????????????
es un firewall de aplicaciones web que le permite monitorear las solicitudes de red que llegan a las aplicaciones web. 
AWS WAF funciona de forma similar para bloquear o permitir el tráfico. Sin embargo, lo hace mediante una lista de control de acceso (ACL)
	web para proteger sus recursos de AWS. 

>>>>>>>>>>> AWS SHIELD <<<<<<<<<< : ESCUDO
Servicio que PROTEGE las aplicaciones DDoS
Proporciona una mitigación en línea automática y una detección siempre activa que minimizan el tiempo de inactividad y la latencia de la
	 aplicación, por lo que no es necesario disponer de AWS Support para beneficiarse de la protección contra DDoS.
Dos niveles : Standard / Advanced 

>>AWS Shield Standard 
	SIN COSTO Protege automaticamente a todos los clientes de aws de ataques Ddos
	AWS Shield Standard utiliza diversas técnicas de análisis para detectar el tráfico malicioso en tiempo real y mitigarlo automáticamente.

>> AWS Shield Advanced 
	DE PAGO servicio que proporciona DIAGNOSTICO DETALLADO de ataques y la capacidad de detectar y mitigar ataques DDoS


** puede integrar AWS Shield con AWS WAF escribiendo reglas personalizadas para mitigar los ataques DDoS complejos
https://aws.amazon.com/es/shield/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc

>>>>>> AWS SHIELD / AWS WAF <<<<< ???????????????????????????????????????????
aws waf usa un firewall para app web para filtrar el trafico entrante, cuenta con capacidades de aprendizaje automatico y puede
reconocer nuevas amenazas a medida que evoluciona y ayuda a defender a su sistema de forma proactiva 



>>>>>Seguridad Adicional
Como proteger DATOS en REPOSO/TRANSITO:
Lo hacemos mediante la Encriptacion / Cifrado:
	Proteger un mensaje o conjunto de datos , de forma que solo puedan acceder a ellos los autorizados 
	Las parte no autorizadas tienen muy pocas posibilidades de acceder al msje 


#CIFRADO EN REPOSO: Datos estan inactivo, solo estan almacenado y no se mueven 
	EJ: el cifrado en reposo esta activo en todos los datos de las tablas dedynamoDB y eso ayuda a
		evitar el acceso no autorizado 
	*Se integra con AWS Key Management Services (AWS KMS)
>>>>>>>>>> AWS Key Management Services (AWS KMS) <<<<<<<<<<
Servicio de ADMINISTRACION DE LLAVES que permite gestionar las llaves de cifrado que se utilizan para
	 cifrar las tablas 
Permite realizar operaciones de cifrado mediante el uso de llaves criptográficas, que es una cadena aleatoria de digitos
	para cifrar y descifrar datos 
*puede deshabilitar temporalmente las claves para que nadie las pueda utilizar.

#CIFRADO EN TRANSITO: Datos que se desplazan entre A y B 
	*Podemos ocupar la capa de conexion segura (SSL) para cifrar los datos y podemos usar cetificdo de
		servicios para validar y autorizar a un cliente, significa que los datos estan protegidos al
		estar en movimiento

>>>>>>>>> Amazon Inspector <<<<<<<<<<
Ayuda a mejorar la seguridad y conformidad de las aplicaciones al ejecutar una EVALUACIONES DE SEGURIDAD  en relacion
	con la infraestuctura
Ayuda a revisar si hay desviaciones/vulnerabilidades en las practicas recomendadas de seguridad, exposision y vulnerabilidad 
Una vez que Amazon Inspector ha realizado una evaluación, le proporciona una lista de los resultados de seguridad. La lista
	prioriza por nivel de gravedad, incluida una descripción detallada de cada problema de seguridad y una recomendación sobre 
	cómo solucionarlo, aws no garantiza que siguiendo las recomendaciones se solucionen los problemas de seguridad 
*PARA REALIZAR EVALUACIONES DE SEGURIDAD AUTOMATIZADAS 


>>>>>>>>>> Amazon GuardDuty <<<<<<<<<<< :GUARDIA
Servicio de DETECCION INTELIGENTE DE AMENAZA, analiza toda la actividad de la cuenta mediante eventos de CloudTrail y tambien
	analiza la actividad de la red mediante los registro de flujo de VPC y los registos de DNS 
Si GuardDuty detecta amenazas, puede revisar las conclusiones detalladas sobre ellas en la consola de administración de
	AWS. Los hallazgos incluyen los pasos recomendados para la corrección.


https://aws.amazon.com/es/products/security/
https://aws.amazon.com/es/compliance/

~~~

### MODULO 7 : MONITOREO Y ANALISIS
#### Amazon CLoudWatch / Amazon CloudTrail / AWS Trusted Advisor
~~~~
Podemos utilizar metricas para ver que tal funcionan los sistemas y procesos 

MONITOREO: Sistema de observacion, recoleccion de metricas y luego uso de datos para tomar decisiones 

>>>>>>>>>> Amazon CLoudWatch <<<<<<<<<<
Para visibilidad/monitoreo del estado de los servicios 
Permite monitorear infraestructura de aws y las app que se ejecutan en tiempo real, opera mediante el 
	siguimiento y monitoreo de metricas
Metricas:variables vinculadas a sus recursos (la utilizacion de CPU de una instancia )

>>ALARMAS DE CLOUDWATCH
	Podemos establecer un umbral de una metrica personalizada y cuando se alcanza ese umbral, CLOUDWATCH genera una
		alerta y puede descencadenar una accion
	Las alarmas estan integradas a SNS, podemos enviar mje de texto para avisar algo 
	*Podemos crear diferentes tipos de alarmas de cloudwatch para diferentes recurso

>>DASHBOARD DE CLOUDWATCH / panel de cloudwatch 
Panel que muestra todas las metricas casi en tiempo real, se van actualizando automaticamente
*Ponedos crear un panel que agrupe todas la metricas de las instancias  

Beneficios de CLOUDWATCH
	Acceso central de todas las metricas 
	Visibilidad de todas las app, infraestructura y servicion(info de los recursos distribuidos )
	Reducir el MTTR, tiempo medio de resolucion 
	Mejorar el TCO, costo total de propiedad 
	Manipular informacion de las metricas 


>>>>>>>>>> Amazon CloudTrail <<<<<<<<<<<
Servicio de auditoria de llamadas a la APIs de la cuenta 
Cada solicitud realizada a aws (lanzar instancia, insertar datos a una DB) se registra en el motor de CLOUDTRAIL
Se registra QUIEN hizo la solicitud, CUANDO, IP, TIPO DE RECURSO y RESPUESTA de la API
*Puede guardas esos registro/historial indefinidamente en un bucket de S3 
*Por lo general los eventos se acualizan en 15minutos despues de la llamada a la APi 
*Podemos filtrar la busqueta por usuario, recurso, fecha, etc 
*Ayuda a los usuarios a habilitar la gobernanza, la conformidad y la auditoría operativa y de riesgos en sus cuentas de AWS

>>> CLOUDTRAIL Insights 
Puede habilitarlo y permite detectar automaticamente actividades de API inusuales


>>>>>>>>>> AWS Trusted Advisor <<<<<<<<<<<
Asesor automatizado *BUENAS PRACTICAS* 
Servicio que asesora/aconseja/valora/inspecciona el entorno de AWS 
En tiempo real ejecuta comprobaciones/chequeos para cada pilar segun la practicas recomendadas 

5 Pilares/Categorias:  
	Optimizacion de costos 
	Rendimiento
	Seguridad
	Toleracia a fallos
	Limites de servicio

*Algunas comprobaciones son gratuitas y estan incluidas, y otras dependen del plan de soporte 
Trusted Advisor ofrece una lista de acciones recomendadas y recursos adicionales para obtener más información
	sobre las prácticas recomendadas de AWS. 
Tipos de iconos/niveles/acciones en el panel 
	NO SE DETECTARON PLOBLEMAS/INVESTIGACION RECOMENDADA/ ACCION RECOMENDADA
*Puede configurar alertas de correo para contactos
*Asegurese de que este activo en su cuenta 
*Ubicado en la seccion de Management Tools Herramientas de administracion en la consola 


https://aws.amazon.com/es/products/management-and-governance/use-cases/monitoring-and-observability/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&blog-posts-cards.sort-by=item.additionalFields.createdDate&blog-posts-cards.sort-order=desc
https://aws.amazon.com/es/products/management-and-governance/use-cases/configuration-compliance-and-auditing/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&blog-posts-cards.sort-by=item.additionalFields.createdDate&blog-posts-cards.sort-order=desc
config 
systems manager 
CodeGuru 
~~~~

### MODULO 8 : PRECIOS Y SOPORTE
#### Calculadora de precios(AWS Pricing Calculator) / Panel de facturacion(Billing dashboard) / AWS Budgets / AWS Cost Explorer
#### AWS Support (Basic, Developer, Bussines, Enterprisse)
~~~
Podriamos tener una aproximacion de cuanto cuesta por mes y hacer una estimacion de los otros meses
>CAPA GRATUITA/ AWS FREE TIE 
	Gratuito para siempre
	12 meses de uso gratuito
	Pruebas 
*Lambda tiene 1 millos de invocaciones gratuitas por mes
*S3 es gratis 1 año para hasta 5GB de almacenamiento 
*AWS Lightsail ofrece prueba de 1 mes de hasta 750 horas de uso 
*SageMaker, Comprehend Medical, DynamoDB, SNS, Cognito mas de 60 servicios 
https://aws.amazon.com/es/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all
https://aws.amazon.com/es/pricing/?aws-products-pricing.sort-by=item.additionalFields.productNameLowercase&aws-products-pricing.sort-order=asc&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all

>>>>>>>>>> Calculadora de precios de AWS  <<<<<<<<<<
Permite explorar los servicios de AWS y crear una estimación del costo de sus casos de uso 

*Cuando haya creado un presupuesto, puede guardarlo y generar un enlace para compartirlo con otras personas.
EJ: Una empresa quiere utilizar EC2 pero no está seguro de qué región o tipo de instancia de AWS sería la más
	rentable para su caso de uso., mediate la calculadora puede hacer una comparacion estimada 


>>>>>>>>>> Panel de facturacion/ Billing dashboard <<<<<<<<<< FACTURACION 
Como va la facturacion de la cuenta ?
>>> Bills :
	Acceso a los servicios que estamos pagando (Facturacion)
Gasto mensual hasta la fecha y los servicios utilizados 
Grafico con montos de mes anterior, actuales y previstos del mes sig 
Tabla con uso actual de la capa gratuita 
*Para pagar la factura de AWS, monitorear el uso y analizar y controlar los costos.
https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html

>>>Billing Consolidado:  AWS Organization 
	Beneficios de usar AWS Organization es la facturacion consolidada, al final del mes puede unir 
		la facturacion al propietario de la organizacion 
	Simplifica el proceso de facturacion 
	Compartir ahorros entre cuentas (descuentos por volumen)
	Funcion billing gratuita 

	>>>>>>>>>> AWS Budgets <<<<<<<<<<<	PRESUPUESTOS PERSONALIZADOS PARA ESCENARIOS COSTO/USO 
Presupuesto personalizados para escenarios de costos y uso
Recibe notificacion de forma anticipada si va exceder el monto presupuestado de ese recurso 
Puede crear presupuestos para planificar el uso del servicio, los costos de los servicios y las reservas de instancias.
*Para personalizar un budgets debe establacer un monto y especificar un umbral por ej cuando se llegue a ocupa
	el 80% y añadimos un email para que llegue la notificacion  

>>>>>>>>>> Cost Explorer <<<<<<<<<<<< OBSERVAR Y ANALIZAR COSTOS A LO LARGO DEL TIEMPO 
Permite observar y analizar como gasta su dinero en aws a lo largo del tiempo
*12 meses de gastos historicos para analizar y hacer seguimiento de los gastos (puedo agrupar por
	 atributos, las etiquetas son utiles para filtrar )
AWS Cost Explorer incluye un informe predeterminado de los costos y el uso de los cinco servicios de AWS de mayor costo acumulados. 
*Puede crear  informes personalizados de costos y guardarlos para volver a revisarlos 

https://aws.amazon.com/es/aws-cost-management/aws-cost-explorer/


>>>>>>>>>>> Planes de AWS Support <<<<<<<<<<<
Soporte para todos lo clientes dependiendo de sus necesidades

<<< BASIC SUPPORT :
	Servicio de atencio al cliente 24/7
	Documentacion y documentos tecnicos
	Foros de soporte
	AWS Trusted Advisor
	AWS Personal Health Dashboard, vista personalizada del estado de los servicios de aws  
	**GRATUITO y para todos los clientes

<<< DEVELOPER SUPPORT:
	Basic Support
	Orientación de prácticas recomendadas
	Acceso en horario comercial por CORREO al soporte tecnico 
	TIEMPO DE RESPUESTA 
		24h sobre cualquier pregunta
		12h en caso de que su sistema tenga falla 

<<< BUSINESS SUPPORT 
	Basic support 
	Trusted advisor, con todo el conjunto de comprobaciones 
	Acceso TELEFONICO directo a ing de soporte 
	TIEMPO DE RESPUESTA 
		4h si su sistema tiene fallas
		1h si su sistema esta detenido 
	Acceso a la admi de eventos de infraestructura

<<< ENTERPRISE SUPPORT 
	*cargas de trabajo criticas
	Incluye Basic support
	Director Tecnico de Cuentas Dedicado (TAM): 	
		Punto de contacto especializado con aws, parte del equipo de soporte , se especializa en el monitoreo proactivo de su entorno y apoyo 
		con optimizaciones, tambien proporciona adm de eventos de infrestructura, revision de well arcchitec

	TIEMPO DE RESPUESTA 
		de 15 minutos para carga de trabajo criticas 
	
*tienen precio de pago mensual y no requiere contratos 
https://aws.amazon.com/es/premiumsupport/plans/

>>>>>>>>>>> Well Architec <<<<<<<<<<< ???????????????????????????????????????????????????????????????????????????????????????



>>>>>>>>>>> AWS Marketplace <<<<<<<<<<
Catalogo digital, para buscar, implementar, administrar software de terceros que se ejecuten en su adquitectura
Implementacion rapida y segura de soluciones +Implementacion con un solo clic
Puede acceder a información detallada sobre opciones de precios, soporte disponible y opiniones de otros clientes
Caracteristicas
	+precios personalizados, acuerdo de licencias personalizados  +Opciones de pago por uso 
	+mercado privado
	+integracion dentro de su sistema de adquisiciones
	+herramientas de administracion de costos 	
https://aws.amazon.com/marketplace
~~~

### MODULO 9 : MIGRACION E INNOVACION 
#### AWS Snow Family
~~~
Si ya tiene immplementacion en on-premiss puede migrar hacia la nube :

>>>>>>>>> AWS Cloud Adoption Framework (AWS CAF) <<<<<<<<<<
Marco de adopcion de la nube de aws 
AWS CSF Existe para accesosar a la empresa para posibilitar una migracion sin problemas a aws 
Organiza la orientacion en seis areas de interes denomidad PERSPECTIVAS 	
	Negocios / Personas / Gobernanza se centran en las capacidades empresariales 
	Plataforma / Seguridad / Operaciones se centran en las capacidades tecnicas 
Plan de accion AWS CAF  
	Orientar a la administracion de cambios de la organizacion mientras realiza su traspaso a la nube 

**Tener un plan de accion que tenga sentido para la e, puede ayudarlo a mantenerlo en camino 

>>Estrategias de migracion 
	
.......
6R
	Como mover cantidades masivas de datos sin pasar por la red: 
>>>>>>>>>> AWS Snow Family <<<<<<<<<<

Conjunto de dispositivos FISICOS que ayudan a transportar físicamente hasta exabytes de datos dentro y fuera de AWS. 
Seguros y resistente a manipulaciones 
Firmado criptograficamente / datos cifrados 
https://aws.amazon.com/es/snow/

AWS Snowcone
	Dispositivo pequeño robusto y seguro
	Puede contener 8TB de datos, puede incluir capacidad de computo 
	Pedido mediante la consola y se envia fisicamente 
	AWS copia todos los datos a un bucket de s3 a tu cuenta 
	**Gerenalmente para datos de analitica, copias de seguridad

AWS Snowball Edge 
Adecuados para migraciones de datos a gran escala y flujos de trabajo de transferencias recurrentes
	AWS Snowball Egde compute optimized 42TB 
	AWS Snowball Egde storage optimized 80TB 

AWS Snowmobile 
	Alojado en un contenedor de transporte arrastrado por un camion
	Para trasportar hasta 100PTB de datos 
	**Ideal para migraciones grandes 


>>INNOVACION 

VMWARE Cloud en AWS
Inteligencia artificial / Machine Learnning
Amazon SageMaker
	Desarrolle, entrene e implemente modelo de machine learning agran escala
Amazon Augmented AI 
	maching learnign 
Amazon Lex
	Servicio de Machine Learning que extrae automáticamente texto y datos de documentos
	 escaneadosAyuda a crear box de chat interactivo
Amozn Textract
	Extraccion de textos y datos de documentos 
AWS DeepRacer 
	maching learning , oportunidad para aprender
AWS Groun Station 
	tiempo de pago en satelite 
Amazon Transcribe
	convierte voz en texto
Amazon comprehend 
	Descubrir patrones en texto

>>>>>>>>>> AWS Well-Architected Framework <<<<<<<<<<<
Le ayuda a comprender cómo diseñar y operar sistemas fiables, seguros, eficientes y rentables en la nube de AWS.
Herramienta para evaluar la excelencia de la arquitectura 
Describe los conceptos clave, los principios de diseño y las prácticas recomendadas de arquitectura para diseñar y ejecutar cargas de trabajo en la nube. 
	
>>Excelencia operativa / Operational excellence:
	Mejora constante y automatizacion 
	*Se centra en ejecutar y monitorear los sistemas y en MEJORAR CONSTANTEMENTE los procesos y los procedimientos. 
	*la clave es la AUTOMATIZACION de cambios, la respuesta a eventos y la definición de estándares para administrar las operaciones diarias.
	
>>Seguridad :
	Proteger la información y los sistemas.
	*La clave es la CONFIDENCIALIDAD y la INTEGRIDAD DE LOS DATOS , la administración de los permisos de usuarios y el establecimiento
	de controles para detectar eventos de seguridad.
	
>>Fiabilidad/ CONFIABILIDAD /. Reliability :
	Planificacion de la recuperacion 
	*Se centra en las cargas de trabajo que realizan las funciones previstas y en cómo recuperarse rápidamente de los errores para cumplir con las demandas. 
	La clave se incluyen el diseño de sistemas distribuidos, la planificación de la recuperación y cómo adaptarse a los requisitos cambiantes.
	
>>Eficiencia/eficacia del rendimiento /Performance eciency:
	Utilizar los recurso informaticos de forma eficiente
	*Se centra en la ASIGNACION ESTRUCTURADA Y SIMPLIFICADA de TI y en los recursos informáticos. 
	*La selección de los tipos y tamaños de recursos optimizados para los requisitos de la carga de
	trabajo, la supervisión del rendimiento y el mantenimiento de la eficacia a medida que evolucionan las necesidades de la empresa.
	
>>Optimización de costos / Reliability: 
	Se centra en evitar gastos innecesarios.
	*Entre los temas clave se incluyen la comprensión del tiempo dedicado y el control de la asignación de
	fondos, la selección de recursos para el tipo y la cantidad adecuados y el escalado para cumplir con las necesidades de la
	empresa sin gastos excesivos.
	
>>Sostenibilidad:
	Se centra en minimizar los impactos ambientales de ejecutar cargas de trabajo en la nube.
	*Entre los temas clave se incluyen un modelo de responsabilidad compartida para la sostenibilidad, la
		comprensión del impacto y la maximización del uso para minimizar los recursos necesarios y 
		reducir los impactos posteriores. 

<<<<< AWS Well-Architected Tool>>>>>
Herramienta de autoservicio para simular cargas de trabajo y ver aspectos de mejora en los diferentes aspectos, y 
entrega presenta un plan de como diseñar la infraestructura con las practicas recomendadas 



~~~

mejor tamaññññññññññññññññññño 
politicas de terminacion : define qe instancia se termina con el escalado descendentes /1.balancear las zona???????????





































AWS X-RAY , es un servicio que recopila datos sobre las solicitudes que atiende su aplicacion y proporciona
herramientas que puede usar para ver, filtrar y obtener info sobre los datos para IDENTIFICAR PROBLEMAS 
https://aws.amazon.com/es/xray/

https://aws.amazon.com/es/cloudwatch/
https://aws.amazon.com/es/about-aws/whats-new/2018/11/s3-intelligent-tiering/
https://aws.amazon.com/es/cloudtrail/

Reliability: refiere a la capacidad de un sistema para recuperarse de las interrupciones de la infraestructura o del servicio y
adquirir dinámicamente recursos informáticos para satisfacer la demanda

Performance efficiency : Una empresa está planeando reemplazar sus servidores informáticos locales físicos con servicios informáticos sin servidor de AWS. La empresa quiere poder
para aprovechar las tecnologías avanzadas rápidamente después de la migración.

Cost Explorer : Una empresa desea revisar sus costos mensuales de uso de Amazon EC2 y Amazon RDS durante el último año.

. AWS Consulting Partners : empresa desea migrar sus cargas de trabajo a AWS, pero carece de experiencia en computación en la nube de AWS.


Agility: A company's on-premises application deployment cycle was 3-4 weeks. After migrating to the AWS Cloud, the company can deploy the application
in 2-3 days.



Amazon Athena
 Amazon Kinesis
 Amazon QuickSight
AWS Batch
Amazon Lightsail
 Amazon WorkSpaces
 AWS CodeBuild
 AWS CodeCommit
 AWS CodeDeploy
 AWS CodePipeline
 AWS CodeStar












______________________________________________________________________________________________________________________________________________________-




#### CLOUD
~~~
¿Qué es la computación en la nube? 
La computación en la nube es la entrega  bajo demanda de recursos de TI en línea, con precios de pago por uso

Tres modelos de computación en la nube
	Infraestructura como servicio (IaaS) : el proveedor de la nube ejecuta el  hardware  y el software de virtualización . Usted aprovisiona y administra sus servidores virtuales y todo el software que está instalado en ellos.

	Plataforma como servicio (PaaS) : el proveedor de la nube ejecuta y administra el hardware , el software de virtualización y los servidores virtuales . Solo necesita implementar su aplicación y sus datos.

	Software como servicio (SaaS ): el proveedor de la nube  ejecuta y administra todo , desde el hardware hasta la aplicación. Solo necesita suscribirse a la aplicación para usarla 


~~~


### AMAZON VPC
~~~

	


ENRUTADOR : instancias dentro de distintas subredes se puede conectar gracias a las reglas de las tablas de enturtamiento

*al crear la subred defino si quiero asignar automaticamnte la IP pblica lo hacemos mediante un check -asignar automaticamnte una IP publica (debe estar toda la configuracion/conexion de la tabla de ruteo/internet gateway para que si sea una ip publica) (cuando defino que mi ip es publica, recordar habilitar la opcion de "habilitada" en las setting de subnet, por defecto esta "desabilitada")

*cuanndo creo una instanciaaa tengo una nic primaria siempre (tambien puedo tener asociada nic2 y nic3)( nic -> interfaz de red elastica)


SUBNET PRIVADA 
Los recursos de una private subnet (subred privada) no tienen conectividad a Internet. Esto se hace a propósito porque, de esta manera, se protegen los recursos para que no sean accesibles desde Internet.
Sin embargo, a veces es necesario que los recursos de una subred privada se comuniquen con Internet para descargar actualizaciones de software y servicios de acceso a Internet. Por lo tanto, se recomienda otorgar los recursos de outbound connectivity (conectividad de salida) a Internet a la vez que los protege de los accesos inbound (entrantes).
Esto se puede lograr con una Gateway NAT (puerta de enlace de traducción de direcciones de red) que se lanza en la subred pública 


____Opciones de DNS para una VPC
*cuando cramos VPC se le asigna un nombre de dominio por defecto, DNS proporcionado por aws(aws route 53 reolver)
*si desabilito la opcion de DNS automatico, solo podre acceder a la web mediante la IP 
*cuando habilito el DNS, desde zonas alojadas privada de aws route 53 proporciona dns a las instancias 
*Servidor propio DNS

____Escenarios de conectividad VPC
*conectar una subred privada a internet, ocupamos Gateway NAT (NAT instance deprecada)
*conectar subnet publica que necesitamos que tenga salia a internet , Internet gateway
*conectar VPC a VPC , VPC peering (Interconexion de VPC)
*conectar VPC a una red externa , VPN (red privada virtual), Direct Connect mas VPN ,VPN, CLoudHunb
*conectar VPC a servicios de AWS sin dejar la red AWS, PrivateLink, 
*conectar una VPC a varias VPC y a redes externas AWS Transit Gateway 

NAT(traducciones de direcciones de red)
Tengo una Subnet privada tiene que salir a internet pero esta protegido por el grupo de seguridad, para eso ocupamos NAT gateway, cuando sale a internet "cambia" tu IP y luego cuando vuelve a la instancia vuelve con la IP original (agrega un nivel de seguridad) 
Nat gateway vive en la subnet publica en la misma zona de disponibilidad, pero 
le decimos ala subnet privada que se conecte a ese nat gateway para tener salida
a internet 

VPC peering (interconexion de VPC)
*conexion de VPC a VPC
permite que el trafico fluya en diferentes direcciones
como hcaemos la coneccion atraves de las tabla de enrutamiento,
cada VPC tiene su tabla de enrutamiento 
como creamos VPC peering, propietario vpc1 solicita y propietario vpc2 acepta,
ambos propietarios agregan entradas a tabla de enrutamiento en ambas vpc participantes 
* no es transcitivo, AyB estan conectado , si conecto ByC, C no tiene acceso a A   
*las VPC tiene que ser de diferentes rango IP


AWS Transit Gateway 
conectar 3 o mas redes (VPC/VPN)

AWS Direct connect mas VPC 
Forma de conexion dedicada para el cliente, no sale a internet, literal es una servicio fisico,
que comparte con compañias como telefonica/movistar, la conexion es por fibra optica desde el 
centro de datos corportivo 

AWS VPN CloudHub
para conectar VPC con varias VPN 
habilita que sitios remotos puedan conectarse a la VPC  

Endpoint VPC (private link) 


-LAB Configuaracio de VPC : dar acceso a internet a una instancia en una subred privada con NAT gateway y una instancia bastion
creacion VPC
creacion subredes(habilitar la autoasiganacion de direccio IPV4 publicas)
creacion internet gateway 
internet gateway attach to VPC(La subred pública ahora tiene conexión a Internet.Sin embargo, para dirigir el tráfico a Internet, también debe configurar la route table (tabla de enrutamiento) de la subred pública de modo de que use la puerta de enlace de Internet.)
añadir la tabla de enrutamiento prederminada para la subnet privada
crear una tabla de enrutamiento para la subnet publica, que tenga una ruta para dirigir el trafico de internet al internet Gateway
asociar la tabla a la subnet publica 
lanzar instancia BASTION en la subnet publica
crear NAT gateway enla subnet publica 
agregar ruta a NAT gateway en la tabla de enrutamiento de la subnet privada
crear instancia LABInstance en la subred privada 
acceder mediante ssh a instancia BASTION
acceder a LABInstance desde BASTION con ssh PRIVATE-IP (copiar la ip privada de LABinstance)






~~~

#### Seguridad por capa Redes 
~~~
Defensa de red por niveles para las VPC
(de afuera para adentro):
1.Tablas de enrutamiento(obligatoria)
2.ACL de subred: entrante o saliente(opcional)(stalen)
3.Grupos de sefuridad de interfaz de red elastica o EC2(obligatoria)(stateful: con estado)
4.Proteccion basada en host de terceros(antiwalmare,)
~~~



##### Tabla de enrutamiento
~~~
Una tabla de enrutamiento contiene una serie de reglas, llamadas rutas, que se utilizan para determinar la dirección del tráfico de red. Cada subred de una VPC debe estar asociada a una tabla de enrutamiento. La tabla controla el enrutamiento de la subred. La subred solo puede asociarse a una tabla de enrutamiento; 
*no obstante, puede asociar varias subredes a la misma tabla de enrutamiento.
* cuando creo mi subnet se crean tablas de enrutamiento por defecto, si quiero una subnet publica, debo definir una regla que establezca conexion al internet gateway
*permiten el trafico GATEWAY (nat, internet,s3gateway)

*Para usar Internet Gateway, la tabla de enrutamiento de la subred debe contener una ruta/regla que dirija el tráfico de Internet a la puerta de enlace de Internet. Si una subred está asociada a una tabla de enrutamiento que tiene una ruta hacia una puerta de enlace de Internet, se la conoce como public subnet (subred pública).


https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html
~~~

##### Lista de control de acceso de red (ACL de red ) opcionales,sin estado
~~~
Una lista de control de acceso de red (ACL de red) es una capa de seguridad opcional para una VPC. Actúa como un firewall sin estado para controlar el tráfico entrante y saliente de una o más subredes.
*estan ligadas solo a nivel de subred
*se ejecutan en orden correlativo
*las reglas que tienen mayor prioridad son las que deniega 
*debo establecer si o si las reglas de salida y entrada (predeterminadamente permite todo el trafico entrante y saliente)
*definen o deniegan el trafico dentro y fuera de las subredes 
*si el grupo de seguridad permite el trafico por el puerto 80, tambien tiene que definirlas en las ACL, sino sera denegado
*las reglas con asterisco(*) son las ultimas en ser evaluadas 
~~~

##### Grupos de seguridad (obbligatorio)
~~~
Un grupo de seguridad es un firewall virtual con estado que controla el tráfico de red entrante y saliente hacia los recursos de AWS y las instancias EC2.
*La VPC tiene un grupo de seguridad por defecto ,deniega todas las reglas entradas,acepta todas las salidas 
*las reglas se evaluan antes de recibir trafico
*con estado

https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html
~~~

#### Host bastion 
~~~
Proporciona acceso de subred publica a subred privada (inicio de sesion en la instancia privada via bastion)
Quien se conecte tiene la clave privadas, no almacenarla en el host bastion por seguridad!!
*como buena practica renovar las claves constantemente 
Un servidor bastión (también conocido como Jump Box) es una instancia de Amazon EC2 en una subred pública que se configura de forma segura para brindar acceso a los recursos de una subred privada. Los operadores de sistemas se pueden conectar al servidor bastión y, luego, jump into (pasar a) los recursos de la subred privada.
~~~


#### GATEWAY privada virtual ?? 
~~~
para conexiones de VPN desde un centro de datos corporativo 
se hace la conexion entre el gateway de cliente y gateway privada virtual
~~~

###  Amazon Elastic Compute Cloud (AWS EC2) 
~~~
Amazon EC2 proporciona servidores virtuales, también llamados instancias , que pueden hacer casi todo lo que puede hacer un servidor local. Cuando lanza una instancia EC2, dos parámetros que debe especificar son:
	1. Un tipo de instancia : este parámetro especifica las características de rendimiento de la CPU, la memoria, el almacenamiento y la red de la instancia. El tipo de instancia a menudo se denomina tamaño de la instancia.
	2. Una imagen de máquina de Amazon (AMI) : este parámetro define el software inicial y el sistema operativo (SO) para la instancia. Hay muchas opciones disponibles para sistemas operativos y software preinstalado.
		Beneficios : capacidad de repeticion/reutilizacion/recuperacion
	3.Especificar la configuracion de red : Identificar VPC y/o subred donde se implementara y asigne IP publica si necesita acceso a internet
	4.Rol IAM (opcional): necesita adjuntar un rol de iam adecuado si va a interactur con otros servicios de aws(por ej rol que concede permisos de acceso a un bucket de S3)
	5.script de datos de usuario (opcional): utilice para personalizar el entorno en tiempo de jecucion de la instacias
	6.Especificar almacenamiento : volumen raiz y volumenes de almacenamiento adicionales
		opciones de almacenamiento:
			Amazon Elastic Block Store (AWS EBS) -> persiste esta info , si se apaga y prende una instancia (EBS es un servicio de almacenamiento en bloque fácil de usar, escalable y de alto rendimiento)
	Intance store -> se pierde la info si se apaga y prende una instancia (Instance store son ideales para almacenar datos temporales, especialmente si estos cambian frecuentemente)
		
	7.Etiquetas/tags
	8.Grupo de seguridad : conjunto de reglas de firewall que controlan el trafico a la instancia , creacion de reglas de entrada y salida especificando el puerto y el protocolo 
	9. par de claves: en el lanzamiento se especifica o se crea , consite en una clave publica que almacena aws y un archivo de clave privada que uno almacena y estas permiten la CONEXION segura a la instancia 
	
** Si inicialmente elige un tipo de instancia que tiene poca o demasiada potencia para su aplicación, puede cambiar el tipo de instancia más fácilmente que cambiar un servidor local.
Una instancia EC2 se puede comprar de cuatro maneras:
	1. Instancias bajo demanda : pague solo por lo que usa, sin compromisos.
	2. Instancias al contado: pague por instancias EC2 no utilizadas, sin compromisos. Puede ahorrar hasta un 90% en costos en comparación con las instancias bajo demanda.
	3. Instancias reservadas : Reserve una instancia EC2 por 1 año o 3 años, con varios niveles de ahorro. (Nota: si planea usar un servidor durante mucho tiempo, es decir, más de 1 año, este tipo de compra es la mejor opción).
	4. Host dedicado : ejecute instancias EC2 en hardware dedicado a un solo cliente
	
** 169.254.169.254 -> para cada instancia se brinda un servicio de meta data en la sig direccion ip  169.254.169.254
** si la intsnacia se reincia no cambia la ip, cuando apagamos y prendemos si 

** las ip siempre son dinamicas, cuando ocupamos una ip elastica(estatica)?, cuando queremos apagar y prender una instancia y no queremos que se cambie la ip 
* hibernacion de una instancia, el sistema op guarda toda la info en memoria (asignamos ip elastica), por la instancia hibernada no pagamos pero todo lo que almacena en el disco ebs si se cobra, requisistos para hibernar una instancia
	1.habilitar la hibernacion en el moemnto del lanzamiento / tipo de instancia compatible3.
	
RE LANZAMIENTO DE UNA INSTANCIA
Cuando hay mucho trafico en la red, cuando necesitamos una instancia mas pequeña, cuando el hadware necesita algun cambio,(para tamaño/ parches) vamos a necesitar lanzar una instancia desde 0, es imaportante diseñar instancias, todo lo que ira dentro en los user-script y la ami y asi no se pierde nignuna configuracion
* cuando transicionamos a un nuevo tamaño de instancia , primero tenemos que apagarla para cambiar el tamaño

** AMI, y su obsolencia, amazon mantiene las que ya estan en uso, pero ya no se puede crear mas instancias con esta ami (como buena practica se recomienda tener una misma ami para todas la instancias y asi tener la misma configuracion )
* actualizacion de ejecuacion de EC2, Sistem manager permite manejar muchas instancias a la vez, ocupamos un solo comando para podr actualizar todas la instancias  

Qué método debería usar?

Lanzar desde la Management Console cuando necesite lanzar con rapidez una instancia temporal o única.
Lanzar con un script cuando deba automatizar la creación de una instancia de forma repetida y confiable.
Lanzar con CloudFormation cuando desee lanzar recursos relacionados en conjunto.
~~~



#### Cloud adoption framework (AWS CAF)
~~~
ayuda a las organizaciones a desarollar planes eficiente  y eficaces,tambien orientar y dar buena practicas para crear un buen enfoque en la nube y su proceso de 
actores para definir los objetivos 
**se organiza en 6 perspectivas y son capacidades 
	enfoque empresarial(orientado a la e/arquitectos empresariales )
		1.empresa -> con que contamos para soportar la tecnologia de la e 
		2.personas-> priorizar capacitacion para desarrollar organizacion agil  
		3.gobernanza -> darle continuidad a cualquir proyecto / riesgos empresariales (prince2, SaFe, OKRs)
		
	enfoque tecnico(arquitectos y administradores TI)
	1.plataforma -> entender y comunicar las naturaleza de los sitemas informaticos 
	2.seguridad -> como aseguramos las platafoormas/asegurarque la org cumpla obj de seguridad  
	3.operaciones -> cuales son la operaciones/acciones que se ejecutan para que las plataformas/negocio puedan seguir funcionando, definimos como se llevaran a cabo os negocios diarios 
~~~


#### AWS systems Manager:  
~~~
Es un conjunto de capacidades que ayudan a administrar las aplicaciones y la infraestructura que se ejecutan en la Nube
session manager: administracion/gestion de instancias, queda registrado en cloud trail, no hay que establecer puerto ni concecciones de grupos 
#### patch manager: 
maintenance windows : programar periodos para ejecutar tareas administrativas y de mantenimiento en las instancias
state manager : administrador de estados -> mantener una configuracion uniforme d elas instacias de amazon EC2 (documento json con acciones que esten definidas para controlar las inslacias , pasos y parametros definidos )
inventory : recopila informacion acerca de las instancias y del software instalado en ellas 
insights : panel de informacion es una muestra de datosoperativos para cada recurso (Cloudwatch Dashboard)
~~~



#### PROTOCOLOS networking
~~~
Protocolo Secure Shell (SSH) es un protocolo que abre una interfaz de línea de comandos (CLI) segura en una computadora remota Linux o Unix.
Protocolo de transferencia de hipertexto HTTP es el protocolo que se utiliza para llegar a las páginas web. Una dirección HTTP completa se expresa como un localizador uniforme de recursos (URL).
TCP/IP es un protocolo orientado a la conexión. Define cómo establecer y mantener las comunicaciones de red donde los programas de las aplicaciones pueden intercambiar datos. Los datos que se envían a través de este protocolo se dividen en fragmentos más pequeños denominados paquetes.
HTTP:80
HTTPS:443
FTP:21
SSH:22
DNS:52
*protocolo de transporte TCP
~~~

#### BIBLIA CLI comandos 
https://docs.aws.amazon.com/cli/latest/reference/index.html
~~~
Para acceder desde la CLI 
Putty 
par de claves de acceso 
ip publica cuando te conectas desde afuera 
ingresar con ec2-user

** CONEXIONES, si no puede hacer la conexion por ssh verfique que el grupo de seguridad tenga habilitada una regla de entrada el puerto 22 (ssh) , lo mismo si quiere sacarlo a la web, debe habilitar el puerto 80 (htttp)
~~~





#### Escalamiento VERTICAL/HORIZONTAL
~~~
ESCALABILIDAD:  los sistemas exitoso y en crecimiento a menudo ven un aumento en la demanda. Un sistema que es ESCALABLE puede adaptarse para cumplir con este nuevo nivel de demanda 
ESCALABILIDAD VERTICAL : la capacidad de uns sitema para crecer aumentando rendimiento (hadware: RAM/CPU) a un servidor
ESCALABILIDAD HORIZONTAL : la capacidad de un sistema para crecer agregando computadoras adicionales con las mismas caracteristicas 
ELASTICIDAD : capacidad de adquirir recurso cuando los necesite y liberarlos cuando ya no los necesite , *automatizacion 
~~~



#### AWS cloudfront
~~~
Servicio que brinda una manera fácil y rentable de distribuir contenido con baja latencia y altas velocidades de transferencia de datos ( gracias al almacenamineto en cache)
Es una buena opción para la distribución de contenido estático de acceso frecuente
alto nivel de transferencia de datos atendiendo solicitudes utilizando una red de ubicaciones de borde en todo el mundo.
~~~


#### Amazon Storage Gateway
~~~
Almacenamiento hibrido, queme permite que suus aplicaciones locales utilicen el almacenamiento en la nube .Podemos ocuparlos para copias de seguridad y archivaado, recuperacion ante desastre, procesamiento de datos en la nube, migraciones 
Concepto PUENTE: conexion entre la aplicacion en la instalaciones(VM, NFS,SMB,ISCSI) y la nube a traves de AWS Storage Gateway

*La gateway se conecta a servicios storage S3, S3glacier,EBS

Proporciona tres tipos de soluciones/almacenamiento en AWS 	
	Archivo/volumen/cintas

Casos de uso ?
	tres casos practicos clave de nube hibrida 
	-mueva copias de seguridad y archivos a la nube
	-Reduzca el almacenamiento local con recursos compartidos de archivos respaldados por la nube
	-da a al app en las instalaciones acceso de baja latencia a los datos almacenados en aws
	
Sttorage Gateway se configura ne las instalacion y lo vinculo el entorno local a la nube de aws 



~~~


#### AWS Well-Architected Framework
~~~
AWS Well-Architected Framework describe los conceptos clave, los principios de diseño y las prácticas recomendadas de arquitectura para diseñar y ejecutar cargas de trabajo en la nube. 
	Excelencia operativa / Operational excellence:El pilar de la excelencia operativa se concentra en ejecutar y monitorear los sistemas y en mejorar constantemente los procesos y los procedimientos. Entre los temas clave se incluyen la AUTOMATIZACION de cambios, la respuesta a eventos y la definición de estándares para administrar las operaciones diarias.
	Seguridad : El pilar de la seguridad se concentra en proteger la información y los sistemas. Entre los temas clave se incluyen la CONFIDENCIALIDAD y la INTEGRIDAD DE LOS DATOS , la administración de los permisos de usuarios y el establecimiento de controles para detectar eventos de seguridad.
	Fiabilidad/ CONFIABILIDAD /. Reliability : El pilar de fiabilidad se centra en las cargas de trabajo que realizan las funciones previstas y en cómo recuperarse rápidamente de los errores para cumplir con las demandas. Entre los temas clave se incluyen el diseño de sistemas distribuidos, la planificación de la recuperación y cómo adaptarse a los requisitos cambiantes.
	Eficiencia/eficacia del rendimiento / . Performance eciency: El pilar de eficacia del rendimiento se centra en la asignación estructurada y simplificada de TI y en los recursos informáticos. Entre los temas clave se incluyen la selección de los tipos y tamaños de recursos optimizados para los requisitos de la carga de trabajo, la supervisión del rendimiento y el mantenimiento de la eficacia a medida que evolucionan las necesidades de la empresa.
	Optimización de costos / Reliability: El pilar de optimización de costos se centra en evitar gastos innecesarios. Entre los temas clave se incluyen la comprensión del tiempo dedicado y el control de la asignación de fondos, la selección de recursos para el tipo y la cantidad adecuados y el escalado para cumplir con las necesidades de la empresa sin gastos excesivos.
	Sostenibilidad: El pilar de sostenibilidad se centra en minimizar los impactos ambientales de ejecutar cargas de trabajo en la nube. Entre los temas clave se incluyen un modelo de responsabilidad compartida para la sostenibilidad, la comprensión del impacto y la maximización del uso para minimizar los recursos necesarios y reducir los impactos posteriores. 

~~~



~~~
Lightsail??
si hay una aplicacion desarrollada y queremos trasladarla a la nube,
para app medianas 
Beanstalk ??* costo mas bajos
como remplazo de heroku
mediano/grande
~~~

~~~
CLI regio de la instancia en cuestion : curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region 
~~~~
