from flask import Flask,jsonify,request

app=Flask(__name__)

tasks=[
    {
        "Contact":"9987644456"
        "Name":"Raju",
        "done":False
        "id":1,
    },
    {
        "Contact":"9876543222"
        "New Title":"Rahul",
        "done":False
        "id":2,
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

