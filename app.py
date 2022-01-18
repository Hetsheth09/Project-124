from flask import Flask,jsonify,request

app=Flask(__name__)

tasks=[
    {
        "id":1,
        "New Title":u"brush and take bath",
        "done":False
    },
    {
        "id":2,
        "New Title":u"Do My breakfast",
        "done":False
    },
    {
        "id":3,
        "New Title":u"GO to the school",
        "done":False
    }

]
@app.route("/add-data",methods=["POST"])
def Add_Task():
    if not request.json:
        return jsonify({
        "status":"eror",
        "message":"Add your message"
    },400)
    task={
        "id":tasks[-1]["id"]+1,
        "new Title":request.json["new Title"],
        "done":False
    
    }
    tasks.append (task)
    return jsonify({
    "status":"success",
    "message":"task added successful"
})

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if(__name__=="__main__"):
    app.run(debug=True)

