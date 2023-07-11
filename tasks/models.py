from django.db import models


# Create your models here.
class cliente (models.Model):
    rut_cliente= models.CharField(max_length=20, primary_key=True)
    nombre=models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    direccion= models.CharField(max_length=35)
    telefono= models.CharField(max_length=20,unique=True)
    correo_electronico=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre+' | '+self.apellido+' | '+self.rut_cliente

class vendedor(models.Model):
    id_vendedor=models.BigAutoField(primary_key=True)
    rut_vendedor=models.CharField(max_length=30)
    nombre_vendedor=models.CharField(max_length=20)
    fecha_Ingreso=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_vendedor)+' | '+self.nombre_vendedor
   
class categoria(models.Model):
    id_categoria=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    
    def __str__(self):
        return  str(self.id_categoria) +' | '+ self.nombre 


class proveedor(models.Model):
    id_proveedor=models.BigAutoField(primary_key=True)
    nombre= models.CharField(max_length=20)
    direccion= models.CharField(max_length=30)
    telefono= models.CharField(max_length=20)
    email=models.CharField(max_length=30)

    def __str__(self):
        return str(self.id_proveedor)+' | '+self.nombre

class producto(models.Model):
    id_producto= models.BigAutoField(primary_key=True)
    nombre_producto=models.CharField(max_length=30)
    descripcion=models.TextField(blank=True)
    precio =models.IntegerField()
    stock=models.IntegerField()
    categoria=models.ForeignKey(categoria,null=True,blank=True, on_delete=models.CASCADE)
    proveedor=models.ForeignKey(proveedor,null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre_producto

class venta(models.Model):
    id_venta= models.BigAutoField(primary_key=True)
    fecha=models.DateTimeField(auto_now_add=True)
    producto_comprado=models.ForeignKey(producto,null=True,blank=True, on_delete=models.CASCADE)
    comprador=models.ForeignKey(cliente,null=True,blank=True, on_delete=models.CASCADE)
    total_neto=models.IntegerField()
    total_iva=models.IntegerField(null=False)

    def __str__(self):
        return str(self.producto_comprado)+' | '+str(self.comprador)
    
class compra_de_productos (models.Model):
    id_compra=models.BigAutoField(primary_key=True)
    fecha= models.DateTimeField(auto_now_add=True)
    proveedor= models.ForeignKey(proveedor,null=True,blank=True, on_delete=models.CASCADE)
    producto=models.ForeignKey(producto,null=True,blank=True, on_delete=models.CASCADE)
    cantidad= models.IntegerField()

    def __str__(self):
        return str(self.id_compra)+' | '+ str(self.producto)
    
class boleta(models.Model):
    id_boleta=models.BigAutoField(primary_key=True)
    venta_asociada=models.ForeignKey(venta,null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_boleta)+' | '+str(self.venta_asociada)

    
    
class factura (models.Model):
    id_factura= models.BigAutoField(primary_key=True)
    nombre_empresa=models.CharField(max_length=20)
    razon_social=models.CharField(max_length=20)
    rut_empresa=models.CharField(max_length=20)
    fecha=models.DateTimeField(auto_now_add=True)
    producto=models.ForeignKey(producto,null=True,blank=True, on_delete=models.CASCADE)
    vendedor_asociado=models.ForeignKey(vendedor,null=True,blank=True, on_delete=models.CASCADE)
    total_neto=models.IntegerField()
    total_iva=models.IntegerField()

    def __str__(self):
        return str(self.id_factura)+' | '+self.fecha
    
class jefes_ventas(models.Model):
    id_jefe_ventas= models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=20)
    rut=models.CharField(max_length=20)
    fecha_ingreso=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_jefe_ventas)+' | '+self.nombre
    
class cajas(models.Model):
    id_caja=models.IntegerField(primary_key=True)
    vendedor=models.ForeignKey(vendedor,null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_caja)+' | '+self.vendedor.nombre_vendedor
    
class informe_ventas(models.Model):
    id_informe=models.BigAutoField(primary_key=True)
    fecha_solicitud= models.DateTimeField(auto_now_add=True)
    solocitado_por=models.ForeignKey(jefes_ventas, null=True,blank=True, on_delete=models.CASCADE)
    caja_solicitada=models.ForeignKey(cajas,null=True,blank=True, on_delete=models.CASCADE)
    

    