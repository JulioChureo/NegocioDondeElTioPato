from django.contrib import admin
from .models import cliente,vendedor,venta,proveedor,categoria,producto,compra_de_productos,boleta,factura,jefes_ventas,cajas,informe_ventas

# Register your models here.
admin.site.register(cliente)
admin.site.register(vendedor)
admin.site.register(venta)
admin.site.register(proveedor)
admin.site.register(categoria)
admin.site.register(producto)
admin.site.register(compra_de_productos)
admin.site.register(boleta)
admin.site.register(factura)
admin.site.register(jefes_ventas)
admin.site.register(cajas)
admin.site.register(informe_ventas)
