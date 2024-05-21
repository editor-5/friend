(defun C:bf(/ ss p1 ss1 os)
;->*error* start
 (defun *error* (msg)(princ "error: ")(princ msg)
 (setvar "osmode" os)
 (princ))
;-<*error* end
  (setq os (getvar "osmode"))
  (setq ss (ssget))
  (setq p1 (getpoint "\n>>>끊을점을 선택해주세염: "))
  (setq ss1 (ssadd))
  (while p1
   (setvar "osmode" 0)
   (command "break" ss p1 p1)
   (setq ss (ssadd (entlast) ss1))
   (setvar "osmode" os)
   (setq p1 (getpoint "\n>>>끊을점을 선택해주세염: ")) 
  );while
(prin1)
);defun