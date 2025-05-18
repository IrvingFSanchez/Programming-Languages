# Name: Irving F. Sanchez  
# Course: Programming Languages SP25-CPSC 46000  
# School: Lewis University, Romeoville, IL  
# Purpose: Chainable function to accumulate transactions in a global account balance


def add(coin):
    global z
    z += coin  # Dropping the coin into the storage bin

    def insert_more(next_coin=None):
        """
        Inner function that either:
        - Continues the chain if given another coin, or
        - Returns itself to keep the chain alive
        """
        if next_coin is not None:
            return add(next_coin)  # Continue the chain
        return insert_more  # Keep the chain alive (key difference from earlier versions)

    return insert_more  # Ready for the next coin to be added

# =====================================
#    TEST CASES
# =====================================
print("\n" + "="*27)
print("Coin Inserter Machine Tests")
print("="*27)

# Test 1: Single coin
z = 0
add(1)
print("Test 1 - Single coin:", z)

# Test 2: Standard chain
z = 0
add(1)(2)(3)(4)(5)
print("Test 2 - 5-coin chain:", z) 

# Test 3: Even numbers
z = 0
add(2)(4)(6)(8)(10)
print("Test 3 - Even coins:", z)

# Test 4: Mixed values
z = 0
add(3)(1)(5)(2)(7)
print("Test 4 - Mixed coins:", z)