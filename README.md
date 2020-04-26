# cmb_bed_dup
#### Usage:
It's a python3 script. You can use it to combine overlap regions in bed format file (3 columns)

#### Parameter
- -i/--input bed file [must]
- -o/--output  result file [must]

### Test:
input file as: test.txt 
```
1       1       10
1       11      12
2       1       10
2       3       15
2       4       12
```
command:
```
pyhton3 cmb_bed_dup.py -i test.txt -o result.txt
```

result file as: result.txt
```
1       1       10
1       11      12
2       1       15
```

