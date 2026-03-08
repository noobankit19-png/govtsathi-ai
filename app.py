from flask import Flask, request, render_template_string

app = Flask(__name__)

# ---------------- SCHEME DATABASE ----------------

schemes = [
{"name":"PM Kisan Samman Nidhi","occupation":"Farmer","income":500000,"category":"All","state":"All"},
{"name":"Ayushman Bharat","occupation":"All","income":300000,"category":"All","state":"All"},
{"name":"PM Mudra Loan","occupation":"Business","income":800000,"category":"All","state":"All"},
{"name":"Startup India","occupation":"Business","income":1000000,"category":"General","state":"All"},
{"name":"National Scholarship","occupation":"Student","income":400000,"category":"SC","state":"All"},
{"name":"Skill India Mission","occupation":"Unemployed","income":500000,"category":"All","state":"All"},
]

# ---------------- AI LOGIC ----------------

def recommend(age,income,occupation,category,state):

    results=[]

    for s in schemes:

        if s["occupation"]=="All" or s["occupation"]==occupation:

            if income <= s["income"]:

                if s["category"]=="All" or s["category"]==category:

                    if s["state"]=="All" or s["state"]==state:

                        results.append(s["name"])

    if not results:
        results=["No matching schemes found"]

    return results


# ---------------- HTML ----------------

page = """

<!DOCTYPE html>
<html>

<head>

<title>GovtSathi AI</title>

<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

body{
margin:0;
font-family:Arial;
background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

/* container */

.container{
display:flex;
justify-content:center;
align-items:center;
min-height:100vh;
padding:20px;
}

/* card */

.box{
background:rgba(255,255,255,0.08);
padding:40px;
border-radius:15px;
width:100%;
max-width:850px;
text-align:center;
box-shadow:0 0 20px rgba(0,0,0,0.4);
}

/* logo */

.logo{
font-size:30px;
margin-bottom:10px;
}

/* form layout */

.form-grid{
display:grid;
grid-template-columns:1fr 1fr;
gap:15px;
}

input,select{
padding:12px;
border-radius:8px;
border:none;
width:100%;
}

/* button */

button{
background:#27ae60;
color:white;
border:none;
padding:14px;
font-size:18px;
border-radius:10px;
cursor:pointer;
transition:0.3s;
width:100%;
margin-top:10px;
}

button:hover{
background:#2ecc71;
}

/* result */

.result{
margin-top:20px;
padding:20px;
background:rgba(0,0,0,0.3);
border-radius:10px;
}

/* language buttons */

.lang{
position:absolute;
top:15px;
right:15px;
}

.lang a{
background:#27ae60;
padding:7px 12px;
color:white;
text-decoration:none;
border-radius:6px;
margin-left:5px;
}

/* MOBILE RESPONSIVE */

@media(max-width:768px){

.form-grid{
grid-template-columns:1fr;
}

.box{
padding:25px;
}

.logo{
font-size:24px;
}

}

</style>

</head>

<body>

<div class="lang">
<a href="/?lang=en">English</a>
<a href="/?lang=hi">हिन्दी</a>
</div>

<div class="container">

<div class="box">

<div class="logo">🇮🇳 GovtSathi</div>

<h1>{{title}}</h1>
<p>{{subtitle}}</p>

<form method="POST">

<div class="form-grid">

<input type="number" name="age" placeholder="{{age}}" required>

<input type="number" name="income" placeholder="{{income}}" required>

<select name="occupation">
<option>Student</option>
<option>Farmer</option>
<option>Business</option>
<option>Unemployed</option>
</select>

<select name="category">
<option>General</option>
<option>OBC</option>
<option>SC</option>
<option>ST</option>
</select>

<select name="state">
<option>All</option>
<option>Haryana</option>
<option>Delhi</option>
<option>Punjab</option>
<option>Rajasthan</option>
<option>Uttar Pradesh</option>
<option>Maharashtra</option>
</select>

</div>

<button type="submit">{{button}}</button>

</form>

{% if schemes %}

<div class="result">

<h2>{{result}}</h2>

<ul>

{% for s in schemes %}
<li>{{s}}</li>
{% endfor %}

</ul>

</div>

{% endif %}

</div>

</div>

</body>

</html>

"""

# ---------------- ROUTE ----------------

