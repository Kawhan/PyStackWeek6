<h1 align="center">PyStackWeek6 </h1>

## 🖥️ Descrição do projeto 

O sistema giram em torno de uma necessidade vista por mim (Kawhan) em ajudar os professores que disponibilizam oportunidades de bolsas, emprego, mestrado e etc, voltado para os alunos do Campus IV. Então, vendo essa oportunidade, criei uma API para gerenciar cadastro de informações de vagas e permitir que os alunos se inscrevam em uma determinada vaga, além de disponibilizar end-poins para o contato direto de várias informações. Planejo também deixar o projeto open source caso algum aluno deseje criar algo que consuma a api ou melhorar cada vez mais a ideia inicial, criando oportunidade de contrinbuir com a oportunidade open source e também incentivando os alunos para que utilizem do conhecimento que tem para gerar soluções viaveis para faculdade em que estudam.


The system revolves around a need seen by me (Kawhan) in helping professors who provide opportunities for scholarships, jobs, master's degrees, etc., aimed at Campus IV students. So, seeing this opportunity, I created an API to manage vacancy information registration and allow students to enroll in a given vacancy, in addition to providing end-points for direct contact of various information. I also plan to leave the project open source in case any student wants to create something that consumes the api or increasingly improve the initial idea, creating an opportunity to contribute to the open source opportunity and also encouraging students to use the knowledge they have to generate solutions viable for the college where they study.

## 🖥️ Descrição do projeto FULL STACK DJANGO TEMPLATE
O sistema ganhou uma versõa com django full stack template que tem as mesmas funcionalidades da API utilizando django rest_framework, porém, adicionando funcionalidades em HTML e CSS3 para produzir algo visual ou front-end, a web page foi construido usando boostrap, html 5, CSS3 e JS juntamente com funcionalidades do django template. O objetivo dessa parte do projeto foi aprensetar o que seria um primeiro MVP utilizando tecnicas de web design e responsividade, trazendo um aspecto de simplicidade para o produto, visando também atingir o máximo possivel dos estudantes e professores do CAMPUS IV.


The system gained a version with django full stack template that has the same functionality as the API using django rest_framework, however, adding functionality in HTML and CSS3 to produce something visual or front-end, the web page was built using boostrap, html 5, CSS3 and JS along with django template functionality. The objective of this part of the project was to show what a first MVP would be using web design and responsiveness techniques, bringing an aspect of simplicity to the product, also aiming to reach the maximum possible number of students and professors of CAMPUS IV.

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

