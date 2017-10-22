# def is_correct(student_answer, correct_answer):
#     if student_answer == correct_answer:
#         return True
#     else:
#         return False
#
# def check_answers(my_answers,answers):
#     """
#     Checks the five answers provided to a multiple choice quiz and returns the results.
#     """
#     results= []
#
#     for i in range(len(my_answers)):
#         results.append(is_correct(my_answers[i], answers[i]))
#
#     count_correct = 0
#
#     for result in results:
#         if result == True:
#             count_correct += 1
#
#     if count_correct/5 > 0.7:
#         return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
#     else:
#         return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."
#
# test_dict = { "One":1, "Two":2, "Three":3, "Four":4, "Five":5 }
# #print(test_dict[7])
#
#
# def todo_list(new_task, base_list=['wake up']):
#     base_list.append(new_task)
#     return base_list
#
# print(todo_list("check the mail"))
# print(todo_list("begin orbital transfer"))
#
# # egg_count = 0
# #
# # def buy_eggs():
# #     egg_count += 12 # purchase a dozen eggs
# #
# # buy_eggs()
# # print(egg_count)
#
# from datetime import datetime
#
# import pytz
#
# utc = pytz.utc # utc is Coordinated Universal Time
# ist = pytz.timezone('Asia/Kolkata') #IST is Indian Standard Time
#
# now = datetime.now(tz=utc) # this is the current time in UTC
# ist_now = now.astimezone(ist) # this is the current time in IST.
#
# print("This is the current time in UTC: {}, and this is the current time in IST: {}.".format(now, ist_now))
#


def course_grader(test_scores):
    total = 0
    f = 0
    for score in test_scores:
        if score < 50:
            f = f + 1
        total = total + score

    average = total / len(test_scores)

    if average >=70 and f == 0:
        return "pass"
    else:
        return "fail"

def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70, 70, 70, 70, 70]))  # "pass"

if __name__ == "__main__":
    main()
