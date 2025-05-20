
class cliente:
    class cliente_persona:
           
        nro_cliente=int
        domicilio=str
        telefono=int
        email=str
        nombre=str

        create
        mostrar

     class cliente_empresa:
        razon_social=str
        usuario=str
       

class auto:
    modelo=str
    año=int
    seguro_de_cobertura=int
    precio_de_alquiler_por_dia=int

    set.add(camioneta):
    mostrar
    conocer_modelo
    conocer_seguro_de_cobertura

    
class marca:
    nombre=str
    descripcion=str
    modelo=str
class seguro_de_cobertura:
    nombre=str
    descripcion=str
    nro_poliza=str

    crear
    mostrar
    tomar_nombre
    tomar_descripcion
    mostrar_nombre
    mostrar_descripcion

class modelo:
    nombre=str
    descripcion=str
    
    crear
    mostrar

class medio_de_pago:
    nombre=str
    descripcion=str

    crear
    mostrar

class alquiler:
    nroalquiler=int
    fecha_devolucion_pactada=int
    cliente =str
    detalle_alquiler=str
    forma_de_pago=str

    crear
    mostrar
    conocercliente
    conocermediodepago
    agregardetalledealqiiler
    conocerdetalledealquiler
    calculartotal
    contarautos

class detalle_alquiler:
    auto=str
    cantidad_de_dias=int
    precio_por_dia=str
    fecha_devolucion_pactada=str
    fecha_devolucion_real=str

    crear
    mostrar
    calcular_subtotal
    conocer_automovil
    registrar_devolucion
