# PythonOpenSource

  ```
  # tworzymy środowisko dla pythona
  > python -m venv .venv

  # aktywujemy środowisko
  > source .venv/Scripts/activate
  > pip install -r requirements.txt

  # zobacz czy jest zainstalowanie
  > pip list
  ```

- Uruchamianie applikacji:

  ```
  > set FLASK_APP=helloworld.py
  > python helloworld.py
  ```

- Aktywacja środowiska hermetycznego.

  ```
  # deaktywacja
  > deactivate
  ```

  ```
  ...

  # aktywacja 
  > source .venv/bin/activate
  ```
