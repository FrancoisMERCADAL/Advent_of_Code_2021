FILE_NAME = 'chunks.txt'
SCORE_DICT = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
SCORE_DICT2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
OPENING_CHARS = ['(', '[', '{', '<']
CLOSING_CHARS = [')', ']', '}', '>']

## PART 1
def count_syntax_error_score(file):
    count = 0
    for line in file:
        chunks_opened = ''
        expected_closing_chars = ''
        for char in line:
            if char in OPENING_CHARS:
                chunks_opened += char
                index_char = OPENING_CHARS.index(char)
                expected_closing_chars = CLOSING_CHARS[index_char] + expected_closing_chars
            elif char in CLOSING_CHARS:
                if char == expected_closing_chars[0]:
                    chunks_opened = expected_closing_chars[:-1]
                    expected_closing_chars = expected_closing_chars[1:]
                else:
                    count += SCORE_DICT[char]
                    break
    return count

def syntax_scoring_part1():
    file = open(FILE_NAME, 'r')
    count = count_syntax_error_score(file)
    file.close()
    return count

## PART 2
def middle_score(file):
    scores = []
    for line in file:
        score = 0
        chunks_opened = ''
        is_corrupted = False
        expected_closing_chars = ''
        for char in line:
            if char in OPENING_CHARS:
                chunks_opened += char
                index_char = OPENING_CHARS.index(char)
                expected_closing_chars = CLOSING_CHARS[index_char] + expected_closing_chars
            elif char in CLOSING_CHARS:
                if char == expected_closing_chars[0]:
                    chunks_opened = chunks_opened[:-1]
                    expected_closing_chars = expected_closing_chars[1:]
                else:
                    is_corrupted = True
                    break
        if not is_corrupted:
            for char in expected_closing_chars:
                score = score * 5 + SCORE_DICT2[char]
            scores.append(score)
    scores.sort()
    return scores[int(len(scores)/2)]

def syntax_scoring_part2():
    file = open(FILE_NAME, 'r')
    score = middle_score(file)
    file.close()
    return score

## TESTS
### PART 1
print(syntax_scoring_part1()) # 413733

### PART 2
print(syntax_scoring_part2()) # 3354640192
