# Tarea4_PCD

* Crear un nuevo repositorio que se llame `Tarea4_PCD`
* Clonar el repositorio en tu local
* Crear un ambiente virtual
* Crear una nueva API, la cuál contenga cuatro endpoints con las siguientes consideraciones:

1. Un endpoint para crear un usuario con los siguientes atributos y guargarlos en una tabla en una database:
```
{
    "user_name": "name",
    "user_id": id,
    "user_email": "email",
    "age" (optional): age,
    "recommendations": lsit[str],
    "ZIP" (optional): ZIP
}
```

2. Si se envía datos con un email ya repetido, se debe regresar un mensaje de error que mencione este hecho.

3. Un endpoint para actualizar la información de un usuario específico buscándolo por id.
Si el id no existe, debe regresar un mensaje de error que mencione este hecho.

4. Un endpoint para obtener la información de un usuario específico buscándolo por id.
Si el id no existe, debe regresar un mensaje de error que mencione este hecho.

5. Un endpoint para eliminar la información de un usuario específico buscándolo por id.
Si el id no existe, debe regresar un mensaje de error que mencione este hecho.

6. Crear dicho endpoint en un archivo llamado `main.py`.