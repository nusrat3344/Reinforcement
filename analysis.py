# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    " to cross the bridge noise must be less than 0.0169 (close to zero) "
    answerNoise = 0.002
    return answerDiscount, answerNoise

def question3a():
    """ 1) To make the agent take the close exit discount should be lower than 0.316
            so that it doesn't take long route
        2) Noise must be close to zero if the agent wants to risk the cliff
    """
    answerDiscount = 0.3
    answerNoise = 0
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    """ 1) To make the agent take the close exit discount should be lower than 0.316
                so that it doesn't take long route
        2) Noise must be greater if the agent wants to avoid the cliff
    """

    answerDiscount = 0.3
    answerNoise = 0.2
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    """ 1) To make the agent take the close exit discount should be greater than 0.316
                    so that it takes long route
        2) Noise must be close to zero if the agent wants to risk the cliff
    """
    answerDiscount = 0.9
    answerNoise = 0
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    """
        1) To make the agent take the close exit discount should be greater than 0.316
                        so that it takes long route
        2) Noise must be greater if the agent wants to avoid the cliff
    """
    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    """
        Discount must be higher so that the agent doesn't take an exit
        as he gets more reward for living than taking an exit
        so it prefers living and never terminates.
        Noise doesn't effect in this case as the agent will keep choosing longer
        path to get more reward.
    """
    answerDiscount = 1
    answerNoise = 0.2
    answerLivingReward = 20
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question8():
    """
    In this case for both the epsilon values 0 and 1, the agent can not
    pass the bridge. As epsilon value ranges within 0 to 1, for no other
    value the agent will be able to cross the bridge. As there is no possible
    epsilon value to cross the bridge, there is no learning rate.
    """

    # answerEpsilon = None
    # answerLearningRate = None
    return 'NOT POSSIBLE'
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
