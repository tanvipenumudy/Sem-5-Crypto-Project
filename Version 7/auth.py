from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, redirect, url_for, request, flash, send_file, Response
from app import db
from flask_login import login_user
from models import User
from flask_login import login_user, logout_user, login_required, current_user
from flask import Markup
from Crypto import Random
from Crypto.Cipher import AES
from werkzeug.utils import secure_filename
import os
import random
import string
import os.path
import hashlib
from resources import get_bucket, get_buckets_list

auth = Blueprint('auth', __name__)
app_root = os.path.dirname(os.path.abspath(__file__))

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

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index')) 

@auth.route('/signup',methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    if(email == '' or name == '' or password == ''):
        flash('Please enter all the fields.')
        return redirect(url_for('auth.signup'))
    user = User.query.filter_by(email=email).first() 

    if(user): 
        flash(Markup('Email address already exists. Please go to <a href="http://127.0.0.1:5000/login" class="alert-link">Login Page</a>'))
        return redirect(url_for('auth.signup'))
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'),keydir="{}")

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()   
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('profile'))


@auth.route('/account_set')
@login_required
def account_set():
	return render_template('settings.html')

@auth.route('/set1', methods=["GET", "POST"])
@login_required
def set1():
    from app import current_user
    if(request.method == 'GET'):
        return render_template('setting1.html')
    else:
        new_email = request.form.get('email')
        if(new_email == ''):
            flash('Email field is left blank.')
            return redirect(url_for('auth.set1'))

        user = User.query.get_or_404(current_user.id)
        user.email = new_email
        try:
            db.session.commit()
        except:
            flash('Technical error, failed to update')
            return redirect(url_for('auth.set1'))
        flash('Successfully Updated!')
        return redirect(url_for('auth.set1'))

@auth.route('/set2', methods=["GET", "POST"])
@login_required
def set2():
    from app import current_user
    if(request.method == 'GET'):
        return render_template('setting2.html')
    else:
        new_psw = request.form.get('password')
        con_psw = request.form.get('confirmpass')
        if(new_psw == '' or con_psw == ''):
            flash('Password field is left blank.')
            return redirect(url_for('auth.set2'))
        if(new_psw != con_psw):
            flash('Passwords do not match')
            return redirect(url_for('auth.set2'))
        passhash = generate_password_hash(new_psw, method='sha256')
        user = User.query.get_or_404(current_user.id)
        user.password = passhash
        try:
            db.session.commit()
        except:
            flash('Technical error, failed to update')
            return redirect(url_for('auth.set2'))
        flash('Successfully Updated!')
        return redirect(url_for('auth.set2'))


@auth.route('/cancel account')
def cancel():
    from app import current_user
    if current_user is None:
        return redirect(url_for('index'))
    try:
        db.session.delete(current_user)
        db.session.commit()
    except:
        return 'unable to delete the user.'
    flash('Your account has been deleted')
    return redirect(url_for('auth.login'))

@auth.route('/enc_upload', methods=['POST'])
@login_required
def enc_upload():
    from app import current_user
    user = User.query.get_or_404(current_user.id)
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
        loc0 = os.path.join(source,file.filename)
        file.save(loc0)
        loc = os.path.join(target,file.filename+".enc")
        with open(loc0, 'rb') as fo:
            plaintext = fo.read()
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 20))
        res1 = bytes(res, 'utf-8') 
        key = hashlib.sha256(res1).digest()
        enc = encrypt(plaintext, key)
        with open(loc, 'wb') as fo:
            fo.write(enc)
        my_bucket = get_bucket()
        my_bucket.Object(file.filename+".enc").put(Body=open(loc,'rb'))
        source1 = os.path.join(app_root, 'keys')
        if(not os.path.exists(source1)):
            os.makedirs(source1)
        source2 = os.path.join(source1, file.filename+".enc key.txt")
        keydir = eval(user.keydir)
        keydir[file.filename+".enc"] = key
        user.keydir = str(keydir)
        db.session.commit()
        with open(source2, "w") as file1:    
            file1.write(res)
        file1.close()
        flash('File uploaded successfully')
        return send_file(source2, as_attachment=True)
    return redirect(url_for('files'))

@auth.route('/upload', methods=['POST'])
@login_required
def upload():
    file = request.files['file']
    if(file.filename==''):
        flash('No file selected')
    if(file):
        my_bucket = get_bucket()
        my_bucket.Object(file.filename).put(Body=file)
        flash('File uploaded successfully')
    return redirect(url_for('files'))

@auth.route('/delete', methods=['POST'])
@login_required
def delete():
    key = request.form['key']
    my_bucket = get_bucket()
    my_bucket.Object(key).delete()
    flash('File deleted successfully')
    return redirect(url_for('files'))


@auth.route('/download', methods=['POST'])
@login_required
def download():
    from app import current_user
    user = User.query.get_or_404(current_user.id)
    key = request.form['key']
    if('.enc' == key[-4:]):
        user.download = key
        db.session.commit()
        return redirect(url_for('auth.download1'))
    elif('.enc' != key[-4:]):
        my_bucket = get_bucket()
        file_obj = my_bucket.Object(key).get()
        return Response(
        file_obj['Body'].read(),
        mimetype='text/plain',
        headers={"Content-Disposition": "attachment;filename={}".format(key)}
    )

@auth.route('/download1')
@login_required
def download1():
    return render_template('download1.html')

@auth.route('/download1', methods=['POST'])
@login_required
def download1_post():
    from app import current_user
    seckey = request.form['seckey']
    seckey = bytes(seckey, 'utf-8') 
    seckey = hashlib.sha256(seckey).digest()
    user = User.query.get_or_404(current_user.id)
    key = user.download
    keydir = eval(user.keydir)
    source = os.path.join(app_root,'uploads')
    if(keydir[key]==seckey):
        loc0 = os.path.join(source,key[:-4])
        flash('Your Download is Ready!')
        return send_file(loc0, as_attachment=True)
    else:
        flash('Please Enter the Correct Key')
        return redirect(url_for('auth.download1'))
    

    
        
        
        



