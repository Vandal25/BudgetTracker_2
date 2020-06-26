=================================== Tutorial ====================================

Aplicatia e web si se deschide din consola cu comanda:
 python manage.py runserver

Nu l-am testat pe Windows dar, teoretic ar trebui sa mearga bine legaturile.
Daca nu gaseste django: python -m pip install django

Dupa aprinderea aplicatiei o sa apara un o pagina de register/login.
Un cont deja creat e admin si parola admin.

Dupa intrarea in cont in meniul aflat in dreapta sus o sa apara 3 optiuni noi:
  -profile: De aici se poate reseta parola. Nu o sa mearga by default pentu ca
              nu este configrurat, din motive evidente, mailul de pe care
              trimite linkul de resetare. Poate fi configurat din ultimele linii
              de cod din fisierul settings.py aflat in folderul BudgetTrackerV2

  -new transaction: Aici se poate crea o noua tranzactie. Daca se alege varianta
              de a primi bani optiunea 'Transaction type' nu va mai conta.

  -statistics: Dupa adaugarea de tranzatii aici se va putea ,vizualiza pe un
                grafic, in ce mod au fost cheltiuti banii

Pe pagina principala se poate vedea suma ramasa de bani ,dar si sumela de banii
primita/cheltuita. Sub acestea se afla tranzactiile. Fiecare are o iconita
reprezentativa pentru categoria de produse platite. Numarul verde reprezinta
banii primiti, iar cel cu rosu sunt cei cheltiuti. Pe centru este trecut
destinatarul/expeditorului si data de efectuare a tranzactiei. Se poate da
click pe tranzactii pentu a le putea edita (data va ramane cea initiala).
De asemenea tranzactiile pot fi sterse din acelasi meniu.

In fisierul test.log se vor regasi datele trimise de logger.

================================== Tehnologii ===================================

Aplicatia este in principal realizata cu ajutorul framework-ului django. Acestea
este bazat pe limbajul pyton. Partea de interfata este realizata cu ajutorul
html si CSS(Bootstrap). Formularele sunt realizate cu django crispy forms
Graficul este realizat cu ajutorul librariei de Java Script, ZingChart.
Baza de date este una PostgreSQL si este hostata pe ElephantSQL.

=================================================================================
