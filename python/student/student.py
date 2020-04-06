class Student:

    def __init__(self, name, id, score):

        self.name = name
        self.id = id
        self.homeworkScores = []

        for data in score:
            if data["name"] == "midterm":
                self.midtermScore = data["score"]
            elif data["name"] == "final":
                self.finalScore = data["score"]
            else:
                self.homeworkScores.append(data["score"])

    def calculateHomeworkScore(self):
        '''returns the total marks scored in homework, out of 70'''

        l = len(self.homeworkScores)
        min_marks = min(self.homeworkScores)
        total = sum(self.homeworkScores)

        if l == 8:
            total -= min_marks

        return total

    def calculateFinalPercent(self):
        '''returns the rounded up value of the final percentage'''

        homeworkScore = self.calculateHomeworkScore()
        midtermScore = self.midtermScore
        finalScore = self.finalScore

        finalPercentScore = (35 * homeworkScore/70) + \
            (30 * midtermScore/100) + (35 * finalScore/100)

        return round(finalPercentScore)

    def calculateFinalLetterGrade(self):
        '''returns the final grade, based off on the final percentage'''

        finalPercentScore = self.calculateFinalPercent()
        FinalLetterGrade = ''

        if(finalPercentScore >= 93):
            FinalLetterGrade = 'A'
        elif(finalPercentScore >= 90):
            FinalLetterGrade = 'A-'
        elif(finalPercentScore >= 87):
            FinalLetterGrade = 'B+'
        elif(finalPercentScore >= 83):
            FinalLetterGrade = 'B'
        elif(finalPercentScore >= 80):
            FinalLetterGrade = 'B-'
        else:
            FinalLetterGrade = 'C'

        return FinalLetterGrade


s1 = Student("Gertrude",
             1901001,
             [{"name": "hw1",  "score": 7},
              {"name": "hw2",  "score": 3},
              {"name": "hw3",  "score": 8},
              {"name": "hw4",  "score": 9},
              {"name": "hw5",  "score": 2},
              {"name": "midterm",  "score": 85},
              {"name": "hw6",  "score": 6},
              {"name": "hw7",  "score": 7},
              {"name": "hw8",  "score": 8},
              {"name": "final",  "score": 92}])


print(f'name = {s1.name}')
print(f'id = {s1.id}')
print(f'homework scores = {s1.homeworkScores}')
print(f'midterm score = {s1.midtermScore}')
print(f'final score = {s1.finalScore}')
print(f'\ntotal homework score = {s1.calculateHomeworkScore()}')
print(f'final percentage score = {s1.calculateFinalPercent()}')
print(f'final letter grade : {s1.calculateFinalLetterGrade()}')
