def startfile(data):
    maincode = f'''

python3 -m venv env

. env/bin/activate

pip install -r requirements.txt

python main.py


    

    '''
    return maincode