# Name: Irving F. Sanchez
# Course: Programming Languages SP25-CPSC 46000
# School: Lewis University, Romeoville, IL
# Purpose: Trie-based word counter for text analysis

'''
THE WORD ARCHIVISTS' CHALLENGE:
Metaphorically speaking this is a team of linguistic specialists competes to organize and analyze historical documents.
Each archivist brings unique skills for tracking word occurrences:

1. The Librarian (Trie Structure) - Master of prefix organization
2. The Lexicographer (Word Counting) - Precise frequency analyst
3. The Etymologist (Prefix Search) - Expert in word origins and connections

In this challenge my made up team processes the Declaration of Independence, demonstrating how efficiently
each specialist can store, retrieve, and analyze word patterns in historical texts. Which in this context we are using the declare.txt file.
'''

''' /*---+---+---+--Start of Archivists' Tools (Trie Implementation)---+---+---+--*/ '''

#==================== START OF LIBRARIAN DEFINITION (TRIE STRUCTURE) ====================#
class Trie:
    '''
    This is the Librarian's Master Structure:
    A 26-branch knowledge tree where each path represents word fragments.
    Terminal nodes record how often words complete their journey.

    Storage Strategy:
    - Each node contains 26 knowledge shelves (a-z)
    - Red ribbons (occurrence counts) mark complete words
    - Empty shelves remain bare until needed
    '''
    def __init__(self):
        """Prepares a new empty knowledge station"""
        self.occurrence = 0          # Red ribbon counter
        self.children = [None] * 26  # Alphabetical shelves
#==================== END OF LIBRARIAN DEFINITION (TRIE STRUCTURE) ====================#


#==================== START OF LEXICOGRAPHER DEFINITION (WORD COUNTING) ====================#
    def add(self, word):
        '''
        This is the Lexicographer's Cataloging Technique:
        1. Follows the word's path shelf-by-shelf
        2. Creates new shelves when encountering unknown fragments
        3. Ties a red ribbon at the terminal shelf
        
        Args:
            word (str): New word to archive (auto-lowercased)
        '''
        node = self
        for char in word.lower():
            shelf = ord(char) - ord('a')
            if not node.children[shelf]:
                node.children[shelf] = Trie()
            node = node.children[shelf]
        node.occurrence += 1  # Tie the ribbon

    def get(self, word):
        '''
        This is the Lexicographer's Retrieval Method:
        Follows word fragments to their terminal shelf,
        returning the red ribbon count (0 if path incomplete)
        '''
        node = self
        for char in word.lower():
            shelf = ord(char) - ord('a')
            if not node.children[shelf]:
                return 0  # Path crumbles
            node = node.children[shelf]
        return node.occurrence  # Ribbon count
#==================== END OF LEXICOGRAPHER DEFINITION (WORD COUNTING) ====================#


#==================== START OF ETYMOLOGIST DEFINITION (PREFIX SEARCH) ====================#
    def has_prefix(self, prefix):
        '''
        This is the Etymologist's Inquiry:
        Verifies whether any archived words begin with given fragments
        
        Args:
            prefix (str): Word beginnings to investigate
            
        Returns:
            bool: True if prefix leads to existing words
        '''
        node = self
        for char in prefix.lower():
            shelf = ord(char) - ord('a')
            if not node.children[shelf]:
                return False  # Path terminates
            node = node.children[shelf]
        return True  # Continuation exists
#==================== END OF ETYMOLOGIST DEFINITION (PREFIX SEARCH) ====================#


#==================== START OF CATALOG PRODUCTION (OUTPUT METHODS) ====================#
    def _collect_words(self, prefix, word_list):
        '''
        This is the Librarian's Inventory Process:
        Recursively traverses all valid paths, recording
        complete words with their ribbon counts
        
        Args:
            prefix (str): Current path being explored
            word_list (list): Growing inventory registry
        '''
        if self.occurrence > 0:
            word_list.append(f"{prefix}: {self.occurrence}")
        for i, child in enumerate(self.children):
            if child:
                char = chr(ord('a') + i)
                child._collect_words(prefix + char, word_list)

    def __str__(self):
        """Produces the official archival inventory"""
        words = []
        self._collect_words("", words)
        return "\n".join(words) if words else "Archive Empty"
#==================== END OF CATALOG PRODUCTION (OUTPUT METHODS) ====================#


#==================== START OF ARCHIVE MAINTENANCE (UTILITIES) ====================#
    def size(self):
        """Counts unique words in the archive"""
        count = 1 if self.occurrence > 0 else 0
        for child in self.children:
            if child:
                count += child.size()
        return count

    def is_empty(self):
        """Checks for empty archives"""
        return all(child is None for child in self.children) and self.occurrence == 0

    def clear(self):
        """Resets the entire archive system"""
        self.occurrence = 0
        self.children = [None] * 26

    __repr__ = __str__  # Standard reference format
#==================== END OF ARCHIVE MAINTENANCE (UTILITIES) ====================#

''' /*---+---+---+--End of Archivists' Tools (Trie Implementation)---+---+---+--*/ '''


''' /*---+---+---+--Start of Historical Analysis---+---+---+--*/ '''

#==================== START OF DOCUMENT PROCESSING ====================#
def process_historical_document():
    '''
    The Grand Analysis:
    1. Invokes the archivist team
    2. Processes the declare.txt document
    3. Preserves original punctuation handling
    '''
    try:
        archive = Trie()
        
        print("\n=== THE ARCHIVISTS BEGIN THEIR WORK ===")
        
        with open("declare.txt", "r") as scroll:
            for line in scroll:
                for word in line.strip().split():
                    # Preserve historical accuracy
                    cleaned = ''.join(c for c in word.lower() if c.isalpha())
                    if cleaned:
                        archive.add(cleaned)

        # Present findings
        print("\nWord Frequency Catalog:")
        print(archive)
        print(f"\nTotal Unique Words: {archive.size()}")
        print(f"Occurrences of 'liberty': {archive.get('liberty')}") # This can be changed, but just to show the functionality I added it.
        
        # Etymologist's special report
        print("\nEtymological Findings:")
        print(f"Words beginning with 'free': {archive.has_prefix('free')}") # Same with this line and the line below, this can be changed.
        print(f"Words beginning with 'xyz': {archive.has_prefix('xyz')}")

    except FileNotFoundError:
        print("\nALERT: Missing historical document (declare.txt)")
    except Exception as e:
        print(f"\nARCHIVAL ERROR: {str(e)}")
#==================== END OF DOCUMENT PROCESSING ====================#

''' /*---+---+---+--End of Historical Analysis---+---+---+--*/ '''


''' /*---+---+---+--Main Archival Event---+---+---+--*/ '''

#==================== START OF MAIN EVENT ====================#
if __name__ == "__main__":
    print("""
====================================
  HISTORICAL WORD ARCHIVE INITIATIVE
====================================
    """)
    
    print("Deploying specialist team:")
    print("1. The Librarian - Trie Structure :D")
    print("2. The Lexicographer - Word Counting >:D")
    print("3. The Etymologist - Prefix Analysis >:]\n")
    
    process_historical_document()
    
    print("""
====================================
      ARCHIVAL PROCESS COMPLETE
====================================
    """)
#==================== END OF MAIN EVENT ====================#