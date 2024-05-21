;;;Purge할때 "Y"누르기 싫으면 사용하세요...
;
;
;사용방법:PP.LSP를 Load한후 PP를 입력하세요.
;그럼 Text window가 나타나며 Purge상황을 보여 줍니다.
;Purge는 지울게 더이상 없을때 까지 계속해서 반복합니다.
;
;
;
;연락처...
;천리안 : ykafox
;email  : ykafox@chollian.net



(defun myerr(msg)
     (if (/= msg "Function cancelled")
         (princ (strcat "\nError: " msg))
   )
   (setq *error* err)
   (princ)
)



(defun c:pp()

  (setq err *error* *error* myerr)

  (textscr)
  (setvar "cmdecho" 0)

  (if (= "DIM" (getvar "cmdnames")) (command "exit"))

  (setvar "cmdecho" 1)

  (fp)

  (while (/= fm "")

       (rp)
       (fp)

  )


  (setq *error* err)
  (princ)

)




(defun fp()


  (command "purge")
  (command "all")
  (princ "\n")
  (command "")
  (princ "\n")
  (command "")

  (setq fm (getvar "cmdnames")
        cm fm)


)


(defun rp()

  (while (/= cm "")
     (command "y")

     (setq cm (getvar "cmdnames"))
  )


)

(Princ "\nC:PP  AutoPurge.  1999.11.16")
(princ)
