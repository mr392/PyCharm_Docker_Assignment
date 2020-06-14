FROM python:3

ADD src /src

RUN pip install pyfiglet

RUN pip install colorama

RUN pip install termcolor

CMD [ "python", "./src/my_script.py" ]