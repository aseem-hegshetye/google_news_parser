<h1>google_news_parser</h1>

Django, DjangoRestFramework, Sqlite3, Vuejs, Axios, css, html, js.

Django project that parses all articles on 1st page of google news, saves them into local sqlite3 db.
Then displays a list of all those articles on homepage. When you click on any articles, you can 
see the article rendered as html, hosted on local server. We can reload new articles from google news into db
by clicking **Reload News** button on homepage. This would call a DRF API which does the job.

To run this project:

* Clone this repository into your local machine
* cd into that repo
* creates a virtual env named venv using python3.8 
  * `python3.8 -m venv venv`
* Active the venv:
  * `source venv/bin/activate`
* Install all requirements in our newly created venv:
  * `pip install -r requirements.txt`
* `python manage.py migrate`
* `python manage.py runserver`

You can run test to make sure the API is working:

`python manage.py test`

---
--- 
<div >
<h4>Homepage</h4>
<img src="https://raw.githubusercontent.com/aseem-hegshetye/google_news_parser/main/images/homepage.png" alt=""
    width="1000">
</div>
