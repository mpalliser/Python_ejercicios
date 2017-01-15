class Yatzy:

    @staticmethod
    def chance(*dice):
        score = 0
        for die in dice:
            score = score + die
        return score

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) == 5:
            return 50
        return 0
        
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
    

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5
    
    def fours(self):
        sum = 0
        for at in range(5):
            if (self.dice[at] == 4): 
                sum += 4
        return sum
    

    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dice)): 
            if (self.dice[i] == 5):
                s = s + 5
        return s
    

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)): 
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum
    
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
