from flask import Flask, render_template_string
app = Flask(__name__)
HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tchad Celib - Rencontres Tchadiennes</title>
<style>
body{font-family:Arial;background:linear-gradient(135deg,#00205B,#FFCC00,#C8102E);min-height:100vh;margin:0;padding:20px}
.card{background:white;max-width:500px;margin:20px auto;border-radius:20px;padding:30px;box-shadow:0 10px 30px rgba(0,0,0,0.3)}
h1{text-align:center;color:#00205B} h1 span{color:#C8102E}
.btn{background:#00205B;color:white;border:none;padding:15px;width:100%;border-radius:10px;font-size:18px;font-weight:bold;cursor:pointer;margin-top:15px}
.btn:hover{background:#C8102E}
input,select{width:100%;padding:12px;margin:8px 0;border-radius:8px;border:1px solid #ccc;box-sizing:border-box}
.profile{background:#f8f9fa;padding:15px;border-radius:10px;margin:10px 0;display:flex;gap:15px;align-items:center}
.profile img{width:60px;height:60px;border-radius:50%}
.badge{background:#FFCC00;color:#00205B;padding:3px 8px;border-radius:10px;font-size:12px;font-weight:bold}
</style>
</head>
<body>
<div class="card">
<h1>🇹🇩 Tchad <span>Celib</span></h1>
<p style="text-align:center;color:#666">Le 1er site de rencontres 100% Tchadien</p>
<div id="form">
<h3>Créer ton profil</h3>
<input id="nom" placeholder="Ton prénom">
<select id="ville"><option>N'Djamena</option><option>Moundou</option><option>Sarh</option><option>Abéché</option><option>Diaspora</option></select>
<select id="age"><option>18-25 ans</option><option>26-35 ans</option><option>36-45 ans</option></select>
<button class="btn" onclick="inscrire()">Voir les célibataires ❤️</button>
</div>
<div id="list" style="display:none">
<h3>Célibataires près de toi 🔥</h3>
<div class="profile"><img src="https://i.pravatar.cc/100?img=5"><div><b>Aicha, 24 ans</b> <span class="badge">N'Djamena</span><br><small>Relation sérieuse</small></div></div>
<div class="profile"><img src="https://i.pravatar.cc/100?img=8"><div><b>Moussa, 28 ans</b> <span class="badge">Moundou</span><br><small>Entrepreneur</small></div></div>
<div class="profile"><img src="https://i.pravatar.cc/100?img=26"><div><b>Zara, 22 ans</b> <span class="badge">Sarh</span><br><small>Étudiante</small></div></div>
<div class="profile"><img src="https://i.pravatar.cc/100?img=12"><div><b>Brahim, 31 ans</b> <span class="badge">Diaspora</span><br><small>En France</small></div></div>
<button class="btn" onclick="location.reload()">Retour</button>
<p style="text-align:center;margin-top:20px;font-size:13px;color:#888">Site créé par Ramadji - ramadji275 • 2026</p>
</div>
</div>
<script>
function inscrire(){
 let n=document.getElementById('nom').value;
 if(!n){alert('Mets ton prénom!');return;}
 document.getElementById('form').style.display='none';
 document.getElementById('list').style.display='block';
}
</script>
</body>
</html>
"""
@app.route('/')
def home():
    return render_template_string(HTML)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
