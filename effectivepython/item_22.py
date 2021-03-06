# -*- coding: utf-8 -*-
"""
Created on 2019/6/11 22:54

@author: LIUBO
"""
import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


# Example
book = SimpleGradebook()
book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 90)
book.report_grade('Isaac Newton', 95)
book.report_grade('Isaac Newton', 85)
print(book.average_grade('Isaac Newton'))


# Eample 3
class BySubjectGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_suject = self._grades[name]
        grade_list = by_suject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grad(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)

        return total / count


# Example 5
book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75)
book.report_grade('Albert Einstein', 'Math', 65)
book.report_grade('Albert Einstein', 'Gym', 90)
book.report_grade('Albert Einstein', 'Gym', 96)
print(book.average_grad('Albert Einstein'))


# Example 6

class WeightedGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def repot_grades(self, name, subject, score, weigth):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weigth))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight
            score_sum += subject_avg / total_weight
            score_count += 1
        return score_sum / score_count


# Example 8
book = WeightedGradebook()
book.add_student('Albert Einstein')
book.repot_grades('Albert Einstein', 'Math', 80, 0.10)
book.repot_grades('Albert Einstein', 'Math', 80, 0.10)
book.repot_grades('Albert Einstein', 'Math', 70, 0.80)
book.repot_grades('Albert Einstein', 'Gym', 100, 0.40)
book.repot_grades('Albert Einstein', 'Math', 85, 0.60)
print(book.average_grade('Albert Einstein'))

# Example 9
grades = []
grades.append((95, 0.45))
grades.append((85, 0.55))
total = sum(score * weight for score, weight in grades)
total_weight = sum(weight for _, weight in grades)
average_grade = total / total_weight
print(average_grade)

# Example 11
import collections

Grade = collections.namedtuple('Grade', ('score', 'weight'))


# Example 12

class Subject(object):
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student(object):
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
            return self._students[name]

book = Gradebook()
albert = book.student('Albert Einstein')
math = albert.subject('Math')
math.report_grade(80, 0.1)
math.report_grade(80, 0.1)
math.report_grade(70, 0.1)
gym = albert.subject('Gym')
gym.report_grade(100, 0.4)
gym.report_grade(100, 0.6)
print(albert.average_grade())




