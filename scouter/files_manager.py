import os

def search_create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory in '{path}'")


def create_template():
    html_content = '''
                        <html>
                            <head>

                                <title>Scan Result</title>
                                <link rel="stylesheet" type="text/css" href="style.css">
                            </head>
                            <body>
                                    <h1>{{ title }}</h1>
                                    <h2> {{subtitle}} </h2>
                                    {{ table }}
                            </body>
                        </html>
    '''
    filename = "template.html"
    filepath = os.path.join(os.getcwd(), filename)
    with open(filepath, 'w') as f:
        f.write(html_content)
    css_content = '''
                        /* Estilos para el archivo HTML generado */
                        a {
                            color: azure;
                        }
                        h1{
                            color: #ccc;
                            text-align: center;
                        }
                        h2{
                            color: #ccc;
                            text-align: center;
                        }
                        
                        body{
                                background: #343a40;
                            }
                        
                        .table {
                            font-family: Arial, sans-serif;
                            font-size: 14px;
                            margin: 20px;
                        }

                        .table-bordered {
                            border-collapse: collapse;
                        }

                        .table-bordered td, .table-bordered th {
                            border: 1px solid #ccc;
                            padding: 8px;
                        }

                        .table-dark td, .table-dark th {
                            background-color: #343a40;
                            color: azure;
                            text-align: center;
                        }
                            '''
    css_filename = "style.css"
    css_filepath = os.path.join(os.getcwd(), css_filename)
    with open(css_filepath, 'w') as css:
        css.write(css_content)

def delete_template():
    print("\033[1;31mDeleting \033[0;33mtemporal files\033[0;m")
    files = os.listdir()
    for file in files:
        if file == 'template.html':
            os.remove(file)