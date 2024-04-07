va = int(input('ingrese los votos por Apruebo '))
vr = int(input('ingrese los votos por Rechazo '))
vb = int(input('ingrese los votos por Blanco '))
vn = int(input('ingrese los votos por Nulo '))

vt = (va+vr+vb+vn)
prb = round(((vb/vt)*100), 2)
prn = round(((vn/vt)*100), 2)

vv = (va+vr)
pra = round(((va/vv)*100), 2)
prr = round(((vr/vv)*100), 2)

print('porcentaje de apruebo:', pra)
print('porcentaje de rechazo:', prr)
print('porcentaje de blanco:', prb)
print('porcentaje de nulo:', prn)
