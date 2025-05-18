#lang racket

(define (reverse-list lst)
  "Reverse a list recursively using tail recursion"
  (define (helper original reversed)
    (if (null? original)
        reversed
        (helper (cdr original) (cons (car original) reversed))))
  (helper lst '()))


(define test-list '(1 2 3 4 5))
(display "Original: ") test-list
(display "Reversed: ") (reverse-list test-list)  ; → '(5 4 3 2 1)
