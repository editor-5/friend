;;;
;;;     +-------------------------------------------------------------------+
;;;     |  Program Name :  Bcc.lsp     Ver 1.0                              |
;;;     |  Purpose      :  Block counting                                   |
;;;     |                  Auto fil, Text update                            |
;;;     |  Syntax       :  Command:(load"bcc.lsp")                          |
;;;     |                  Command:bcc  < Enter >                           |
;;;     |  Designed By  :  CHOONGSIG KIM                                    |
;;;     |                  1995. 11. 10                                     |
;;;     |  Last Upadte  :  1995. 11. 27                                     |
;;;     +-------------------------------------------------------------------+
;;;
(defun c:bcc(/ tr blist bn bsc con SS STR ANS TSS P1 STT )
 (setvar "cmdecho" 0)
 (setq TR(entsel "\nSelect tree to count:"))
 (setq blist(entget (car TR)))
  (setq bn (cdr(assoc 2  blist)))
  (setq bsc(cdr(assoc 41 blist)))
  (setq con(list (cons 2 bn)(cons 41 bsc)))
  (setq ss (ssget "x" con))
  (setq str (sslength ss))
  (setq str (- str 1))
  (setq str (itoa str))
   (setq ans (getstring "\nNew or Change <N>: "))
   (if (or (= ans "C")(= ans "c"))
     (progn
       (setq stt (entsel "\nSelect text to change :"))
       (adt str)
     )
     (progn
       (setq tss (getvar "textsize"))
       (PROMPT "\nThe sum is --> " )
       (princ StR)
       (setq p1  (getpoint "\nPick the text point :"))
       (command "text" p1 tss "" str)
     )
   )
 (princ)
)                           

(defun adt (str / ENT ASS AS1 CON SUB)
 (setq ent (entget (car stt)))
 (setq ass (assoc 1 ent))
 (setq as1 (cdr ass))
 (setq con (cons 1 str))
 (setq sub (subst con ass ent))
 (entmod sub)
 (prin1)
)

 (princ "\nType 'bcc' to Count Tree ...")
 (princ)
