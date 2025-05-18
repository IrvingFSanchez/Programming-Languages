# Name: Irving F. Sanchez  
# Course: Programming Languages SP25-CPSC 46000  
# School: Lewis University, Romeoville, IL  
# Purpose: Sorts 3D points based on customizable dimension priority

def sort_tools(tools, priority, show_keys=False):
    """
    Sorts 3D points with optional key printing.
    Args:
        tools: List of (x,y,z) tuples
        priority: Sort order like "xyz" or "zyx"
        show_keys: If True, prints key generation table
    """
    dimension_index = {'x': 0, 'y': 1, 'z': 2}
    
    # Generate keys for all tools
    sorting_key = lambda tool: tuple(tool[dimension_index[dim]] for dim in priority)
    
    # Print comparison table if requested
    if show_keys:
        print("\n" + "="*61)
        print("Tool -> Keys Comparison:")
        print(f"{'Tool':<10} | {'Key (xyz)':<10} | {'Key (zyx)':<10} | {'Key (yzx)':<10} | {'Key (xzy)':<10}")
        print("-"*61)
        for tool in tools:
            key_xyz = tuple(tool[dimension_index[dim]] for dim in "xyz")
            key_zyx = tuple(tool[dimension_index[dim]] for dim in "zyx")
            key_yzx = tuple(tool[dimension_index[dim]] for dim in "yzx")
            key_xzy = tuple(tool[dimension_index[dim]] for dim in "xzy")       
            print(f"{str(tool):<10} | {str(key_xyz):<10} | {str(key_zyx):<10} | {str(key_yzx):<10} | {str(key_xzy):<10}")
        print("="*61 + "\n")
    
    return sorted(tools, key=sorting_key)

# Test Data
toolbox = [(2,1,2), (2,1,3), (1,2,3), (1,2,2), (3,1,2), (3,3,1), (2,3,1), (1,3,3), (2,4,1)]

# Print the comparison table once
sort_tools(toolbox, "xyz", show_keys=True)

# Now print the actual sorted results
print("Sorted by Length-Width-Height (xyz):", sort_tools(toolbox, "xyz"))
print("Sorted by Height-Width-Length (zyx):", sort_tools(toolbox, "zyx"))
print("Sorted by Width-Height-Length (yzx):", sort_tools(toolbox, "yzx"))
print("Sorted by Length-Height-Width (xzy):", sort_tools(toolbox, "xzy"))

'''
How this works as an example:

# 'for dim in priority' iterates over each character in priority string ("xyx" or "zyx")
# dimension_index[dim] tells python to look in the tuple for each dimension
# tool[] fetches the value from the 3D point for the dimension given
# the tuple() combines all the extracted values into a tuple in priority order for example priority="zxy" and tool=(2,1,3) generates (z,x,y) -> (3,2,1)
# lambda is a essentially a tiny function that reshapes the data for sorting, it doesnt modify them it just creates comparison keys

tool = (2, 1, 3)
priority = "zxy"
Execution:

Loop 1 (dim='z'):
dimension_index['z'] → 2
tool[2] → 3
Loop 2 (dim='x'):
dimension_index['x'] → 0
tool[0] → 2
Loop 3 (dim='y'):
dimension_index['y'] → 1
tool[1] → 1
Resulting tuple: (3, 2, 1)

'''