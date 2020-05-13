#pypy3 solution.py < data/sample/1.in
#diff data/sample/1.out data/sample/1.ans
#python3 solution.py < data/secret/0mini.in
diff data/secret/1small.out data/secret/1small.ans
pypy3 solution.py < data/secret/1small.in
#cat data/secret/1small.ans
#diff data/secret/1small.out data/secret/1small.ans
#python3 solution.py < data/secret/2med.in
#diff data/secret/2med.out data/secret/2med.ans
#pypy3 solution.py < data/secret/3large.in
#diff data/secret/1small.out data/secret/1small.ans
#pypy3 solution.py < data/secret/4huge.in
#diff data/secret/1small.out data/secret/1small.ans
