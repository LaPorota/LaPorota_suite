import pandas as pd
from jinja2 import Template
import pdfkit
import tempfile
import os


def pdf_maker(data):

    html_template = Template('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Claro Web Scan Report</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
            }
            
            h1 {
                background-color: #222;
                color: white;
                padding: 20px;
                margin: 0;
            }

            h3 {
                color: #333;
                background-color: #f2f2f2;
                padding: 10px;
                margin: 0;
                border-top: 1px solid #ddd;
            }

            h4 {
                color: #444;
                margin: 20px ;
                padding: 10px;
                             
            }

            table {
                font-family: Arial, sans-serif;
                font-size: 12px;
                margin: 20px;
                border-collapse: collapse;
                width: 97%;
                background-color: white;
            }

            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: center;
            }
            
            th {
                background-color: #f5f5f5;
            }

            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            td:first-child {
                text-align: left;
                white-space: nowrap;  /* Evitar saltos de línea */
                overflow: hidden;     /* Ocultar contenido que se desborda */
                text-overflow: ellipsis; /* Mostrar "..." si se desborda */
                font-weight: bold;
                color: blue;
            }
        </style>
    </head>
    <body>
                           
        <h1>Claro Web Scan Report</h1>
                            
        {% for category, subcategories in data.items() %}
            <h3>{{ category }}</h3>
            {% for subcategory, df in subcategories.items() %}
                <h4>{{ subcategory }}</h4>
                <table>
                    <thead>
                        <tr>
                            {% for col in df.columns %}
                                <th>{{ col }}</th>
                            {% endfor %}
                        </tr>
                    </thead>
                    <tbody>
                        {% for _, row in df.iterrows() %}
                            <tr>
                                {% for col, value in row.items() %}
                                    <td>{{ format_cell(col, value) | safe }}</td>
                                {% endfor %}
                            </tr>
                        {% endfor %}
                    </tbody>
                </table>
            {% endfor %}
        {% endfor %}
    </body>
    </html>
    ''')  # Formato predeterminado

    def format_cell(column, value):
        if column == 'CVSS Score':
            if value >= 8:
                color = "red"
            elif value >= 4:
                color= "gold"
            else:
                color = "green"
                        
            return f'<span style="color: {color}; font-weight: bold; font-size: 14px;">{value}</span>'
        return str(value)
    # Renderizar la plantilla HTML con los datos
    html_content = html_template.render(data=data, format_cell=format_cell)

    # Guardar el contenido HTML en un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as temp_file:
        temp_file.write(html_content.encode())
        temp_file_path = temp_file.name

    # Generar el PDF desde el archivo temporal
    pdf_output_path = 'report.pdf'
    pdfkit.from_file(temp_file_path, pdf_output_path)

    # Eliminar el archivo temporal
    os.remove(temp_file_path)

    print(f'PDF generado: {pdf_output_path}')

if __name__=="__main__":
    data_1 = {
    "CVE ID": ["CVE-2023-001", "CVE-2023-002", "CVE-2023-003"],
    "Description": ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin erat sapien, tempus nec lectus sed, hendrerit eleifend ipsum. Sed ornare orci purus, in egestas dui pulvinar sed. Donec posuere, nisi elementum egestas porttitor, erat orci sollicitudin ex, ut vestibulum tellus neque quis tortor. Morbi pellentesque, neque eget vulputate placerat, nisl nunc gravida justo, vitae posuere risus enim sit amet lectus. In finibus ornare rhoncus. Nullam at nibh maximus, fermentum enim vitae, vehicula libero. Nulla augue lacus, euismod sit amet consequat ac, laoreet sed libero. Donec ut vulputate massa. Fusce libero massa, scelerisque vitae turpis quis, luctus volutpat sem. Nunc ac commodo justo, a iaculis dolor. Morbi ac ligula leo. Vivamus non pulvinar metus, sed placerat risus. Donec elementum at erat ut egestas. Aliquam elit diam, elementum vel turpis in, pretium tincidunt sapien", 
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin erat sapien, tempus nec lectus sed, hendrerit eleifend ipsum. Sed ornare orci purus, in egestas dui pulvinar sed. Donec posuere, nisi elementum egestas porttitor, erat orci sollicitudin ex, ut vestibulum tellus neque quis tortor. Morbi pellentesque, neque eget vulputate placerat, nisl nunc gravida justo, vitae posuere risus enim sit amet lectus. In finibus ornare rhoncus. Nullam at nibh maximus, fermentum enim vitae, vehicula libero. Nulla augue lacus, euismod sit amet consequat ac, laoreet sed libero. Donec ut vulputate massa. Fusce libero massa, scelerisque vitae turpis quis, luctus volutpat sem. Nunc ac commodo justo, a iaculis dolor. Morbi ac ligula leo. Vivamus non pulvinar metus, sed placerat risus. Donec elementum at erat ut egestas. Aliquam elit diam, elementum vel turpis in, pretium tincidunt sapien", 
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin erat sapien, tempus nec lectus sed, hendrerit eleifend ipsum. Sed ornare orci purus, in egestas dui pulvinar sed. Donec posuere, nisi elementum egestas porttitor, erat orci sollicitudin ex, ut vestibulum tellus neque quis tortor. Morbi pellentesque, neque eget vulputate placerat, nisl nunc gravida justo, vitae posuere risus enim sit amet lectus. In finibus ornare rhoncus. Nullam at nibh maximus, fermentum enim vitae, vehicula libero. Nulla augue lacus, euismod sit amet consequat ac, laoreet sed libero. Donec ut vulputate massa. Fusce libero massa, scelerisque vitae turpis quis, luctus volutpat sem. Nunc ac commodo justo, a iaculis dolor. Morbi ac ligula leo. Vivamus non pulvinar metus, sed placerat risus. Donec elementum at erat ut egestas. Aliquam elit diam, elementum vel turpis in, pretium tincidunt sapien"],
    "CVSS Score": [7.5, 9.2, 8.7],
    "Severity": ["Alta", "Critica", "Alta"]
    }
    
    df_1 = pd.DataFrame(data_1)
    
    # Ejemplo 2
    data_2 = {
        "CVE ID": ["CVE-2023-004", "CVE-2023-005", "CVE-2023-006"],
                    "Description": ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin erat sapien, tempus nec lectus sed, hendrerit eleifend ipsum. Sed ornare orci purus, in egestas dui pulvinar sed. Donec posuere, nisi elementum egestas porttitor, erat orci sollicitudin ex, ut vestibulum tellus neque quis tortor. Morbi pellentesque, neque eget vulputate placerat, nisl nunc gravida justo, vitae posuere risus enim sit amet lectus. In finibus ornare rhoncus. Nullam at nibh maximus, fermentum enim vitae, vehicula libero. Nulla augue lacus, euismod sit amet consequat ac, laoreet sed libero. Donec ut vulputate massa. Fusce libero massa, scelerisque vitae turpis quis, luctus volutpat sem. Nunc ac commodo justo, a iaculis dolor. Morbi ac ligula leo. Vivamus non pulvinar metus, sed placerat risus. Donec elementum at erat ut egestas. Aliquam elit diam, elementum vel turpis in, pretium tincidunt sapien", 
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin erat sapien, tempus nec lectus sed, hendrerit eleifend ipsum. Sed ornare orci purus, in egestas dui pulvinar sed. Donec posuere, nisi elementum egestas porttitor, erat orci sollicitudin ex, ut vestibulum tellus neque quis tortor. Morbi pellentesque, neque eget vulputate placerat, nisl nunc gravida justo, vitae posuere risus enim sit amet lectus. In finibus ornare rhoncus. Nullam at nibh maximus, fermentum enim vitae, vehicula libero. Nulla augue lacus, euismod sit amet consequat ac, laoreet sed libero. Donec ut vulputate massa. Fusce libero massa, scelerisque vitae turpis quis, luctus volutpat sem. Nunc ac commodo justo, a iaculis dolor. Morbi ac ligula leo. Vivamus non pulvinar metus, sed placerat risus. Donec elementum at erat ut egestas. Aliquam elit diam, elementum vel turpis in, pretium tincidunt sapien", 
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin erat sapien, tempus nec lectus sed, hendrerit eleifend ipsum. Sed ornare orci purus, in egestas dui pulvinar sed. Donec posuere, nisi elementum egestas porttitor, erat orci sollicitudin ex, ut vestibulum tellus neque quis tortor. Morbi pellentesque, neque eget vulputate placerat, nisl nunc gravida justo, vitae posuere risus enim sit amet lectus. In finibus ornare rhoncus. Nullam at nibh maximus, fermentum enim vitae, vehicula libero. Nulla augue lacus, euismod sit amet consequat ac, laoreet sed libero. Donec ut vulputate massa. Fusce libero massa, scelerisque vitae turpis quis, luctus volutpat sem. Nunc ac commodo justo, a iaculis dolor. Morbi ac ligula leo. Vivamus non pulvinar metus, sed placerat risus. Donec elementum at erat ut egestas. Aliquam elit diam, elementum vel turpis in, pretium tincidunt sapien"],        
                    "CVSS Score": [5.8, 6.4, 9.0],
        "Severity": ["Media", "Media", "Critica"]
    }
    
    df_2 = pd.DataFrame(data_2)
    
    # Ejemplo 3
    data_3 = {
        "CVE ID": ["CVE-2023-007", "CVE-2023-008", "CVE-2023-009"],
                    "Description": ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin erat sapien, tempus nec lectus sed, hendrerit eleifend ipsum. Sed ornare orci purus, in egestas dui pulvinar sed. Donec posuere, nisi elementum egestas porttitor, erat orci sollicitudin ex, ut vestibulum tellus neque quis tortor. Morbi pellentesque, neque eget vulputate placerat, nisl nunc gravida justo, vitae posuere risus enim sit amet lectus. In finibus ornare rhoncus. Nullam at nibh maximus, fermentum enim vitae, vehicula libero. Nulla augue lacus, euismod sit amet consequat ac, laoreet sed libero. Donec ut vulputate massa. Fusce libero massa, scelerisque vitae turpis quis, luctus volutpat sem. Nunc ac commodo justo, a iaculis dolor. Morbi ac ligula leo. Vivamus non pulvinar metus, sed placerat risus. Donec elementum at erat ut egestas. Aliquam elit diam, elementum vel turpis in, pretium tincidunt sapien", 
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin erat sapien, tempus nec lectus sed, hendrerit eleifend ipsum. Sed ornare orci purus, in egestas dui pulvinar sed. Donec posuere, nisi elementum egestas porttitor, erat orci sollicitudin ex, ut vestibulum tellus neque quis tortor. Morbi pellentesque, neque eget vulputate placerat, nisl nunc gravida justo, vitae posuere risus enim sit amet lectus. In finibus ornare rhoncus. Nullam at nibh maximus, fermentum enim vitae, vehicula libero. Nulla augue lacus, euismod sit amet consequat ac, laoreet sed libero. Donec ut vulputate massa. Fusce libero massa, scelerisque vitae turpis quis, luctus volutpat sem. Nunc ac commodo justo, a iaculis dolor. Morbi ac ligula leo. Vivamus non pulvinar metus, sed placerat risus. Donec elementum at erat ut egestas. Aliquam elit diam, elementum vel turpis in, pretium tincidunt sapien", 
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin erat sapien, tempus nec lectus sed, hendrerit eleifend ipsum. Sed ornare orci purus, in egestas dui pulvinar sed. Donec posuere, nisi elementum egestas porttitor, erat orci sollicitudin ex, ut vestibulum tellus neque quis tortor. Morbi pellentesque, neque eget vulputate placerat, nisl nunc gravida justo, vitae posuere risus enim sit amet lectus. In finibus ornare rhoncus. Nullam at nibh maximus, fermentum enim vitae, vehicula libero. Nulla augue lacus, euismod sit amet consequat ac, laoreet sed libero. Donec ut vulputate massa. Fusce libero massa, scelerisque vitae turpis quis, luctus volutpat sem. Nunc ac commodo justo, a iaculis dolor. Morbi ac ligula leo. Vivamus non pulvinar metus, sed placerat risus. Donec elementum at erat ut egestas. Aliquam elit diam, elementum vel turpis in, pretium tincidunt sapien"],        
                    "CVSS Score": [8.2, 2.5, 6.5],
        "Severity": ["Alta", "Baja", "Media"]
    }
    df_3 =pd.DataFrame(data_3)

    data={'Certificados': {'TLS 1.2': df_1},'Librerias':{'php 2.2.2': df_2, 'bingo 1.2.3': df_3}}

    pdf_maker(data)