;;;Purge�Ҷ� "Y"������ ������ ����ϼ���...
;
;
;�����:PP.LSP�� Load���� PP�� �Է��ϼ���.
;�׷� Text window�� ��Ÿ���� Purge��Ȳ�� ���� �ݴϴ�.
;Purge�� ����� ���̻� ������ ���� ����ؼ� �ݺ��մϴ�.
;
;
;
;����ó...
;õ���� : ykafox
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
