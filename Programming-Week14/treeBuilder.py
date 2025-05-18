# Name: Irving F. Sanchez
# Course: Programming Languages SP25-CPSC 46000
# School: Lewis University, Romeoville, IL
# Purpose: Build expression syntax trees from algebraic expressions

"""
This program works like a construction foreman building a house from blueprints:

1. The Infix Expression is like the architect's original blueprint
2. Converting to Postfix is like creating simplified construction instructions
3. Building the Tree is like assembling the house frame from those instructions
4. Infix Traversal is like walking through the finished house to verify construction

Each part of the process has specialized workers (functions) that know exactly how to do their job.
"""

class TreeNode:
    """
    The Construction Worker class - each worker handles one piece of the structure
    
    Attributes:
        value (str): The building material (operator or operand) this worker holds
        left (TreeNode): The worker handling the left part of the structure
        right (TreeNode): The worker handling the right part of the structure
    
    Think of each worker as knowing:
    - What they're holding (value)
    - Who works to their left (left)
    - Who works to their right (right)
    """
    def __init__(self, value):
        self.value = value  # What this worker is holding
        self.left = None    # Worker to the left
        self.right = None   # Worker to the right

def is_operator(char):
    """
    The Tool Checker - identifies if a character is a construction tool (operator)
    
    Args:
        char (str): The character to check
        
    Returns:
        bool: True if it's a tool, False if it's building material (operand)
        
    The foreman uses this to know who gets workers under them (operators)
    versus who just holds materials (operands)
    """
    return char in '+-*/^'

def precedence(op):
    """
    The Union Rules Book - defines which tools (operators) get priority
    
    Args:
        op (str): The operator to check
        
    Returns:
        int: The priority level (higher number = higher priority)
        
    Just like construction unions have rules about who works first,
    this tells us which operators get handled before others
    """
    union_rules = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2}
    return union_rules.get(op, 0)  # Default to 0 if not found

def infix_to_postfix(infix):
    """
    The Blueprint Translator - converts architect plans to worker instructions
    
    Args:
        infix (str): The original expression blueprint
        
    Returns:
        str: The postfix instructions workers can follow
        
    This is like taking the architect's complex plans and creating
    simple step-by-step instructions the construction crew can follow
    """
    instruction_stack = []  # The foreman's clipboard for tracking
    postfix = []           # The final instructions list
    
    for char in infix:
        if char == ' ':
            continue  # Skip empty spaces, they're not part of the structure
        elif char == '(':
            instruction_stack.append(char)  # Start a new construction zone
        elif char == ')':
            # Close the construction zone and assign workers
            while instruction_stack and instruction_stack[-1] != '(':
                postfix.append(instruction_stack.pop())
            instruction_stack.pop()  # Remove the zone marker
        elif is_operator(char):
            # Handle operator priority according to union rules
            while (instruction_stack and instruction_stack[-1] != '(' and 
                   precedence(char) <= precedence(instruction_stack[-1])):
                postfix.append(instruction_stack.pop())
            instruction_stack.append(char)
        else:  # It's building material (operand)
            postfix.append(char)  # Add directly to instructions
    
    # Clear any remaining instructions
    while instruction_stack:
        postfix.append(instruction_stack.pop())
    
    return ''.join(postfix)

def build_expression_tree(postfix):
    """
    The Construction Crew - builds the structure from instructions
    
    Args:
        postfix (str): The step-by-step construction instructions
        
    Returns:
        TreeNode: The foreman of the completed structure
        
    Each worker takes two subordinates (left and right) unless they're
    just holding materials (operands), in which case they work alone
    """
    crew_stack = []  # The team of available workers
    
    for char in postfix:
        if not is_operator(char):
            crew_stack.append(TreeNode(char))  # New worker with materials
        else:
            # Operator needs a team under them
            foreman = TreeNode(char)
            foreman.right = crew_stack.pop()  # Right worker first (LIFO)
            foreman.left = crew_stack.pop()   # Then left worker
            crew_stack.append(foreman)        # Now this team is available
    
    return crew_stack.pop() if crew_stack else None  # Head foreman

def infix_traversal(node, parent_precedence=0):
    """
    The Building Inspector - verifies construction matches original plans
    
    Args:
        node (TreeNode): Current worker/team to inspect
        parent_precedence (int): Priority level of the parent team
        
    Returns:
        str: The inspected structure with proper construction zones (parentheses)
        
    The inspector walks through each part of the structure (left-root-right)
    and adds safety barriers (parentheses) where needed based on union rules
    """
    if node is None:
        return ''  # Empty construction site
    
    if not is_operator(node.value):
        return node.value  # Just building materials, no inspection needed
    
    # Check both sides of the team
    current_precedence = precedence(node.value)
    left_report = infix_traversal(node.left, current_precedence)
    right_report = infix_traversal(node.right, current_precedence)
    
    # Add safety barriers if union rules require
    if parent_precedence > current_precedence:
        return f"({left_report}{node.value}{right_report})"
    else:
        return f"{left_report}{node.value}{right_report}"

def main():
    """
    The Construction Site Foreman - oversees the entire building process
    
    1. Gets the architect's blueprint (infix expression)
    2. Translates it to worker instructions (postfix)
    3. Builds the structure (expression tree)
    4. Verifies the construction (infix traversal)
    """
    print("=== Construction Foreman - Expression Tree Builder ===")
    
    # 1. Get the architect's blueprint
    print("\n[ARCHITECT'S OFFICE]")
    infix_expression = input("Enter the algebraic blueprint: ")
    print(f"\nOriginal Blueprint (Infix): {infix_expression}")
    
    # 2. Translate to worker instructions
    print("\n[TRANSLATION DEPARTMENT]")
    postfix_expression = infix_to_postfix(infix_expression)
    print(f"Worker Instructions (Postfix): {postfix_expression}")
    
    # 3. Construct the building
    print("\n[CONSTRUCTION SITE]")
    construction_foreman = build_expression_tree(postfix_expression)
    
    # 4. Final inspection
    print("\n[INSPECTION TEAM]")
    inspection_report = infix_traversal(construction_foreman)
    print(f"Final Inspection Report: {inspection_report}")

if __name__ == "__main__":
    main()