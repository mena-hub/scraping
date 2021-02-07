#### Incremental crawler with Scrapy and MongoDB
*por Adrien Di Pasquale*

**¿Qué vamos a aprender?**
- How to scrape
- Export the items to a JSON file
- Store items in database

**¿Nos hace falta algo?**
- [Python 3.6 +](https://www.python.org/)
- [Scrapy](https://doc.scrapy.org/en/latest/index.html)
- [MongoDB](https://www.mongodb.com/)
- [PyMongo](https://pypi.org/project/pymongo/)
- [Website](https://andreaga.com/)


**¿A quién va dirigido este taller?**

Con echarle un vistazo a la documentación basta.

**Algunos comandos utilizados**

SCRAPY

Globales 

```zsh
» scrapy startproject <project_name> [project_dir]
» cd project_dir
» scrapy genspider [-t template] <name> <domain>
```
<details>
<summary markdown="span">Ver</summary>

```zsh
» scrapy startproject website_scraper .
» website_scraper
» scrapy genspider andreaga andreaga.com/blog
```
</details>

```zsh
» scrapy shell [url]
```
<details>
<summary markdown="span">Ver</summary>

```zsh
» scrapy shell http://andreaga.com/blog
```
</details>

Del proyecto

```zsh
» scrapy crawl <spider>
» scrapy crawl <spider> -a 
```
<details>
<summary markdown="span">Ver</summary>

```zsh
» scrapy crawl andreaga
» scrapy crawl andreaga -a limit_pages=2
```
</details>

Exportación

```zsh
» scrapy crawl <spider_name> -a -o "%(spider_name)s.json"
```
<details>
<summary markdown="span">Ver</summary>

```zsh
» scrapy crawl andreaga -a limit_pages=2 -o posts.json
» cat posts.json| jq
```
</details>

MONGO

[Ir al posteo original](https://blog.dipasquale.fr/)

**NOTA**

Se utilizó el tutorial como referencia. El resultado final difiere del contenido original. Si bien la aproximación al tema es la misma, el código fue ligeramente modificado, personalizado, para un mejor entendimiento.