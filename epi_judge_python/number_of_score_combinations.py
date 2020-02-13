from test_framework import generic_test

# 16.1 Count the number of score combinations
#
# In an American football Bame, a play can lead to 2 points (safety), 3 points (field goal),
# or 7 points (touchdown, assuming the extra point). Many different
# combinations of 2,3, and 7 point plays can make up a final score.
# Write a program that takes a final score and scores for individual plays, 
# and returns the number of combinations of plays that result in the final score.
# Hint: Count the number of combinations in which there are 0 w0 plays, then 1 w0 plays, etc.
def num_combinations_for_final_score(final_score, individual_play_scores):
    num_combinations_for_score = [[1] + [0] * final_score
                                  for _ in individual_play_scores]

    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            w_out_this_indv_play_score = num_combinations_for_score[i-1][j] if i>=1 else 0
            prev_w_this_indv_play_score = (num_combinations_for_score[i][j-individual_play_scores[i]]
                                            if j>=individual_play_scores[i] else 0)
            num_combinations_for_score[i][j] = w_out_this_indv_play_score + prev_w_this_indv_play_score
    return num_combinations_for_score[-1][-1]
    



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
