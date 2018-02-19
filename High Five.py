#There are two properties in the node student id and scores, to ensure that each student will have at least 5 points, find the average of 5 highest scores for each person.
#


'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        res = {}
        d = {}
        for record in results:
            d[record.id] = d.get(record.id, [])
            d[record.id].append(record.score)
        for id in d:
            d[id].sort()
            res[id] = sum(d[id][-5:]) / 5.0
        return res
