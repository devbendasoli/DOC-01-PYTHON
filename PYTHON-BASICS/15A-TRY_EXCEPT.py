
print("-----------")
print("Bem-vindo ao programa de divisão!")
try:
    # Bloco principal que pode gerar erros
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    resultado = a / b

except ValueError:
    print("❌ Erro: Digite apenas números inteiros válidos.")

except ZeroDivisionError:
    print("❌ Erro: Não é possível dividir um número por zero.")

else:
    # 🟢 SÓ EXECUTA SE DEU TUDO CERTO (sem erros)
    print(f"✅ Sucesso! O resultado da divisão é: {resultado}")

finally:
    # 🔄 EXECUTA SEMPRE (com erro ou sem erro)
    print("🔄 Bloco finally: Operação finalizada"
    " (limpando recursos / encerrando).")

print("fim do programa.")
print("-----------")