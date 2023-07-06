import unittest
from neo import *
import fractions

class TestGCD(unittest.TestCase):

    def test_gcd_2_8(self):
        self.assertEquals(gcd(2,8),2)

    def test_gcd_88_77(self):
        self.assertEquals(gcd(88,77),11)

    def test_gcd_coprime_numbers(self):
        self.assertEquals(gcd(13,7),1)


class TestLCM(unittest.TestCase):

    def test_lcm_same_number(self):
        self.assertEquals(lcm(8,8),8)

    def test_lcm_5_10(self):
        self.assertEquals(lcm(5,10),10)

    def test_lcm_300_1000(self):
        self.assertEquals(lcm(300,1000), 3000)

    def test_lcm_coprime_primes(self):
        self.assertEquals(lcm(23,11), 23*11)

    def test_lcm_coprime_numbers(self):
        self.assertEquals(lcm(10,21), 210)


class TestMatrixFunctions(unittest.TestCase):
    case_1 = [  [0, 1, 0, 0, 0, 1],
                [4, 0, 0, 3, 2, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0] ]
    
    info_1 = ([2,3,4,5],[0,1],{0:2,1:7})
    
    case_2 = [  [0, 2, 1, 0, 0],
                [0, 0, 0, 3, 4],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0] ]

    info_2 = ([2,3,4],[0,1],{0:3,1:7})

    def test_copy_matrix(self):
        x = list([[0],[1]])
        y = copy_matrix(x)
        self.assertEquals(y,x)
        x[0] = [5]
        self.assertNotEqual(y,x)

    def test_case_1(self):
        case_1 = [  [0, 1, 0, 0, 0, 1],
                [4, 0, 0, 3, 2, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0] ]
    
        info_1 = ([2,3,4,5],[0,1],{0:2,1:9})
        R_1 = [[0,0,0,fractions.Fraction(1,2)],
                [0,fractions.Fraction(3,9),fractions.Fraction(2,9),0]]
        Q_1 = [[1,fractions.Fraction(-1,2)],
                [fractions.Fraction(-4,9),1]]
        inverse_1 = [[fractions.Fraction(9,7),fractions.Fraction(9,14)],
                    [fractions.Fraction(4,7),fractions.Fraction(9,7)]]
        answer_1 = [0,3,2,9,14]
        self.assertEquals(parse_to_standardized_form(case_1),info_1)
        self.assertEquals(make_r_i_minus_q(info_1[0],info_1[1],
            case_1,info_1[2]),(R_1,Q_1))
        self.assertEquals(invert_matrix(Q_1), inverse_1)
        self.assertEquals(multiply_matrix(inverse_1,R_1),
            [0,fractions.Fraction(3,14),fractions.Fraction(2,14),
            fractions.Fraction(9,14)])
        self.assertEquals(make_answer(multiply_matrix(inverse_1,R_1)),answer_1)
        self.assertEquals(solution(case_1),answer_1)
    def test_case_2(self):
        case_2 = [  [0, 2, 1, 0, 0],
                [0, 0, 0, 3, 4],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0] ]

        info_2 = ([2,3,4],[0,1],{0:3,1:7})
        R_2 = [ [fractions.Fraction(1,3),0,0],
                [0,fractions.Fraction(3,7),fractions.Fraction(4,7)] ]
        Q_2 = [ [1,0-fractions.Fraction(2,3)],
                [0,1] ]
        inverse_2 = [[1,fractions.Fraction(2,3)],
                    [0,1]]
        answer_2 = [7,6,8,21]
        self.assertEquals(parse_to_standardized_form(case_2),info_2)
        self.assertEquals(make_r_i_minus_q(info_2[0],info_2[1], case_2,info_2[2]),(R_2,Q_2))
        self.assertEquals(invert_matrix(Q_2), inverse_2)
        self.assertEquals(multiply_matrix(inverse_2,R_2),
            [fractions.Fraction(1,3),fractions.Fraction(2,7),
            fractions.Fraction(8,21)])
        self.assertEquals(make_answer(multiply_matrix(inverse_2,R_2)), answer_2)
        self.assertEquals(solution(case_2),answer_2)

    def test_case_3(self):
        case_3 = [
        [1, 2, 3, 0, 0, 0],
        [4, 5, 6, 0, 0, 0],
        [7, 8, 9, 1, 0, 0],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
        answer_3 = [1, 2, 3]
        self.assertEquals(solution(case_3),answer_3)
    
    def test_case_4(self):
        case_4 = [[0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
        [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
        [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
        [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        answer_4 = [1, 2, 3, 4, 5, 15]
        
        self.assertEquals(solution(case_4), answer_4)


    def test_case_5(self):
        case_5 = [
        [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
        [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
        [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        answer_5 = [4, 5, 5, 4, 2, 20]

        self.assertEquals(solution(case_5),answer_5)
 
#     answer_6[
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]) == [1, 1, 1, 1, 1, 5]
# )
 
# assert (
#     answer([
#         [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]) == [2, 1, 1, 1, 1, 6]
# )
 
# assert (
#     answer([
#         [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
#         [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
#         [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]) == [6, 44, 4, 11, 22, 13, 100]
# )
 
# assert (
#     answer([
#         [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
#         [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
#         [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
#         [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
#         [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]) == [1, 1, 1, 2, 5]

if __name__ == '__main__':
    unittest.main()