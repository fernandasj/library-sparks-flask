from flask import render_template, request, redirect, url_for

from app import app
from app.forms import ReservaForm, EmprestarForm
from app.conn import get_connection, get_cursor

# ============================
# home
# ============================


@app.route('/')
@app.route('/home')
def home():
    conn = get_connection()
    cur = get_cursor(conn)

    cur.execute("""SELECT * FROM reserva WHERE id_usuario = 1""")
    reservas = cur.fetchall()

    cur.execute("""SELECT * FROM emprestimo WHERE id_usuario = 1""")
    emprestimos = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('home.html', reservas=reservas, emprestimos=emprestimos)

#  ============================
#  Reserva
# =============================


@app.route('/reservar_livro', methods=['POST', 'GET'])
def reservar_livro():

    conn = get_connection()
    cur = get_cursor(conn)

    form = ReservaForm()

    if request.method == 'POST':
        conn = get_connection()
        cur = get_cursor(conn)

        Id_usuario = request.form['Id_usuario']
        Id_livro = request.form['Id_livro']

        cur.execute("""INSERT INTO reserva (id_usuario, id_livro) VALUES ('%s', '%s')""" % (Id_usuario, Id_livro))

        cur.execute("""UPDATE livro SET status = 'reservado' WHERE id_livro = '%s'""" % Id_livro)

        conn.commit()

        return redirect(url_for('home'))

        cur.close()
        conn.close()

    cur.execute("""SELECT * FROM usuario""")
    usuarios = cur.fetchall()

    cur.execute("""SELECT * FROM livro WHERE status = 'emprestado' or status = 'disponivel'""")
    livros = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('add_reserva.html', form=form, livros=livros, usuarios=usuarios)


@app.route('/cancelar_reserva/<id_reserva>', methods=['GET'])
def cancelar_reserva(id_reserva):

    conn = get_connection()
    cur = get_cursor(conn)

    cur.execute("""SELECT id_livro FROM reserva WHERE id_reserva = '%s'""" % id_reserva)
    id_livro = cur.fetchone()

    cur.execute("""UPDATE livro SET status = 'disponivel' WHERE id_livro = '%s'""" % id_livro[0])

    cur.execute("""DELETE FROM reserva WHERE Id_reserva = '%s'""" % id_reserva)

    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for('home'))


# ===============================
# Livros
# ===============================


@app.route('/livros')
def livros():
    conn = get_connection()
    cur = get_cursor(conn)

    cur.execute("""SELECT * FROM livro """)
    livros = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('livros.html', livros=livros)


# ==============================
# Emprestar
# ==============================


@app.route('/emprestar_livro', methods=['POST', 'GET'])
def emprestar_livro():
    conn = get_connection()
    cur = get_cursor(conn)

    form = EmprestarForm()

    if request.method == 'POST':
        conn = get_connection()
        cur = get_cursor(conn)

        Id_usuario = request.form['Id_usuario']
        Id_livro = request.form['Id_livro']
        Data_emprestimo = request.form['Data_emprestimo']

        cur.execute("""INSERT INTO emprestimo (id_usuario, id_livro, data_emprestimo) VALUES ('%s', '%s', '%s')""" % (Id_usuario, Id_livro, Data_emprestimo))

        cur.execute("""UPDATE livro SET status = 'emprestado' WHERE id_livro = '%s'""" % Id_livro)

        conn.commit()

        return redirect(url_for('home'))

        cur.close()
        conn.close()

    cur.execute("""SELECT * FROM usuario""")
    usuarios = cur.fetchall()

    cur.execute("""SELECT * FROM livro WHERE status = 'reservado' or status = 'disponivel'""")
    livros = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('emprestimo.html', form=form, livros=livros, usuarios=usuarios)


@app.route('/devolver_livro/<id_emprestimo>', methods=['GET'])
def devolver_livro(id_emprestimo):

    conn = get_connection()
    cur = get_cursor(conn)

    cur.execute("""SELECT id_livro FROM emprestimo WHERE id_emprestimo = '%s'""" % id_emprestimo)
    id_livro = cur.fetchone()

    cur.execute("""UPDATE livro SET status = 'disponivel' WHERE id_livro = '%s'""" % id_livro[0])

    cur.execute("""DELETE FROM emprestimo WHERE Id_emprestimo = '%s'""" % id_emprestimo)

    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for('home'))



if __name__ == '__main__':
    app.debug = True
    app.run()
