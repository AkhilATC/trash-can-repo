from flask import Flask, redirect, url_for, request,render_template,send_file
import pdf_generator as pdf_gen
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def login():
    return render_template('index.html')

@app.route('/gen_report', methods=['POST'])
def gen_report():
    clinic_name = request.form.get('clinic-name', None)
    clinic_logo = request.form.get('clinic-logo')

    print("DATA WE GOT")
    print(clinic_name)
    print(clinic_logo)
    # physical's info
    physician_name = request.form.get('physician-name')
    physician_contact = request.form.get('physician-contact')
    print(physician_name)
    print(physician_contact)
    # patient's info

    patient_fname = request.form.get('p-name')
    patient_lname = request.form.get('p-lname')
    print(patient_fname)
    print(patient_lname)
    patient_dob = request.form.get('p-dob')
    patient_contact = request.form.get('p-contact')
    # notes
    c_note = request.form.get('input-message')
    con_note = request.form.get('input-message-2')
    resp = pdf_gen.__generate_pdf_attributes(
        clinic_name,
        clinic_logo,
        physician_name,
        physician_contact,
        patient_fname+" "+patient_lname,
        patient_dob,
        patient_contact,
        c_note,
        con_note

    )
    file_name = f"CR_{patient_fname}_{patient_lname}_{patient_dob}.pdf"
    is_error = pdf_gen.convert_html_to_pdf(resp, file_name)
    if is_error:
        return redirect(url_for("/"))
    else:
        return send_file(file_name, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)