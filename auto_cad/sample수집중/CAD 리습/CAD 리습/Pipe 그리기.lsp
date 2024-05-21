;;-------------------------------=={ PIPE }==-----------------------------;;
;;                                                                        ;;
;;                               DRAWING PIPE                             ;;
;;                                                                        ;;
;;------------------------------------------------------------------------;;
;;  Author: Park-Taeeun  ,   2011 February 16th                           ;;
;;                                                                        ;;
;;  Copyright ? 2011 by Park-Taeeun, All Rights Reserved.                 ;;
;;  Contact: Park   @   blog.naver.com/arin9916                           ;;
;;  Forums : Park   @   TheSwamp.org, CADTutor.net, AUGI.com              ;;
;;------------------------------------------------------------------------;;
;;  Description                                                           ;;
;;         → PIPE O.D 만큼의 MLINE이 생성합니다.                          ;;
;;         → Layer "3"으로 Drawing 됩니다.                                ;;
;;         → Closed MLINE을 원하시면 (70 . 0) --> (70 . 274)로 변경.      ;;
;;------------------------------------------------------------------------;;
;;  Syntax    :    15     → PIPE 15A                                      ;;
;;                      ~                                                 ;;
;;                 1500   → PIPE 1500A                                    ;;
;;------------------------------------------------------------------------;;



