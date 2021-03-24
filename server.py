from flask import Flask, render_template, request
from scripts import forms, build

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def homepage():
    form = forms.lgw_form(request.form, 
        dns="1.1.1.1",
        lic_bandwidth="10",
        interface="Gi0",
        int_subnet="255.255.255.0",
        ntp_server="pool.ntp.org")
    if request.method == 'POST' and form.validate():
        config = build.generate_config(**form.data)
        return(f'<pre>{config}</pre>')
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0')