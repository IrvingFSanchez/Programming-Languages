#lang racket

; Binary search function
; tabula = sorted list (Latin for "table")
; quaesitum = target value to find (Latin for "sought")
(define (binaria tabula quaesitum)
  ; Inner helper function that does the actual searching
  ; sinistra = left boundary (Latin for "left")
  ; dextera = right boundary (Latin for "right")
  (define (quaere sinistra dextera)
    (cond
      ; Base case: search boundaries crossed - value not found
      [(> sinistra dextera) -1]
      
      ; Recursive case: continue searching
      [else
       (let* ([medius (quotient (+ sinistra dextera) 2)]  ; Calculate midpoint
              [elementum (list-ref tabula medius)])       ; Get middle element
         
         (cond
           ; Found the value - return its index
           [(= elementum quaesitum) medius]
           
           ; Target is in left half - search left side
           [(< quaesitum elementum) (quaere sinistra (- medius 1))]
           
           ; Target is in right half - search right side
           [else (quaere (+ medius 1) dextera)]))]))
  
  ; Start the search with full list range
  (quaere 0 (- (length tabula) 1)))

; Test cases (must be sorted list)
(define tabula-numerorum '(1 3 7 9 12 18 20 23 25 37 46))

; Test executions with expected results:
(binaria tabula-numerorum -2)  ; → -1  (not found)
(binaria tabula-numerorum 9)   ; → 3   (found at index 3)
(binaria tabula-numerorum 16)  ; → -1  (not found)
(binaria tabula-numerorum 37)  ; → 9   (found at index 9)