# ./dboost/dboost-stdin.py --statistical 1 --histogram 0.8 0.2 datasets/real/csail.txt
# ./dboost/dboost-stdin.py --statistical 1 --histogram 0.8 0.2 datasets/real/csail-tiny.txt
# ./dboost/dboost-stdin.py --statistical 1 --gaussian 3 datasets/real/csail-tiny.txt -vv

./datasets/synthetic/fizzbuzz.py
./dboost/dboost-stdin.py --histogram 0.8 0.05 --discretestats 8 2 datasets/synthetic/fizzbuzz -v > "fizzbuzz_hist.txt"
./dboost/dboost-stdin.py --partitionedhistogram 5 0.8 0.05 --discretestats 8 2 datasets/synthetic/fizzbuzz -vv > "fizzbuzz_part_hist.txt"

./datasets/synthetic/logins.py
./dboost/dboost-stdin.py --histogram 0.6 0.05 --discretestats 8 2 datasets/synthetic/logins0 -d unix2date -d bits > "login0_hist.txt"
./dboost/dboost-stdin.py --histogram 0.6 0.05 --discretestats 8 2 datasets/synthetic/logins1 -d unix2date -d bits > "login1_hist.txt"
./dboost/dboost-stdin.py --histogram 0.6 0.05 --discretestats 8 2 datasets/synthetic/logins2 -d unix2date -d bits > "login2_hist.txt"

# ./dboost/dboost-stdin.py --histogram 0.9 0.01 --discretestats 8 2 datasets/real/tcph/tcph-clean -F "	" -v -d div -d bits -d unix2date_float -d unix2date -d string_case -d is_weekend

# ./dboost/dboost-stdin.py -F ' ' --statistical .7 --mixture 2 .1 datasets/real/intel/sensors-1000_dataonly.txt -d unix2date_float
# ./dboost/dboost-stdin.py -F ' ' --statistical .7 --mixture 2 .075 datasets/real/intel/sensors-1000_dataonly.txt -d unix2date_float
# ./dboost/dboost-stdin.py -F ' ' --statistical .7 --mixture 1 .075 datasets/real/intel/sensors-1000_dataonly.txt -d unix2date_float
# ./dboost/dboost-stdin.py -F ' ' --statistical .7 --gaussian 1.5 datasets/real/intel/sensors-1000_dataonly.txt -d unix2date_float
