import jinja2xlsx

html_str = open("nauka01.html", "r", encoding="UTF-8").read()

jinja2xlsx.render_xlsx(html_str).save("nauka01.xlsx")

