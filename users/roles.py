from rolepermissions.roles import AbstractUserRole

class   CLIENTE(AbstractUserRole):
    available_permissions = {}


class ADMINISTRADOR(AbstractUserRole):
    available_permissions = {}


class GERENTE(AbstractUserRole):
    available_permissions = {}
