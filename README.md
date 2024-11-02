# Sintonize
O Sintonize é um espaço que oferece funcionalidades focadas na saúde mental em relação ao trabalho. Nossa plataforma ajuda você a identificar e gerenciar o estresse, além de fornecer ferramentas práticas para melhorar sua saúde mental e manter o equilíbrio entre sua vida pessoal e profissional.

# Dependências
Instalar o Python - https://www.python.org/downloads/

# Instalação
- Clone do projeto
```ruby
git clone https://github.com/ProjetoSafira/Sintonize.git
```

# No windows

## Instalar pacote pip
``` ruby
python -m pip install --upgrade pip --user
```

## Instalar as dependências
- Na pasta `raiz` execute:
``` ruby
pip3 install -r requirements.txt
```

## Executar aplicação
- Na pasta `raiz` execute:
``` ruby
python manage.py runserver
```
- Abra no navegador: http://127.0.0.1:8000

# Com Makefile

## Instalar Chocolatey
- Abra o PowerShell como Administrador e execute o seguinte comando:
``` ruby
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

## Instalar Makefile
- Abra o PowerShell como Administrador e execute o seguinte comando:
``` ruby
choco install make
```

## Instalar Dependências
- Na pasta `raiz` execute:
``` ruby
make install
```

## Executar aplicação
- Na pasta `raiz` execute:
``` ruby
make run
```
- Abra no navegador: http://127.0.0.1:8000


# No mac

## Iniciar virtual venv
- Na pasta `raiz` execute:  
``` ruby
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
```

# Instalar Dependências
- Na pasta `raiz` execute:  
``` ruby
pip3 install django
```

# Executar aplicação
- Na pasta `raiz` execute:
``` ruby
python manage.py runserver
```
- Abra no navegador: http://127.0.0.1:8000