@app.route("/",methods=["GET","POST"])
def home():

    lang=request.args.get("lang","en")

    if lang=="hi":

        text={
        "title":"AI आधारित सरकारी योजना सुझाव",
        "subtitle":"अपने लिए सही योजना खोजें",
        "age":"आयु",
        "income":"वार्षिक आय",
        "button":"योजना खोजें",
        "result":"आपके लिए योजनाएँ"
        }

    else:

        text={
        "title":"AI Powered Government Scheme Recommendation",
        "subtitle":"Find the best schemes for yourself",
        "age":"Age",
        "income":"Annual Income",
        "button":"Find My Schemes",
        "result":"Recommended Schemes"
        }

    result=None

    if request.method=="POST":

        age=int(request.form["age"])
        income=int(request.form["income"])
        occupation=request.form["occupation"]
        category=request.form["category"]
        state=request.form["state"]

        result=recommend(age,income,occupation,category,state)

    return render_template_string(page,schemes=result,**text)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=10000)
                if s["category"]=="All" or s["category"]==category:

                    if s["state"]=="All" or s["state"]==state:

                        results.append(s["name"])

    if not results:
        results=["No matching schemes found"]

    return results


# -------------------------
# WEBSITE HTML
# -------------------------

page = """

<!DOCTYPE html>
<html>

<head>

<title>GovtSathi AI</title>

<style>

body{
margin:0;
font-family:Arial;
background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

/* Full screen container */

.container{
width:100%;
min-height:100vh;
display:flex;
align-items:center;
justify-content:center;
}

/* Animation */

@keyframes fadeUp{
0%{opacity:0; transform:translateY(30px);}
100%{opacity:1; transform:translateY(0);}
}

.box{
animation:fadeUp 1s ease;
background:rgba(255,255,255,0.08);
padding:40px;
border-radius:15px;
width:90%;
max-width:900px;
text-align:center;
box-shadow:0 0 20px rgba(0,0,0,0.4);
}

/* India logo */

.logo{
font-size:32px;
margin-bottom:10px;
}

/* Inputs */

input,select{
width:90%;
padding:12px;
margin:10px;
border-radius:8px;
border:none;
font-size:15px;
}

/* Button */

button{
background:#27ae60;
color:white;
border:none;
padding:14px 30px;
font-size:18px;
border-radius:10px;
cursor:pointer;
transition:0.3s;
}

button:hover{
background:#2ecc71;
transform:scale(1.05);
}

/* Language buttons */

.lang{
position:absolute;
top:20px;
right:20px;
}

.lang a{
background:#27ae60;
padding:8px 14px;
color:white;
text-decoration:none;
border-radius:6px;
margin-left:5px;
}

/* Result */

.result{
margin-top:20px;
padding:20px;
background:rgba(0,0,0,0.3);
border-radius:10px;
}

footer{
text-align:center;
margin-top:40px;
color:#bbb;
}

</style>

</head>

<body>

<div class="lang">
<a href="/?lang=en">English</a>
<a href="/?lang=hi">हिन्दी</a>
</div>

<div class="container">

<div class="box">

<div class="logo">🇮🇳 GovtSathi</div>

<h1>{{title}}</h1>
<p>{{subtitle}}</p>

<form method="POST">

<input type="number" name="age" placeholder="{{age}}" required>

<input type="number" name="income" placeholder="{{income}}" required>

<select name="occupation">
<option>Student</option>
<option>Farmer</option>
<option>Business</option>
<option>Unemployed</option>
</select>

<select name="category">
<option>General</option>
<option>OBC</option>
<option>SC</option>
<option>ST</option>
</select>

<select name="state">

<option>All</option>
<option>Haryana</option>
<option>Punjab</option>
<option>Delhi</option>
<option>Uttar Pradesh</option>
<option>Rajasthan</option>
<option>Maharashtra</option>
<option>Gujarat</option>
<option>Madhya Pradesh</option>
<option>Bihar</option>

</select>

<br>

<button type="submit">{{button}}</button>

</form>

{% if schemes %}

<div class="result">

<h2>{{result}}</h2>

<ul>

{% for s in schemes %}
<li>{{s}}</li>
{% endfor %}

</ul>

</div>

{% endif %}

</div>

</div>

<footer>

<p>Design and Developed by ANKIT SAINI</p>
<p>Email: as3126061@gmail.com</p>

</footer>

</body>
</html>

"""

# -------------------------
# ROUTE
# -------------------------

@app.route("/",methods=["GET","POST"])
def home():

    lang=request.args.get("lang","en")

    if lang=="hi":

        text={
        "title":"AI आधारित सरकारी योजना सुझाव",
        "subtitle":"अपने लिए सही योजना खोजें",
        "age":"आयु",
        "income":"वार्षिक आय",
        "button":"योजना खोजें",
        "result":"आपके लिए योजनाएँ"
        }

    else:

        text={
        "title":"AI Powered Government Scheme Recommendation",
        "subtitle":"Find the best schemes for yourself",
        "age":"Age",
        "income":"Annual Income",
        "button":"Find My Schemes",
        "result":"Recommended Schemes"
        }

    result=None

    if request.method=="POST":

        age=int(request.form["age"])
        income=int(request.form["income"])
        occupation=request.form["occupation"]
        category=request.form["category"]
        state=request.form["state"]

        result=recommend(age,income,occupation,category,state)

    return render_template_string(page,schemes=result,**text)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=10000)
