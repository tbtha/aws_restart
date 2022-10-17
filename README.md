* apuntes pablo 
* https://pablo-dev.notion.site/pablo-dev/c483bcdd69194cec9b7619596844be98?v=cad8574c8ae3499286c9d27097b038f5

# MIS APUNTES 
#### IDE
~~~
Entorno de desarrollo integrado / Integrated Development Environment
Es una aplicación informática (Software) que proporciona servicios integrales para facilitarle al desarrollador o programador el desarrollo de software  
IDE de AWS  es Cloud9
~~~

#### CLOUD
~~~
¿Qué es la computación en la nube? 
La computación en la nube es la entrega  bajo demanda de recursos de TI en línea, con precios de pago por uso

Tres modelos de computación en la nube
	Infraestructura como servicio (IaaS) : el proveedor de la nube ejecuta el  hardware  y el software de virtualización . Usted aprovisiona y administra sus servidores virtuales y todo el software que está instalado en ellos.

	Plataforma como servicio (PaaS) : el proveedor de la nube ejecuta y administra el hardware , el software de virtualización y los servidores virtuales . Solo necesita implementar su aplicación y sus datos.

	Software como servicio (SaaS ): el proveedor de la nube  ejecuta y administra todo , desde el hardware hasta la aplicación. Solo necesita suscribirse a la aplicación para usarla

Tres modelos de implementación en la nube
	All-in cloud :Todo en la nube : todas sus aplicaciones se implementan completamente en la nube.
	Hybrid : Híbrido : algunas de sus aplicaciones se implementan en la nube, pero otras permanecen en las instalaciones. Las aplicaciones aún pueden conectarse entre sí.
	Privete cloud : (on-premises) : Nube privada ( instalaciones) : todas sus aplicaciones se implementan completamente en una infraestructura de nube que se ejecuta en su propio centro de datos.

Ventajas:
+ Gasto de capital a gasto variable : no es necesario pagar por adelantado los activos físicos que necesita. En su lugar, paga sobre la marcha por los recursos que utiliza.
+ Economías de escala : obtenga un costo variable más bajo para los recursos que el que puede obtener por su cuenta. Por ejemplo, como proveedor de servicios en la nube, AWS le transfiere ahorros a medida que crece.
+ Planificación de la capacidad : reduzca el suspenso sobre sus necesidades de capacidad.
+ Velocidad y agilidad : aprovisione recursos de forma rápida y bajo demanda.
+ Gaste estratégicamente : gaste dinero en sus proyectos comerciales en lugar de administrar centros de datos
+ Facilidad de implementación : Globalícese en minutos.

*El modelo de precios de AWS se basa en el principio de que paga por lo que usa .
~~~

##### Acceso a los servicios:
~~~
Consola de administración de AWS : una aplicación basada en web o móvil para administrar sus servicios de AWS
Interfaz de línea de comandos de AWS (AWS CLI) : una herramienta de línea de comandos para administrar sus servicios de AWS
Kits de desarrollo de software (SDK) : un conjunto de herramientas de software (como bibliotecas, recursos y muestras) que un desarrollador puede usar en un programa para acceder a los servicios de AWS.
~~~

#### Términos clave de la infraestructura de AWS
~~~
REGIONES : areas geograficas aisladas,atraves de las regiones podemos acceder a los servicios de aws, una region  se compone de dos o más zonas de disponibilidad

ZONAS DE DISPONIBILIDAD: uno o mas centros de datos discretos que que están diseñados para el aislamiento de fallas suficientemente cerca para una latencia baja( tiempo de solicitud y recepcion del contenido) y suficientemente lejos para reducir los riegos de desastres en un conjunto de zonas de disponibilidad, se recomienda dejar nuestros recursos en dos zonas de disponibilidad, para garantizar la alta disponibilidad 

UBICACION DE BORDE / UBICACION PERIFERICA : para poder crear copias de la informacion para tenerlas mas cercnas a os clientes y asi reducir la latencia, aws para no crear regiones en absolutamente todo elmunod, crea pequeñas infraestructuras, las "ubicaciones pefirericas" (cloudfront, red de entrega de contenido que permite hacer la copia de la info que esta en una region hacia estas ubicaciones perifericas )  

 Que tomar en cuenta para elegir una region ?
