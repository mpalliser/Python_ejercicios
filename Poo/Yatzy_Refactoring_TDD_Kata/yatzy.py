class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        score = 0
        for die in dice:
            score = score + die
        return score

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) != 5:
            return 0
        return 50
        
    @staticmethod
    def ones(*dice):
        '''
        ONE = 1
        return dice.count(ONE) *ONE
        '''
        total_ones = 0
        for die in dice:
            if (die == 1):
                total_ones += 1
        return total_ones
    

    @staticmethod
    def twos(*dice):
        TWO = 2
        return dice.count(TWO) * TWO
    
    @staticmethod
    def threes( *dice):
        THREE = 3
        return dice.count(THREE) * THREE

    
    def fours(self):
        FOUR = 4
        return self.dice.count(FOUR) *FOUR
    

    def fives(self):
        FIVE = 5
        return self.dice.count(FIVE) *FIVE
    

    def sixes(self):
        SIX = 6
        return self.dice.count(SIX) *SIX
    
    @staticmethod
    def pair(*dice):
        total_score_pair = 0
        for die in dice:
            if dice.count(die) >= 2 and die > total_score_pair /2:
                total_score_pair = die * 2
        return total_score_pair
        '''
        PAIR=2
        for numero in range(6, 0, -1):
            if dice.count(numero) >=2:
                return PAIR * numero
        return 0
        '''
    
    @staticmethod
    def two_pair(*dice):
        PAIR = 2
        pairs = 0
        score = 0
        for number in range(1, 7, 1):
            if dice.count(number) >= PAIR:
                pairs += 1  
                score += number*PAIR
        if pairs == PAIR:
            return score
        return 0


    @staticmethod
    def four_of_a_kind(*dice):
        POKER = 4
        score = 0
        for number in range(1, 7, 1):
            if dice.count(number) >= POKER: 
                score += number * POKER
        return score
    

    @staticmethod
    def three_of_a_kind(*dice):
        THREE = 3
        score = 0
        for number in range(1, 7, 1):
            if dice.count(number) >= THREE: 
                score += number * THREE
        return score
    

    @staticmethod
    def smallStraight(*dice):
        score = 0
        for number in range(1, 6, 1):
            if dice.count(number) != 1:
                return 0
            score += number
        return score
    

    @staticmethod
    def largeStraight(*dice):
        score = 0
        for number in range(2, 7, 1):
            if dice.count(number) != 1:
                return 0
            score += number
        return score
    

    @staticmethod
    def fullHouse(*dice):
        TWO= 2
        for number in range(6, 0, -1):
            if dice.count(number) == TWO and Yatzy.three_of_a_kind(*dice):
                return number*TWO + Yatzy.three_of_a_kind(*dice)      
        return 0
