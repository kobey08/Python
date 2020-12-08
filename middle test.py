with open('report.txt') as f:
    data = f.readlines()
    result = []
    for i in data:
        result.append(i.split())
    result[0].insert(0,'名次')  # 新表头
    result[0].extend(['总分','平均分'])

    # 单人总分、平均分
    for i in result[1:]:
        single_sum = 0
        single_ave = 0
        for j in i[1:]:
            single_sum = single_sum +float(j)
        single_ave = round((single_sum / len(i[1:])),2)
        i.extend([str(single_sum),str(single_ave)])

    # 总体平均分、总分
    new_line = []
    for i in range(1,12):
        total_sum = 0
        total_ave = 0
        for j in result[1:]:
            total_sum = total_sum + float(j[i])
        total_ave = round((total_sum / (len(result)-1)),2)
        new_line.append(total_ave)
    new_line.insert(0,'平均')
    new_line.insert(0,'-')

    # 排序、替换不及格
    result.insert(1,new_line)
    result_0 = result[0:2]
    result_1 = result[2:]
    result_1.sort(key=lambda x:x[-2],reverse=True)
    num_0 = 1
    for i in result_1:
        i.insert(0,num_0)
        for j in i[2:len(i)-2]:
            if float(j) < 60:
                i[i.index(j)] = '不及格'
        num_0 = num_0 + 1
    #print(result_1)

    #生成result
    result_final = result_0 +result_1
    with open('result.txt','w') as f:
        for i in result_final:
            for j in i:
                f.writelines(str(j)+'  ')
            f.writelines('\n')
