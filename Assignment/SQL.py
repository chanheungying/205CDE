#!/usr/bin/python3
from flask import  Flask, render_template,request,session,redirect,url_for
import pymysql

app = Flask(__name__)
app.secret_key = 'abc'

db = pymysql.connect(host='localhost',
                     user='phpmyadmin',
                     password='20160715',
                     db='205CDE',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

cursor =db.cursor()

@app.route("/index")
@app.route("/")
def index():
  if 'id' in session:
        sql = "SELECT id, phone, Email, username, Balance FROM CustomerInformation WHERE id= (%s)"
        cursor.execute(sql, session['id'])
        db.commit()
        
        result = cursor.fetchone()
        UserID = session['id']
        email = result.get("Email")
        phone = result.get("phone")
        Name= result.get("username")
        Balance = result.get("Balance")


        sql = "SELECT `MusicID`,`MusicName`,`TypeOfMusic`, `Price`, `Share`, `Description` FROM `MusicInformation` WHERE `UserID`= (%s)"
        cursor.execute(sql, session['id'])
        db.commit()

        result = cursor.fetchall()
        Number = len(result)

        return render_template('Account.html', User=Name, email= email, phone =phone, AccountID =UserID, Balance = Balance,result = result, Number = Number)
  else:
    return render_template('Home.html')

# Log In to the account
@app.route('/Account', methods = ['POST','GET'])
def Account():
  error= None
  if request.method == 'POST':
        session.pop=('id', None)
        UserID = request.form["UserID"]
        pwd = request.form['pwd']

    
        sql = "SELECT id, pwd, phone, Email, username, Balance FROM CustomerInformation WHERE id= (%s)"
        cursor.execute(sql, UserID)
        db.commit()

        result = cursor.fetchone()
        password = result.get("pwd")
        email = result.get("Email")
        phone = result.get("phone")
        Name= result.get("username")
        Balance = result.get("Balance")

        if pwd == password:
          session['id'] = UserID

          sql = "SELECT `MusicID`,`MusicName`,`TypeOfMusic`, `Price`, `Share`, `Description` FROM `MusicInformation` WHERE `UserID`= (%s)"
          cursor.execute(sql, session['id'])
          db.commit()

          result = cursor.fetchall()
          Number = len(result)
          return render_template('Account.html', User=Name, email= email, phone =phone, AccountID =UserID, Balance = Balance, result= result, Number = Number)
        return redirect(url_for('index'))
  return redirect(url_for('index'))


# Log Out
@app.route('/LogOut')
def LogOut():
  session.pop('id',None)
  return redirect(url_for('index'))

# Show success page for Sign Up
@app.route('/Success', methods= ['POST','GET'])
def Success():
  error = None
  if request.method == 'POST':
    UserName = request.form["UserName"]
    email = request.form["email"]
    phone = int(request.form["Phone"])
    pwd = request.form['pwd']

    try:
        sql = "INSERT INTO `CustomerInformation` (`username`, `pwd`,`Email`,`Phone`) VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, (UserName,pwd,email,phone))
        db.commit()
        
        
        sql = "SELECT id FROM CustomerInformation WHERE username = (%s)"
        cursor.execute(sql,(UserName))
        db.commit
        result=cursor.fetchone()
        UserID = result.get("id")

    finally:
        return render_template('Success.html',UserID=UserID, UserName = UserName, Email=email,phone=phone,pwd = pwd, error = error)
        db.close()


# Upload Music to Database
@app.route('/UploadMusic', methods= ['POST','GET'])
def UploadMusic():
  error = None
  if request.method =='POST':
    result = request.form
    MusicName = request.form["Mname"]
    #Image = request.files["image"]
    Type = request.form["Type"]
    Share = request.form["Sharing"]
    Price = request.form["pric"]
    Description = request.form["Description"]
    UserID = session['id']

    #image =Image.read()
    #ImgName = Image.filename
  
    try:
    #    sql = "INSERT INTO `MusicInformation`(`MusicName`,`ImgName`,`Musicimage`,`Price`,`TypeOfMusic`,`Description`, `UserID`) VALUES (%s, %s, %s,%s,%s, %s, %s)"
     #   cursor.execute(sql, (MusicName,ImgName, image,Price,Type, Description, UserID))
        sql = "INSERT INTO `MusicInformation`(`MusicName`,`Price`,`TypeOfMusic`,`Description`, `UserID`) VALUES (%s, %s, %s,%s,%s)"
        cursor.execute(sql, (MusicName,Price,Type, Description, UserID))
        db.commit()

        if Price != None:

            sql = "SELECT `MusicID` FROM `MusicInformation` WHERE `UserID`= (%s)"
            cursor.execute(sql, UserID)
            db.commit()

            result = cursor.fetchall()
            New = result[-1]
            MusicID = New.get("MusicID")


            sql = "INSERT INTO `SaleMusic`( `MusicID`, `UserID`) VALUES (%s,%s)"
            cursor.execute(sql, (MusicID,UserID))
            db.commit()

    except:
        db.rollback()
 
    finally:
    #    return render_template("result.html",result = result)
        return redirect(url_for('index'))
        db.close()


# Change Account Information
@app.route('/ChangeInformation', methods= ['POST','GET'])
def ChangeInformation():
  error = None
  if request.method == 'POST':
    UserName = request.form["UserName"]
    email = request.form["email"]
    phone = request.form["Phone"]

    try:
        sql ="UPDATE `CustomerInformation` SET `username`= (%s),`Phone`=(%s),`Email`= (%s) WHERE id = (%s)"
        cursor.execute(sql, (UserName,phone,email,session['id']))
        db.session.commit()

    finally:
        return redirect(url_for('index'))
        db.close()


# Change Music Information
@app.route('/EditMusic', methods= ['POST','GET'])
def EditMusic():
  error = None
  if request.method =='POST':
    result = request.form
    MusicID = request.form["MusicID"]
    MusicName = request.form["Mname"]
    Image = request.files["image"]
    Share = request.form["Sharing"]
    Price = request.form["pric"]
    Description = request.form["Description"]
  
    try:
        sql ="UPDATE `MusicInformation` SET`MusicName`=(%s),`Price`=(%s),`Share`=(%s),`Description`=(%s) WHERE `MusicID` = (%s)"
        cursor.execute(sql, (MusicName, Price, Share, Description,MusicID))
        db.commit()

    finally:
        return redirect(url_for('index'))
        db.close()


@app.route('/Deposit')
def DepositPage():
  if 'id' in session:
    sql = "SELECT Balance FROM CustomerInformation WHERE id= (%s)"
    cursor.execute(sql, session['id'])
    db.commit()

    result = cursor.fetchone()
    Balance = result.get("Balance")
    return render_template('Deposit.html', Balance= Balance)
  else:
    return redirect(url_for('index'))


@app.route('/DepositMoney', methods= ['POST','GET'])
def Deposit():
  error = None
  if request.method =='POST':
    Deposit = request.form["Deposit"]

    sql = "SELECT Balance FROM CustomerInformation WHERE id= (%s)"
    cursor.execute(sql, session['id'])
    db.commit()

    result = cursor.fetchone()
    Balance = result.get("Balance")

    NewBalance= float(Balance) + float(Deposit)
  
    try:
        sql ="UPDATE `CustomerInformation` SET `Balance`=(%s) WHERE `CustomerInformation`.`id` = (%s)"
        cursor.execute(sql, (NewBalance, session['id']))
        db.commit()

    finally:
        return redirect(url_for('index'))
        db.close()


# Delete Music from database
@app.route('/RemoveMusic',methods=['POST','GET'])
def RemoveMusic():
  if request.method == 'POST':
    MusicID =request.form['MusicID']

    try:
        sql ="DELETE FROM `MusicInformation` WHERE `MusicInformation`.`MusicID` = (%d)"
        cursor.execute(sql, (MusicID))
        db.commit()

    finally:
        return redirect(url_for('index'))
        db.close()


@app.route('/account')
def account():
  if 'id' in session:
    return redirect(url_for('index'))
  else:
    return redirect(url_for('index'))


# Show html Music Collection
@app.route('/MusicCollection')
def Collection():
  if 'id' in session:
    return render_template('MusicType.html')
  else:
    return redirect(url_for('index'))


# Show the Page for changing account information
@app.route('/Change')
def Change():

  if 'id' in session:
        UserID = session['id']

        sql = "SELECT id, pwd, phone, Email, username, Balance FROM CustomerInformation WHERE id= (%s)"
        cursor.execute(sql, UserID)
        db.commit()

        result = cursor.fetchone()
        password= result.get("pwd")
        email = result.get("Email")
        phone = result.get("phone")
        Name= result.get("username")
        Balance = result.get("Balance")

        return render_template('ChangeInfor.html', User=Name, email= email, phone =phone, AccountID =UserID, Balance = Balance)

  else:
    return redirect(url_for('index'))


# Page for friends list
@app.route('/Friends')
def Friends():
  if 'id' in session:
    return render_template('FriendList.html')
  else:
    return redirect(url_for('index'))

#Page for Q&A
@app.route('/Q&A')
def QA():
  if 'id' in session:
    return render_template('Q.html')
  else:
    return redirect(url_for('index'))

# Page for All types of music
@app.route('/All')
def all():
  if 'id' in session:
    sql = "SELECT `MusicID`,`MusicName`,`TypeOfMusic`, `Price`, `Share`, `Description`, `UserID` FROM `MusicInformation` WHERE `Share`= 'Public'"
    cursor.execute(sql)
    db.commit()

    result = cursor.fetchall()
    Number = len(result)

    sql = "SELECT `CommentID`, `MusicID`, `UserID`, `Comment` FROM `CommentTable`"
    cursor.execute(sql)
    db.commit()

    results = cursor.fetchall()
    Num = len(results)

    return render_template('Music Collection.html', result= result, Number = Number, results=results, Num = Num )
  else:
    return redirect(url_for('index'))

@app.route('/Purchase', methods=['POST','GET'])
def Purchase():
  if 'id' in session:
        MusicID = request.form["MusicID"]
        Price = request.form["Price"]

        sql = "INSERT INTO `Purchase`(`UserID`, `MusicID`) VALUES (%s, %s)"
        cursor.execute(sql, (session['id'], MusicID))
        db.commit()

        sql = "SELECT `Number`FROM `SaleMusic` WHERE `MusicID`= (%s)"
        cursor.execute(sql, (MusicID))
        db.commit()
        results = cursor.fetchone()
        Number = results.get("Number") + 1

        sql = "UPDATE `SaleMusic` SET `Number`=(%s) WHERE `MusicID`=(%s),"
        cursor.execute(sql, (Number,MusicID))
        db.commit()

        sql = "SELECT Balance FROM CustomerInformation WHERE id= (%s)"
        cursor.execute(sql, session['id'])
        db.commit()

        result = cursor.fetchone()
        Balance = result.get("Balance")

        NewBalance = float(result.get("Balance")) - float(Price)

        sql ="UPDATE `CustomerInformation` SET `Balance`=(%s) WHERE `CustomerInformation`.`id` = (%s)"
        cursor.execute(sql, (NewBalance, session['id']))
        db.commit()


        return redirect(url_for('PurchasedMusic'))
  else:
    return redirect(url_for('index'))

@app.route('/PurchasedMusic')
def PurchasedMusic():
  if 'id' in session:
        sql = "SELECT `MusicID` FROM `Purchase` WHERE `UserID`= (%s)"
        cursor.execute(sql, (session['id']))
        db.commit()

        result = cursor.fetchall()
        Number = len(result)

        Information = []

        for No in range(Number):
              MusicID = result[No].get("MusicID")
              sql = "SELECT `MusicID`,`MusicName`,`TypeOfMusic`, `Price`, `Share`, `Description`, `UserID` FROM `MusicInformation` WHERE `MusicID`= (%s)"
              cursor.execute(sql, MusicID)
              db.commit()
              results = cursor.fetchone()
              Information.append(results)

        sql = "SELECT `CommentID`, `MusicID`, `UserID`, `Comment` FROM `CommentTable`"
        cursor.execute(sql)
        db.commit()

        results = cursor.fetchall()
        Num = len(results)

        return render_template("Purchase.html",result= Information, Number = Number, results=results, Num = Num )
  else:
    return redirect(url_for('index'))


@app.route('/SoldMusic')
def SoldMusic():
  if 'id' in session:
        sql = "SELECT `MusicID`, `Number` FROM `SaleMusic` WHERE `UserID`= (%s)"
        cursor.execute(sql, (session['id']))
        db.commit()

        result = cursor.fetchall()
        Number = len(result)

        Information = []

        for No in range(Number):
              MusicID = result[No].get("MusicID")
              sql = "SELECT `MusicID`,`MusicName`,`TypeOfMusic`, `Price`,`Description`, `UserID` FROM `MusicInformation` WHERE `MusicID`= (%s)"
              cursor.execute(sql, MusicID)
              db.commit()
              results = cursor.fetchone()
              results["Number"]=result[No].get("Number")
              Information.append(results)

        sql = "SELECT `CommentID`, `MusicID`, `UserID`, `Comment` FROM `CommentTable`"
        cursor.execute(sql)
        db.commit()

        results = cursor.fetchall()
        Num = len(results)

        return render_template("MusicSold.html",result= Information, Number = Number, results=results, Num = Num )
  else:
    return redirect(url_for('index'))


@app.route('/Comment', methods=['POST','GET'])
def Comment():
  if 'id' in session:
        MusicID = request.form["MusicID"]
        Comment = request.form["Comment"]

        sql = "INSERT INTO `CommentTable`(`MusicID`, `UserID`, `Comment`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (MusicID,session['id'], Comment))
        db.commit()
        return redirect(url_for('all'))
  else:
    return redirect(url_for('index'))


@app.route('/Edit',methods=['POST','GET'])
def edit():
  if 'id' in session:
        MusicID = request.form["MusicID"]

        sql = "SELECT `MusicName`,`TypeOfMusic`, `Price`, `Share`, `Description` FROM `MusicInformation` WHERE `MusicID`= (%s)"
        cursor.execute(sql, MusicID)
        db.commit()

        result = cursor.fetchone()
        MusicName = result.get("MusicName")
        Type = result.get("TypeOfMusic")
        Price = result.get("Price")
        Share = result.get("Share")
        Description = result.get("Description")

        return render_template('EditMusic.html', MusicID = MusicID , Name=MusicName, Type= Type, Price =Price, Description =Description)

  else:
    return redirect(url_for('index'))




if __name__ == '__main__':

  app.run(debug=True)
