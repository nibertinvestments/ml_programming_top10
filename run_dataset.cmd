@echo off
setlocal
set PYTHON=C:\Users\jnibe\AppData\Local\Programs\Python\Python312\python.exe
"%PYTHON%" "%~dp0generate_large_corpus_v2.py"
"%PYTHON%" "%~dp0validate_large_corpus_v2.py"
