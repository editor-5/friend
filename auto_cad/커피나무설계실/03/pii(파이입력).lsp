(defun c:pii ()   

   (princ "=pi()")  
   (command "dimoverride" "dimpost" "%%c<>" "") 
   (prompt "\n표시할 치수를 선택하세요.")

   (princ)
)


