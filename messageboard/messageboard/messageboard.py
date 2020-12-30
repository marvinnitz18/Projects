print("Messageboard started")
from flask import Flask,render_template,request
from _datetime import datetime
import os
app = Flask(__name__)

#create folder architecture
#try:
#    os.mkdir("./messages",0o755)
#except: pass


@app.route("/",methods=["GET","POST"])
def home():
    count = 0
    try:
        db = open('messages.txt', 'r')
    except:
        print("no previus messages")
        print(len(db))

    
    db = open('messages.txt', 'r')
    for line in db:
        items = []
        items.append(str(line))
        items = reversed(items)

    if request.method == "POST":
        message = request.form["message"]
        db = open('messages.txt', 'a')

        Date = str(datetime.now())[:10]
        Hour = str(datetime.now())[11:13]
        Minute = str(datetime.now())[14:16]
        if message == "":
            #print("Message empty, not posting")
            pass
        else:
            db.write(Date+" "+Hour+":"+Minute+" : "+message+"\n")
            print("User Message:  " +Date + " " + Hour + ":" + Minute + " : " + message + "\n")
    
    count = count + 1
    print(count)
    db.close()
    try:
        return render_template("home.html", list=items)
    except: 
        return render_template("home.html")


#create apps
if __name__ == "__main__":
        app.run(host="0.0.0.0",debug=True)
#app.run(host="192.168.0.31",port=4455,debug=True)
