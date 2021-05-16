from sklearn.preprocessing import MultiLabelBinarizer

import pickle
import os
import numpy as np


def PersonalityGrouper(e_score, i_score, n_score, s_score, t_score, f_score, p_score, j_score):
    if e_score > i_score:
        if n_score > s_score:
            if f_score > t_score:
                if j_score > p_score:

                    return set('enfj - elephant')
                elif p_score > j_score:
                    return set('enfp - elephant')

                elif t_score > f_score:
                    if j_score > p_score:
                        return set('entj - owl')

                    elif p_score > j_score:
                        return set('entp - owl')

        elif s_score > n_score:
            if f_score > t_score:
                if j_score > p_score:
                    return set('esfj - beaver')

                elif p_score > j_score:
                    return set('esfp - fox')

                elif t_score > f_score:
                    if j_score > p_score:
                        return set('estj - beaver')

                    elif p_score > j_score:
                        return set('estp - fox"')

        elif i_score > e_score:
            if n_score > s_score:
                if f_score > t_score:
                    if j_score > p_score:

                        return set('infj - elephant')

                    elif p_score > j_score:
                        return set('infp - elephant')

                elif t_score > f_score:
                    if j_score > p_score:
                        return set('intj - owl')

                    elif p_score > j_score:

                        return "intp - owl"
        elif s_score > n_score:
            if f_score > t_score:
                if j_score > p_score:
                    return set('isfj - beaver')

                elif p_score > j_score:
                    return set('isfp - fox')

            elif t_score > f_score:
                if j_score > p_score:
                    return set('istj - beaver')

                elif p_score > j_score:
                    return set('istp - fox')


def AnimaltoJob(sample):

    test_requests = tuple([sample])
    print(test_requests)
    tags_split = [['sj'], ['sj'], ['nt'], ['nf'], ['sp'], ['nt'], ['sj'], ['nf'], ['sp'], ['sp'], ['sj'], ['sp'], ['sp'], ['nf'], ['nf'], ['sp'], ['sp'], ['sj'], ['nt'], ['nt'], ['sp'], [
        'sj'], ['sj'], ['sj'], ['sj'], ['nt'], ['sj'], ['nf'], ['nf'], ['nf'], ['nf'], ['sp'], ['nt'], ['sj'], ['nf'], ['nf'], ['sj'], ['sj'], ['sj'], ['nf'], ['nt'], ['sj'], ['nt'], ['nf']]
    tag_encoder = MultiLabelBinarizer()
    tag_encoded = tag_encoder.fit_transform(tags_split)
    num_tag = len(tag_encoded[0])
    classifier = CustomModelPrediction.from_path('.')
    results = classifier.predict(test_requests)
    for i in range(len(results)):
        for idx, val in enumerate(results[i]):
            if val > 0.6:
                print(tag_encoder.classes_[idx])
                personality = tag_encoder.classes_[idx]
                print(personality)

        if personality == "nt":
            return set('owl')
        elif personality == "nf":
            return set('elephany')
        elif personality == 'sp':
            return set('fox')
        else:
            return set('beaver')


def RankingApplications(person_type, employeeskills):
    job_type = "owl"
    jobskills = {'Java', 'Python', 'Testing'}
    match = False
    score = 0
    intersection = employeeskills.intersection(jobskills)
    intersection_as_list = list(intersection)

    if job_type == person_type:

        match = True
        score += 1

    else:

        match = False

    for x in intersection_as_list:

        score += 1

    return score


class Job(str):
    title = ""
    city = ""
    animal_type = ""
    score = ""


class JobSkill(Job):
    skill_title = ""


def Making_Recommendations(employee_skills, employee_city, employee_person):
    job1 = Job("Python Dev", "Dublin", "owl")
    job2 = Job("Java Dev", "Dublin",  "owl")
    job3 = Job("Web Dev", "Dublin", "beaver")
    job4 = Job("Database Dev", "Dublin", "beaver")
    job5 = Job("Design Dev", "Cork", "owl")
    job6 = Job("Security Dev", "Cork", "fox")

    skill1 = JobSkill(job1, "Python")
    skill2 = JobSkill(job1, "Java")
    skill3 = JobSkill(job2, "SQL")
    skill4 = JobSkill(job2, "Python")
    skill5 = JobSkill(job3, "CSS")
    skill6 = JobSkill(job3, "Python")
    skill7 = JobSkill(job4, "Django")
    skill8 = JobSkill(job4, "Database")
    skill9 = JobSkill(job5, "Python")
    skill10 = JobSkill(job5, "Django")
    skill11 = JobSkill(job6, "Network")
    skill12 = JobSkill(job6, "Cyber")
    jobs = Job.objects.all()
    for job in jobs:
        jobskills = job.jobskill_set.all().values_list('title', flat=True).distinct()
        intersection = employee_skills.intersection(jobskills)
        intersection_as_list = list(intersection)
        matched_amount = len(intersection)/2
        score = matched_amount
        if job.animal_type == employee_person:
            score += 1
        else:
            lscore = 0
        job.score = score
        jobset = Job.objects.all().values_list('title').order_by('-score')
        print(jobset)
