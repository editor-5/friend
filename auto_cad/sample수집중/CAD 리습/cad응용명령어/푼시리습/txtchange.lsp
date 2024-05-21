(defun c:tc()
    (command "redraw")
    (setq i 0)
    (prompt "A->B  A를 선택하세요")
    (setq e1(ssget))
    (setq n (sslength e1))      
    
    (Prompt "\nA->B  B를 선택하세요")
    (setq f1(ssget))
    (setq ed1(entget (setq f2(ssname f1 i))))
    (setq uu1(assoc 1 ed1))
    (setq uu2(cdr uu1))     
    
         
  (while (< i n)

    (setq ed(entget (setq e2(ssname e1 i))))
    (setq tt1(assoc 1 ed))
    (setq tt2(cdr tt1))
    (setq ed(subst (cons 1 uu2)(assoc 1 ed) ed))
    (entmod ed)

  (setq i (+ 1 i))
  )
)

  
