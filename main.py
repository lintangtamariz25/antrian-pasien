# from flask import Flask, render_template, request, redirect, url_for
# from livereload import Server
# import sys
# # import create_app

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')


# @app.route('/panggil/<nama><keperluan>')
# def output(nama, keperluan):
#     return render_template('panggil.antrian.html' .format(nama, str(nama)))
#     # nm = request.args.get['namaPasien']
#     # kp = request.args.get['keperluan']

#     # hasil = output(nm, kp)


# @app.route('/tambah-antrian', methods=['POST', 'GET'])
# def tambah():
#     if request.method == 'POST':
#         nm = request.form['namaPasien']
#         kp = request.form['keperluan']
#         # formData['namaPasien'] = nama
#         # formData['keperluan'] = kp 
#         # print('This is error output', file=sys.stderr)
#         # print('This is standard output', file=sys.stdout)
#         # print("holla" ,file=sys.stderr)
#         return redirect(url_for('output', nama = nm, keperluan = kp))
#     else :
#         # nm = request.args.get['namaPasien']
#         # kp = request.args.get['keperluan']
#         return render_template('tambah.antrian.html')




# @app.route('/history-antrian')
# def lihat():
#     return render_template('lihat.antrian.html')

# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True, use_reloader=False)


from client import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)