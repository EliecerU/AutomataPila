
from automata.pda.npda import NPDA
from django import forms

class PushdownAutomata(forms.Form):

    word = forms.CharField(max_length=100, label=None)
    npda = NPDA(
        states={'p', 'q', 'r'},
        input_symbols={'a', 'b'},
        stack_symbols={'A', 'B', '#'},
        transitions={
            'p': {
                '': {
                    '#': {('r', '#')},
                },
                    'a': {
                        '#': {('p', ('A', '#'))},
                        'A': {
                            ('p', ('A', 'A')),
                            ('q', ''),
                    },
                    'B': {('p', ('A', 'B'))},
                },
                    'b': {
                        '#': {('p', ('B', '#'))},
                        'A': {('p', ('B', 'A'))},
                         'B': {
                            ('p', ('B', 'B')),
                            ('q', ''),
                    },
                },
            },
                'q': {
                    '': {'#': {('r', '#')}},
                    'a': {'A': {('q', '')}},
                    'b': {'B': {('q', '')}},
            },
        },
        initial_state='p',
        initial_stack_symbol='#',
        final_states={'r'},
        acceptance_mode='final_state'
    )




