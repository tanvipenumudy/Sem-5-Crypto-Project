from flask import Flask, render_template, request, redirect, url_for, flash, \
    Response, session, send_file
from flask_bootstrap import Bootstrap
from filters import datetimeformat, file_type
from resources import get_bucket, get_buckets_list
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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        bucket = request.form['bucket']
        session['bucket'] = bucket
        return redirect(url_for('files'))
    else:
        buckets = get_buckets_list()
        return render_template("index.html", buckets=buckets)


@app.route('/files')
def files():
    my_bucket = get_bucket()
    summaries = my_bucket.objects.all()

    return render_template('files.html', my_bucket=my_bucket, files=summaries)


@app.route('/upload', methods=['POST'])
def upload():
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


@app.route('/delete', methods=['POST'])
def delete():
    key = request.form['key']

    my_bucket = get_bucket()
    my_bucket.Object(key).delete()

    flash('File deleted successfully')
    return redirect(url_for('files'))


@app.route('/download', methods=['POST'])
def download():
    key = request.form['key']
    source = os.path.join(app_root,'uploads')
    loc0 = os.path.join(source,key[:-4])
    return send_file(loc0, as_attachment=True)
    # my_bucket = get_bucket()
    # file_obj = my_bucket.Object(key).get()

    # with open(file_name, 'rb') as fo:
    #    ciphertext = fo.read()
    # dec = decrypt(ciphertext, key)
    # with open(file_name[:-4], 'wb') as fo:
    #    fo.write(dec)

    # return Response(
    #    file_obj['Body'].read(),
    #    mimetype='text/plain',
    #    headers={"Content-Disposition": "attachment;filename={}".format(key)}
    #)


if __name__ == "__main__":
    app.run()
