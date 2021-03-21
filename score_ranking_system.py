class Student():
    '''
    生徒の名前と教科毎の点数を格納する
    '''
    def __init__(self,name,japanese,math,chemistry):
        self.name = name
        self.japanese = japanese
        self.math = math
        self.chemistry = chemistry

    def profile(self):
        rslt=str(self.name)+" 国語:"+str(self.japanese)+" 算数:"+str(self.math)+" 化学:"+str(self.chemistry)+" 合計:"+str(self.japanese+self.math+self.chemistry)
        return print(rslt)
    
    def totalscore(self):
        self.total=self.japanese+self.math+self.chemistry
        return self.total

class Scoresystem():
    '''
    成績を集計する
    '''
    def __init__(self,members):
        self.members = members
        
    def ranking(self):
        temp_list=self.members
        ranked=[]
        temp_score=0
        order=0
        for x in range(len(temp_list)):
            temp_score=temp_list[0].totalscore()
            order=0
            for i in range(len(temp_list)):
                if temp_list[i].totalscore()>temp_score:
                    temp_score=temp_list[i].totalscore()
                    order=i
            ranked.append(temp_list[order].name)
            del temp_list[order]
        return ranked
                    

if __name__ == "__main__":
    sugai=Student('sugai',55,88,88)
    doi=Student('doi',85,77,99)
    saito=Student('saito',85,85,85)
    takei=Student('takei',95,100,40)
    hirota=Student('hirota',99,70,100)

    sugai.profile()
    doi.profile()
    saito.profile()
    takei.profile()
    hirota.profile()

    KM=Scoresystem([sugai,doi,saito,takei,hirota])
    rslt=KM.ranking()
    for i in range(len(rslt)):
        print('{}位は{}さんです。'.format(i+1,rslt[i]))