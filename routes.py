routers = dict(

    # base router
    BASE=dict(
        default_application='projeto',
    ),

    projeto=dict(
        default_controller='initial',
        default_function='home',
        functions=['home', 'contact', 'about', 'user', 'download', 'account', 'register', 'login', 'exemplo', 'teste1', 'teste2'],
    )

)
