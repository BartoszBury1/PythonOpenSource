# PythonOpenSource

  ```
  # tworzymy środowisko dla pythona
  $ python -m venv .venv

  # aktywujemy środowisko
  $ source .venv/Scripts/activate
  $ pip install -r requirements.txt
  $ pip install -r test_requirements.txt

  # zobacz czy jest zainstalowanie
  $ pip list
  ```

- Uruchamianie applikacji:

  ```
  $ PYTHONPATH=. FLASK_APP=hello_world flask run
  ```

- Kontynuując pracę z projektem, aktywowanie hermetycznego środowiska dla aplikacji py:

  ```
  # deaktywacja
  $ deactivate
  ```

  ```
  ...

  # aktywacja 
  $ source .venv/bin/activate
  ```