Requirimientos legales/Restriciones geograficas para almacenas datos, impedimentos que requiera desplegar los recursos en cierta region (si los datos requieren estar en latinoamerica, lo mejor seria la region de sao paulo)
cercania con tus clientes : donde estan tus bases de cliente ? conviene estar en una region cercana a los clientes para reducir la latencia que existiria entre las peticiones y los recursos
servicios disponibles : no hay los mismo servicios en todas las regiones al mismo tiempo, los servios nuevo generalmente estan disponibles en la region de virginia (para pruebas, virginia es la region que selccionaria )
precios : por la forma de estuctura fiscal en brasil por ej. es mas caro

~~~


### AMAZON VPC
~~~
Amazon Virtual Private Cloud (Amazon VPC) es un servicio que puede utilizar para aprovisionar una sección de la nube de AWS aislada lógicamente, que sedenomina nube virtual privada o VPC
podemos crear una red definida de forma personalizada en la nube de AWS 
Amazon VPC es un servicio básico de AWS comprender e implementar permitira hacer uso con muchos servicios de AWS.
Una VPC:
	Está dedicada a una cuenta de AWS
	Pertenece a una sola región de AWS
	Puede abarcan varias zonas de disponibilidad
	Está aislada lógicamente de otras VPC
Puede crear varias VPC en una cuenta de AWS para separar los entornos de redes
Puede crear subredes en una VPC
EL intervalos de direccion IP de un VPC se define mediante un bloque CIDR
SUBRED 
	Una subred es un segmento de un intervalo de direcciones de VPC. Puede lanzar servicios de AWS en una subred
	*Se puede acceder a una subred pública desde la VPC y desde Internet.
	*Solo se puede acceder a una subred privada desde la VPC y no se puede acceder a ella desde Internet
	*la subnet permite dividir la VPC y debe pertenecer unicamente a una zona de disponibilidad, una subred publica su principal caracteristica es que esta conectada a internet gateway
	*si no especifico un grupo de seguridad al momento de lanzar la intancia, aws le asocia el grupo de seguridad de la vpc
	*grupos de seguridad funcionan a nivel de computo
	*
	
______VPC
VPC es una red suministrada en una seccion aislada logicamente de aws 
Cuando creamos VPC definimos un bloque de IP con notacion CIDR(podemos tener un bloque de direcciones IP primario y 4 segundario )
Cuando utilizamo IPV6, amazon proporciona las direcciones IP

aws ec2 create-vpc --cidr-block 10.0.0.0/16

Direcciones IP reservadas de amazon VPC: (10.0.0.0/16)
primera direccion -> direccionamiento 
10.0.0.1 -> reservada por aws para direccion de enrutador de VPC
10.0.0.2->
10.0.0-3 -> reservada para futura utilizacionn de aws
10.0.0.255 -> direccion de difusion de red 

