from flask import Flask, request, render_template 
app = Flask(__name__)

@app.route("/")
def item():
  return render_template("item.html")

@app.route("/purchase", methods=['GET', 'POST'])
def purchase():
  return render_template("purchase.html", itemname=request.form['itemname'], itemqty=request.form['itemqty'], itemprice=request.form['itemprice'])

if __name__ == '__main__':
  app.run()