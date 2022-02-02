from django.dispatch import Signal

notificar = Signal(providing_args=['nivel', 'destino', 'actor', 'verbo', 'create_at'])