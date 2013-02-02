from gluon.storage import Storage

config = Storage(
        db=Storage(),
        auth=Storage(),
        mail=Storage()
        )

config.db.uri = "sqlite://projeto.sqlite"
config.db.pool_size = 10
config.db.check_reserved = ['all']


db = DAL(**config.db)

# logging
import logging
logger = logging.getLogger("web2py.app.blog")
logger.setLevel(logging.DEBUG)

#auth Rbac
from gluon.tools import Auth

auth = Auth(db, controller="initial", function="user")

#settings
auth.settings.remember_me_form = False
auth.settings.formstyle = "divs"
auth.settings.login_next = URL('initial', 'home')
auth.settings.registration_requires_verification = True
auth.settings.registration_requires_approval = True
#auth.settings.actions_disabled = ['register']

#mail
mail = auth.settings.mailer
mail.settings.server = "mail.ad2.com.br"
mail.settings.sender = "fernando@ad2.com.br"
mail.settings.login = "fernando@ad2.com.br:123456"

#signals
def notifica(form):
	logger.info("notifica")
	mail.send(
		to="fndiaz02@gmail.com",
		subject="Usuario %(first_name)s pendente" % form.vars,
		message="<html>Voce tem um novo usuario para aprovacao %(first_name)s %(last_name)s </html>" % form.vars
	)

auth.settings.register_onaccept = notifica
#auth.settings.register_onaccept = funcao

#messages
auth.messages.login_button = "Entrar"

#fields
auth.settings.extra_fields['auth_user'] = [
	Field("bio", "text"),
	Field("photo", "upload"),
	Field("gender", requires=IS_IN_SET(["masculino","feminino"]))
]

#janrain
#from gluon.contrib.login_methods.rpx_account import use_janrain
#use_janrain(auth, filename="private/janrain.key")

auth.define_tables(username=False)

#genericas views
if request.is_local:
	response.generic_patterns = ['*']

#response
response.title = "Meu site magnifico"
response.subtitle = "O blog do sheldon"
response.meta.keywords = "chave, outra, e utra"
response.meta.description = "blog do shedon"