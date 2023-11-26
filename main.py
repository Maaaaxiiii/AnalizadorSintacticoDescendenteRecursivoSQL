from MiScanner import MiScanner
from ASDR import ASDR
class Principal:
    existen_errores = False

    @staticmethod
    def main():
        Principal.ejecutar_prompt()

    @staticmethod
    def ejecutar_prompt():
        while True:
            try:
                linea = input(">>> ")
                if not linea:
                    break  # Presionar Ctrl + D
                Principal.ejecutar(linea)
                Principal.existen_errores = False
            except EOFError:
                break

    @staticmethod
    def ejecutar(source):
        scanner = MiScanner(source)
        tokens = scanner.scan_tokens()

        parser = ASDR(tokens)
        resultado = parser.parse()

        if resultado:
            print("Consulta SQL válida.")
        else:
            print("Consulta SQL inválida.")

    @staticmethod
    def error(linea, mensaje):
        Principal.reportar(linea, "", mensaje)

    @staticmethod
    def reportar(linea, donde, mensaje):
        print(f"[linea {linea}] Error {donde}: {mensaje}")
        Principal.existen_errores = True

if __name__ == "__main__":
    Principal.main()