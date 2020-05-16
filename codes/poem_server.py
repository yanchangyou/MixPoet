#coding=utf8
import os
from flask import Flask,request
from generator import Generator

generator = Generator()

app = Flask(__name__)
application = app

path = os.getcwd()    #获取当前工作目录
print(path)

global count 

count = 1

@app.route('/poem')
def write_poem():

    global count 
    count += 1

#    print(request.args)
    params = request.args

    label1 = count % 3
    label2 = count % 2 

    beam_size = 20
    verbose = 0
    manu = False 
    length = int(params['length'])

    keyword= params['keywords']

    lines, info = generator.generate_one(keyword, length, label1, label2,
         beam_size, verbose, manu)
    result = ",".join(lines)
    print(result)

    return result


if __name__ == "__main__":
    app.run(port=5001)
