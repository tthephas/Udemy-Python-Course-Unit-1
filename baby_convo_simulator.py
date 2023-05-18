# talking to a baby simulator

answer = input('Why is the sky blue?: ').strip().lower()

while answer != 'just because':
    answer = input('Why?: ').strip().lower()
    
