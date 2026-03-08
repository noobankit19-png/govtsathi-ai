from flask import Flask, request, render_template_string

app = Flask(__name__)

# ---------------- SCHEME DATABASE ----------------

schemes = [

{"name":"PM Kisan Samman Nidhi","occupation":"Farmer","income":500000,"category":"All","state":"All"},
{"name":"Ayushman Bharat Yojana","occupation":"All","income":300000,"category":"All","state":"All"},
{"name":"PM Mudra Loan","occupation":"Business","income":800000,"category":"All","state":"All"},
{"name":"Startup India","occupation":"Business","income":1000000,"category":"General","state":"All"},
{"name":"National Scholarship","occupation":"Student","income":400000,"category":"SC","state":"All"},
{"name":"Skill India Mission","occupation":"Unemployed","income":500000,"category":"All","state":"All"},
{"name":"PM Awas Yojana","occupation":"All","income":300000,"category":"All","state":"All"},
{"name":"PM Fasal Bima","occupation":"Farmer","income":800000,"category":"All","state":"All"},
{"name":"Digital India Internship","occupation":"Student","income":600000,"category":"OBC","state":"All"},
{"name":"Stand Up India","occupation":"Business","income":1000000,"category":"SC","state":"All"}

]

# ---------------- AI RECOMMENDATION ----------------

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


# ---------------- WEBSITE HTML ----------------

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

/* Full screen */

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
box-shadow:0 0 25px rgba(0,0,0,0.4);
}

/* Logo */

.logo{
font-size:34px;
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

/* Language Switch */

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
margin-left:6px;
}

/* Result */

.result{
margin-top:20px;
padding:20px;
background:rgba(0,0,0,0.3);
border-radius:10px;
animation:fadeUp 1.2s ease;
}

/* Footer */

footer{
text-align:center;
margin-top:40px;
color:#ccc;
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

<hr style="border:1px solid rgba(255,255,255,0.2);width:80%;margin:auto;margin-top:30px;">

<p>🚀 Design & Development by <b>ANKIT SAINI</b></p>

<p>Email: as3126061@gmail.com</p>

<p style="font-size:13px;color:#888;">
© 2026 GovtSathi AI – Government Scheme Recommendation Platform
</p>

</footer>

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
