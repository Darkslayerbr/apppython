import sqlite3

from flask import Flask, render_template,request, redirect, flash
from flask_bootstrap import Bootstrapw
app=Flask(__name__)
##inicialização
bootstrap=Bootstrap(app)

@app.route('/')
def index():
	return render_template('1.tpl')
	
@app.route('/marcas')
def lista_marcas():
	with sqlite3.connect('automoveis.db') as conn:
		c=conn.cursor()
		sql="SELECT * FROM marca"
		c.execute(sql)
		dados=c.fetchall()
	return render_template('lista_marcas.tpl',dados=dados)

@app.route('/marca/ins',methods=['GET'])
def ins_marca_get():
	return render_template('marca_ins.tpl')
	
@app.route('/marca/ins',methods=['POST'])
def ins_marca_post():
	nome= request.form.get('nome')
	presidente= request.form.get('presidente')
	origem= request.form.get('origem')
	fundacao= request.form.get('fundacao')
	with sqlite3.connect("automoveis.db") as conn:
		c=conn.cursor()
		sql="""INSERT INTO marca	
				(nome, presidente, origem, fundacao)
				VALUES
				(?,?,?,?)"""
		c.execute(sql,(nome,presidente,origem,fundacao))
		c.close
	return redirect('/marcas')
#EDIT
@app.route('/marca/edit/<_id_>',methods=['GET'])
def edit_get_marcas(_id_):
     with sqlite3.connect("automoveis.db") as conn:
          c = conn.cursor()
          sql = "SELECT * FROM marca WHERE id=?"
          c.execute(sql,(_id_,))
          dados = c.fetchone()
     return render_template('editar.tpl',dados = dados)

@app.route('/marca/edit/<_id_>',methods=['POST'])
def edit_post_marcas(_id_):
	id = _id_
	nome = request.form.get('nome')
	presidente = request.form.get('presidente')
	origem = request.form.get('origem')
	fundacao = request.form.get('fundacao')
	with sqlite3.connect('automoveis.db') as conn:
		c = conn.cursor()
		sql = """UPDATE marca set nome=?, 
		                          presidente=?,
								  origem=?, 
								  fundacao=?
								  WHERE id=?"""
		c.execute(sql,(nome,presidente,origem,fundacao,id))
		c.close()
		#flash("Editado com sucesso.")
		return redirect("/marcas")

#################### VIEW

@app.route('/marca/view/<int:_id_>',methods=['GET'])
def view_get_marcas(_id_):
	with sqlite3.connect("automoveis.db") as conn:
		c = conn.cursor()
		sql = "select * from marca where id =?"
		c.execute(sql,(_id_,))
		dados = c.fetchone()
		return render_template('view.tpl', dados = dados)


###################DELETE
@app.route('/marca/del/<int:_id_>',methods=['GET'])
def delete_get_marcas(_id_):
	with sqlite3.connect("automoveis.db") as conn:
		c = conn.cursor()
		sql = "select * from marca where id =?"
		c.execute(sql,(_id_,))
		dados = c.fetchone()
		return render_template('delete.tpl', dados = dados)

@app.route('/marca/del', methods=['POST'])
def del_post_marcas():
	_id_=request.form.get('id')
	print(_id_)
	with sqlite3.connect("automoveis.db") as conn:
		c = conn.cursor()
		sql = "delete from marca where id =?"
		c.execute(sql,(_id_,))
		c.close()
	return redirect('/marcas')

if __name__=='__main__':
    app.run()
