son1 = int(input())
son2 = int(input())

if son1 == 0:
    print("Invalid number")
elif son2 == 0:
    print("Invalid number")
    
elif son1 < 0:
    sonw = abs(son1)
    print('+ -', son1 + son2, '\n* -', son1 * son2, '\nmodule - |',sonw,'|,', '|',son2,'|')
elif son2 < 0:
    sonx = abs(son2)
    print('+ -', son1 + son2, '\n* -', son1 * son2, '\nmodule - |',son1,'|,', '|',sonx,'|')
    
else:
    print('+ -', son1 + son2, '\n* -', son1 * son2, '\nmodule - |',son1,'|,', '|',son2,'|')
    
    
