;;레이어지우기
(defun C:DL ( / ent slayr echo)
   (setq echo (getvar "CMDECHO"))
   (setvar "CMDECHO" 0)
   (setq ent (entsel
      "\nSelect an entity on the layer you want to DEL: "
   )         )
   (setq ent (entget (car ent)))
   (setq slayr (cdr (assoc 8 ent)))
   (COMMAND "SELECT" (SSGET "X" (LIST(CONS 8 slayr)))"")
   (COMMAND "ERASE" "P" "")
   (setvar "CMDECHO" echo)
   (princ)
); Defun LAYR-DEL