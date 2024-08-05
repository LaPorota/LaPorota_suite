### Intro

Muchas páginas proveen funcionalidades de generación de PDFs (reportes, facturas, etc...) y muchos de estos PDFs se sirven de User Inputs dinámicos.

### Librerías más comunes:

- TCPDF
- html2pdf
- mPDF
- DomPDF
- PDFKit
- wkhtmltopdf
- PD4ML

Como las aplicaciones web necesitan designar la presentación/formato del PDF resultante, aceptan HTML para lograr esta funcionalidad. Basicamente parsean el HTML, lo reenderizan y crean el PDF.

Deberemos descubrir las librerías que se están usando para poder apuntar a las vulnerabilidades y fallas de configuración específicas.

### Descubriendo la librería

Afortunadamente, la gran mayoría de las librerías dejan metadata al momento de la construcción del PDF.

Para esto podemos generar un pdf y correrlo con exiftool

    exiftool <pdf>

Usualmente los atributos **creator** y **producer** suelen darnos estos datos.
