from flask import Flask
app = Flask(__name__)

try:
    os.mkdir("./messages",0o755)
except: pass



@app.route("/",methods=["GET","POST"])
def home():
    try:
        db = open('./messages/messages.txt', 'r')
    except:
        print("no previus messages")
    items = []
    for line in db:
        items.append(line)
    items = reversed(items)

    if request.method == "POST":
        message = request.form["message"]
        db = open('./messages/messages.txt', 'a')

        Date = str(datetime.now())[:10]
        Hour = str(datetime.now())[11:13]
        Minute = str(datetime.now())[14:16]
        if message == "":
            print("Message empty, not posting")
        else:
            db.write(Date+" "+Hour+":"+Minute+" : "+message+"\n")
            print(Date + " " + Hour + ":" + Minute + " : " + message + "\n")

    return render_template("home.html", list=items)




if __name__ == "__main__":
    app.run(host="0.0.0.0")
