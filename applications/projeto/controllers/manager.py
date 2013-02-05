# if not auth.has_membership("admin"):
#     redirect(URL('initial', 'home'))

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

@auth.requires_membership("admin")
def user():
    grid = SQLFORM.grid(db.auth_user)
    return dict(grid=grid)

@auth.requires_membership("admin")
def posts():
	#Post.post_date.represent = lambda v, row: prettydate(v)    

    grid = SQLFORM.grid(db.post)
    return dict(grid=grid)

