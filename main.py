nama = 'Surya Eka Kurnia'
program = 'Arus Listrik'

print(f'program {program} oleh {nama}')

def hitung_arus(daya,tegangan):
    arus = daya / tegangan
    print(f'daya joule dalam setiap satuan aliran tegangan volt')
    print(f'Sehingga arus = {arus} Ampere')
    return arus

# daya = 600
# tegangan = 20
arus = hitung_arus(600, 20)
arus = hitung_arus(900, 30)

program = 'Arus Listrik'

print(f'program {program} oleh {nama}')

def hitung_arus(tegangan,tahanan):
    arus = tegangan / tahanan
    print(f'tegangan listrik volt dalam setiap satuan aliran tahanan ohm')
    print(f'Sehingga arus = {arus} Ampere')
    return arus

# tegangan = 1000
# tahanan = 25
arus = hitung_arus(1000, 25)
arus = hitung_arus(900, 30)

program = 'Arus Listrik'

print(f'program {program} oleh {nama}')

def hitung_arus(muatan,waktu):
    arus = muatan / waktu
    print(f'muatan listrik coulomb dalam setiap satuan waktu = {waktu / 60}menit ')
    print(f'Sehingga arus = {arus} Ampere')
    return arus

#muatan = 3000
#waktu = 3 * 50
arus = hitung_arus(3000, 3*50)
arus = hitung_arus(2000, 2*60)
