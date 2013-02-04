@auth.requires_login()
def category():
	form = SQLFORM(db.category, formstyle='divs', submit_button='Enviar', _class='admform', _id='formblog')

	if form.process().accepted:
		response.flash = "Sucesso"
	elif form.errors:
		response.flash = "erro"
	else:
		response.flash = "Preencha o form"

	return dict(form=form)

@auth.requires_membership('admin')
def blogs():
	form = SQLFORM(db.blog, formstyle='divs', submit_button='Enviar', _class='admform', _id='formblog')

	if form.process().accepted:
		response.flash = "Sucesso"
	elif form.errors:
		response.flash = "erro"
	else:
		response.flash = "Preencha o form"

	return dict(form=form)