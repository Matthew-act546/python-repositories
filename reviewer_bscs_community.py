from random import randint;

questions = ['Why did you choose to pursue a BSCS degree?',
            'What specific areas of computer science interest you the most?',
            'What do you hope to achieve by joining the BSCS society?',
            'Can you share a programming project you\'re proud of?',
            'What programming languages and tools are you comfortable with?',
            'How do you stay updated on the latest advancements in computer science?',
            'Describe a time you worked effectively in a team on a project',
            'What leadership experiences do you have?',
            'How do you handle disagreements within a team?',
            'What ideas do you have for events or activities that the BSCS society could organize?',
            'How can you contribute to the society\'s goals?',
            'What do you think are the challenges facing computer science students today?']

print(f'\nQuestion:\n{questions[randint(0, len(questions)-1)]}\n')

