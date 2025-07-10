import os
import sys

sys.path.append(os.path.abspath("..")+"/proyecto_de_software/src/conexion_sql")
print(sys.path)
import  conexion
import webbrowser


def gestion_busqueda(dni,id_curso,id_periodo):
    conx = conexion.conexion_()
    query = f"""
        SELECT 
            a.nombres AS nombre_estudiante,
            c.nombre_curso AS curso,
            p.periodo AS periodo,
            pr.nombres AS profesor,
            cal.valor AS nota
        FROM calificacion cal
        INNER JOIN alumno a ON cal.alumno_DNI = a.DNI
        INNER JOIN curso c ON cal.curso_idcurso = c.idcurso
        INNER JOIN periodo p ON c.periodo_idperiodo = p.idperiodo
        INNER JOIN profesor pr ON c.profesor_DNI = pr.DNI
        WHERE a.DNI = '{dni}' AND c.idcurso = {id_curso} AND p.idperiodo = {id_periodo};
        """
    conx.cursor.execute(query)
    lista_ = conx.cursor.fetchall()
    conx.cerrar_conexion()

    columnas = ("Nombre", "Curso", "Periodo", "Profesor", "Nota")
    exportar_html(lista_,"Calificacion del alumno",columnas)

def exportar_boleta_notas(dni,id_periodo):
    conx = conexion.conexion_()

    if id_periodo == '':
        query = f"""
        SELECT 
            a.nombres AS nombre_estudiante,
            c.nombre_curso AS curso,
            p.periodo AS periodo,
            pr.nombres AS profesor,
            cal.valor AS nota
        FROM calificacion cal
        INNER JOIN alumno a ON cal.alumno_DNI = a.DNI
        INNER JOIN curso c ON cal.curso_idcurso = c.idcurso
        INNER JOIN periodo p ON c.periodo_idperiodo = p.idperiodo
        INNER JOIN profesor pr ON c.profesor_DNI = pr.DNI
        WHERE a.DNI = '{dni}' ;"""
    else:
         query = f"""
        SELECT 
            a.nombres AS nombre_estudiante,
            c.nombre_curso AS curso,
            p.periodo AS periodo,
            pr.nombres AS profesor,
            cal.valor AS nota
        FROM calificacion cal
        INNER JOIN alumno a ON cal.alumno_DNI = a.DNI
        INNER JOIN curso c ON cal.curso_idcurso = c.idcurso
        INNER JOIN periodo p ON c.periodo_idperiodo = p.idperiodo
        INNER JOIN profesor pr ON c.profesor_DNI = pr.DNI
        WHERE a.DNI = '{dni}' AND p.idperiodo = {id_periodo};"""

    
    conx.cursor.execute(query)
    lista_ = conx.cursor.fetchall()
    conx.cerrar_conexion()
    columnas = ("Nombre", "Curso", "Periodo", "Profesor", "Nota")
    exportar_html(lista_,"Boleta de Notas ",columnas)
      

def aperturar_curso(nombre,seccion,dni_profesor,id_periodo):
    conx = conexion.conexion_()
    query = """
    INSERT INTO curso (nombre_curso, seccion, profesor_DNI, periodo_idperiodo)
    VALUES (%s, %s, %s, %s);
    """
    valores = ( nombre, seccion, dni_profesor, id_periodo)
    conx.cursor.execute(query, valores)
    conx.database.commit()

    query = """
    SELECT 
        c.nombre_curso AS curso,
        c.seccion,
        pr.nombres AS profesor,
        p.periodo
    FROM curso c
    INNER JOIN profesor pr ON c.profesor_DNI = pr.DNI
    INNER JOIN periodo p ON c.periodo_idperiodo = p.idperiodo;
    """
    conx.cursor.execute(query)
    lista_cursos = conx.cursor.fetchall()
    conx.cerrar_conexion()


    columnas = ("Nombre del curso", "seccion", "nombre profesor", "periodo")
    exportar_html(lista_cursos,"Lista de cursos ",columnas)
    

    
