def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating

def convert_to_numeric(score):
    """
    Takes score input and changes the type to a float,
    """
    sanitized_score = float(score)
    return sanitized_score

def sum_of_middle_three(score1,score2,score3,score4,score5):
    """
    This will remove the min and max and add the remaining three together.
    """

    max_of_three = max(score1, score2, score3, score4, score5)
    min_of_three = min(score1, score2, score3, score4, score5)

    sum_of_middle_three = (score1 + score2 + score3 + score4 + score5) - max_of_three - min_of_three

    return sum_of_middle_three

def score_to_rating_string(score):
    """
    This will take the calculated score and return the string containing the written rating.
    """

    if 0 <= score < 1:
        rating_string = "Terrible"
    elif 1 <= score < 2:
        rating_string = "Bad"
    elif 2 <= score < 3:
        rating_string = "OK"
    elif 3 <= score < 4:
        rating_string = "Good"
    else:
        rating_string = "Excellent"

    return rating_string


print(scores_to_rating(10,20,30,40,50))
