# Name: Irving F. Sanchez
# Course: Programming Languages SP25-CPSC 46000
# School: Lewis University, Romeoville, IL
# Purpose: Measure and compare the performance of sorting algorithms

import time
import random
import matplotlib.pyplot as plt

'''
THE SORTING OLYMPICS:
Five algorithmic athletes compete to organize disordered number crowds.
Each athlete represents a fundamental sorting approach with unique strengths:

1. Weightlifter (Selection Sort) - Strong but methodical
2. Gymnast (Insertion Sort) - Agile with small groups  
3. Swimmer (Bubble Sort) - Steady rhythmic passes
4. Marathoner (Merge Sort) - Endurance for long runs
5. Sprinter (Quick Sort) - Explosive average performance

The competition measures how each athlete's performance scales with crowd sizes
from 10 to 100,000 elements, visualized on a log-log scale to clearly show
algorithmic complexity growth rates.
'''


''' /*---+---+---+--Start of Athlete Training Grounds (Algorithm Definitions)---+---+---+--*/ '''

#==================== START OF WEIGHTLIFTER DEFINITION (SELECTION SORT) ====================#
def weightlifter_selection(disordered_crowd):
    '''
    The Weightlifter's Strategy:
    1. Scans the entire crowd to find the heaviest (max) element  
    2. Moves it to the current station
    3. Repeats with remaining unsorted portion
    
    Performance Characteristics:
    - Always O(n²) comparisons
    - Minimal O(1) space usage
    - In-place sorting
    '''
    # Outer loop: Each iteration places one element in final sorted position
    for current_station in range(len(disordered_crowd)):
        # Assume current position holds the minimum value
        max_pos = current_station
        
        # Inner loop: Search unsorted portion for actual minimum
        for scout_pos in range(current_station+1, len(disordered_crowd)):
            if disordered_crowd[scout_pos] < disordered_crowd[max_pos]:
                max_pos = scout_pos
                
        # Swap minimum element into current sorted position
        disordered_crowd[current_station], disordered_crowd[max_pos] = \
            disordered_crowd[max_pos], disordered_crowd[current_station]
    
    return disordered_crowd
#==================== END OF WEIGHTLIFTER DEFINITION (SELECTION SORT) ====================#


#==================== START OF GYMNAST DEFINITION (INSERTION SORT) ====================#
def gymnast_insertion(disordered_crowd):
    '''
    The Gymnast: Agile with small groups - flexible positioning
    Implements Insertion Sort by building the sorted portion one element
    at a time through careful positioning.
    '''
    # Start from second element (first element is trivially sorted)
    for unsorted_pos in range(1, len(disordered_crowd)):
        # Extract current element to be inserted
        current_val = disordered_crowd[unsorted_pos]
        
        # Initialize comparison to previous element
        comparison_pos = unsorted_pos - 1
        
        # Shift elements greater than current_val rightwards
        while comparison_pos >= 0 and current_val < disordered_crowd[comparison_pos]:
            disordered_crowd[comparison_pos + 1] = disordered_crowd[comparison_pos]
            comparison_pos -= 1
            
        # Insert current_val in its correct position
        disordered_crowd[comparison_pos + 1] = current_val
    
    return disordered_crowd
#==================== END OF GYMNAST DEFINITION (INSERTION SORT) ====================#


#==================== START OF SWIMMER DEFINITION (BUBBLE SORT) ====================#
def swimmer_bubble(disordered_crowd):
    '''
    The Swimmer: Steady rythm through the crowd - pushes large values up
    Implements Bubble Sort by repeatedly swapping adjacent elements if they
    are in the wrong order, bubbling larger values to the end.
    '''
    
    n = len(disordered_crowd)
    
    # Each pass gurantees one more sorted element at the end
    for pass_count in range(n):
        swapped = False # Track if any swaps have occurred
        
        # This compares adjacent elements in unsorted portion
        for compare_idx in range(n - pass_count - 1):
            if disordered_crowd[compare_idx] > disordered_crowd[compare_idx + 1]:
                # Swap if out of order (bubble up the larger value)
                disordered_crowd[compare_idx], disordered_crowd[compare_idx + 1] = \
                    disordered_crowd[compare_idx + 1], disordered_crowd[compare_idx]
                swapped = True
                
        # Early exit if no swaps occurred (meaning already sorted)
        if not swapped:
            break
    return disordered_crowd
#==================== END OF SWIMMER DEFINITION (BUBBLE SORT) ====================#


#==================== START OF MARATHONER DEFINITION (MERGE SORT) ====================#
def marathoner_merge(disordered_crowd):
    '''
    The Marathoner: Divides and conquers with endurance - excels on long runs
    Implements Merge Sort using recursive division and stable merging of
    sorted sub-arrays.
    '''
    def merge(arr, left, mid, right):
        '''Helper function to merge two sorted subarrays'''
        left_copy = arr[left:mid+1]
        right_copy = arr[mid+1:right+1]
        
        i = j = 0
        k = left
        
        # Merge by comparing smallest elements of each subarray
        while i < len(left_copy) and j < len(right_copy):
            if left_copy[i] <= right_copy[j]:
                arr[k] = left_copy[i]
                i += 1
            else:
                arr[k] = right_copy[j]
                j += 1
            k += 1
            
        # Copy remaining elements if any
        while i < len(left_copy):
            arr[k] = left_copy[i]
            i += 1
            k += 1
            
        while j < len(right_copy):
            arr[k] = right_copy[j]
            j += 1
            k += 1
    
    # Iterative merge sort to avoid recursion depth limits
    arr = disordered_crowd.copy()
    current_size = 1
    
    while current_size < len(arr) - 1:
        left = 0
        
        while left < len(arr) - 1:
            mid = min(left + current_size - 1, len(arr) - 1)
            right = min(left + 2 * current_size - 1, len(arr) - 1)
            merge(arr, left, mid, right)
            left += 2 * current_size
            
        current_size *= 2
    
    return arr
