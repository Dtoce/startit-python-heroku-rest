from flask import Flask, request, render_template
import json
# šī rinda laikam palaiž mūsu kodu kā flask api
app = Flask(__name__)

# Uzstada test.html ka nokluseto web lapas sākumu.
@app.route('/')
def root():
    return render_template('test.html')

@app.route('/api/rezultati')
def rez():
    vards=request.args.get("vards")
    punkti=request.args.get("punkti")
    f=open('static/vardi.txt','r')
    saraksts=json.load(f)
    f.close()
    jauns={"vards":vards,"punkti":int(punkti)}
    saraksts.append(jauns)
    f=open('static/vardi.txt','w')
    json.dump(saraksts,f)
    f.close()
    response = {
        'rezultati': sorted(saraksts,key=lambda vi: vi["punkti"])
    }
    return json.dumps(response)

app.run(host='0.0.0.0', port=8080)

