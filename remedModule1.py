def cekNPWP(x):
    hrf = '0123456789-.'
    status = True
    syarat1 = ['01','02','03','04','06','05','07','08','09']

    for i in x:
        if i not in hrf:
            status = False
            
    if '-' not in x and '.' not in x:
        status = False

    if x.split('.')[0] not in syarat1:
        status = False

    if status:
        print('Output: Kode seri NPWP valid!')
            
        if x.split('.')[0] in syarat1[:3]:
            print('Identitas Wajib Pajak:', x.split('.')[0], 'Wajib Pajak Badan')
        elif x.split('.')[0] in syarat1[3:5]:
            print('Identitas Wajib Pajak:', x.split('.')[0], 'Wajib Pajak Pengusaha')
        elif x.split('.')[0] in syarat1[5]:
            print('Identitas Wajib Pajak:', x.split('.')[0], 'Wajib Pajak Karyawan')
        elif x.split('.')[0] in syarat1[6:9]:
            print('Identitas Wajib Pajak:', x.split('.')[0], 'Wajib Pajak Orang Pribadi')
                
        print('Nomor Registrasi: ', x.split('.')[1] + '.' + x.split('.')[2])            
        print('Alat pengaman: ', x.split('.')[3].split('-')[0])
        print('Kode KPP: ', x.split('.')[3].split('-')[-1])      
        print('Status Wajib Pajak: ', x.split('.')[-1])      
    else:
        print('Output: Kode seri NPWP tidak valid!')

# cekNPWP('091234560123123')
# cekNPWP('99.999.999.9-999.999')
# cekNPWP('09.123.456.A-123.123')
cekNPWP('07.123.456.0-212.191')