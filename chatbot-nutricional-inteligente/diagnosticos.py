import sys
import os

print("--- RELATÓRIO DE DIAGNÓSTICO ---")
print(f"1. Python que está rodando: {sys.executable}")
print(f"2. Pasta onde estou: {os.getcwd()}")
print("\n3. Teste de Importação:")

try:
    import langchain_google_genai
    print("   ✅ SUCESSO! O pacote 'langchain_google_genai' foi encontrado.")
    print(f"   Local: {langchain_google_genai.__file__}")
except ImportError as e:
    print(f"   ❌ FALHA: {e}")

try:
    import langchain
    print("   ✅ SUCESSO! O pacote 'langchain' foi encontrado.")
except ImportError as e:
    print(f"   ❌ FALHA: {e}")

print("\n4. Bibliotecas instaladas neste Python (primeiras 20):")
try:
    from pip._internal.operations import freeze
    pkgs = list(freeze.freeze())
    for pkg in pkgs[:20]: print(f"   - {pkg}")
except:
    print("   (Não foi possível listar com pip interno)")