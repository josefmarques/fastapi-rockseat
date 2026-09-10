class ContextoSimples:
    def __enter__(self):
        print("Iniciar conexão com o banco de dados")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Fechar conexão com o banco de dados")

with ContextoSimples() as cs:
    print("Executando operações no banco de dados")