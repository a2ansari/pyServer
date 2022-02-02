import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from datetime import datetime
        

        
@app.route('/sdlfalldetection')
def sdlpi():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from tblFallDetection where ID=(select MAX(ID) from tblFallDetection)")
        rows = cursor.fetchall()
        #respone = jsonify(empRows)
        
        response1="empty"
        for row in rows:
            response1=row["Status"]
        response=jsonify("{\"status\":\""+response1+"\"}")
        #response=response1;
        #respone.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
      	
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
s
