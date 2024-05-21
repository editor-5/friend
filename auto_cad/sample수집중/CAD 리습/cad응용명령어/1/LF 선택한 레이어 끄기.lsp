(defun c:LLF ()
       (princ "\n Select entity to frozen layer : ")
        (setq A (ssget)
              ln (cdr (assoc 8 (entget (ssname A 0)
                                )
                       )
                  )
         ); setq c
       (command "layer" "off" ln ""))   
