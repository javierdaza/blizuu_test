### Blizuu Test

Para correr este proyecto localmente, es necesario crear un archivo `.env` en la raíz del proyecto con la siguiente informacion:

```
DJANGO_SECRET_KEY='12345567'
DJANGO_READ_DOT_ENV_FILE=True
DJANGO_DEBUG=True
```

**coverage**
```
Name                             Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------------
proyecto/urls.py                     3      0      0      0   100%
seegithub/admin.py                   5      0      0      0   100%
seegithub/models.py                 15      0      0      0   100%
seegithub/tests/test_models.py      23      0      0      0   100%
seegithub/tests/test_urls.py        10      0      0      0   100%
seegithub/tests/test_views.py       21      0      0      0   100%
seegithub/urls.py                    6      0      0      0   100%
seegithub/views.py                  73     20     24      5    66%
------------------------------------------------------------------
TOTAL                              156     20     24      5    82%
```