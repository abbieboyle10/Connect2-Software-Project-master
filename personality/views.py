from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView
from django.http import JsonResponse


class QuizListView(ListView):
    model = Quiz
    template_name = 'personality/homequiz.html'


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'personality/quiz.html', {'obj': quiz})


def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
    })


def save_quiz_view(request, pk):
    if request.is_ajax():
        questions = []
        employee = Employee.objects.get(user=request.user)
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')
        print(data_)

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)
        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        e_score = 0
        i_score = 0
        n_score = 0
        s_score = 0
        f_score = 0
        t_score = 0
        p_score = 0
        j_score = 0

        results = []

        for q in questions:
            a_selected = request.POST.get(q.text)
            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if q.category == "e":
                            if a_selected == "Always":
                                e_score += 10
                                print(e_score)
                            elif a_selected == "Often":
                                e_score += 7
                                print(e_score)
                            elif a_selected == "Sometimes":
                                e_score += 5
                                print(e_score)
                            elif a_selected == "Rarely":
                                e_score += 3
                                print(e_score)
                            elif a_selected == "Never":
                                e_score += 0
                                print(e_score)
                        elif q.category == "i":
                            if a_selected == "Always":
                                i_score += 10
                                print(i_score)
                            elif a_selected == "Often":
                                i_score += 7
                                print(i_score)
                            elif a_selected == "Sometimes":
                                i_score += 5
                                print(i_score)
                            elif a_selected == "Rarely":
                                i_score += 3
                                print(i_score)
                            elif a_selected == "Never":
                                i_score += 0
                                print(i_score)
                        elif q.category == "n":
                            if a_selected == "Always":
                                n_score += 10
                                print(n_score)
                            elif a_selected == "Often":
                                n_score += 7
                                print(n_score)
                            elif a_selected == "Sometimes":
                                n_score += 5
                                print(n_score)
                            elif a_selected == "Rarely":
                                n_score += 3
                                print(n_score)
                            elif a_selected == "Never":
                                n_score += 0
                                print(n_score)
                        elif q.category == "s":
                            if a_selected == "Always":
                                s_score += 10
                                print(s_score)
                            elif a_selected == "Often":
                                s_score += 7
                                print(s_score)
                            elif a_selected == "Sometimes":
                                s_score += 5
                                print(s_score)
                            elif a_selected == "Rarely":
                                s_score += 3
                                print(s_score)
                            elif a_selected == "Never":
                                s_score += 0
                                print(s_score)
                        elif q.category == "t":
                            if a_selected == "Always":
                                t_score += 10
                                print(t_score)
                            elif a_selected == "Often":
                                t_score += 7
                                print(t_score)
                            elif a_selected == "Sometimes":
                                t_score += 5
                                print(t_score)
                            elif a_selected == "Rarely":
                                t_score += 3
                                print(t_score)
                            elif a_selected == "Never":
                                t_score += 0
                                print(t_score)
                        elif q.category == "f":
                            if a_selected == "Always":
                                f_score += 10
                                print(f_score)
                            elif a_selected == "Often":
                                f_score += 7
                                print(f_score)
                            elif a_selected == "Sometimes":
                                f_score += 5
                                print(f_score)
                            elif a_selected == "Rarely":
                                f_score += 3
                                print(f_score)
                            elif a_selected == "Never":
                                f_score += 0
                                print(f_score)
                        elif q.category == "p":
                            if a_selected == "Always":
                                p_score += 10
                                print(p_score)
                            elif a_selected == "Often":
                                p_score += 7
                                print(p_score)
                            elif a_selected == "Sometimes":
                                p_score += 5
                                print(p_score)
                            elif a_selected == "Rarely":
                                p_score += 3
                                print(p_score)
                            elif a_selected == "Never":
                                p_score += 0
                                print(p_score)
                        elif q.category == "j":
                            if a_selected == "Always":
                                j_score += 10
                                print(j_score)
                            elif a_selected == "Often":
                                j_score += 7
                                print(j_score)
                            elif a_selected == "Sometimes":
                                j_score += 5
                                print(j_score)
                            elif a_selected == "Rarely":
                                j_score += 3
                                print(j_score)
                            elif a_selected == "Never":
                                j_score += 0
                                print(j_score)

            else:
                results.append({str(q): 'not answered'})
        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)

        if e_score > i_score:
            if n_score > s_score:
                if f_score > t_score:
                    if j_score > p_score:

                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='e', second_letter='n', third_letter='f', fourth_letter='j', person_type='enfj', employee=employee,)
                    elif p_score > j_score:

                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='e', second_letter='n', third_letter='f', fourth_letter='p', person_type='enfp', employee=employee,)
                elif t_score > f_score:
                    if j_score > p_score:
                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='e', second_letter='n', third_letter='t', fourth_letter='j', person_type='entj', employee=employee,)
                    elif p_score > j_score:
                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='e', second_letter='n', third_letter='t', fourth_letter='p', person_type='entp', employee=employee,)
            elif s_score > n_score:
                if f_score > t_score:
                    if j_score > p_score:

                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='e', second_letter='s', third_letter='f', fourth_letter='j', person_type='esfj', employee=employee,)
                    elif p_score > j_score:

                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='e', second_letter='s', third_letter='f', fourth_letter='p', person_type='esfp', employee=employee,)
                elif t_score > f_score:
                    if j_score > p_score:

                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='e', second_letter='s', third_letter='t', fourth_letter='j', person_type='estj', employee=employee,)
                    elif p_score > j_score:

                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='e', second_letter='s', third_letter='t', fourth_letter='p', person_type='estp', employee=employee,)
        elif i_score > e_score:
            if n_score > s_score:
                if f_score > t_score:
                    if j_score > p_score:

                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='i', second_letter='n', third_letter='f', fourth_letter='j', person_type='infj', employee=employee,)
                    elif p_score > j_score:
                        infp
                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='i', second_letter='n', third_letter='f', fourth_letter='p', person_type='infp', employee=employee,)
                elif t_score > f_score:
                    if j_score > p_score:

                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='i', second_letter='n', third_letter='t', fourth_letter='j', person_type='intj', employee=employee,)
                    elif p_score > j_score:

                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='i', second_letter='n', third_letter='t', fourth_letter='p', person_type='intp', employee=employee,)
            elif s_score > n_score:
                if f_score > t_score:
                    if j_score > p_score:

                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='i', second_letter='s', third_letter='f', fourth_letter='j', person_type='isfj', employee=employee,)
                    elif p_score > j_score:

                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='i', second_letter='s', third_letter='f', fourth_letter='p', person_type='isfp', employee=employee,)
                elif t_score > f_score:
                    if j_score > p_score:

                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='i', second_letter='s', third_letter='t', fourth_letter='j', person_type='istj', employee=employee,)
                    elif p_score > j_score:

                        Result.objects.create(quiz=quiz, employee=employee, e_score=e_score, i_score=i_score, s_score=s_score,
                                              n_score=n_score, f_score=f_score, t_score=t_score, j_score=j_score, p_score=p_score)
                        Personality.objects.create(
                            first_letter='i', second_letter='s', third_letter='t', fourth_letter='p', person_type='istp', employee=employee,)
