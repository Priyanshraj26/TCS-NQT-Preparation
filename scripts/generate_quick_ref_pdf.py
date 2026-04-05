#!/usr/bin/env python3
"""
Generate Quick Reference PDF for TCS NQT Aptitude Preparation
Compact 20-30 page reference sheet with formulas, shortcuts, and tips.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.pdf_generator import TCSNQTPDFGenerator


def build_pdf():
    output = os.path.join(os.path.dirname(__file__), '..', '01-Aptitude', 'Quick-Reference-PDF.pdf')
    pdf = TCSNQTPDFGenerator(
        output_path=output,
        title="TCS NQT Quick Reference",
        subject="Aptitude Formulas, Shortcuts & Tips"
    )
    pdf.add_cover_page()

    # ================================================================
    # SECTION 1: NUMBER SYSTEM
    # ================================================================
    pdf.add_topic_header("1. Number System", "Divisibility, HCF/LCM, remainders and properties of numbers.")

    pdf.add_subtopic_header("Divisibility Rules")
    pdf.add_table([
        ["Divisor", "Rule"],
        ["2", "Last digit is even (0, 2, 4, 6, 8)"],
        ["3", "Sum of digits divisible by 3"],
        ["4", "Last two digits form a number divisible by 4"],
        ["5", "Last digit is 0 or 5"],
        ["6", "Divisible by both 2 and 3"],
        ["7", "Double last digit, subtract from rest; result div by 7"],
        ["8", "Last three digits divisible by 8"],
        ["9", "Sum of digits divisible by 9"],
        ["11", "Difference of sum of alternate digits divisible by 11"],
    ])

    pdf.add_subtopic_header("HCF and LCM")
    pdf.add_formula_section("Product Rule", "HCF(a,b) x LCM(a,b) = a x b",
                            "Applies only for two numbers.")
    pdf.add_formula_section("HCF of Fractions", "HCF = HCF(numerators) / LCM(denominators)")
    pdf.add_formula_section("LCM of Fractions", "LCM = LCM(numerators) / HCF(denominators)")
    pdf.add_tip("For three numbers: LCM(a,b,c) = LCM(LCM(a,b), c)")

    pdf.add_subtopic_header("Remainder Theorems")
    pdf.add_formula_section("Remainder Theorem",
        "(a x b) mod n = [(a mod n) x (b mod n)] mod n")
    pdf.add_formula_section("Fermat's Little Theorem",
        "a^(p-1) mod p = 1, when p is prime and gcd(a,p)=1")
    pdf.add_formula_section("Wilson's Theorem",
        "(p-1)! mod p = p-1, when p is prime")
    pdf.add_tip("Cyclicity of units digits: 2->{2,4,8,6}, 3->{3,9,7,1}, 7->{7,9,3,1}, 8->{8,4,2,6}")

    pdf.add_page_break()

    # ================================================================
    # SECTION 2: PERCENTAGES
    # ================================================================
    pdf.add_topic_header("2. Percentages", "Conversion shortcuts and successive percentage changes.")

    pdf.add_subtopic_header("Fraction-Percentage Conversion Table")
    pdf.add_table([
        ["Fraction", "Percentage", "Fraction", "Percentage"],
        ["1/2", "50%", "1/8", "12.5%"],
        ["1/3", "33.33%", "1/9", "11.11%"],
        ["1/4", "25%", "1/10", "10%"],
        ["1/5", "20%", "1/11", "9.09%"],
        ["1/6", "16.67%", "1/12", "8.33%"],
        ["1/7", "14.28%", "1/15", "6.67%"],
        ["2/3", "66.67%", "1/20", "5%"],
        ["3/4", "75%", "2/5", "40%"],
        ["4/5", "80%", "3/5", "60%"],
        ["5/6", "83.33%", "7/8", "87.5%"],
    ])

    pdf.add_subtopic_header("Key Formulas")
    pdf.add_formula_section("Percentage Change",
        "Change% = (Difference / Original) x 100")
    pdf.add_formula_section("Successive Percentage Change",
        "Net% = a + b + (a x b)/100",
        "For two successive changes of a% and b%.")
    pdf.add_formula_section("Reverse Percentage",
        "If price increases by R%, original = New x 100/(100+R)")
    pdf.add_tip("To increase by 20% multiply by 1.2; to decrease by 20% multiply by 0.8.")

    pdf.add_page_break()

    # ================================================================
    # SECTION 3: PROFIT & LOSS
    # ================================================================
    pdf.add_topic_header("3. Profit and Loss", "Formulas and shortcut methods for profit/loss problems.")

    pdf.add_formula_section("Profit %", "Profit% = (Profit / CP) x 100")
    pdf.add_formula_section("Loss %", "Loss% = (Loss / CP) x 100")
    pdf.add_formula_section("SP from Profit%", "SP = CP x (100 + P%) / 100")
    pdf.add_formula_section("SP from Loss%", "SP = CP x (100 - L%) / 100")
    pdf.add_formula_section("Discount", "SP = MP x (100 - D%) / 100, where MP = Marked Price")
    pdf.add_formula_section("Two Successive Discounts",
        "Effective Discount = a + b - (a x b)/100")
    pdf.add_formula_section("False Weight Gain%",
        "Gain% = (True Weight - False Weight) / False Weight x 100")

    pdf.add_tip("If CP of x items = SP of y items, then Profit% = (x-y)/y x 100")
    pdf.add_tip("Buy x get y free => Discount% = y/(x+y) x 100")

    pdf.add_page_break()

    # ================================================================
    # SECTION 4: TIME, SPEED & DISTANCE
    # ================================================================
    pdf.add_topic_header("4. Time, Speed and Distance", "Relative speed, trains, boats, and circular motion.")

    pdf.add_formula_section("Basic Formula", "Distance = Speed x Time")
    pdf.add_formula_section("Unit Conversion", "1 km/hr = 5/18 m/s  |  1 m/s = 18/5 km/hr")
    pdf.add_formula_section("Average Speed (same distance)",
        "Avg Speed = 2 x S1 x S2 / (S1 + S2)",
        "When equal distances are covered at two different speeds.")

    pdf.add_subtopic_header("Trains")
    pdf.add_formula_section("Train passing a pole/person",
        "Time = Length of train / Speed of train")
    pdf.add_formula_section("Train passing a platform",
        "Time = (Length of train + Length of platform) / Speed")
    pdf.add_formula_section("Two trains - same direction",
        "Relative Speed = |S1 - S2|; Distance = Sum/Diff of lengths")
    pdf.add_formula_section("Two trains - opposite direction",
        "Relative Speed = S1 + S2; Distance = Sum of lengths")

    pdf.add_subtopic_header("Boats and Streams")
    pdf.add_formula_section("Downstream Speed", "D = B + S (boat speed + stream speed)")
    pdf.add_formula_section("Upstream Speed", "U = B - S")
    pdf.add_formula_section("Still Water Speed", "B = (D + U) / 2")
    pdf.add_formula_section("Stream Speed", "S = (D - U) / 2")

    pdf.add_subtopic_header("Circular Motion")
    pdf.add_formula_section("First Meeting (opposite direction)",
        "Time = Track Length / (S1 + S2)")
    pdf.add_formula_section("First Meeting (same direction)",
        "Time = Track Length / |S1 - S2|")

    pdf.add_page_break()

    # ================================================================
    # SECTION 5: TIME & WORK
    # ================================================================
    pdf.add_topic_header("5. Time and Work", "Work-rate problems, pipes and cisterns, efficiency method.")

    pdf.add_formula_section("Basic Concept",
        "If A can do work in 'n' days, A's 1 day work = 1/n")
    pdf.add_formula_section("Combined Work",
        "1/T = 1/A + 1/B  =>  T = (A x B) / (A + B)")
    pdf.add_formula_section("Three workers",
        "1/T = 1/A + 1/B + 1/C")
    pdf.add_formula_section("Wages Ratio",
        "Wages are distributed in ratio of efficiencies (or work done)")

    pdf.add_subtopic_header("Pipes and Cisterns")
    pdf.add_formula_section("Filling pipe",
        "Work rate = +1/t (positive)")
    pdf.add_formula_section("Emptying pipe (leak)",
        "Work rate = -1/t (negative)")
    pdf.add_formula_section("Net rate",
        "Net = 1/Fill - 1/Empty; Time = 1/Net")

    pdf.add_subtopic_header("LCM / Efficiency Method")
    pdf.add_text("1. Take LCM of all given days as Total Work units.")
    pdf.add_text("2. Efficiency of each = Total Work / Individual days.")
    pdf.add_text("3. Combined efficiency = Sum of individual efficiencies.")
    pdf.add_text("4. Time = Total Work / Combined efficiency.")
    pdf.add_tip("This method avoids fractions entirely -- use it in exams!")

    pdf.add_page_break()

    # ================================================================
    # SECTION 6: AVERAGES & MIXTURES
    # ================================================================
    pdf.add_topic_header("6. Averages and Mixtures", "Weighted average, alligation rule.")

    pdf.add_formula_section("Average", "Average = Sum of observations / Number of observations")
    pdf.add_formula_section("Weighted Average",
        "W.Avg = (w1*x1 + w2*x2 + ...) / (w1 + w2 + ...)")
    pdf.add_formula_section("New Average (adding a member)",
        "New Avg = Old Avg + (New value - Old Avg) / (n + 1)")

    pdf.add_subtopic_header("Alligation Rule")
    pdf.add_formula_section("Alligation Formula",
        "n1/n2 = (A2 - Avg) / (Avg - A1)",
        "n1, n2 = quantities; A1 = cheaper price; A2 = dearer price; Avg = mean price")
    pdf.add_tip("Draw the alligation cross: Cheaper -- Mean -- Dearer; differences give the ratio.")

    pdf.add_page_break()

    # ================================================================
    # SECTION 7: RATIO & PROPORTION
    # ================================================================
    pdf.add_topic_header("7. Ratio and Proportion")

    pdf.add_formula_section("Proportion", "If a:b = c:d then a*d = b*c (cross multiplication)")
    pdf.add_formula_section("Componendo", "(a+b)/b = (c+d)/d")
    pdf.add_formula_section("Dividendo", "(a-b)/b = (c-d)/d")
    pdf.add_formula_section("Componendo-Dividendo",
        "(a+b)/(a-b) = (c+d)/(c-d)")
    pdf.add_formula_section("Direct Proportion", "If x increases, y increases: y = kx")
    pdf.add_formula_section("Inverse Proportion", "If x increases, y decreases: xy = k")
    pdf.add_tip("In mixture replacement: After n operations, remaining = V x (1 - R/V)^n")

    pdf.add_page_break()

    # ================================================================
    # SECTION 8: SIMPLE & COMPOUND INTEREST
    # ================================================================
    pdf.add_topic_header("8. Simple and Compound Interest")

    pdf.add_subtopic_header("Simple Interest")
    pdf.add_formula_section("SI Formula", "SI = P x R x T / 100")
    pdf.add_formula_section("Amount", "A = P + SI = P(1 + RT/100)")

    pdf.add_subtopic_header("Compound Interest")
    pdf.add_formula_section("CI Formula", "A = P(1 + R/100)^T")
    pdf.add_formula_section("CI Amount", "CI = A - P = P[(1 + R/100)^T - 1]")
    pdf.add_formula_section("Half-yearly compounding",
        "A = P(1 + R/200)^(2T)")
    pdf.add_formula_section("Quarterly compounding",
        "A = P(1 + R/400)^(4T)")
    pdf.add_formula_section("Difference (2 years)",
        "CI - SI = P(R/100)^2",
        "Shortcut for 2-year problems.")
    pdf.add_formula_section("Difference (3 years)",
        "CI - SI = P(R/100)^2 x (3 + R/100)")

    pdf.add_page_break()

    # ================================================================
    # SECTION 9: PERMUTATIONS & COMBINATIONS
    # ================================================================
    pdf.add_topic_header("9. Permutations and Combinations")

    pdf.add_formula_section("Factorial", "n! = n x (n-1) x (n-2) x ... x 1;  0! = 1")
    pdf.add_formula_section("Permutation (nPr)",
        "nPr = n! / (n-r)!",
        "Arrangement of r items from n (order matters).")
    pdf.add_formula_section("Combination (nCr)",
        "nCr = n! / [r! x (n-r)!]",
        "Selection of r items from n (order does NOT matter).")
    pdf.add_formula_section("Circular Permutation", "(n-1)! ways to arrange n items in a circle")
    pdf.add_formula_section("With repetition",
        "Permutations = n! / (p! x q! x ...)",
        "Where p, q... are frequencies of repeated items.")
    pdf.add_formula_section("Key Identity", "nCr = nC(n-r)  |  nC0 = nCn = 1")
    pdf.add_formula_section("Pascal's Rule", "nCr = (n-1)C(r-1) + (n-1)Cr")

    pdf.add_page_break()

    # ================================================================
    # SECTION 10: PROBABILITY
    # ================================================================
    pdf.add_topic_header("10. Probability")

    pdf.add_formula_section("Basic Probability", "P(E) = Favourable outcomes / Total outcomes")
    pdf.add_formula_section("Complementary", "P(E') = 1 - P(E)")
    pdf.add_formula_section("Addition Rule",
        "P(A or B) = P(A) + P(B) - P(A and B)")
    pdf.add_formula_section("Mutually Exclusive",
        "P(A or B) = P(A) + P(B)  [when P(A and B) = 0]")
    pdf.add_formula_section("Independent Events",
        "P(A and B) = P(A) x P(B)")
    pdf.add_formula_section("Conditional Probability",
        "P(A|B) = P(A and B) / P(B)")
    pdf.add_formula_section("Dice: sum of two dice",
        "Total outcomes = 36; P(sum=7) = 6/36 = 1/6 (highest)")
    pdf.add_formula_section("Cards",
        "52 cards: 4 suits x 13 ranks; P(Ace) = 4/52 = 1/13")

    pdf.add_page_break()

    # ================================================================
    # SECTION 11: GEOMETRY & MENSURATION
    # ================================================================
    pdf.add_topic_header("11. Geometry and Mensuration", "Areas, volumes, surface areas of all common shapes.")

    pdf.add_subtopic_header("2D Figures -- Area & Perimeter")
    pdf.add_table([
        ["Shape", "Area", "Perimeter"],
        ["Square (side a)", "a^2", "4a"],
        ["Rectangle (l x b)", "l x b", "2(l + b)"],
        ["Triangle (base b, ht h)", "(1/2) x b x h", "a + b + c"],
        ["Equilateral Triangle (a)", "(sqrt(3)/4) x a^2", "3a"],
        ["Circle (radius r)", "pi x r^2", "2 x pi x r"],
        ["Semicircle (r)", "(pi x r^2) / 2", "pi x r + 2r"],
        ["Trapezium (a,b,h)", "(1/2)(a+b) x h", "Sum of all sides"],
        ["Parallelogram (b, h)", "b x h", "2(a + b)"],
        ["Rhombus (d1, d2)", "(1/2) x d1 x d2", "4a"],
    ])

    pdf.add_subtopic_header("3D Figures -- Volume & Surface Area")
    pdf.add_table([
        ["Shape", "Volume", "TSA / CSA"],
        ["Cube (a)", "a^3", "TSA=6a^2, CSA=4a^2"],
        ["Cuboid (l,b,h)", "l x b x h", "TSA=2(lb+bh+lh), CSA=2h(l+b)"],
        ["Cylinder (r, h)", "pi x r^2 x h", "TSA=2pi*r(r+h), CSA=2pi*r*h"],
        ["Cone (r, h, l)", "(1/3) pi r^2 h", "TSA=pi*r(r+l), CSA=pi*r*l"],
        ["Sphere (r)", "(4/3) pi r^3", "4 pi r^2"],
        ["Hemisphere (r)", "(2/3) pi r^3", "TSA=3pi*r^2, CSA=2pi*r^2"],
    ])

    pdf.add_subtopic_header("Important Geometry Facts")
    pdf.add_formula_section("Heron's Formula",
        "Area = sqrt[s(s-a)(s-b)(s-c)], where s = (a+b+c)/2")
    pdf.add_formula_section("Angle sum of polygon",
        "(n-2) x 180 degrees, each interior angle of regular polygon = (n-2)*180/n")
    pdf.add_formula_section("Arc and Sector",
        "Arc length = (theta/360) x 2*pi*r  |  Sector area = (theta/360) x pi*r^2")

    pdf.add_page_break()

    # ================================================================
    # SECTION 12: ALGEBRA IDENTITIES
    # ================================================================
    pdf.add_topic_header("12. Algebra Identities")

    pdf.add_formula_section("Square of Sum", "(a + b)^2 = a^2 + 2ab + b^2")
    pdf.add_formula_section("Square of Difference", "(a - b)^2 = a^2 - 2ab + b^2")
    pdf.add_formula_section("Difference of Squares", "a^2 - b^2 = (a + b)(a - b)")
    pdf.add_formula_section("Cube of Sum", "(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3")
    pdf.add_formula_section("Cube of Difference", "(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3")
    pdf.add_formula_section("Sum of Cubes", "a^3 + b^3 = (a + b)(a^2 - ab + b^2)")
    pdf.add_formula_section("Difference of Cubes", "a^3 - b^3 = (a - b)(a^2 + ab + b^2)")
    pdf.add_formula_section("Sum of first n naturals", "n(n+1)/2")
    pdf.add_formula_section("Sum of squares", "n(n+1)(2n+1)/6")
    pdf.add_formula_section("Sum of cubes", "[n(n+1)/2]^2")
    pdf.add_formula_section("AP: nth term", "a_n = a + (n-1)d  |  Sum = n/2 [2a + (n-1)d]")
    pdf.add_formula_section("GP: nth term", "a_n = a*r^(n-1)  |  Sum = a(r^n - 1)/(r - 1)")

    pdf.add_page_break()

    # ================================================================
    # SECTION 13: SHORTCUT METHODS
    # ================================================================
    pdf.add_topic_header("13. Shortcut Methods and Vedic Math Tricks")

    pdf.add_subtopic_header("Quick Multiplication Tricks")
    pdf.add_formula_section("Multiply by 11",
        "Insert sum of digits between them: 23 x 11 = 2_(2+3)_3 = 253",
        "If sum > 9, carry over: 78 x 11 = 7_(7+8)_8 = 858")
    pdf.add_formula_section("Multiply by 5",
        "Divide by 2 and multiply by 10: 48 x 5 = 48/2 x 10 = 240")
    pdf.add_formula_section("Multiply by 25",
        "Divide by 4 and multiply by 100: 48 x 25 = 48/4 x 100 = 1200")
    pdf.add_formula_section("Multiply by 125",
        "Divide by 8 and multiply by 1000")
    pdf.add_formula_section("Multiply numbers near 100",
        "97 x 96: Deficiencies 3, 4. Answer: (97-4)|(3x4) = 93|12 = 9312",
        "Base method: (a-d2)*100 + d1*d2 where d1,d2 are deficiencies from 100.")

    pdf.add_subtopic_header("Quick Division Tricks")
    pdf.add_formula_section("Divide by 5", "Multiply by 2 and divide by 10")
    pdf.add_formula_section("Divide by 25", "Multiply by 4 and divide by 100")
    pdf.add_formula_section("Divide by 50", "Multiply by 2 and divide by 100")

    pdf.add_subtopic_header("Common Pythagorean Triplets")
    pdf.add_table([
        ["Triplet", "Multiple x2", "Multiple x3"],
        ["3, 4, 5", "6, 8, 10", "9, 12, 15"],
        ["5, 12, 13", "10, 24, 26", "15, 36, 39"],
        ["7, 24, 25", "14, 48, 50", "21, 72, 75"],
        ["8, 15, 17", "16, 30, 34", "24, 45, 51"],
        ["9, 40, 41", "18, 80, 82", "--"],
        ["11, 60, 61", "20, 21, 29", "12, 35, 37"],
    ])

    pdf.add_page_break()

    # ================================================================
    # SECTION 14: SQUARES AND CUBES TABLE
    # ================================================================
    pdf.add_topic_header("14. Squares and Cubes (1-30)")

    # Split into two tables for readability
    sq_data_1 = [["n", "n^2", "n^3"]]
    for n in range(1, 16):
        sq_data_1.append([str(n), str(n**2), str(n**3)])

    sq_data_2 = [["n", "n^2", "n^3"]]
    for n in range(16, 31):
        sq_data_2.append([str(n), str(n**2), str(n**3)])

    pdf.add_table(sq_data_1)
    pdf.add_table(sq_data_2)

    pdf.add_page_break()

    # ================================================================
    # SECTION 15: LOGICAL REASONING TIPS
    # ================================================================
    pdf.add_topic_header("15. Logical Reasoning Tips")

    pdf.add_subtopic_header("Number Series Patterns")
    pdf.add_text("<b>Common patterns to check:</b>")
    pdf.add_text("1. Constant difference (AP): 2, 5, 8, 11, ... (diff = +3)")
    pdf.add_text("2. Increasing/decreasing differences: 1, 2, 4, 7, 11 (diff: 1,2,3,4)")
    pdf.add_text("3. Multiplication pattern: 2, 6, 18, 54 (x3)")
    pdf.add_text("4. Squares/Cubes: 1, 4, 9, 16, 25 or 1, 8, 27, 64")
    pdf.add_text("5. Alternating operations: +2, x2, +2, x2")
    pdf.add_text("6. Two interleaved series: 1, 10, 2, 20, 3, 30")
    pdf.add_text("7. n^2+1 or n^2-1 type: 2, 5, 10, 17, 26 (n^2+1)")
    pdf.add_tip("Always compute first differences, then second differences. If second differences form a pattern, you have found it.")

    pdf.add_subtopic_header("Coding-Decoding Methods")
    pdf.add_text("<b>Letter coding:</b> Check position shifts (A=1, B=2, ..., Z=26).")
    pdf.add_text("<b>Reverse alphabet:</b> A<->Z, B<->Y, C<->X ... (position + reverse = 27)")
    pdf.add_text("<b>Number coding:</b> Map letters to numbers; check +1, +2, -1, reverse patterns.")
    pdf.add_text("<b>Substitution coding:</b> Real-world objects mapped to other words -- track consistently.")
    pdf.add_tip("Make a quick A-Z numbered reference: A=1 through Z=26 before solving.")

    pdf.add_subtopic_header("Blood Relations Shortcuts")
    pdf.add_text("<b>Key:</b> Draw a family tree diagram. Males on left, females on right.")
    pdf.add_text("Father's/Mother's son = Brother | daughter = Sister")
    pdf.add_text("Father's/Mother's brother = Uncle | sister = Aunt")
    pdf.add_text("Son's wife = Daughter-in-law | Daughter's husband = Son-in-law")
    pdf.add_text("Brother's/Sister's son = Nephew | daughter = Niece")
    pdf.add_tip("Use + for male, - for female. Go generation by generation.")

    pdf.add_subtopic_header("Direction Sense Tricks")
    pdf.add_text("Draw N-E-S-W cross. Start at origin.")
    pdf.add_text("Right turn from North = East, Left turn from North = West.")
    pdf.add_text("Opposite: N<->S, E<->W.")
    pdf.add_text("Use Pythagoras for final distance when path has right-angle turns.")
    pdf.add_tip("Clockwise: N -> E -> S -> W. Counter-clockwise: N -> W -> S -> E.")

    pdf.add_subtopic_header("Seating Arrangement Approach")
    pdf.add_text("1. Read ALL clues before drawing. Identify fixed positions first.")
    pdf.add_text("2. Use definite clues first (e.g., 'A sits at end'), then relative clues.")
    pdf.add_text("3. For circular: fix one person, place others relative to them.")
    pdf.add_text("4. For linear: mark Left-Right clearly; 'left of' means towards left end.")
    pdf.add_text("5. Use elimination -- if clue says 'not adjacent', rule out those spots.")
    pdf.add_tip("Always verify your final arrangement against ALL given clues.")

    pdf.add_page_break()

    # ================================================================
    # SECTION 16: MENTAL MATH TECHNIQUES
    # ================================================================
    pdf.add_topic_header("16. Mental Math Techniques")

    pdf.add_subtopic_header("Squaring Numbers Near 50")
    pdf.add_formula_section("Method",
        "n^2 = (25 + d) | d^2,  where d = n - 50",
        "Example: 53^2 => d=3, Answer = (25+3)|(3^2) = 28|09 = 2809. "
        "47^2 => d=-3, Answer = (25-3)|(3^2) = 22|09 = 2209.")

    pdf.add_subtopic_header("Squaring Numbers Near 100")
    pdf.add_formula_section("Method",
        "n^2 = (n + d) | d^2,  where d = n - 100",
        "Example: 103^2 => d=3, Answer = (103+3)|(3^2) = 106|09 = 10609. "
        "97^2 => d=-3, Answer = (97-3)|(3^2) = 94|09 = 9409.")

    pdf.add_subtopic_header("Squaring Numbers Ending in 5")
    pdf.add_formula_section("Method",
        "n5^2 = n x (n+1) | 25",
        "Example: 35^2 = 3x4|25 = 1225.  85^2 = 8x9|25 = 7225.")

    pdf.add_subtopic_header("Quick Percentage Calculations")
    pdf.add_text("<b>10% of x:</b> Move decimal one place left. 10% of 450 = 45.")
    pdf.add_text("<b>5% of x:</b> Half of 10%. 5% of 450 = 22.5.")
    pdf.add_text("<b>15% of x:</b> 10% + 5%. 15% of 450 = 45 + 22.5 = 67.5.")
    pdf.add_text("<b>20% of x:</b> Divide by 5. 20% of 450 = 90.")
    pdf.add_text("<b>25% of x:</b> Divide by 4. 25% of 450 = 112.5.")
    pdf.add_text("<b>33.3% of x:</b> Divide by 3. 33.3% of 450 = 150.")
    pdf.add_text("<b>1% of x:</b> Move decimal two places left. 1% of 450 = 4.5.")
    pdf.add_tip("Combine: 17% = 10% + 5% + 2%. Build any percentage from 10%, 5%, 1%.")

    pdf.add_subtopic_header("Estimation Techniques")
    pdf.add_text("1. <b>Round to nearest 10/100</b> for quick approximation.")
    pdf.add_text("2. <b>Use compatible numbers:</b> 498 x 7 ~ 500 x 7 = 3500, adjust -14 = 3486.")
    pdf.add_text("3. <b>For fractions:</b> 29/31 is close to 1; 7/15 is close to 1/2.")
    pdf.add_text("4. <b>Eliminate options:</b> Use units digit or divisibility to rule out wrong answers.")
    pdf.add_text("5. <b>Order of magnitude:</b> Quickly check if answer should be hundreds/thousands/lakhs.")
    pdf.add_tip("In MCQs, estimation can save 30-40 seconds per question. Use it aggressively!")

    # ================================================================
    # FINAL PAGE
    # ================================================================
    pdf.add_page_break()
    pdf.add_topic_header("Quick Exam Tips")
    pdf.add_text("<b>1.</b> Attempt easy questions first -- scan the paper in first 2 minutes.")
    pdf.add_text("<b>2.</b> No negative marking in TCS NQT -- attempt ALL questions.")
    pdf.add_text("<b>3.</b> For calculation-heavy problems, use approximation and eliminate options.")
    pdf.add_text("<b>4.</b> Time per question: ~1 minute for aptitude. Skip if stuck > 90 seconds.")
    pdf.add_text("<b>5.</b> Practice mental math daily -- squares, cubes, fraction-percentage conversions.")
    pdf.add_text("<b>6.</b> For ratio problems, assume convenient values (LCM method).")
    pdf.add_text("<b>7.</b> Read the question carefully -- 'increased BY' vs 'increased TO' are different.")
    pdf.add_text("<b>8.</b> In geometry, always draw a rough figure.")

    pdf.generate()


if __name__ == '__main__':
    build_pdf()
