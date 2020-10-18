from flask import Flask, render_template, request, redirect, url_for, flash, \
    Response, session, Blueprint, send_file
from flask_bootstrap import Bootstrap
from filters import datetimeformat, file_type
from resources import get_bucket, get_buckets_list
from flask_login import login_required, current_user
# from . import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from Crypto import Random
from Crypto.Cipher import AES
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app_root = os.path.dirname(os.path.abspath(__file__))
Bootstrap(app)
app.secret_key = 'MDlp+ObL6Bg0SArdX3vWIQGB163k4vKOKP/8OOnk'
app.jinja_env.filters['datetimeformat'] = datetimeformat
app.jinja_env.filters['file_type'] = file_type

key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message) 

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".enc", 'wb') as fo:
        fo.write(enc)

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name[:-4], 'wb') as fo:
        fo.write(dec)

db = SQLAlchemy()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
@login_required
def profile():
    
        return render_template("profile.html", name=current_user.name)

@app.route('/bucket', methods=['GET', 'POST'])
@login_required
def bucket():
    if request.method == 'POST':
        bucket = request.form['bucket']
        session['bucket'] = bucket
        return redirect(url_for('files'))
    else:
        buckets = get_buckets_list()
    return render_template("bucket.html", buckets=buckets)


@app.route('/files')
@login_required
def files():
    my_bucket = get_bucket()
    summaries = my_bucket.objects.all()

    return render_template('files.html', my_bucket=my_bucket, files=summaries)


@app.route('/enc_upload', methods=['POST'])
def enc_upload():
    source = os.path.join(app_root,'uploads')
    if(not os.path.exists(source)):
        os.makedirs(source)
    target = os.path.join(app_root, 'encrypted')
    if(not os.path.exists(target)):
        os.makedirs(target)
    file = request.files['file']
    if(file.filename==''):
        flash('No file selected')
    if(file):
        # filename = secure_filename(file.filename)
        loc0 = os.path.join(source,file.filename)
        # loc0 = loc0.replace('\\','/')
        file.save(loc0)
        # loc0 = '/'+loc0
        loc = os.path.join(target,file.filename+".enc")
        # loc = loc.replace('\\','/')
        # loc = '/'+loc
        with open(loc0, 'rb') as fo:
            plaintext = fo.read()
        enc = encrypt(plaintext, key)
        with open(loc, 'wb') as fo:
            fo.write(enc)
        my_bucket = get_bucket()
            # my_bucket.upload_file(loc,file.filename+".enc")
        my_bucket.Object(file.filename+".enc").put(Body=open(loc,'rb'))
        flash('File uploaded successfully')
    return redirect(url_for('files'))

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if(file.filename==''):
        flash('No file selected')
    if(file):
        my_bucket = get_bucket()
        my_bucket.Object(file.filename).put(Body=file)
        flash('File uploaded successfully')
    return redirect(url_for('files'))

@app.route('/delete', methods=['POST'])
@login_required
def delete():
    key = request.form['key']

    my_bucket = get_bucket()
    my_bucket.Object(key).delete()

    flash('File deleted successfully')
    return redirect(url_for('files'))


@app.route('/download', methods=['POST'])
def download():
    key = request.form['key']
    if('.enc' in key):
        source = os.path.join(app_root,'uploads')
        loc0 = os.path.join(source,key[:-4])
        return send_file(loc0, as_attachment=True)
    elif('.enc' not in key):
        my_bucket = get_bucket()
        file_obj = my_bucket.Object(key).get()
        
        return Response(
        file_obj['Body'].read(),
        mimetype='text/plain',
        headers={"Content-Disposition": "attachment;filename={}".format(key)}
    )

def create_app():

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    app_blueprint = Blueprint('app', __name__)
    app.register_blueprint(app_blueprint)
    return app

def run_app():
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        return User.query.get(int(user_id))
    app.run(debug=True)

if __name__ == "__main__":
    run_app()
