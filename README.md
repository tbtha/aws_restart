
* apuntes pablo 
* https://pablo-dev.notion.site/pablo-dev/c483bcdd69194cec9b7619596844be98?v=cad8574c8ae3499286c9d27097b038f5

# MIS APUNTES 
#### IDE
~~~
Entorno de desarrollo integrado / Integrated Development Environment
Es una aplicación informática (Software) que proporciona servicios integrales para facilitarle al desarrollador o programador el desarrollo de software  
IDE de AWS  es Cloud9
~~~



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


### BASES DE DATOS
~~~
Elastic Cahche ()
Neptune : determinar relacion entre dos nodos que quieren conectarse (grafos)

~~~

#### AWS Database Migration Service (AWS DMS)
##### AWS SCT(AWS Schema Conversion Tool)
~~~


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
