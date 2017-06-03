from EvaluateClass import *
import pickle
import math  # .sqrt함수 사용

class data_handler:
    #클래스 변수 : 클래스의 모든 인스턴스들이 공유하는 변수
    evaluator = Evaluate()   # 객체합성

    #class method : 전역함수처럼 쓸 수 있다              
    @classmethod
    def get_rawdata_in_dic(cls, filename):
        items = []
        with open(filename, 'rb') as f:
            while 1:
                try: 
                    data = pickle.load(f)
                except EOFError:
                    break    
                items.append(data)
        
        rawdata={}
        for item in items:
            for i in item.items():
                rawdata.update({i[0] : i[1]})
        return rawdata


    def __init__(self, filename, clsname):
        self.rawdata = data_handler.get_rawdata_in_dic(filename)  # 파일이름을 써주어야함.
        self.clsname = clsname
        # 연산한 값을 저장해두는 저장소 
        # 필요할 때 값을 연산하되 이미 연산된 값이면 연산 없이 저장된 값을 반환.
        self.cache = {} #이미 계산된 데이터를 저장할 저장공간
        
    def get_scores(self):
        if "scores" not in self.cache:
            self.cache['scores'] = list(self.rawdata.value())
            
        return self.cache.get('scores')
            # scores = [95, 25,....]
            # self.cache = ['scores': score,....] 
            # raw data = {'greg': 95, 'sam': 25, ....}
            # raw data에서 value값만 모은 것이 scores의 값이다.
            # 따라서 GetScores 함수는 rawdata에서 value 값을 리스트에 끌어모은 것.
            # reduce(lambda: r, e:
            #        r.append(e) or r, self.rawdata.values(),
            #        []
            #       )
            # 스코어스가 캐쉬 안에 없다면 value 값만 모아서 리스트로 만들고, 있다면 반환하도록. 
            # 점수만 담을 함수

            
    def get_average(self):
        if "average" not in self.cache:
            self.cache['average'] = self.evaluator.average(self.get_scores())

        return self.cache.get("average")

    
    def get_variance(self):
        if "variance" not in self.cache:
            vari = round(self.evaluator.variance(self.get_scores(), self.get_average()), 1)
            self.cache["variance"] = vari
  
        return self.cache.get("variance")

    
    def get_standard_deviation(self):
        if "standard_deviation" not in self.cache:
            std_dev = round(math.sqrt(self.get_variance()), 1)
            self.cache["standard_deviation"] = std_dev

        return self.cache.get("standard_deviation")

    def get_score_by_name(self, name):
        return self.rawdata[name]
    
    def who_is_highest(self):
        if "highest" not in self.cache:
            high = reduce(lambda a, b: a if self.rawdata.get(a) > self.rawdata.get(b)\
                             else b, self.rawdata.keys()) # 최대값에서는 초기값 필요 없음. 
            self.cache["highest"] = high
            
        return self.cache.get("highest")

    def get_highest_score(self):
        return self.rawdata[self.who_is_highest()]
    
    def who_is_lowest(self):
        if "lowest" not in self.cache:
            low = reduce(lambda a, b: a if self.rawdata.get(a) < self.rawdata.get(b)\
                     else b, self.rawdata.keys())
            self.cache["lowest"] = low

        return self.cache.get("lowest")

    def get_lowest_score(self):
        return self.rawdata[self.who_is_lowest()]    

    def get_evaluation(self):
        print('*' * 50)
        print("%s 반 성적 분석 결과" % self.clsname)
        print("{0}반의 평균은 {1}점이고 분산은 {2}이며,따라서 표준편차는{3}이다".\
              format(self.clsname, self.get_average(), self.get_variance()\
                     , self.get_standard_deviation()))
        print('*' * 50)
        print("%s 반 종합 평가" % self.clsname)
        print('*' * 50)
        self.evaluate_class()

    def evaluate_class(self):
        avrg = self.get_average()
        std_dev = self.get_standard_deviation()
        
        if avrg <50 and std_dev >20:
            print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
        elif avrg > 50 and std_dev >20:
            print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
        elif avrg < 50 and std_dev <20:
            print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
        elif avrg > 50 and std_dev <20:
            print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")