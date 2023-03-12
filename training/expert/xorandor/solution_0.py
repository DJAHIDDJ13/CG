from itertools import combinations
from collections import deque
import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = []
        self.children = []
        
    def set_name(self, name):
        self.name = name
        
    def evaluate(self):
        return 0 
       
    def __repr__(self):
        return f"{type(self).__name__}({self.name})"

class InputNode(Node):
    def __init__(self, name, value):
        super().__init__(name)
        self.value = value
        
    @property
    def evaluation(self):
        return self.value
    
    def toggle(self):
        # All the parents must be recalculated 
        parent_stack = [p for p in self.parent]
        while parent_stack:
            parent = parent_stack.pop()
            parent.require_recalc = True
            parent_stack.extend([p for p in parent.parent])
        self.value = 1 if self.value == 0 else 0

    def set_value(self, value):
        if value not in [1, 0]:
            raise Exception(f"Value provided not 1 or 0: {value}")
        self.value = value

    def __repr__(self):
        return self.name

class Operation(Node):
    def __init__(self, name, op, inputs):
        super().__init__(name)
        self.op = op
#        for inp in inputs:
#            inp.parent.append(self)
        self.children = inputs
        self.parent = []
        self.eval_recalc = True
        self._evaluation = None

    def __repr__(self):
        return self.name
    
    @property
    def evaluation(self): 
 #       if self.eval_recalc or self._evaluation is None:
 #           self._evaluation = self.calc_eval()
 #           self.eval_recalc = False
        # not working properly for some reason gotta do it the old way
        return self.calc_eval()

    def calc_eval(self):
        # lookahead to check for switches
        child_evals = []
#        print(self, *zip(self.children, [c.parent for c in self.children]), file=sys.stderr)
        for child in self.children:
            if child.name[0] == 'K':
                if child.parent[0] is self and child.direction == '<':
                    child_evals.append(child.evaluation)
                elif child.parent[1] is self and child.direction == '>':
                    child_evals.append(child.evaluation)
                else:
                    child_evals.append(0)                
            else:
                child_evals.append(child.evaluation)

#        print(self, *zip(self.children, child_evals), file=sys.stderr)
#        for c in self.children:
#            if c.name[0] == 'K':
#                print("\t", str(c)+c.direction, c.parent)
        if self.op == "~":
            return not child_evals[0]
        elif self.op == "&":
            return child_evals[0] & child_evals[1]
        elif self.op == "|":
            return child_evals[0] | child_evals[1]
        elif self.op == "+":  # XOR
            return child_evals[0] ^ child_evals[1]
        elif self.op == "^":  # NAND
            return not(child_evals[0] & child_evals[1])
        elif self.op == "-":  # NOR
            return not(child_evals[0] | child_evals[1])
        elif self.op == "=":  # XNOR
            return not(child_evals[0] ^ child_evals[1])
        elif self.op == '@':
            ret_val = True
            for i, child in enumerate(self.children):
                ret_val = ret_val and child_evals[i]
            return 1 if ret_val else 0
        else:
            raise ValueError(f"Invalid operation: {self.op}")

class SwitchNode(Node):
    def __init__(self, name, direction, input_nodes):
        super().__init__(name)
        self.set_direction(direction)
        self.children = input_nodes
#        for inp in input_nodes:
#            inp.parent.append(self)

    def __repr__(self):
        return self.name
    
    def toggle(self):
        # All the parents must be recalculated 
        parent_stack = [p for p in self.parent]
        while parent_stack:
            parent = parent_stack.pop()
            parent.require_recalc = True
            parent_stack.extend([p for p in parent.parent])
        self.direction = '>' if self.direction == '<' else '<'

    def set_direction(self, direction):
        if direction not in "<>":
            raise Exception(f"Unknown direction provided {direction}")
        self.direction = direction

    @property
    def evaluation(self):
        return self.children[0].evaluation

