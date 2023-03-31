from jinja2 import Template
import pandas as pd



def export_file(arg:str, df: pd.DataFrame):
    template = Template(open("template.html").read())

    table_html = df.to_html(index=False, col_space=None, 
                        classes=['table', 'table-bordered', 'table-dark'])
    html = template.render(title="Results", table=table_html)


    with open(f"{arg}.html", "w") as f:
        f.write(html.replace("&lt;br&gt;", "<br>"))