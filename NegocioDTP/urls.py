"""
URL configuration for NegocioDTP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Inicio,name='inicio'),
    path('registro/',views.Registro,name='registro'),
    path('cerrarSesion/',views.CerrarSesion,name='cerrarSesion'),
    path('iniciarSesion/',views.IniciarSesion,name='iniciarSesion'),
    path('crearDatos/',views.crearDatos,name='crearDatos'),
    path('crearCliente/',views.crearCliente,name='crearCliente'),
    path('crearVendedor/',views.crearVendedor,name='crearVendedor'),
    path('crearCategoria/',views.crearCategoria,name='crearCategoria'),
    path('crearProveedor/',views.crearProveedor,name='crearProveedor'),
    path('crearProducto/',views.crearProducto,name='crearProducto'),
    path('crearVenta/',views.crearVenta,name='crearVenta'),
    path('crearCompraProd/',views.crearOrdenDeCompra,name='crearOrdenCompra'),
    path('crearBoleta/',views.crearBoleta,name='crearBoleta'),
    path('crearFactura/',views.crearFactura,name='crearFactura'),
    path('crearJefeVenta/',views.crearJefVent,name='crearJefeVenta'),
    path('crearCaja/',views.vincularCaja,name='crearCaja'),
    path('crearInformeVent/',views.crearInforme,name='crearInformeVent'),
    path('listarDatos/',views.listarDatos,name='listarDatos'),
    path('listarClientes/',views.listarClientes,name='listaClientes'),
    path('listarVendedores/',views.listarVendedores,name='listaVendedores'),
    path('listarCategorias/',views.listarCategorias,name='listaCategorias'),
    path('listarProveedor/',views.listarProveedor,name='listaProveedores'),
    path('listarProductos/',views.listarProductos,name='listaProductos'),
    path('listarVentas/',views.listarVenta,name='listaVentas'),
    path('listarCompraProd/',views.listarCompraProd,name='listaCompraProd'),
    path('listarBoleta/',views.listarBoletas,name='listaBoleta'),
    path('listarFacturas/',views.listarFactura,name='listaFacturas'),
    path('listarJefesVent/',views.listarJefesVent,name='listaJefesVent'),
    path('listarCajas/',views.listarCajas,name='listaCajas'),
    path('listarInformes/',views.listarInformes,name='listaInformes'),
    path('modificarClientes/<str:rut_cliente>/',views.actualizarCliente,name='modificarClientes'),
    path('modificarVendedor/<int:id_vend>/',views.actualizarVendedor,name='modificarVendedor'),
    path('modificarCategorias/<int:id_cat>/',views.actualizarCategoria,name='modificarCategoria'),
    path('modificarProveedor/<int:id_prov>/',views.actualizarProveedor,name='modificarProveedor'),
    path('modificarProducto/<int:id_prod>/',views.actualizarProducto,name='modificarProducto'),
    path('modificarVenta/<int:id_vent>/',views.actualizarVenta,name='modificarVenta'),
    path('modificarCompraProd/<int:id_comp>/',views.actualizarCompraProd,name='modificarCompraProd'),
    path('modificarJefVent/<int:id_jefes>/',views.actualizarJefVent,name='modificarJefVent'),
    path('modificarCaja/<int:id_caja>/',views.actualizarCaja,name='modificarCaja'),
    path('listarClientes/<str:rut_cliente>',views.eliminarCliente,name='eliminarCliente'),
    path('listarVendedores/<int:id_vend>',views.eliminarVendedor,name='eliminarVendedor'),
    path('listarCategorias/<int:id_cat>',views.eliminarCategorias,name='eliminarCategoria'),
    path('listarProveedor/<int:id_prov>',views.eliminarProveedor,name='eliminarProveedor'),
    path('listarProductos/<int:id_prod>',views.eliminarProducto,name='eliminarProducto'),
    path('listarCompraProd/<int:id_comp>/',views.eliminarCompraProd,name='eliminarCompraProd'),
    path('listarJefesVent/<int:id_jefes>',views.eliminarJefesVent,name='eliminarJefesVent'),
    path('listarCajas/<int:id_caja>',views.eliminarCaja,name='eliminarCaja')
]
