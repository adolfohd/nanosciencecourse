# Conceptos básicos HYDRA

### Estructura

Ell cluster (hydra) está compuesto de:

* 	Un equipo front-end (16 cores/32 Gb ram) 
* 	Cuatro workers (64 cores/64 Gb ram). 


### Acceso
Tu cuenta para acceder al cluster es:


> user: ahoyos
passwd: ******

Para ingresar al sistema se debe utilizar una conexión VPN. El sofware para realizar esta conexión se puede descargar de: https://openvpn.net/index.php/download/community-downloads.html (Windows, Linux, IOS, Android) o Tunnelblick (https://code.google.com/p/tunnelblick/) para OSX.
Luego de instalado se debe usar el archivo de configuración que se encuentra adjunto a este correo.
El sistema te pedirá el usuario y password para establecer la conexión.

Luego de conectado ya se puede acceder al cluster.

El cluster se accede a través de ssh, haciendo:

```
  ssh ahoyos@hydra
```

ó
```
  ssh ahoyos@192.168.10.10 (En caso que el nombre hydra no lo conozca)
```
Se puede utilizar *Putty* en windows para realizar la conexión.

Para transferir archivos se puede hacer por medio de *sftp, scp o wget*.

#### Configuración de acceso rápido

Para guardar la dirección IP de Hydra en los hosts conocidos de la máquina, agregar una línea al final del archivo /etc/hosts:

```
192.168.10.10		hydra 
```
Además, para no requerir de contraseña cuando se haga login, se puede generar una llave privada:

```
ssh-keygen -t rsa -C <usuario>@hydra
```

y agregarla a hydra:

```
ssh-copy-id <usuario>@hydra
```

esto hace que se pueda acceder fácilmente a hydra así:

```
ssh <usuario>@hydra
```

### Módulos

El sistema trabaja con el modelo de módulos, los cuales configuran el software que se requiera (dependiendo del software que se encuentre disponible). 

Para ver el software disponible a través de los módulos se puede ejecutar: 

```
  $ module avail
```
Para cargar alguno de los módulos:
```
  $ module load nombre_del_modulo
```
Para listar los módulos que están cargados en esta sección:
```
  $ module list
```
Mayor información para manejo de módulos se puede encontrar en: http://brazos.tamu.edu/docs/modules.html

#### SLURM: Delegación de tareas

El cluster cuenta con un sistema de administración de recursos llamado SLURM. Para ejecutar programas en el cluster se usa el comando 'srun', y para encolar un trabajo usar 'sbatch'.

Por ejemplo, el siguiente comando ejecuta el programa sleep con parámetro 100 segundos usando un solo procesador: 
```
   srun sleep 100 &
```
Para ejecutar un programa en múltiples procesadores (4 en este caso) usar:
```
  srun -n 4 sleep 100 &
```
Para verificar la cola de ejecución se usa el comando: squeue

Mayor información sobre la ejecución de programas se puede encontrar en: https://rc.fas.harvard.edu/resources/running-jobs/

Cualquier duda me comentas,

>  Antal A. Buss
  Director de Carrera
  Ingeniería de Sistemas y Computación
  Pontificia Universidad Javeriana - Cali
  Calle 18 No. 118-250, Av. Cañasgordas
  Tel: +57 (2) 3218200 ext 8804
  abuss@javerianacali.edu.co
  Cali, Colombia.