def asginar_materia(dni_profesor,id_curso):
    conx = conexion.conexion_()
    conx.cursor.execute("UPDATE curso SET profesor_DNI = %s WHERE idcurso = %s", (dni_profesor, id_curso))
    conx.database.commit()

    conx.cursor.execute("""
    SELECT c.nombre_curso, c.seccion, p.periodo
    FROM curso c
    INNER JOIN periodo p ON c.periodo_idperiodo = p.idperiodo
    WHERE c.profesor_DNI = %s
    """, (dni_profesor,))
    lista_cursos = conx.cursor.fetchall()
    conx.cursor.execute("SELECT nombres FROM profesor WHERE DNI = %s", (dni_profesor,))
    nombre = conx.cursor.fetchone()[0]


    conx.cerrar_conexion()
    columnas = ("Nombre del curso", "seccion", "periodo")
    exportar_html(lista_cursos,f"Lista de cursos del profesor {nombre}",columnas)

def opciones_crud_user(opcion,id_user,nombre_user,password_,id_rol):
    conx = conexion.conexion_()
    if opcion == 1:
        query="""
        INSERT INTO usuario (nombre_user, password_, rol_idrol)
        VALUES ( %s, %s, %s);

        """
        valores = (nombre_user, password_, id_rol)
        conx.cursor.execute(query,valores)
        conx.database.commit()
        conx.cerrar_conexion()

    elif opcion == 2:
        conx.cursor.execute("select u.id_user, u.nombre_user,r.name_rol from usuario u  INNER JOIN rol r ON  r.idrol = u.rol_idrol;")
        lista = conx.cursor.fetchall()
        conx.cerrar_conexion()
        columnas = ("id de usuario", "nombre de usuario", "rol")
        exportar_html(lista,"LISTA DE USUARIOS",columnas)
    elif opcion == 3:
        conx.cursor.execute(f"UPDATE usuario SET password_='{password_}' where id_user={id_user}")
        conx.database.commit()
        conx.cerrar_conexion()


def registrar_notas(valor,dni_alumno,idc_curso):
    conx = conexion.conexion_()
    conx.cursor.execute(f"SELECT * FROM curso_has_alumno WHERE curso_idcurso ={idc_curso} and alumno_DNI ={dni_alumno}")
    datos = conx.cursor.fetchall()
    if len(datos) != 0:
        query=""" INSERT INTO calificacion ( valor, alumno_DNI, curso_idcurso)
            VALUES (%s, %s, %s);"""

        valores = (valor, dni_alumno, idc_curso)
        conx.cursor.execute(query,valores)
        conx.database.commit()
    else:
        print("el alumno no lleva el curso")
    conx.cerrar_conexion()



def actualizar_notas(id_calificacion,valor):
    conx = conexion.conexion_()
    conx.cursor.execute(f"UPDATE calificacion SET valor={valor} where idcalificacion={id_calificacion}")
    conx.database.commit()
    conx.cerrar_conexion()


def exportar_html(lista_, titulo, columnas):
    html = f"""
    <html>
    <head>
        <title>{titulo}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f2f9ff;
                padding: 20px;
            }}
            h1 {{
                text-align: center;
                color: #0d47a1;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
                box-shadow: 0px 0px 10px #ccc;
                background-color: #ffffff;
            }}
            th, td {{
                border: 1px solid #90caf9;
                padding: 12px;
                text-align: center;
                font-size: 14px;
            }}
            th {{
                background-color: #64b5f6;
                color: white;
                font-weight: bold;
            }}
            tr:nth-child(even) {{
                background-color: #e3f2fd;
            }}
            tr:hover {{
                background-color: #bbdefb;
            }}
        </style>
    </head>
    <body>
        <h1>{titulo}</h1>
        <table>
            <tr>
    """

    # Insertar encabezados dinámicos
    for col in columnas:
        html += f"<th>{col}</th>"
    html += "</tr>\n"

    # Insertar filas de datos
    for fila in lista_:
        html += "<tr>" + "".join(f"<td>{dato}</td>" for dato in fila) + "</tr>\n"

    html += """
        </table>
    </body>
    </html>
    """

    with open("boleta.html", "w", encoding="utf-8") as f:
        f.write(html)

    webbrowser.open("boleta.html")
