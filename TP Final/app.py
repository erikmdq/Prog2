import flask
import zoologico
import servicio_zoologicos
import servicio_empleados
import servicio_animales

app = flask.Flask(__name__)


@app.route("/zoologicos/<id_zoologico>/", methods=["GET"])
def obtener_zoologico(id_zoologico):

    servicio = servicio_zoologicos.ServicioZoologicos()

    zoologico_encontrado = servicio.obtener_por_id(id_zoologico)

    if zoologico_encontrado is None:
        flask.abort(404)

    return f"<pre>{str(zoologico_encontrado)}</pre>", 200


@app.route(
    "/zoologicos/<id_zoologico>/cuidadores-principales/",
    methods=["GET"],
)
def obtener_cuidadores_principales(id_zoologico):

    servicio_zoologico = servicio_zoologicos.ServicioZoologicos()

    zoologico_encontrado = servicio_zoologico.obtener_por_id(id_zoologico)

    if zoologico_encontrado is None:
        flask.abort(404)

    servicio = servicio_empleados.ServicioEmpleados()

    empleados = servicio.obtener_cuidadores_principales(id_zoologico)

    texto_respuesta = "Cuidadores principales:\n  "

    texto_respuesta = texto_respuesta + "\n  ".join(str(empleado) for empleado in empleados)

    return f"<pre>{texto_respuesta}</pre>", 200


@app.route(
    "/zoologicos/<id_zoologico>/cuidadores-principales/<id_cuidador_principal>/animales",
    methods=["GET"],
)
def obtener_animales_por_cuidador_principal(id_zoologico, id_cuidador_principal):

    servicio_zoologico = servicio_zoologicos.ServicioZoologicos()

    zoologico_encontrado = servicio_zoologico.obtener_por_id(id_zoologico)

    if zoologico_encontrado is None:
        flask.abort(404)

    empleado_encontrado = None

    empleados = zoologico_encontrado.obtener_empleados()

    for empleado in empleados:
        if empleado.obtener_id() == int(id_cuidador_principal):
            empleado_encontrado = empleado
            break

    if empleado_encontrado is None:
        flask.abort(404)

    servicio = servicio_animales.ServicioAnimales()

    animales = servicio.obtener_animales_por_cuidador_principal(
        id_zoologico, id_cuidador_principal
    )

    texto_respuesta = "Animales:\n  "

    texto_respuesta = texto_respuesta + "\n  ".join(str(animal) for animal in animales)

    return f"<pre>{texto_respuesta}</pre>", 200
