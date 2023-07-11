from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .formularios import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def Inicio(request):
    return render(request, 'inicio.html')


def Registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'formulario': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'formulario': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
    return render(request, 'registro.html', {
        'formulario': UserCreationForm,
        'error': 'Las contraseñas no coinciden'
    })

@login_required
def CerrarSesion(request):
    logout(request)
    return redirect('inicio')


def IniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'iniciarSesion.html', {
            'formulario': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'iniciarSesion.html', {
                'formulario': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('inicio')


#|----------------------------------------------------|
#|FUNCIONES PARA LA CREACION DE DATOS PARA LAS TABLAS |
#|----------------------------------------------------|
@login_required
def crearDatos(request):
    return render(request, 'crearDatos.html')

@login_required
def crearCliente(request):
    if request.method == 'GET':
        return render(request, 'crearCliente.html', {
            'formulario': cli_form
        })
    else:
        try:
            formulario = cli_form(request.POST)
            nuevo_cliente = formulario.save(commit=False)
            nuevo_cliente.user = request.user
            nuevo_cliente.save()
            messages.success(request,"Ingresado Correctamente")
            return redirect('listaClientes')
        except ValueError:
            return render(request, 'crearCliente.html', {
                'formulario': cli_form,
                'error': 'Porfavor ingrese datos validos'
            })

@login_required
def crearVendedor(request):
    if request.method == 'GET':
        return render(request, 'crearVendedor.html', {
            'formulario': formVendedor
        })
    else:
        try:
            formulario = formVendedor(request.POST)
            nuevoVendedor = formulario.save(commit=False)
            nuevoVendedor.user = request.user
            nuevoVendedor.save()
            messages.success(request,"Ingresado Correctamente")
            return redirect('listaVendedores')
        except ValueError:
            return render(request, 'crearVendedor.html', {
                'formulario': formVendedor,
                'error': 'Porfavor ingrese datos validos'
            })

@login_required
def crearCategoria(request):
    if request.method == 'GET':
        return render(request, 'crearCategoria.html', {
            'formulario': categoriaForm
        })
    else:
        try:
            formulario = categoriaForm(request.POST)
            nuevaCat = formulario.save(commit=False)
            nuevaCat.user = request.user
            nuevaCat.save()
            messages.success(request,"Ingresado Correctamente")
            return redirect('listaCategorias')
        except ValueError:
            return render(request, 'crearCategoria.html', {
                'formulario': categoriaForm,
                'error': 'Porfavor ingrese datos validos'
            })

@login_required
def crearProveedor(request):
    if request.method == 'GET':
        return render(request, 'crearProveedor.html', {
            'formulario': proveedorForm
        })
    else:
        try:
            formulario = proveedorForm(request.POST)
            nuevoprov = formulario.save(commit=False)
            nuevoprov.user = request.user
            nuevoprov.save()
            messages.success(request,"Ingresado Correctamente")
            return redirect('listaProveedores')
        except ValueError:
            return render(request, 'crearProveedor.html', {
                'formulario': proveedorForm,
                'error': 'Porfavor ingrese datos validos'
            })

@login_required
def crearProducto(request):
    if request.method == 'GET':
        return render(request, 'crearProducto.html', {
            'formulario': productForm
        })
    else:
        try:
            formulario = productForm(request.POST)
            nuevoProd = formulario.save(commit=False)
            nuevoProd.user = request.user
            nuevoProd.save()
            messages.success(request,"Ingresado Correctamente")
            return redirect('listaProductos')
        except ValueError:
            return render(request, 'crearProducto.html', {
                'formulario': productForm,
                'error': 'Porfavor ingrese datos validos'
            })

@login_required
def crearVenta(request):
    if request.method == 'GET':
        return render(request, 'crearVenta.html', {
            'formulario': ventForm
        })
    else:
        try:
            formulario = ventForm(request.POST)
            nuevaVent = formulario.save(commit=False)
            nuevaVent.user = request.user
            nuevaVent.save()
            messages.success(request,"Ingresado Correctamente")
            return redirect('listaVentas')
        except ValueError:
            return render(request, 'crearVenta.html', {
                'formulario': ventForm,
                'error': 'Porfavor ingrese datos validos'
            })

@login_required
def crearOrdenDeCompra(request):
    if request.method == 'GET':
        return render(request, 'crearCompraProd.html', {
            'formulario': compraProdForm
        })
    else:
        try:
            formulario = compraProdForm(request.POST)
            nuevaOrden = formulario.save(commit=False)
            nuevaOrden.user = request.user
            nuevaOrden.save()
            messages.success(request,"Ingresado Correctamente")
            return redirect('listaCompraProd')
        except ValueError:
            return render(request, 'crearCompraProd.html', {
                'formulario': compraProdForm,
                'error': 'Porfavor ingrese datos validos'
            })

@login_required
def crearBoleta(request):
    if request.method == 'GET':
        return render(request, 'crearBoleta.html', {
            'formulario': bolForm
        })
    else:
        try:
            formulario = bolForm(request.POST)
            nuevaBoleta = formulario.save(commit=False)
            nuevaBoleta.user = request.user
            nuevaBoleta.save()
            messages.success(request,"Ingresado Correctamente")
            return redirect('listaBoleta')
        except ValueError:
            return render(request, 'crearBoleta.html', {
                'formulario': bolForm,
                'error': 'Porfavor ingrese datos validos'
            })

@login_required
def crearFactura(request):
    if request.method == 'GET':
        return render(request, 'crearFactura.html', {
            'formulario': facForm
        })
    else:
        try:
            formulario = facForm(request.POST)
            nuevaFactura = formulario.save(commit=False)
            nuevaFactura.user = request.user
            nuevaFactura.save()
            messages.success(request,"Ingresado Correctamente")
            return redirect('listaFacturas')
        except ValueError:
            return render(request, 'crearFactura.html', {
                'formulario': facForm,
                'error': 'Porfavor ingrese datos validos'
            })

@login_required
def crearJefVent(request):
    if request.method == 'GET':
        return render(request, 'crearJefeVenta.html', {
            'formulario': jefVentForm
        })
    else:
        try:
            formulario = jefVentForm(request.POST)
            nuevoJefeVent = formulario.save(commit=False)
            nuevoJefeVent.user = request.user
            nuevoJefeVent.save()
            messages.success(request,"Ingresado Correctamente")
            return redirect('listaJefesVent')
        except ValueError:
            return render(request, 'crearJefeVenta.html', {
                'formulario': jefVentForm,
                'error': 'Porfavor ingrese datos validos'
            })

@login_required
def vincularCaja(request):
    if request.method == 'GET':
        return render(request, 'crearCaja.html', {
            'formulario': cajaForm
        })
    else:
        try:
            formulario = cajaForm(request.POST)
            nuevaCaja = formulario.save(commit=False)
            nuevaCaja.user = request.user
            nuevaCaja.save()
            messages.success(request,"Ingresado Correctamente")
            return redirect('listaCajas')
        except ValueError:
            return render(request, 'crearCaja.html', {
                'formulario': cajaForm,
                'error': 'Porfavor ingrese datos validos'
            })

@login_required
def crearInforme(request):
    if request.method == 'GET':
        return render(request, 'crearInformeVent.html', {
            'formulario': inforVentForm
        })
    else:
        try:
            formulario = inforVentForm(request.POST)
            nuevoInforme = formulario.save(commit=True)
            nuevoInforme.user = request.user
            nuevoInforme.save()
            messages.success(request,"Ingresado Correctamente")
            return redirect('listaInformes')
        except ValueError:
            return render(request, 'crearInformeVent.html', {
                'formulario': inforVentForm,
                'error': 'Porfavor ingrese datos validos'
            })
        

#|----------------------------|
#|FUNCIONES PARA LISTAR DATOS |
#|----------------------------|

@login_required
def listarDatos(request):
    return render(request, 'listarDatos.html')
@login_required
def listarClientes(request):
    lista = cliente.objects.all()
    return render(request, 'listarClientes.html', {'lista': lista})

@login_required
def listarVendedores(request):
    lista = vendedor.objects.all()
    return render(request, 'listarVendedores.html', {'lista': lista})

@login_required
def listarCategorias(request):
    lista = categoria.objects.all()
    return render(request, 'listarCategorias.html', {'lista': lista})

@login_required
def listarProveedor(request):
    lista = proveedor.objects.all()
    return render(request, 'listarProveedor.html', {'lista': lista})

@login_required
def listarProductos(request):
    lista = producto.objects.all()
    return render(request, 'listarProductos.html', {'lista': lista})

@login_required
def listarVenta(request):
    lista = venta.objects.all()
    return render(request, 'listarVentas.html', {'lista': lista})

@login_required
def listarCompraProd(request):
    lista = compra_de_productos.objects.all()
    return render(request, 'listarCompraProd.html', {'lista': lista})

@login_required
def listarBoletas(request):
    lista = boleta.objects.all()
    return render(request, 'listarBoleta.html', {'lista': lista})

@login_required
def listarFactura(request):
    lista = factura.objects.all()
    return render(request, 'listarFacturas.html', {'lista': lista})

@login_required
def listarJefesVent(request):
    lista = jefes_ventas.objects.all()
    return render(request, 'listarJefesVent.html', {'lista': lista})

@login_required
def listarCajas(request):
    lista = cajas.objects.all()
    return render(request, 'listarCajas.html', {'lista': lista})

@login_required
def listarInformes(request):
    lista = informe_ventas.objects.all()
    return render(request, 'listarInformes.html', {'lista': lista})

#|----------------------------------------|  
#|FUNCIONES PARA LA ACTUALIZACION DE DATOS|
#|----------------------------------------|
@login_required
def actualizarCliente(request, rut_cliente):
    if request.method == 'GET':
        Cliente = cliente.objects.get(pk=rut_cliente)
        formulario = cli_form(instance=Cliente)
        return render(request, 'modificarClientes.html', {'cli': Cliente, 'formulario': formulario})
    else:
        try:
            Cliente = cliente.objects.get(pk=rut_cliente)
            formulario = cli_form(request.POST,instance=Cliente)
            formulario.save()
            messages.success(request,"Se ha modificado correctamente")
            return redirect ('listaClientes')
        except ValueError:
            return render(request, 'modificarClientes.html', {'cli': Cliente, 'formulario': formulario ,'error':'Error falta algun dato por ingresar'})
        
@login_required        
def actualizarVendedor(request, id_vend):
    if request.method == 'GET':
        Vendedor = vendedor.objects.get(pk=id_vend)
        formulario = formVendedor(instance=Vendedor)
        return render(request, 'modificarVendedor.html', {'vendedor': Vendedor, 'formulario': formulario})
    else:
        try:
            Vendedor = vendedor.objects.get(pk=id_vend)
            formulario = formVendedor(request.POST,instance=Vendedor)
            formulario.save()
            messages.success(request,"Se ha modificado correctamente")
            return redirect ('listaVendedores')
        except ValueError:
            return render(request, 'modificarVendedor.html', {'vendedor': Vendedor, 'formulario': formulario ,'error':'Error falta algun dato por ingresar'})

@login_required
def actualizarCategoria(request, id_cat):
    if request.method == 'GET':
        Categoria = categoria.objects.get(pk=id_cat)
        formulario = categoriaForm(instance=Categoria)
        return render(request, 'modificarCatgorias.html', {'categoria': Categoria, 'formulario': formulario})
    else:
        try:
            Categoria = categoria.objects.get(pk=id_cat)
            formulario = categoriaForm(request.POST,instance=Categoria)
            formulario.save()
            messages.success(request,"Se ha modificado correctamente")
            return redirect ('listaCategorias')
        except ValueError:
            return render(request, 'modificarCategorias.html', {'categoria': Categoria, 'formulario': formulario ,'error':'Error falta algun dato por ingresar'})
        
@login_required        
def actualizarProveedor(request, id_prov):
    if request.method == 'GET':
        Proveedor = proveedor.objects.get(pk=id_prov)
        formulario = proveedorForm(instance=Proveedor)
        return render(request, 'modificarProveedor.html', {'proveedor': Proveedor, 'formulario': formulario})
    else:
        try:
            Proveedor = proveedor.objects.get(pk=id_prov)
            formulario = proveedorForm(request.POST,instance=Proveedor)
            formulario.save()
            messages.success(request,"Se ha modificado correctamente")
            return redirect ('listaProveedores')
        except ValueError:
            return render(request, 'modificarProveedor.html', {'proveedor': Proveedor, 'formulario': formulario ,'error':'Error falta algun dato por ingresar'})

@login_required        
def actualizarProducto(request, id_prod):
    if request.method == 'GET':
        Producto = producto.objects.get(pk=id_prod)
        formulario =productForm(instance=Producto)
        return render(request, 'modificarProducto.html', {'producto': Producto, 'formulario': formulario})
    else:
        try:
            Producto = producto.objects.get(pk=id_prod)
            formulario =productForm(request.POST,instance=Producto)
            formulario.save()
            messages.success(request,"Se ha modificado correctamente")
            return redirect ('listaProductos')
        except ValueError:
            return render(request, 'modificarProducto.html', {'producto': Producto, 'formulario': formulario ,'error':'Error falta algun dato por ingresar'})

@login_required        
def actualizarVenta(request, id_vent):
    if request.method == 'GET':
        Venta = venta.objects.get(pk=id_vent)
        formulario =ventForm(instance=Venta)
        return render(request, 'modificarVenta.html', {'venta': Venta, 'formulario': formulario})
    else:
        try:
            Venta = venta.objects.get(pk=id_vent)
            formulario =ventForm(request.POST,instance=Venta)
            formulario.save()
            messages.success(request,"Se ha modificado correctamente")
            return redirect ('listaVentas')
        except ValueError:
            return render(request, 'modificarVenta.html', {'venta': Venta, 'formulario': formulario ,'error':'Error falta algun dato por ingresar'})

@login_required        
def actualizarCompraProd(request, id_comp):
    if request.method == 'GET':
        compraProd = compra_de_productos.objects.get(pk=id_comp)
        formulario =compraProdForm(instance=compraProd)
        return render(request, 'modificarCompraProd.html', {'compraProd': compraProd, 'formulario': formulario})
    else:
        try:
            compraProd = compra_de_productos.objects.get(pk=id_comp)
            formulario =compraProdForm(request.POST,instance=compraProd)
            formulario.save()
            messages.success(request,"Se ha modificado correctamente")
            return redirect ('listaCompraProd')
        except ValueError:
            return render(request, 'modificarVenta.html', {'compraProd': compraProd, 'formulario': formulario ,'error':'Error falta algun dato por ingresar'})
        
@login_required        
def actualizarJefVent(request, id_jefes):
    if request.method == 'GET':
        Jefes = jefes_ventas.objects.get(pk=id_jefes)
        formulario =jefVentForm(instance=Jefes)
        return render(request, 'modificarJefVent.html', {'jefes': Jefes, 'formulario': formulario})
    else:
        try:
            Jefes = jefes_ventas.objects.get(pk=id_jefes)
            formulario =jefVentForm(request.POST,instance=Jefes)
            formulario.save()
            messages.success(request,"Se ha modificado correctamente")
            return redirect ('listaJefesVent')
        except ValueError:
            return render(request, 'modificarJefVent.html', {'jefes': Jefes, 'formulario': formulario ,'error':'Error falta algun dato por ingresar'})
        
@login_required
def actualizarCaja(request, id_caja):
    if request.method == 'GET':
        Caja = cajas.objects.get(pk=id_caja)
        formulario =cajaForm(instance=Caja)
        return render(request, 'modificarCaja.html', {'caja': Caja, 'formulario': formulario})
    else:
        try:
            Caja = cajas.objects.get(pk=id_caja)
            formulario =cajaForm(request.POST,instance=Caja)
            formulario.save()
            messages.success(request,"Se ha modificado correctamente")
            return redirect ('listaCajas')
        except ValueError:
            return render(request, 'modificarCaja.html', {'caja': Caja, 'formulario': formulario ,'error':'Error falta algun dato por ingresar'})
        

#|-----------------------------|  
#|FUNCIONES PARA ELIMINAR DATOS|
#|-----------------------------|
@login_required
def eliminarCliente (request,rut_cliente):
    Cliente = cliente.objects.get(pk=rut_cliente)
    if request.method=='GET':
        Cliente.delete()
        messages.success(request,"Se ha eliminado Correctamente")
        return redirect ('listaClientes')

@login_required
def eliminarVendedor(request,id_vend):
    Vendedor = vendedor.objects.get(pk=id_vend)
    if request.method=='GET':
        Vendedor.delete()
        messages.success(request,"Se ha eliminado Correctamente")
        return redirect ('listaVendedores')

@login_required
def eliminarCategorias(request,id_cat):
    Categoria = categoria.objects.get(pk=id_cat)
    if request.method=='GET':
        Categoria.delete()
        messages.success(request,"Se ha eliminado Correctamente")
        return redirect ('listaCategorias')

@login_required    
def eliminarProveedor(request,id_prov):
    Proveedor = proveedor.objects.get(pk=id_prov)
    if request.method=='GET':
        Proveedor.delete()
        messages.success(request,"Se ha eliminado Correctamente")
        return redirect ('listaProveedores')

@login_required    
def eliminarProducto(request,id_prod):
    Producto =producto.objects.get(pk=id_prod)
    if request.method=='GET':
        Producto.delete()
        messages.success(request,"Se ha eliminado Correctamente")
        return redirect ('listaProductos')

@login_required
def eliminarCompraProd(request,id_comp):
    Compra =compra_de_productos.objects.get(pk=id_comp)
    if request.method=='GET':
        Compra.delete()
        messages.success(request,"Se ha eliminado Correctamente")
        return redirect ('listaCompraProd')

@login_required    
def eliminarJefesVent(request,id_jefes):
    Jefes =jefes_ventas.objects.get(pk=id_jefes)
    if request.method=='GET':
        Jefes.delete()
        messages.success(request,"Se ha eliminado Correctamente")
        return redirect ('listaJefesVent')

@login_required    
def eliminarCaja(request,id_caja):
    Caja =cajas.objects.get(pk=id_caja)
    if request.method=='GET':
        Caja.delete()
        messages.success(request,"Se ha eliminado Correctamente")
        return redirect ('listaCajas')