(defun c:cd (/ #j #k #r #e)
  (setq #j(ssget '((0 . "dimension,leader,mtext,text"))))
  (setq #e 0)
  
  (repeat (sslength #j)
    (setq #k(ssname #j #e))

    (if (eq "LEADER" (strcase(cdr(assoc 0(entget #k)))))

      (progn
      (setq #r(cdr(assoc 340(entget #k))))
      (mapcar 'entdel (list #k #r))
      );;progn

    (entdel #k)

    );;if

    (setq #e(1+ #e))
  );;repeat

);;defun