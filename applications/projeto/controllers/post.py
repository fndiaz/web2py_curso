def show():
	return "post"

def edit():
	return dict(form=SQLFORM(db.post, 
							request.args(0, cast=int or redirect(URL('post')))).process())

def delete():
	return "delete"

@auth.requires(auth.has_membership("admin") or auth.has_membership("editor"))
def add():
	form = SQLFORM(db.post)
	print form

	if form.process().accepted:
		response.flash = "Sucesso"
	elif form.errors:
		response.flash = "erro"
	else:
		response.flash = "Preencha o form"

	return dict(form=form)



def add2():
	form = SQLFORM(db.post)
	print form

	if form.process().accepted:
		response.flash = "Sucesso"
	elif form.errors:
		response.flash = "erro"
	else:
		response.flash = "Preencha o form"

	return dict(form=form)

