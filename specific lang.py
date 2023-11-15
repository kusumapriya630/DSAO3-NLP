class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, input_symbol, next_state):
        self.transitions[input_symbol] = next_state

    def process_input(self, input_symbol):
        if input_symbol in self.transitions:
            return self.transitions[input_symbol]
        else:
            return None

class Automaton:
    def __init__(self):
        self.states = {}
        self.current_state = None
        self.build_automaton()

    def build_automaton(self):
        state_q0 = State("q0")
        state_q1 = State("q1")
        state_q2 = State("q2")

        state_q0.add_transition('a', state_q0)
        state_q0.add_transition('b', state_q1)

        state_q1.add_transition('a', state_q0)
        state_q1.add_transition('b', state_q2)

        state_q2.add_transition('a', state_q0)
        state_q2.add_transition('b', state_q1)

        self.states = {
            "q0": state_q0,
            "q1": state_q1,
            "q2": state_q2
        }

        self.current_state = state_q0

    def process_string(self, input_string):
        for symbol in input_string:
            next_state = self.current_state.process_input(symbol)
            if next_state:
                self.current_state = next_state
            else:
                return False  # Input symbol not recognized

        # Check if the final state is the accepting state
        return self.current_state == self.states["q1"]

# Example usage:
automaton = Automaton()
test_strings = ["ab", "aab", "abb", "abc", "abab"]

for test_string in test_strings:
    result = automaton.process_string(test_string)
    print(f'The string "{test_string}" is {"accepted" if result else "rejected"} by the automaton.')
