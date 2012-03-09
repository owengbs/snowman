import os,re,xlwt
params = ['dl1.misses', 'sim_IPC', 'dl1.miss_rate']
LOGS = {}
result = {}
file = xlwt.Workbook()
table = file.add_sheet('EEMBC',cell_overwrite_ok=True)
for root,dirs,files in os.walk(r"F:\zjuResearch\Paper\Stat\config2"):
	for f in files:
		logfile = open(os.path.join(root,f),'r')
		for eachline in logfile:
			m = re.search(params[0]+'|'+params[1]+'|'+params[2], eachline)
			if m is not None:
				if m.group() not in result:
					result[m.group()] = {}
				logfile_str = os.path.join(root,f)
				name = re.match(".*config2\\\\(\w+)\\\\([A-Z0-9]+)\\.log", logfile_str)
				if name is not None:
				    value = re.match(".*"+m.group()+"\s+([0-9]+[\\.]?[0-9]+).*", eachline)
				    if value is not None:
					    if name.group(1) not in result[m.group()]:
						    result[m.group()][name.group(1)] = {}
					    result[m.group()][name.group(1)][name.group(2)] = value.group(1)

def print_values(start_row, start_col, name):       
        table.write(start_row,start_col,name)
        bench_pos = start_col+1
        cond_pos = start_row+1
        value_col = start_col+1
        for bench in result[name]:
                table.write(start_row,bench_pos,bench)
                bench_pos += 1
                value_row = start_row+1;
                for cond in result[name][bench]:
                        if cond_pos <= len(result[name][bench])+start_row:
                                table.write(cond_pos,start_col,cond)
                                cond_pos += 1
                        table.write(value_row,value_col,result[name][bench][cond])
                        value_row += 1
                value_col += 1
print_values(0,0,'dl1.misses')
print_values(26,0,'dl1.miss_rate')
print_values(13,0,'sim_IPC')
file.save(r'F:\owen.xls')