class Circuit:
    def __init__(self, led):
        self.led = led

    def __repr__(self):
        return str(self.led)

    @staticmethod
    def handle_input_nodes(width, height, line, symbol, nodes, i, y, names_matrix):
        inp = InputNode(names_matrix[height-1-y][i], int(symbol))
        nodes[i] = inp
        inp.parent = [i]
        return nodes, i

    @staticmethod
    def handle_cable_nodes(width, height, line, symbol, nodes, i, y, names_matrix):
        input_idx = i
        right_idx = None
        for k in range(i+1, width):
            if line[k] not in '-+|': break
            if line[k] in '+|':
                right_idx = k
                break
        left_idx = None
        for k in range(i-1, -1, -1):
            if line[k] not in '-+|': break
            if line[k] in '+|':
                left_idx = k
                break

        if right_idx is not None and left_idx is not None:
            # Fork
            input_node = nodes[input_idx]
            del nodes[input_idx]
            nodes[right_idx] = input_node
            nodes[left_idx] = input_node
            # we have to do this weird retracing in order to get the proper order of parents
            cur_parents = input_node.parent
            input_node.parent = []
            for p in cur_parents:
                if p == input_idx:
                    input_node.parent.extend([left_idx, right_idx])
                else:
                    input_node.parent.append(p)
            
        elif right_idx is not None:
            node = nodes[input_idx]
            del nodes[input_idx]
            nodes[right_idx] = node
            # we have to do this weird retracing in order to get the proper order of parents
            cur_parents = node.parent
            node.parent = []
            for p in cur_parents:
                if p == input_idx:
                    node.parent.append(right_idx)
                else:
                    node.parent.append(p)
        elif left_idx is not None:
            node = nodes[input_idx]
            del nodes[input_idx]
            nodes[left_idx] = node
            # we have to do this weird retracing in order to get the proper order of parents
            cur_parents = node.parent
            node.parent = []
            for p in cur_parents:
                if p == input_idx:
                    node.parent.append(left_idx)
                else:
                    node.parent.append(p)
        i = right_idx if right_idx is not None else i

        return nodes, i

    @staticmethod
    def handle_component_nodes(width, height, line, symbol, nodes, i, y, names_matrix):
        start_c = i
        op = None
        mid_c = None
        while line[i] != ']':
            if line[i] != ' ':
                mid_c = i
                op = line[i]
            i += 1
        end_c = i

        if op is None:
            raise Exception(f"Component without operation symbol line: {start_c}")

        if op in '&|^+-=':
            inputs_idx = [start_c+1, end_c-1]
            output_idx = [mid_c]
        elif op == '~':
            inputs_idx = [mid_c]
            output_idx = [mid_c]
        elif op == '@':
            inputs_idx = sorted([idx for idx in nodes if start_c < idx < end_c])
            output_idx = [mid_c]
        elif op in '<>':
            inputs_idx = [mid_c]
            output_idx = [start_c+1, end_c-1]
        else:
            raise Exception(f"Component {op} not implemented")

        inputs = []
        for idx in inputs_idx:
            inputs.append(nodes[idx])
            del nodes[idx]
        if op in "<>":
            component = SwitchNode(names_matrix[height-1-y][mid_c], op, inputs)
        else:
            component = Operation(names_matrix[height-1-y][mid_c], op, inputs)

        for idx in output_idx:
            nodes[idx] = component
            component.parent = output_idx

        # set parent to of inputs to be component
        for inp, idx in zip(inputs, inputs_idx):
            inp.parent = [component if i == idx else i for i in inp.parent]
            #print(f"Set parent {component} for {inp}{inp.parent}]")
            #inp.parent.append(component)

        return nodes, i

    @staticmethod
    def _generate_names_matrix(lines):
        names = [["" for _ in range(len(lines[0]))] for _ in range(len(lines))]
        input_counter = 1
        switch_counter = 1
        op_counter = {}
        for y, line in enumerate(lines):
            inside_brackets = False
            for x, s in enumerate(line):
                if s == '[':
                    inside_brackets = True
                if s == ']':
                    inside_brackets = False
                if s in '01':
                    names[y][x] = f'I{input_counter}'
                    input_counter += 1
                if inside_brackets:
                    if s in '&|^@+-~=':
                        op_counter[s] = op_counter.get(s, 0) + 1
                        names[y][x] = f'{s}{op_counter[s]}'
                    elif s in '<>':
                        names[y][x] = f"K{switch_counter}"
                        switch_counter += 1
        return names

    @classmethod
    def from_input(cls):
        height, width = map(int, input().split())
        lines = [input() for _ in range(height)]
        nodes = {}
        names_matrix = cls._generate_names_matrix(lines)
        for y, line in enumerate(reversed(lines)):
            i = 0
            while i < len(line):
                symbol = line[i]
                # Handling inputs
                if symbol in '01':
                    nodes, i = cls.handle_input_nodes(width, height, line, symbol, nodes, i, y, names_matrix)
                # Handling cables
                elif symbol == '+' and i in nodes:
                    nodes, i = cls.handle_cable_nodes(width, height, line, symbol, nodes, i, y, names_matrix)
                # Handling components
                if symbol == '[':
                    nodes, i = cls.handle_component_nodes(width, height, line, symbol, nodes, i, y, names_matrix)
                i += 1
        for k in nodes:
            node = nodes[k]
            if node.op == '@':
                circuit = cls(node)
                # because i did the parents in a dumb way i have to remove the index
                node.parent = [] 
                return circuit
        return None

    def param_extract(self):
        nodes = []
        stack = [self.led]
        while stack:
            current = stack.pop()
            if current.name[0] in "KI":
                nodes.append(current)
            for child in current.children:
                stack.append(child)
        return list(set(nodes))

# this needs fixing, ugly todo
def sort_key(k):
    return [1000, 0][k[0] == 'K'] + int(k[1:])

def find_min_toggles(circuit):
    # Get the list of parameter nodes to toggle
    param_nodes = circuit.param_extract()
    param_nodes = sorted(param_nodes, key=lambda x:sort_key(x.name))

    # Initialize a variable to store the minimum number of toggles required
    min_toggles = float('inf')
    min_toggles_comb = None
    # Iterate through all possible combinations of parameter nodes to toggle
    for num_toggles in range(len(param_nodes) + 1):
        for nodes in combinations(param_nodes, num_toggles):
            # Toggle the selected nodes
            for node in nodes:
                node.toggle()

            # Evaluate the circuit and check if the LED node is True
            if circuit.led.evaluation:
                # If the LED node is True, update the minimum number of toggles required
                if min_toggles > num_toggles:
                    min_toggles = num_toggles
                    min_toggles_comb = nodes
                        
            # Untoggle the selected nodes
            for node in nodes:
                node.toggle()
        
        if min_toggles_comb is not None:
            break
    return min_toggles_comb

circuit = Circuit.from_input()
if circuit is None:
    raise Exception("Couldn't find LED")
param_nodes = circuit.param_extract()
param_nodes = {node.name:node for node in param_nodes}
t = """K1
K4
I2
I3
I4
I6
I7""".split()
#for node in param_nodes.values():
#    print(node, node.parent)
#for s in t:
#    param_nodes[s].toggle()
#print(circuit.led.evaluation)
min_toggles = find_min_toggles(circuit)
#print(min_toggles)
print(*min_toggles, sep="\n")
