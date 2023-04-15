<h1 align="center">TypeEvent </h1>

## 🖥️ Descrição do projeto 

Sistema de cadastro de vagas que permite que pessoas cadastrem eventos na plataforma e disponibilizem para pessoas se inscreverem neles, nesse mesmo sistema possui um gerenciamento de certificados e csvs gerados. Por fim, possui também um sistema de login e registro para usuários da plataforma.

## 🖥️ Project description
Vacancy registration system that allows people to register events on the platform and make them available for people to register for them, in this same system it has a management of certificates and generated csvs. Finally, it also has a login and registration system for platform users.

---


## 📌 Funcionalidades
```
1° Cadastro de eventos
2° Login e registro
3° Criação de certificados
4° Download de certificados
5° Criação de csv das pessoas inscritas no evento
6° Sistema de inscrições em eventos
```


## 🛠️ Usabilidade do código do sistema / system code usability

- Criação do ambiente virtual:
```
python -m venv 

venv\Scripts\activate.ps1                        //Ativar ambiente virtual (powershell)
source venv\Scripts\activate                     //Ativar ambiente virtual (ubuntu)
python -m pip install --upgrade pip             //Atualizar pip
pip install -r requirements.txt                //Instalar dependências
python manage.py migrate                      //Sincronizar database
python manage.py createsuperuser             //Criar um super usuário
python manage.py runserver                  //Iniciar o servidor

```
---

## ✔️ Tecnologias utilizadas | Práticas utilizadas | Technologies used | Practices used

- Python (Django) 
- HTLML 5
- CSS 3
- Bootstrap 5
- Django template