____SUBREDES Y TABLAS DE RUTEO EN VPC
creo subredes para separar logica(? (desarollo/producion/etc) hasta 200 subredes por VPC
bloques de direccione IP 
minimo /28
maximo /16
IPV6 -> puedo segmentar mi red /64

ENRUTADOR : instancias dentro de distintas subredes se puede conectar gracias a las reglas de las tablas de enturtamiento

*al crear la subred defino si quiero asignar automaticamnte la IP pblica lo hacemos mediante un check -asignar automaticamnte una IP publica (debe estar toda la configuracion/conexion de la tabla de ruteo/internet gateway para que si sea una ip publica) (cuando defino que mi ip es publica, recordar habilitar la opcion de "habilitada" en las setting de subnet, por defecto esta "desabilitada")

*cuanndo creo una instanciaaa tengo una nic primaria siempre (tambien puedo tener asociada nic2 y nic3)( nic -> interfaz de red elastica)

*VPC predetermina de la cuenta, no es recomendada para gestionar nuestras app

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


#### Amazon Simple Storage Service (AWS S3)
~~~
Solucion administrada de almacenamiento en la nube
Los datos se almacena como objetos en buckets
diponibilidad y durabilidad

Costos dependen de:
	tipo de clase de almacenamiento
	cantidad de almacenamiento (cantidad y tamaño de los objetos)
	solicitudes (numero y tipo de solicitudes )
	transferencia de datos (se cobran cargos por los datos salientes )	
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

### Redes :
~~~
Direccione IP : direccion unica que identifica un dispositivo o rcurso en internet o dentro de una red local (identificador que permite enviar info entre dispositivos en una red) 
CIDR   
**Subnet publica sale a internet atraves de Internet Gateway
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

curl 169.254.169.254/latest/user-data






#### Elastic Beanstalk (Servicio de computo (PaaS)) (computo)
~~~
Permite implemetar, escalar y administrar aplicaciones web con rapidez, tomar codigo, cargarlo y elastic se encarga de desplegar el codigo, mantiene el control de todos los recursos de mi app
compatible con go, java SE, node js, php, python y demases
elastic es gratuito, solo se paga por lo servicios subyacentes como ec2, rds, balanceador de carga, etc
~~~




#### Escalamiento VERTICAL/HORIZONTAL
~~~
ESCALABILIDAD:  los sistemas exitoso y en crecimiento a menudo ven un aumento en la demanda. Un sistema que es ESCALABLE puede adaptarse para cumplir con este nuevo nivel de demanda 
ESCALABILIDAD VERTICAL : la capacidad de uns sitema para crecer aumentando rendimiento (hadware: RAM/CPU) a un servidor
ESCALABILIDAD HORIZONTAL : la capacidad de un sistema para crecer agregando computadoras adicionales con las mismas caracteristicas 
ELASTICIDAD : capacidad de adquirir recurso cuando los necesite y liberarlos cuando ya no los necesite , *automatizacion 
~~~


#### AMAZON ROUTE 53, convierte tu ip(del balanceador) en un "nombre"/endpoint (elb-mybalancer.aws.com), el balanceador de carga debe tener la ip publica y se conecta a las instacias que deben estar privadas(route53 envia una peticion a "elb-mybalancer.aws.com" a elastic load y asi se conecta a las intancias y envia la peticion a la instancias que corresponda )


#### AWS Elastic Load Balancing (ELB) 
###### Balanceador de carga 
~~~
Distribuye solicitudes entre instancias y aumenta la disponibilidad 
Beneficios:
	SEGURO
	DESACOPLE
	TOLERANCIA A ERRORES (tabaja a nivel de la app en general( se encarga que las instancias estan "bien", si hay algun error en la instancias la elimina y crea otra igual, que me permite trabajar)
	EXPANSIVO aumenta la elasticidad y escalabilidad
	
Elastic Load Balancing distribuye automáticamente el tráfico entrante de aplicaciones entre varias instancias de Amazon EC2. Le permite lograr tolerancia a fallos en sus aplicaciones al proporcionar sin problemas la cantidad necesaria de capacidad de equilibrio de carga necesaria para enrutar el tráfico de aplicaciones.

TIPOS:
	Balanceador de carga de RED, capa 4? protocolo tcp, en los dispositivio IOT, sensores que trasmiten informacion 
		si necesito un app que tenga un rendimiento extremo, maneja solucitudes repentinas a gran velocidad 
	Balanceador de carga de APLICACIONES, capa 7? protocolo HTTP permite trabaja a nivel de app web, tiene la capacidad de recepcion mas lenta que el de red 
		direccionamiento basado en rutas y host /home / contact
	Balancador de carga clasico, esta deprecado 
		habilitamos sesiones pegajosas(? para que el usuario que se le cayo en net, y queremos que vulva a conectarse a la misma instancia para que su carrito vuelva a tener la misma info

 **en un balanceador de carga hay agentes de escucha que clasifica grupos de destino y  en esos grupos hay comprobacion de status
Receptores/AGENTES DE ESCUCHA/listener dentro del balanceador de carga 
proceso que define el puerto y protocolo con el que escucha el balanceador de carga 
cada balanceador necesita al menos un agente de escucha para aceptar el trafico y hasta 50 
las REGLAS de direccionamiento se definen en los agentes de escucha (una regla como minimo)

~~~

#### AMAZON EC2 Auto Scaling
~~~
Grupo de Amazon EC2 auto scaling, (escalamiento horizontal) permite lanza o terminar una cantidad de instancias determinada cuando sea necesario (cuando no hay tanta demanda quiero 2 instancias pero para un cyber necesito 15 instancias, cuando una instancia esta sobrecargada, automaticamente se crean mas instancias ), si no ocupo auto scaling tendria que hacerlo manual , (en base a reglas por ej si se esta al 70% de la instancia, se crea otra instancia y asi sucesivamente )

Necesita una plantilla de lanzamiento(AMI, tipo de intancia,VPC, grupo de seguridad,almacenamiento, par de claves,datos de usuario ,tags)
Permite la configuracion de las politicas de escalado y tamaño del grupo de instancias Ec2, no escala de forma infinita, hay que establecer el limite 
->Auto Scaling le ayuda a mantener la DISPONIBILIDAD de las aplicaciones y le permite escalar su capacidad de Amazon EC2 hacia fuera o en función de las condiciones que defina. Podemos utilizar Auto Scaling para asegurarse de que está ejecutando el número deseado de instancias de Amazon EC2.
->Auto Scaling también puede aumentar automáticamente el número de instancias de Amazon EC2 durante los picos de demanda para mantener el rendimiento y disminuir la capacidad durante las paradas para reducir los costes.
->Auto Scaling es adecuado para aplicaciones que tienen patrones de demanda estables o que experimentan variabilidad horaria, diaria o semanal en el uso.
** Hay que establecer la misma VPC par autoScaling y las intancias 
**Integracion con Elastic Load Balancing 

politicas: como activar politicas? puedo configurar alarmas en CLoudWatch 
como validamos que las instancias esten sanas ?, es saber si las intancias funcionan como corresponde  aws autoscaling set-intance-health 
politicas de terminacion : define qe instancia se termina con el escalado descendentes /1.balancear las zonas de disponibilidad y lugo ya hay diferentes opciones 
Creacion de un grupo de estado estable : configurar unn grupo de amazon Ec2 autoscaling con los mismos valores minimos, maximos y deseados 
** Escalado dinamico : Amazon EC2 /escalado de siguimiento de objetivo(aumenta o reduxca la capacidad en funcion de un valor en base a una metrica )/ escalado por pasos(aumenta o reduce la capacidad segun ciertos pasos if/else)/ escalado simple(aumente o reduzca la capacidad en funcion de un unico ajuste de escalado) 
** Escalado predictivo : Amazon EC2 / escala de forma automatica en base a predicciones de Ec2, tambien se establece un maximo de escalamiento 

****** ALGO QUE FALLA UNICAMENTE AL CREAR UNA INTANCIA ES LA AMI, SI SE CREA Y FALLA DEBE SER OTRA COSA ******

~~~



#### AMAZON ROUTE 53 
##### (SERVICIO GLOBAL(AL IGUAL QUE IAM))
~~~
"convertir" el ip a un nombre de dominio ,route 53 cobra por el 
Cree un registro CNAME que apunto al balanceador de carga 
Politicas de direccionamiento ->  es el primer punto de contacto/entrada cuando queramos acceder a un recurso  / direccionamiento ponderado / de latencia / conmutaccion de error 
**** LOAD BBALANCER balancea las cargas operativas de la instancias 
**** ROUTE 53 balancea en funcion a politicas muhco mas amplias
-> blue/green deploy : cuando tenemos 2 versiones de un sistema y queremos probar que la segunda version funcione bien , debemos implementar blue(version1) y green(version2) , ROUTE 53 balancea de apoco, enviando el 100% del trafico al sistema blue y gradualmente empieza a enviarlo al sistema greend
 
~~~

#### CONTENEDORES  
##### Elastic Container Registry (Amazon  ECR) / Elasticc Container Service (Amazon ECS) / Amazon Elastic Kubernetes (amazon EKS) / AWS Farget
~~~
Docker contenedores / administrar infrestructura, https://kodekloud.com/courses/docker-for-the-absolute-beginner/
ECS, EKS, Fargate -> contenedores en AWS

Como crear contenedores: 
Docker es  una plataforma que nos permite crear (sofware empaquetado) , probar, implementar,ejecutar contenedores

como se ve docker en AWS Amazon:
Elastic Container Registry (Amazon  ECR) : registro de contenedores ADMINISTRADO que facilita (creacion de IMAGENES)()
Elasticc Container Service (Amazon ECS) : servicio de contenedores altamanete escalable y de gra rendimiento (es compatible con los contenedores de docker, puedo ocupar una imagen alojada ahi )
** tareas son epecificas de ECS 
kubernetes : software de codigo abierto para el aprovisionamiento y la administracion de contenedores  
Amazon Elastic Kubernetes (amazon EKS) : (orquestador que contenedores) aprovisiona un cluster, tiene nodos de trabajo,
AWS Farget : tecnologia que permite EJECUTAR contenedores sin tener que administrar servidores ni cluster (no hay que administrar infraestuctura)(administrador de contenedores serverless) 

** contenedor es un pedazo del sitema operativo, podemos transportar a 
** maquina virutal es harward y tiene el sitema operativo completo visrtualizado. dentro de una intancia pueden haber varios contenedores 

** cluster : conjunto de contendores
~~~


#### Lambda AWS(computo)
~~~
para que utilizamos lamba? para tareas especificas que no requiere estar activa todo el timepo, cada vez que se invoca una funcion es que se ejecuta 
servicio administrado de AWS / invocacion basada en eventos / el timepo de ejecucion de una funcion se limita a un maximo de 15min / admite varios lenguajes 
Lambda le permite al codigo ejecutarse sin aprovisionamiento (tiene  de invocaciones gratuitas)
*** TODO LO SERVERLESS SE PAGA POR LO QUE SE USA SOLAMENTE
~~~


#### APIS

### BASES DE DATOS
~~~

dependiendo de lo que quiero es el servicio que elijo
RDS (transacionales) para lecura y escritura (JOIN para hacer relaciones entre tablas )
DinamoDB (transacioales)
Redshif :analizar datos de forma masiva / analisis de grandes volumenes de informacion 
Elastic Cahche ()
Neptune : determinar relacion entre dos nodos que quieren conectarse (grafos)
Aurora: 
~~~

#### Aamazon Relational Database Service (Amazon RDS) (transacional)
~~~
Facilita las tareas de configuración, operación y escalado de una base de datos relacional en la nube. Proporciona una capacidad rentable y de tamaño modificable, al mismo tiempo que permite gestionar las tareas de administración de base de datos que requieren mucho tiempo, lo que permite centrarse en las aplicaciones y el negocio. Amazon RDS le ofrece seis motores familiares de base de datos entre los que elegir: Amazon Aurora, Oracle, Microsoft SQL Server, PostgreSQL, MySQL y MariaDB.

*creamos un grupo de seguridad para permitir que su servidor web acceda a la instancia de base de datos de RDS. El grupo de seguridad se utilizará al lanzar la instancia de base de datos.
*creamos un grupo de subredes de base de datos que se emplea a fin de informar a RDS acerca de qué subredes se pueden utilizar para la base de datos. Cada grupo de subredes de base de datos requiere subredes en al menos dos zonas de disponibilidad.
*Las implementaciones Multi-AZ de Amazon RDS proporcionan mejoras en la DISPONIBILIDAD y la DURABILIDAD de las instancias de base de datos, lo que las hace adecuadas para las cargas de trabajo de bases de datos de producción. Cuando aprovisiona una instancia Multi-AZ de base de datos, Amazon RDS crea automáticamente una instancia de base de datos principal y, de forma sincronizada, replica los datos a una instancia en espera en una zona de disponibilidad diferente.
~~~
#### DynamoDB (no relacional)
~~~
Tablas globales de amazon dynamoDB un beneficio de usar dynamo es que permite tener una repilicar enlas regiones que necesitamos , las ocupamos cuando necesitamos rendimiento en nuestras app
~~~

#### Redshif : es una servicion de almacenamiento de datos administrado 
~~~
que es una almacen de datos? 
como funciona ? puede contener varias bases de datos, y se pueden eoganizar las tablas en esquemas
como esta compueto ? la arquitetcura esta compuesta por 3 niveles base de datos en si, analisis, y frontend que presenta los resultados
que es Redshif ? nos permite hacer analisis de grandes voluemntes de info, es administrado por aws
como procesa los datos ? el procesamiento es paralelo, dos o mas microprocesadores separan programas y ejecutan tareas en forma simultanea
cuando lo ocupamos ? situacione empresariales, big data, softare como servicio,
~~~ 


#### Amazon Aurora
~~~
Motor de base de datos compatible con MySQL y PostresSQL
Esta contruida para la nube y aprovecha todo los beneficios, tambien funciona con RDS
Esta conformada por clusteres 
Caracteristicas : Simple y compatible
		  Pago por uso 
		  Servicio gestionado, funciona con servicios como Database Services
		  Tolerante a fallos, replica para copias de seguridad 2 veces dentro de 3 zona de disponibilidad  
		  Alto rendimiento y escalabilidad de almacenamiento 
		  Alta disponibilidad y durabilidad 
Cuando crea una instancia Amazon Aurora, crea un cluster de base de datos 
Un cluster de base de datos aurora se compone de una o varias instancias de base de datos y de un volumen de cluster que administra los datos para esas instancias db
Un volumen de cluster es un volumen de almacenamientos d db virtual que abarca varias zonas de disponibilidad 
Hay dos tipode cluster de db :
	cada cluster tiene una instancia primaria de Amazon aurora (lectura y escritura )
	cada cluster de db aurora puede tener hasta un max de 15 replicas de amazon aurora  (lectura)
Si falla la instancia primaria, toma una replica como intancia primaria y cuando se solucionen los errores automaticmanete vuelve a ser la instacia primaria original 
Se recupera en menos de 60 segundos en la mayoria de los casos se reincia la instancia, de esto se encarga aws(todo lo administra aws)
Casos de uso ? aurora podria reducir en un 90% ala vez mejora la fiabilidad y disponibilidad de db , por que no migran aurora? porque requiere de una carga operativa alta 
1.
2.
3.juegos web (alto rendimiento y gran escabilidad de almacenamiento)

** https://www.youtube.com/watch?v=SnCWucCEFLw
** puede estar en un VPC y acceder desde otra VPC (?
~~~

#### AWS Database Migration Service (AWS DMS)
##### AWS SCT(AWS Schema Conversion Tool)
~~~
Permite migrar las bases de datos a AWS de manera rapida y segura 
Con DMS  minimiza el tiempo de inactividad (con sct la migracion es mas acelerada) de la app que dependen de la base de datos , ya que su bd de origen funciona todo el tiempo 
Permite migracion homegeneas y heterogeneas( Oracle a Oracle / Microsoft SQL a Amazon Aurora)
	La migracion homogeneas son de 1 solo paso cuando el esquema de origen y destino son compatibles
	La migracion heteogenea son de 2 pasos ya que la estructura pueden ser muy diferentes,es necesario la transformacion de tipos de datos (AWS Schema Conversion Tool) y luego DMS para la migracion  
ALTA DISPONIBILIDAD en AWS DMS : puede replicar datos de forma casi continua 
AWS DMS puede migrar entre lenguajes de consulta estructurados SQL y noSQL

AWS SCT(AWS Schema Conversion Tool): principalmente convierte el esquema de la base de datos de origen para la migracion de los datos mediante AWS DMS
AWS DMS junto a AWS SCT, me permite convertir el codigo de diferentes motores de plantilla (heterogeneas)
hay casos que son automaticas y otras que son necesarias ser manuales

Replicacion casi continua de base de datos, desde su centro de datos a las bases de datos de aws o en sentido inverso 

COnsolidacion de bases de datos, puedo consolidad varias bases de datos y unificar a solo una(tener en cuanta que puede ser necesario SCT)

COmponenes de AWS DMs : Intancia de replicacion (instancias ec2 que contiene las tareas del dms)/ tareas / origen(es la que queremos traspasar) / destino(instancia de base de datos de la nube) 

Con la implementacion Multi-AZ, una intancia de replicacion de AWS DMS tien un alta disponibilidad y admite la conmutacion por error(si falla la instancia principal, se remplaza) 
aprovisiona y conserva de forma automatica una replica en espera sincronica de la instancias 
~~~

#### AWS cloudfront
~~~
Servicio que brinda una manera fácil y rentable de distribuir contenido con baja latencia y altas velocidades de transferencia de datos ( gracias al almacenamineto en cache)
Es una buena opción para la distribución de contenido estático de acceso frecuente
alto nivel de transferencia de datos atendiendo solicitudes utilizando una red de ubicaciones de borde en todo el mundo.
~~~

#### AWS Organizations
~~~
Ayuda a administrar y controlar su entorno de manera centralizada a medida que crece y escala sus recursos de AWS.
El uso de un entorno de múltiples cuentas es una mejor práctica recomendada al escalar su entorno de nube.
**está disponible para todos los clientes de AWS sin cargo adicional.
~~~

#### Amazon Elastic Block Store EBS (almacenamiento en bloques)
~~~
Proporciona volumenes de almacenamiento persistente
Es un mecanismo de almacenamiento subyacente clave para las instancias de Amazon EC2
Cada volumen , se replica automaticamente dentro de su misma zona de disponibilidad 
Ofrece almacenamiento a nivel de bloques 
Puede utilizar EBS para crear volumenes de almacenamiento individuales y adjuntarlos a una instancias de EC2
* Necesitamos almacenamiento ebs para hibernar las instancias
*Intantaneas /Snapshotp,  imagen que le saca al almacenamiento (permite capturar estados/datos para luego restaurarlo)
TIPOS DE VOLUMENES 
Unidad estado solido 
unidad disco duro

IOPS aprovisionadas(SSD)
se cobra por el importe que aprovisione enIOPS (porcentaje del dia o mes que se utiliza )

lab
Amazon Elastic Block Store (Amazon EBS) ofrece almacenamiento persistente para las instancias de Amazon EC2. Los volúmenes de Amazon EBS están adjuntos a la red y su duración es independiente de la vida de una instancia. Los volúmenes de Amazon EBS tienen un alto nivel de disponibilidad y de confianza, y pueden utilizarse como particiones de arranque de instancias de Amazon EC2 o adjuntarse a una instancia de Amazon EC2 en ejecución como dispositivos de bloques estándar.

Cuando se utilizan como particiones de arranque, las instancias de Amazon EC2 pueden detenerse y, posteriormente, reiniciarse, lo que le permite pagar solo por los recursos de almacenamiento utilizados al mismo tiempo que conserva el estado de la instancia. Los volúmenes de Amazon EBS tienen una durabilidad mucho mayor que la de los almacenes de instancias de Amazon EC2 locales porque se replican automáticamente en el backend (en una única zona de disponibilidad).

Sin embargo, si se quiere aún más durabilidad, con Amazon EBS es posible crear instantáneas uniformes puntuales de los volúmenes, que luego se almacenan en Amazon Simple Storage Service (Amazon S3) y se replican automáticamente en varias zonas de disponibilidad. Estas instantáneas se pueden utilizar como punto de partida para nuevos volúmenes de Amazon EBS y permiten proteger la durabilidad de sus datos a largo plazo. También puede compartirlas fácilmente con colegas y otros desarrolladores de AWS.

~~~

#### Amazon S3 ()
~~~


~~~
#### AWS Identify and Acess Management (IAM)(SERVICIO GLOBAL)
#### AWS Outpost



#### AWS Well-Architected Framework


##### STORAGE
~~~
+S3
+EBS
+EFS
backup
storage gateway
~~~
##### SECURITY,IDENTIFY & COMPLIANCE
~~~
AWS Identity and Access Management (IAM)
AWS Artifact
AWS Audit Manager
Amazon Cognito
Amazon Detective
AWS Directory Service
AWS Firewall Manager
Amazon Cloud Directory
Amazon GuardDuty: se puede utilizar para detectar actividades maliciosas y ayuda a proteger la cuenta 
AWS IAM Identity Center (successor to AWS Single Sign-On)
Amazon Inspector
Amazon Macie
AWS Network Firewall
AWS Resource Access Manager (AWS RAM)
AWS Secrets Manager
AWS Security Hub
AWS Shield
AWS WAF
~~~


~~~
CLI regio de la instancia en cuestion : curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region 
~~~~
