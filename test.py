from Bio import SeqIO

extract_list = ['gnl|extdb|pgaptmp_000001']
# 功能多，但是遇到大序列时候比较慢
db_handle = 'Datas/bigFasta/query.faa'
store = []  # 临时存放Bio.SeqRecord对象
num = 0  # 计数
num_no = 0
db = SeqIO.parse(db_handle, format='fasta')

for rec_extr in extract_list:
    print(f'debug: {rec_extr}')
    counter = 0
    for rec in db:
        counter += 1
        if rec_extr == rec.id:      # 一定要用id，而不是name，虽然内容是一样的，但到SeqIO.write（）时候只能识别id
            print(counter, rec.id)
            num += 1           # 序号和计数
            print('正在提取', rec.id, rec.description, num)
            # self.ui.textBrowser.append(f"正在提取\t{rec.id}\t{num}")
            if rec.seq:             # 判断rec是否为空，不为空则添加到store列表中，表示成功提取
                store.append(rec)
                print('成功', len(rec.seq),'bp')
                # self.ui.textBrowser.append(f"成功\t{len(rec.seq)} bp")
            else:
                print('序列为空！')
                # self.ui.textBrowser.append(f"序列为空")
        elif counter == len(db):
                num_no += 1
                print(f'{rec_extr}提取失败\t{num_no}')
                # self.ui.textBrowser.append(f'{rec_extr}\t提取失败\t{num_no}')
if store:
    print('提取完成\n')
    # self.ui.textBrowser.append(f"提取完成: {num} 成功, {num_no} 失败\t{'='*10}")
else:
    print('无对应序列，提取失败！！！')
    # self.ui.textBrowser.append(f"{extract_list}\t无对应序列，提取失败！！！{'='*10}")