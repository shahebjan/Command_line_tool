import pymysql
from flask import Flask, render_template, request

app = Flask(__name__)

conn = pymysql.connect(host='localhost', user='root', password='', database='mirza_mobile_store')
print("Database connected")

@app.route('/')
def query():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def commandLine():
    if request.method == 'POST':
        write_query = request.form.get('write_query')

        with conn.cursor() as cur:
            if "show" in write_query or "SHOW" in write_query:
                cur.execute(write_query)
                data = cur.fetchall()
                return render_template('result.html', data = data)
            
            elif "create" in write_query or "CREATE" in write_query:
                cur.execute(write_query)
                conn.commit()
                return "created successfully."
            
            elif "use" in write_query.split() or "USE" in write_query.split():
                cur.execute(write_query)
                return ("Switched to {}".format(write_query.split()[1]))
            
            elif "describe" in write_query or "DESCRIBE" in write_query:
                cur.execute(write_query)
                conn.commit()
                data = cur.fetchall()
                return render_template('result.html', data=data)
            
            elif "select" in write_query or "SELECT" in write_query:
                cur.execute(write_query)
                conn.commit()
                data = cur.fetchall()

                cur.execute("describe {}".format(write_query.split()[3]))
                columns = cur.fetchall()
                return render_template('result.html', data=data, columns=columns)
            
            elif "insert" in write_query or "INSERT" in write_query:
                cur.execute(write_query)
                conn.commit()
                return "Data inserted successfully."
            
            elif "update" in write_query or "UPDATE" in write_query:
                cur.execute(write_query)
                conn.commit()
                return "Data updated successfully."
            
            elif "alter" in write_query or "ALTER" in write_query:
                cur.execute(write_query)
                conn.commit()
                return "Whatever you have altered, Its successfully altered."
            
            elif "delete" in write_query or "DELETE" in write_query:
                cur.execute(write_query)
                conn.commit()
                return "Data deleted successfully."
            
            elif "drop" in write_query or "DROP" in write_query:
                cur.execute(write_query)
                conn.commit()
                return "Whatever you have dropped, Its dropped successfully."
            
            else:
                return "Ooops...!!! You have an error in your SQL syntax."
            
if __name__ == '__main__':
    app.run(debug=True)



