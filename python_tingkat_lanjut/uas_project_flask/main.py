from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nim = request.form.get('nim')
        nama = request.form.get('nama')
        jurusan = request.form.get('jurusan')
        
        nilai_tugas = request.form.get('tugas', 0, type=float)
        nilai_uts = request.form.get('uts', 0, type=float)
        nilai_uas = request.form.get('uas', 0, type=float)
        
        nilai_akhir = (0.30 * nilai_tugas) + (0.30 * nilai_uts) + (0.40 * nilai_uas)
        
        if nilai_akhir >= 70:
            keterangan = "Lulus"
        else:
            keterangan = "Tidak Lulus"
            
        return render_template('index.html', 
                               nim=nim, 
                               nama=nama, 
                               jurusan=jurusan,
                               tugas=nilai_tugas,
                               uts=nilai_uts,
                               uas=nilai_uas,
                               nilai_akhir=f"{nilai_akhir:.2f}",
                               keterangan=keterangan)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
