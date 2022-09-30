[![N|Solid](https://pbs.twimg.com/profile_images/1183854219268366336/9SLv5DvR_400x400.jpg)](https://mobile.twitter.com/wwcodeguatemala) 
# _Conectando mis metas con una api de python serverless_
## Solución
A continuación encontrarán el step by step de como crear una API Serverless utilizando AWS:

![N|Solid](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/ddb-crud.png)

## Pre-requisitos
para poder realizar el siguiente demo debes poseer lo siguiente:
- Cuenta activa de aws (Puedes realizarlo con el free tier de aws)
- Tener un conocimiento básico de programación con Python
- Para probar tu API puedes utilizar Postman instalado en tu ordenador (https://www.postman.com/downloads/) 
- Puedes ver el video de como realizarlo aqui:


[![API Serverless](https://img.youtube.com/vi/devsr3JviUw/0.jpg)](https://www.youtube.com/watch?v=devsr3JviUw)
 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Temas
* Paso 1: crear una tabla de DynamoDB
* Paso 2: crear una función Lambda
* Paso 3: crear una API HTTP
* Paso 4: crear rutas
* Paso 5: crear una integración
* Paso 6: conectar la integración a las rutas
* Paso 7: probar la API
* Paso 8: Eliminar

### Paso 1: crear una tabla de DynamoDB
Se utiliza una tabla DynamoDB para almacenar datos para la API.
Cada elemento tiene un ID único, que usamos como clave de partición para la tabla.
Cree una tabla de DynamoDB
1. Abra la consola de DynamoDB en https://console.aws.amazon.com/dynamodb/.
2. Seleccione Create table.
3. En Nombre de la tabla, introduzca toDoList.
4. En Clave principal introduzca id.
5. Seleccione Create (Crear).

### Paso 2: crear una función Lambda
Se crea una función Lambda para el backend de la API. Esta función Lambda crea, lee, actualiza y elimina elementos de DynamoDB. La función utiliza eventos de API Gateway para determinar cómo interactuar con DynamoDB. Para simplificar el proceso, este tutorial utiliza una sola función Lambda. Como práctica recomendada, se deben crear funciones separadas para cada ruta.
Para crear una función Lambda, realice el siguiente procedimiento:
1. Inicie sesión en la consola de Lambda en https://console.aws.amazon.com/lambda/.
2. Elija Create function (Crear función).
3. En Function name (Nombre de función), introduzca toDoListCRUD.
4. Seleccione en Tiempo de Ejecución Python 3.9
5. En Permisos, seleccione Cambiar el rol de ejecución predeterminado.
6. Seleccione Create a new role from AWS policy templates (Crear un nuevo rol en plantillas de políticas de AWS).
7. En Nombre del rol, introduzca http-todolist-crud-role.
8. En Plantillas de políticas, seleccione Simple microservice permissions. Esta política concede a la función Lambda permiso para interactuar con DynamoDB. nota ** Para simplificar el proceso, este tutorial utiliza una política administrada. Como práctica recomendada, se deben crear políticas de IAM propias para otorgar los permisos mínimos requeridos.  
9. Elija Create function (Crear función).
10. Abra lambda_function.py en el editor de código de la consola y reemplace su contenido con código del file api-lambda.py. Seleccione Implementar para actualizar la función.

### Paso 3: crear una API HTTP
La API HTTP proporciona un punto de enlace HTTP para su función de Lambda. En este paso, se crea una API vacía. En los siguientes pasos, se configuran rutas e integraciones para conectar la API y la función Lambda.

Para crear una API HTTP
1. Inicie sesión en la consola de API Gateway en https://console.aws.amazon.com/apigateway.
2. Seleccione Crear API ya continuación, para API HTTP, seleccione Crear.
3. En API name (Nombre de la API), escriba toDoListAPI.
4. Elija Next (Siguiente).
5. En Configurar rutas, seleccione Siguiente para omitir la creación de rutas. Se crearán rutas más adelante.
6. Revise la etapa que API Gateway crea y a continuación seleccione Siguiente.
7. Seleccione Create (Crear).

### Paso 4: crear rutas
Las rutas son una manera de enviar solicitudes entrantes de API a los recursos de backend. Las rutas constan de dos partes: un método HTTP y una ruta de recurso, por ejemplo, GET /items. Para este ejemplo de API, creamos cuatro rutas:
* GET /items/{id}
* GET /items
* PUT /items
* DELETE /items/{id}
Para crear rutas
1. Inicie sesión en la consola de API Gateway en https://console.aws.amazon.com/apigateway.
2. Elija la API.
3. Elija Routes (Rutas).
4. Seleccione Create (Crear).
5. En Method (Método), seleccione GET.
6. En la ruta de acceso, introduzca /items/{id}. El {id} al final de la ruta es un parámetro de ruta que API Gateway recupera de la ruta de solicitud cuando un cliente realiza una solicitud.
7. Seleccione Create (Crear).
8. Repita los pasos 4 a 7 para GET /items, DELETE /items/{id}, y PUT /items.

### Paso 5: crear una integración
Se crea una integración para conectar una ruta a los recursos de backend. Para este ejemplo de API, se crea una integración Lambda que se utiliza para todas las rutas.
Para crear una integración
1. Inicie sesión en la consola de API Gateway en https://console.aws.amazon.com/apigateway.
2. Elija la API.
3. Seleccione Integraciones.
4. Seleccione Administrar integraciones y a continuación seleccione Crear.
5. Omitir Conectar esta integración a una ruta. Esta etapa se completará más adelante.
6. En Tipo de integración, seleccione Función Lambda.
7. En Función Lambda, introduzca toDoListCRUD.
8. Seleccione Create (Crear).

### Paso 6: conectar la integración a las rutas
Para este ejemplo de API, se utiliza la misma integración Lambda para todas las rutas. Después de conectar la integración a todas las rutas de la API, la función Lambda se invoca cuando un cliente llama a cualquiera de sus rutas.

Para conectar integraciones a rutas
1. Inicie sesión en la consola de API Gateway en https://console.aws.amazon.com/apigateway.
2. Elija la API.
3. Seleccione Integraciones.
4. Seleccione una ruta.
5. En Elegir una integración existente, seleccione toDoListCRUD.
6. Seleccione Conectar integración.
7. Repita los pasos 4 a 6 para todas las rutas.
Todas las rutas muestran que se adjuntó una integración de AWS Lambda.

Ahora que se tiene una API HTTP con rutas e integraciones, se puede probar la API.

### Paso 7: probar la API
Para asegurarse de que la API está funcionando, se utiliza Postman.
Para obtener la URL para invocar la API
1. Inicie sesión en la consola de API Gateway en https://console.aws.amazon.com/apigateway.
2. Elija la API.
3. Tenga en cuenta la URL de invocación de la API. Aparece en Invocar URL en la página Detalles.
4. Copie la URL de invocación de la API y reemplacela en las peticiones de la colección del file: WWC - API Serverless.postman_collection.json

### Paso 8: Eliminar
Para evitar costos innecesarios, elimine los recursos creados como parte de este ejercicio. Los siguientes pasos eliminan la API HTTP, la función de Lambda y los recursos asociados.
Para eliminar una tabla de DynamoDB
1. Abra la consola de DynamoDB en https://console.aws.amazon.com/dynamodb/.
2. Seleccionar la tabla.
3. Elija Delete table (Eliminar tabla).
4. Confirme la elección y seleccione Eliminar.
Para eliminar una API HTTP
1. Inicie sesión en la consola de API Gateway en https://console.aws.amazon.com/apigateway.
2. En la página API, seleccione una API. Seleccione Actions y, luego, Delete.
3. Elija Eliminar.
Para eliminar una función de Lambda
1. Inicie sesión en la consola de Lambda en https://console.aws.amazon.com/lambda/.
2. En la página Functions (Funciones), seleccione una función. Seleccione Actions y, luego, Delete.
3. Elija Eliminar.
Para eliminar el grupo de registro de una función de Lambda
1. En la consola de Amazon CloudWatch, abra la página de grupos de registro.
2. En la página Grupos de registro, seleccione el grupo de registro de la función (/aws/lambda/toDoListCRUD). Elija Actions (Acciones) y, a continuación, elija Delete log group (Eliminar grupo de registro).
3. Elija Eliminar.
Para eliminar el rol de ejecución de una función de Lambda
1. En la consola de AWS Identity and Access Management, abra la página Roles (Roles).
2. Seleccione el rol de la función.
3. Elija Delete role (Eliminar rol).
4. Elija Sí, eliminar.
