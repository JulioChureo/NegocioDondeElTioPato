from django import forms
from django.forms import ModelForm
from .models import cliente,vendedor,venta,proveedor,categoria,producto,compra_de_productos,boleta,factura,jefes_ventas,cajas,informe_ventas


class cli_form (ModelForm):
    class Meta:
        model=cliente
        fields=['rut_cliente','nombre','apellido','direccion','telefono','correo_electronico']
        widgets={
            'rut_cliente':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'correo_electronico':forms.TextInput(attrs={'class':'form-control'})
        }

class formVendedor(ModelForm):
    class Meta:
        model=vendedor
        fields=['rut_vendedor','nombre_vendedor']
        widgets={
            'rut_vendedor':forms.TextInput(attrs={'class':'form-control'}),
            'nombre_vendedor':forms.TextInput(attrs={'class':'form-control'})
        }

class categoriaForm(ModelForm):
    class Meta:
        model=categoria
        fields=['nombre']
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'})
        }

class proveedorForm(ModelForm):
    class Meta:
        model=proveedor
        fields=['nombre','direccion','telefono','email']
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'})
        }

class productForm(ModelForm):
    class Meta:
        model=producto
        fields=['nombre_producto','descripcion','precio','stock','categoria','proveedor']
        widgets={
            'nombre_producto':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control'}),
            'precio':forms.NumberInput(attrs={'class':'form-control'}),
            'stock':forms.NumberInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
            'proveedor':forms.Select(attrs={'class':'form-control'})
        }

class ventForm(ModelForm):
    class Meta:
        model=venta
        fields=['producto_comprado','comprador','total_neto','total_iva']
        widgets={
            'producto_comprado':forms.Select(attrs={'class':'form-control'}),
            'comprador':forms.Select(attrs={'class':'form-control'}),
            'total_neto':forms.NumberInput(attrs={'class':'form-control'}),
            'total_iva':forms.NumberInput(attrs={'class':'form-control'})
        }


class compraProdForm(ModelForm):
    class Meta:
        model=compra_de_productos
        fields=['proveedor','producto','cantidad']
        widgets={
            'proveedor':forms.Select(attrs={'class':'form-control'}),
            'producto':forms.Select(attrs={'class':'form-control'}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control'}),
        }

class bolForm(ModelForm):
    class Meta:
        model=boleta
        fields=['venta_asociada']
        widgets={
            'venta_asociada':forms.Select(attrs={'class':'form-control'}),
        }


class facForm(ModelForm):
    class Meta:
        model=factura
        fields=['nombre_empresa','razon_social','rut_empresa','producto','vendedor_asociado','total_neto','total_iva']
        widgets={
            'nombre_empresa':forms.TextInput(attrs={'class':'form-control'}),
            'razon_social':forms.TextInput(attrs={'class':'form-control'}),
            'rut_empresa':forms.TextInput(attrs={'class':'form-control'}),
            'producto':forms.Select(attrs={'class':'form-control'}),
            'vendedor_asociado':forms.Select(attrs={'class':'form-control'}),
            'total_neto':forms.NumberInput(attrs={'class':'form-control'}),
            'total_iva':forms.NumberInput(attrs={'class':'form-control'})
        }

class jefVentForm(ModelForm):
    class Meta:
        model=jefes_ventas
        fields=['nombre','rut']
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'rut':forms.TextInput(attrs={'class':'form-control'}),
        }

class cajaForm(ModelForm):
    class Meta:
        model=cajas
        fields=['id_caja','vendedor']
        widgets={
            'id_caja':forms.NumberInput(attrs={'class':'form-control'}),
            'vendedor':forms.Select(attrs={'class':'form-control'}),
        }

class inforVentForm(ModelForm):
    class Meta:
        model=informe_ventas
        fields=['solocitado_por','caja_solicitada']
        widgets={
            'solocitado_por':forms.Select(attrs={'class':'form-control'}),
            'caja_solicitada':forms.Select(attrs={'class':'form-control'}),
        }