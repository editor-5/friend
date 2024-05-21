;;==================================
;  Comma x & o ('00.11-'01.11cho_i)
; -> 천단위의 컴마 찍기 및 없애기
;;----------------------------------
(defun c:,,(/ ss n k kn kk en kna0 a1 a2 a3)
   (prompt "\n컴마 없애기-> ")
   (setq ss (ssget))
   (setq n (sslength ss))
   (setq k 0)
   (while (<= 1 n)
       (setq en (ssname ss k))
       (if (eq (cdr (assoc 0 (entget en))) "TEXT")
           (progn
           (setq ent1 (assoc 1 (entget en)))
           (setq txt1 (cdr ent1))
           (setq kn (strlen txt1))
           (if (/= (wcmatch txt1 "*,*") nil)(progn
               (setq kk 2)
               (setq a0 (substr txt1 KK 1))
               (while (and (/= a0 ",")(<= kk kn))
                   (setq kk (+ kk 1))
                   (setq a0 (substr txt1 KK 1))
               )
               (if (= a0 ",")(progn
                   (setq a1 (substr txt1 1 (- kk 1)))
                   (setq a2 (substr txt1 (+ kk 1) (- kn kk)))
                   (setq a3 (strcat a1 a2))
                   (entmod (subst (cons 1 a3) (assoc 1 (entget en))(entget en)))
               ))
           ))
       ))
       (setq n (- n 1))
       (setq k (+ k 1))
    )
   (prin1)
)
(defun c:,(/ ss n k en ent1 txt1 kn txt2 a1 a2 a3)
   (prompt "\n컴마 찍기 -> ")
   (setq ss (ssget))
   (setq n (sslength ss))
   (setq k 0)
   (while (<= 1 n)
       (setq en (ssname ss k))
     ;종원이 테스트
;	(princ en)(princ)
     ;;종원이테스트 끝
       (if (eq (cdr (assoc 0 (entget en))) "TEXT")
           (progn
           (setq ent1 (assoc 1 (entget en)))
           (setq txt1 (cdr ent1))
           (setq kn (strlen txt1))
           (setq txt2 (atof txt1))
           (cmo_1 txt2)
           );progn end
       );if end
       (setq n (- n 1))
       (setq k (+ k 1))
    );while end
   (prin1)
)
;cmo sub routine
(defun cmo_1(txt2)
   (if (and (>= txt2 1000)(< txt2 10000))(progn
	(princ txt1)
	(princ "\n")
	(princ txt2)

	(setq a1 (substr txt1 1 1))
	
        (princ "\n next")
        (princ txt1)
	(princ "\n")
	(princ txt2)
	
       (setq a2 (substr txt1 2 (- kn 1)))
       (setq a3 (strcat a1 "," a2))
       (entmod (subst (cons 1 a3) (assoc 1 (entget en))(entget en)))
   ))
   (if (and (>= txt2 10000)(< txt2 100000))(progn
       (setq a1 (substr txt1 1 2))
       (setq a2 (substr txt1 3 (- kn 2)))
       (setq a3 (strcat a1 "," a2))
       (entmod (subst (cons 1 a3) (assoc 1 (entget en))(entget en)))
   ))
   (if (and (>= txt2 100000)(< txt2 1000000))(progn
       (setq a1 (substr txt1 1 3))
       (setq a2 (substr txt1 4 (- kn 3)))
       (setq a3 (strcat a1 "," a2))
       (entmod (subst (cons 1 a3) (assoc 1 (entget en))(entget en)))
   ))
)