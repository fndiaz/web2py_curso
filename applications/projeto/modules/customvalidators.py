# coding: utf-8

class IS_NOT_CONTEUDO(object):
    def __init__(self, error_message="conteúdo bloqueado"):
        self.error_message = error_message

    def __call__(self, value):
        # (value, error_message) # invalido
        # (value, None) # valido
        # strip() = sem espaço vazio
        # lower() = maiusculo e minusculo
        if "merda" in value.strip().lower():
            return (value, self.error_message)
        else:
            return (value, None)



