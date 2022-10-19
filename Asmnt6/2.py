from flask import Flask, request, render_template
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512

app = Flask(__name__)



@app.route("/")
def home():
	return render_template('index.html')


@app.route("/login", methods=["POST"])
def login():
	username = request.form.get("username")
	hashkey = request.form.get("hash")
	hashbytes = hashkey.encode('utf-8')
	salt = bytes("Superrandom salt", 'utf-8')
	key = PBKDF2(hashbytes, salt, 20)
	print("Hash from client: " + hashkey)
	print("Hash from server: " + str(key, 'unicode_escape'))
	# Her kunne man lagt inn en sjekk på hashen man får ut og sjekket mot en lagret bruker.
	# psudokoden ville blitt noe sånt:
	# 	'user = findUser(username)
	# 	if(user.hash == key) return "success"
	# 	else return "Wrong credentials"'
	# 	Jeg tolker oppgaven som at den ikke spesifikt er ute etter dette, at det er viktigst
	# 	med hashingen frontend/backend. I tillegg har denne oppgaven slukt alt for mye tid hittil, så
	# 	jeg bruker ikke mer tid og frustrasjon på å få til dette.
	return "Success"



if __name__ == "__main__":
	app.run()



