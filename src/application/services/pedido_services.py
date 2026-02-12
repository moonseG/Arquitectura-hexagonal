class OrderService:

    def __init__(self, order_repo, user_repo):
        sel.order_repo = order_repo
        self.user_repo = user_repo

        #caso de uso: crear orden
        def create_order(self, order_data):
            user = self.user_repo.find_by_id(order_data.idusuario)
            if not user:
                raise ValueError("Usuario no encontrado")
            return self.order_repo.create(order_data)

        def get_all(self):
            return self.order_repo.find_all()

        def get_by_user(self, idusuario):
            return self.order_repo.find_by_user(idusuario)

            def update_status(self, idpedido, status):
                return self.order_repo.update_status(idpedido, status)

                