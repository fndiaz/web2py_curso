# coding: utf-8

def home():
	posts = db(db.post.is_draft == False).select(orderby=~db.post.created_on);
	print posts
	response.title = "Titulo home"
	nome = "fernando"
	return dict(posts=posts, nome=nome)
	
	


def contact():
	return "form"

def about():
	return "sobre"

def user():
	if request.args(0) == 'register':
        	db.auth_user.bio.writable = db.auth_user.bio.readable = False
	return dict(user=auth())

def register():
	return auth.register()

def login():
        return auth.login()

def account():
    return dict(register=auth.register(),
                login=auth.login())
	
def download():
	return response.download(request, db)





def exemplo():
#	return "teste"
	return response.render("default/teste.html", nome="deld", sobrenome="vieira", lista=["item1", "item2", "item3"])

def teste1():
	print "Action index"
	print request.args
	print request.vars 	
	print request.post_vars #somente entradas de formulário
    	print request.get_vars  #somente entradas de url
    	#nome = request.vars['nome']
        mensagem = "Bem Vindo"
        form = "<form action='' method='POST'><input name='nome' id='nome'/><input type='Submit'></form><br>"
        if 'nome' in request.vars:
		form = "<p>Bem vindo %(nome)s</p>" % request.vars + form		
		#mensagem = mensagem + " usuário %(nome)s" % request.vars	#mostrando variavel da url
        	#mensagem = mensagem + " usuário %s" %str(nome)			#mostrando uma variavel local    
	return form

def teste2():
	return "<form><label>Nome</label><input /></form><br><a href='http://www.w3schools.com'>Visit W3Schools</a>"
	#return dict(nome="fernando")
	#return response.render("teste.html", dict(nome="fernando"))

def soma(x, y):
	return x + y

 
