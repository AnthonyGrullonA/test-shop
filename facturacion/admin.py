from django.contrib import admin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph

from .models import Factura, ElementoFactura  # Asegúrate de que los modelos estén correctamente importados

class ElementoFacturaInline(admin.TabularInline):
    model = ElementoFactura
    extra = 1

def generar_pdf_factura(modeladmin, request, queryset):
    factura = queryset.first()  # Obtener la primera factura del queryset
    if not factura:
        return HttpResponse("No se seleccionó ninguna factura.")

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_{factura.id}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Título y encabezado del PDF
    story.append(Paragraph(f"Factura - Franduka Flow", styles['Title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Cliente: {factura.cliente}<br/>Fecha de emisión: {factura.fecha_emision.strftime('%d/%m/%Y')}", styles['Normal']))
    story.append(Spacer(1, 12))

    # Datos de la tabla
    encabezados = ['Producto', 'Cantidad', 'Precio Unitario', 'Subtotal']
    data = [encabezados]
    total_factura = 0
    for elemento in factura.elementos.all():
        subtotal = elemento.cantidad * elemento.producto.precio_venta
        total_factura += subtotal
        data.append([
            elemento.producto.nombre, 
            elemento.cantidad, 
            f"${elemento.producto.precio_venta:.2f}", 
            f"${subtotal:.2f}"
        ])

    # Agregando la tabla al story
    table = Table(data)
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ]))
    story.append(table)

    # Total de la factura
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"<b>Total: ${total_factura:.2f}</b>", styles['Normal']))

    doc.build(story)
    return response

generar_pdf_factura.short_description = "Generar PDF de la factura seleccionada"

class FacturaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'fecha_emision', 'total']
    inlines = [ElementoFacturaInline]
    actions = [generar_pdf_factura]

    def total(self, obj):
        return sum(elemento.cantidad * elemento.producto.precio_venta for elemento in obj.elementos.all())

admin.site.register(Factura, FacturaAdmin)
