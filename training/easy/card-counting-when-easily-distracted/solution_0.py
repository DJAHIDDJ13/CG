from collections import Counter

def is_distraction(thought):
    return any(c not in "A23456789TJQK" for c in thought)

stream_of_consciousness = input().split('.')
bust_threshold = int(input())
card_val = {str(i):i for i in range(2, 9 +1)}
card_val.update({'A': 1, 'K': 10, 'Q': 10, 'J': 10, 'T': 10})
cards_left = Counter([*"A23456789TJQK"]*4)

for thought in stream_of_consciousness:
    if not is_distraction(thought):
        for c in thought:
            cards_left[c] -= 1

num_below_threshold = 0
for c in cards_left:
    if card_val[c] < bust_threshold:
        num_below_threshold += cards_left[c]

percent = round(num_below_threshold * 100 / sum(cards_left.values()))
print(f"{percent}%")