;;========================================================================
;;                                                          ↓↓↓ PIPE 15A  
;;========================================================================
(defun c:15( / #size #od #pipe )
	(setq #SIZE 15 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
    (PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 20A  
;;========================================================================
(defun c:20( / #size #od #pipe )
	(setq #SIZE 20 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 25A  
;;========================================================================
(defun c:25( / #size #od #pipe )
	(setq #SIZE 25 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 32A  
;;========================================================================
(defun c:32( / #size #od #pipe )
	(setq #SIZE 32 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 40A  
;;========================================================================
(defun c:40( / #size #od #pipe )
	(setq #SIZE 40 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 50A  
;;========================================================================
(defun c:50( / #size #od #pipe )
	(setq #SIZE 50 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 65A  
;;========================================================================
(defun c:65( / #size #od #pipe )
	(setq #SIZE 65 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 80A  
;;========================================================================
(defun c:80( / #size #od #pipe )
	(setq #SIZE 80 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 90A  
;;========================================================================
(defun c:90( / #size #od #pipe )
	(setq #SIZE 90 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 100A  
;;========================================================================
(defun c:100( / #size #od #pipe )
	(setq #SIZE 100 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 125A  
;;========================================================================
(defun c:125( / #size #od #pipe )
	(setq #SIZE 125 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 150A  
;;========================================================================
(defun c:150( / #size #od #pipe )
	(setq #SIZE 150 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 175A  
;;========================================================================
(defun c:175( / #size #od #pipe )
	(setq #SIZE 175 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 200A  
;;========================================================================
(defun c:200( / #size #od #pipe )
	(setq #SIZE 200 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 225A  
;;========================================================================
(defun c:225( / #size #od #pipe )
	(setq #SIZE 225 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 250A  
;;========================================================================
(defun c:250( / #size #od #pipe )
	(setq #SIZE 250 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 300A  
;;========================================================================
(defun c:300( / #size #od #pipe )
	(setq #SIZE 300 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 350A  
;;========================================================================
(defun c:350( / #size #od #pipe )
	(setq #SIZE 350 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 400A  
;;========================================================================
(defun c:400( / #size #od #pipe )
	(setq #SIZE 400 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 450A  
;;========================================================================
(defun c:450( / #size #od #pipe )
	(setq #SIZE 450 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 500A  
;;========================================================================
(defun c:500( / #size #od #pipe )
	(setq #SIZE 500 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 550A  
;;========================================================================
(defun c:550( / #size #od #pipe )
	(setq #SIZE 550 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 600A  
;;========================================================================
(defun c:600( / #size #od #pipe )
	(setq #SIZE 600 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 650A  
;;========================================================================
(defun c:650( / #size #od #pipe )
	(setq #SIZE 650 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 700A  
;;========================================================================
(defun c:700( / #size #od #pipe )
	(setq #SIZE 700 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 750A  
;;========================================================================
(defun c:750( / #size #od #pipe )
	(setq #SIZE 750 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 800A  
;;========================================================================
(defun c:800( / #size #od #pipe )
	(setq #SIZE 800 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 850A  
;;========================================================================
(defun c:850( / #size #od #pipe )
	(setq #SIZE 850 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                          ↓↓↓ PIPE 900A  
;;========================================================================
(defun c:900( / #size #od #pipe )
	(setq #SIZE 900 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                         ↓↓↓ PIPE 1000A  
;;========================================================================
(defun c:1000( / #size #od #pipe )
	(setq #SIZE 1000 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                         ↓↓↓ PIPE 1100A  
;;========================================================================
(defun c:1100( / #size #od #pipe )
	(setq #SIZE 1100 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                         ↓↓↓ PIPE 1200A  
;;========================================================================
(defun c:1200( / #size #od #pipe )
	(setq #SIZE 1200 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                         ↓↓↓ PIPE 1350A  
;;========================================================================
(defun c:1350( / #size #od #pipe )
	(setq #SIZE 1350 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)



;;========================================================================
;;                                                         ↓↓↓ PIPE 1500A  
;;========================================================================
(defun c:1500( / #size #od #pipe )
	(setq #SIZE 1500 #clayer (getvar "clayer"))
	(Setvar "cmdecho" 0)
	
	(#PTE:LIBRARY-PIPE-OD)
	(setq #od (cadr(assoc #SIZE #PIPE)))	
	(PTE:MAKE-MLINE-STYLE)
	(PTE:make-layer "3" 3 "CONTINUOUS")
	(setvar "clayer" "3")

	(defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (setvar "clayer" #clayer)
        (setq *ERROR* nil)
	)

	(princ (strcat "\nPipe " (rtos #size 2 0) "A (O.D : " (rtos #OD 2 1)"mm)"))
	(princ)
	(command "mline" "st" "pipe" "s" #od "j" "z" pause)
	(setvar "clayer" #clayer)
)








;;---------------------=={ MAKE-MLINE-STYLE }==--------------------;;
;;                                                                 ;;
;;              MAKE MLINE STYLE FOR DRAWING PIPE LINE             ;;
;;                                                                 ;;
;;-----------------------------------------------------------------;;
;;  Author: Park-Taeeun  ,   2011 February 18th                    ;;
;;                                                                 ;;
;;  Copyright ? 2011 by Park-Taeeun, All Rights Reserved.          ;;
;;  Contact: Park   @   blog.naver.com/arin9916                    ;;
;;  Forums : Park   @   TheSwamp.org, CADTutor.net, AUGI.com       ;;
;;-----------------------------------------------------------------;;
;;  Arguments :   (PTE:MAKE-MLINE-STYLE)                           ;;
;;-----------------------------------------------------------------;;
;;  Returns   :    NOTHING                                         ;;
;;-----------------------------------------------------------------;;

(defun PTE:MAKE-MLINE-STYLE( / opts mlstyle_dict)
  (setq elist
    '(
        (2 . "PIPE")
        (3 . "New MLinestyle Desc")
        (62 . 0)
        (70 . 0)

        (71 . 3)

        (49 . 0.0)
        (62 . 1)
        (6 . "CENTER")

        (49 . 0.5)
        (62 . 256)
        (6 . "CONTINUEOUS")

        (49 . -0.5)
        (62 . 256)
        (6 . "CONTINUEOUS")
    )
  )
  (setq mlstyle_dict (cdr (assoc -1 (dictsearch (namedobjdict) "ACAD_MLINESTYLE"))))
  (setq opts
    (list
      '(0 . "MLINESTYLE")
      '(102 . "{ACAD_REACTORS")
      (cons 330 mlstyle_dict)
      '(102 . "}")
      '(100 . "AcDbMlineStyle")
      '(70 . 274)
      (cons 51 (/ PI 2)) ;Angle1
      (cons 52 (/ PI 2)) ;Angle2
    )
  )
  (dictadd mlstyle_dict (cdr (assoc 2 elist)) (makeTemplate elist opts '(2 3 71 49 62 6) T))
)
;
;
;
(defun makeTemplate(_elist def req xflag / i new-elist newx x)
    (setq def (reverse def))
    (setq i 0)
    (if
        (or
            (not req)
            (apply (function and)
                (mapcar
                    '(lambda (_x)
                        (assoc _x _elist)
                    )
                    req
                )
            )
        )
        (progn
            (foreach x def
                (setq newx
                    (cond
                        ((assoc (car x) _elist)
                        )
                        ((nth i def)
                        )
                    )
                )
                (if newx
                    (setq new-elist
                        (cons newx new-elist)
                    )
                )
                (setq _elist
                        (vl-remove (assoc (car x) _elist) _elist)
                )
                (setq i (1+ i))
            )
            (setq new-elist
                (append new-elist _elist)
            )
        )
    )
    (if
        (or
            (assoc 330 new-elist)
            (assoc 410 new-elist)
        )
        (setq xflag T)
    )
    (if xflag
        (entmakex new-elist)
        (entmake new-elist)
    )
)




;;-----------------------=={ MAKE LAYER }==------------------------;;
;;                                                                 ;;
;;                       MAKE EASY TO LAYER                        ;;
;;                                                                 ;;
;;-----------------------------------------------------------------;;
(defun PTE:make-layer(#name #color  #linetype / )
    (if (not (tblsearch "LAYER" #name))
        (entmake (list (cons 0 "LAYER")
                       (cons 100 "AcDbSymbolTableRecord")
                       (cons 100 "AcDbLayerTableRecord")
                       (cons 2 #name)
                       (cons 70 0)
                       (cons 62 #color)
                       (cons 6 #linetype)))
    )
)






;;--------------------=={ LIBRARY-PIPE-OD }==----------------------;;
;;                                                                 ;;
;;            RETURN PIPE OUT DIAMTER TO LIST TYPE (JIS, KS)       ;;
;;                                                                 ;;
;;-----------------------------------------------------------------;;
(defun #PTE:LIBRARY-PIPE-OD()
	(setq #PIPE '(  (15 21.7)
					(20 27.2)
					(25 34)
					(32 42.7)
					(40 48.6)
					(50 60.5)
					(65 76.3)
					(80 89.1)
					(90 101.6)
					(100 114.3)
					(125 139.8)
					(150 165.2)
					(175 190.7)
					(200 216.3)
					(225 241.8)
					(250 267.4)
					(300 318.5)
					(350 355.6)
					(400 406.4)
					(450 457.2)
					(500 508)
					(550 558.8)
					(600 609.6)
					(650 660.4)
					(700 711.1)
					(750 762)
					(800 812.8)
					(850 863.6)
					(900 914.4)
					(1000 1016)
					(1100 1117.6)
					(1200 1219.2)
					(1350 1371.6)
					(1500 1524)
				)
	)
)

