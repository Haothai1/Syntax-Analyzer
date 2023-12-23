class LRParser:

  def __init__(self):
    # LR Parsing Table
    self.lr_table = {
        0: {
            'id': 's5',
            '(': 's4',
            'E': 1,
            'T': 2,
            'F': 3
        },
        1: {
            '+': 's6',
            '$': 'accept'
        },
        2: {
            '+': 'r2',
            '*': 's7',
            ')': 'r2',
            '$': 'r2'
        },
        3: {
            '+': 'r4',
            '*': 'r4',
            ')': 'r4',
            '$': 'r4'
        },
        4: {
            'id': 's5',
            '(': 's4',
            'E': 8,
            'T': 2,
            'F': 3
        },
        5: {
            '+': 'r6',
            '*': 'r6',
            ')': 'r6',
            '$': 'r6'
        },
        6: {
            'id': 's5',
            '(': 's4',
            'T': 9,
            'F': 3
        },
        7: {
            'id': 's5',
            '(': 's4',
            'F': 10
        },
        8: {
            '+': 's6',
            ')': 's11'
        },
        9: {
            '+': 'r3',
            '*': 's7',
            ')': 'r1',
            '$': 'r1'
        },
        10: {
            '+': 'r3',
            '*': 'r3',
            ')': 'r3',
            '$': 'r3'
        },
        11: {
            '+': 'r5',
            '*': 'r5',
            ')': 'r5',
            '$': 'r5'
        }
    }

    self.stack = []
    self.input_str = ""
    self.productions = self.load_grammar(
        grammar_file)  # text file for user loading in


  def load_grammar(self, grammar_file):
    productions = {}
    with open(grammar_file, 'r') as file:
      for line in file:
        line = line.strip()
        if line:
          parts = line.split(' -> ')
          non_terminal = parts[0].strip()
          production = [symbol.strip() for symbol in parts[1].split()]
          productions[len(productions) + 1] = (non_terminal, production)
    return productions

  def parse_input(self, input_str):
    self.input_str = input_str + '$'
    self.stack = [0]

    print("Input:", self.input_str)
    print("Stack:")
    print("Step".ljust(5), "Stack".ljust(20), "Input".ljust(20),
          "Action".ljust(10))
    self.print_step(0)

    step = 1
    while True:
      symbol = 'id' if self.input_str.startswith('id') else self.input_str[0]
      action = self.lr_table[self.stack[-1]].get(symbol)

      if action is None:
        print("Output: String is not accepted.")
        break

      if action == 'accept':
        print("Output: String is accepted.")
        break
      elif action[0] == 's':
        self.stack.append(symbol)
        self.stack.append(int(action[1:]))
        self.input_str = self.input_str[len(symbol):]
      elif action[0] == 'r':
        production_num = int(action[1:])
        for _ in range(2 * len(self.productions[production_num][1])):
          self.stack.pop()
        state = self.lr_table[self.stack[-1]][self.productions[production_num]
                                              [0]]
        self.stack.append(self.productions[production_num][0])
        self.stack.append(int(state))

      self.print_step(step)
      step += 1

  def print_step(self, step):
    stack_str = ''.join(map(str, self.stack))
    input_str = self.input_str if self.input_str else "$"

    # Determine the action
    state = self.stack[-1]
    current_symbol = 'id' if input_str.startswith('id') else input_str[0]
    action = self.lr_table[state].get(current_symbol, 'NOT ACCEPTED!')

    # Calculate column widths dynamically
    step_width = max(3, len(str(step)))
    stack_width = max(18, len(stack_str))
    input_width = max(20, len(input_str))
    action_width = max(10, len(action))

    # Format and print each column with the calculated width
    print(f"{str(step).rjust(step_width)}   {stack_str.ljust(stack_width)}   "
          f"{input_str.ljust(input_width)}   {action.ljust(action_width)}")

  def get_user_input(self):
    user_input = input("Enter an input string (e.g., id+id)*id$): ")
    return user_input


if __name__ == "__main__":
  grammar_file = "grammar.txt"
  parser = LRParser()

  # Get user input
  user_input = parser.get_user_input()

  # Test the user input
  print("\nTesting user input:", user_input)
  parser.parse_input(user_input)