#==================== END OF MARATHONER DEFINITION (MERGE SORT) ====================#


#==================== START OF SPRINTER DEFINITION (QUICK SORT) ====================#
def sprinter_quick(disordered_crowd):
    '''
    The Sprinter: Fastest on average - explosive partitioning moves
    Implements Quick Sort using in-place partitioning and iterative
    stack-based recursion simulation.
    '''
    def partition(arr, low, high):
        '''Lomuto partition scheme with rightmost pivot'''
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # Use stack to simulate recursion
    arr = disordered_crowd.copy()
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            pi = partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))
    
    return arr
#==================== END OF SPRINTER DEFINITION (QUICK SORT) ====================#

''' /*---+---+---+--End of Athlete Training Grounds (Algorithm Definitions)---+---+---+--*/ '''



''' /*---+---+---+--Start of Olympic Event Coordination---+---+---+--*/ '''
#==================== START OF EVENT COORDINATION ====================#
def generate_athlete_roster():
    '''
    Registers our olypmic sorting athletes with their sorting algorithms.
    Reeturns:
    Dictionary mapping athelete names to their sorting functions
    '''
    
    return {
        'Weightlifter (Selection Sort)': weightlifter_selection,
        'Gymnast (Insertion Sort)': gymnast_insertion,
        'Swimmer (Bubble Sort)': swimmer_bubble,
        'Marathoner (Merge Sort)': marathoner_merge,
        'Sprinter (Quick Sort)': sprinter_quick
    }
    
def create_competition_crowd(crowd_size):
    '''
    Generates a randomized crowd for the atheletes to organize.
    Args:
    crowd_size: Number of elements in the crowd (10^1 to 10^5)
    Returns:
    List of randomly generated integers between 0 and 100,000
    '''
    
    return [random.randint(0, 10**5) for _ in range(crowd_size)]
#==================== END OF EVENT COORDINATION ====================#

''' /*---+---+---+--End of Olympic Event Coordination---+---+---+--*/ '''


''' /*---+---+---+--Start of Performance Measurement Stadium---+---+---+--*/ '''

#==================== START OF TIMING TRIALS ====================#
def conduct_sorting_olympics():
    '''
    This executes sorting the competition across multiple crowd sizes
    Returns:
    Dictionaring of timing results for each athlete
    '''
    
    athletes = generate_athlete_roster()
    crowd_sizes = [10**i for i in range(1, 6)]  # 10^1 to 10^5
    results = {athlete: [] for athlete in athletes}
    
    print("\n=== THE SORTING OLYMPICS BEGIN ===")
    
    for athlete_name, sort_fn in athletes.items():
        print(f"\n-> {athlete_name} entering the arena...")
        
        for size in crowd_sizes:
            crowd = create_competition_crowd(size)
            
            # This times the sorting performances
            start_time = time.perf_counter()
            sort_fn(crowd.copy()) # Preserve original crowd
            elapsed = time.perf_counter() - start_time
            
            results[athlete_name].append(elapsed)
            print(f"   Crowd: {size:>6} | Time: {elapsed:.6f} seconds")
            
    return results
#==================== END OF TIMING TRIALS ====================#

''' /*---+---+---+--End of Performance Measurement Stadium---+---+---+--*/ '''


''' /*---+---+---+--Start of Results Visualization Stadium---+---+---+--*/ '''

#==================== START OF MEDAL CEREMONY ====================#
def display_olympic_results(results):
    '''
    Creates the official results visualization on log-log scale
    Args:
        results: Dictionary containing timing data from competition
    '''
    crowd_sizes = [10**i for i in range(1, 6)]
    
    plt.figure(figsize=(12, 8))
    
    # Plot each athlete's performance curve
    for athlete, times in results.items():
        plt.plot(crowd_sizes, times, marker='o', linestyle='-', label=athlete)
    
    # Configure Olympic-themed chart
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Crowd Size (Log Scale)', fontweight='bold')
    plt.ylabel('Organization Time (seconds, Log Scale)', fontweight='bold')
    plt.title('Sorting Olympics Final Results', fontsize=14, fontweight='bold')
    
    # Style elements
    plt.grid(True, which='both', linestyle=':', linewidth=0.5)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    # Add Olympic rings inspiration
    ax = plt.gca()
    ax.set_facecolor('#F5F5F5')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    print("\n-> Generating official results visualization...")
    plt.show()
#==================== END OF MEDAL CEREMONY ====================#

''' /*---+---+---+--End of Results Visualization Stadium---+---+---+--*/ '''


''' /*---+---+---+--Main Event Execution---+---+---+--*/ '''

#==================== START OF MAIN EVENT ====================#

if __name__ == "__main__":
    print("""
====================================
    THE GREAT SORTING OLYMPICS 2025
====================================
    """)
    
    # Event introduction
    print("Meet our world-class sorting athletes:")
    for i, athlete in enumerate(generate_athlete_roster().keys(), 1):
        print(f"{i}. {athlete}")
    
    # Run competition
    olympic_results = conduct_sorting_olympics()
    
    # Display results
    display_olympic_results(olympic_results)
    
    print("""
====================================
        EVENT CONCLUDED SUCCESSFULLY
====================================
    """)
    
#==================== END OF MAIN EVENT ====================#