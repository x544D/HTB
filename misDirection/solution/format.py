from base64 import b64decode as b64d

fout = open('extract_output' , 'r' , encoding='utf-8');

dic = {}

for line in fout.readlines():
    ln = line.strip()
    if (ln.__len__()>1):
        _i = ln.index('secret')
        _r = ln[_i:_i+12].strip().replace('secret/' , '').split('/')
        dic[_r[1]] = _r[0]

keys_ = sorted(map(int , dic.keys()))

print('FLAG => '+ b64d(bytes(''.join([dic[str(k)] for k in keys_]), encoding='ascii')).decode('ascii'))


fout.close()
