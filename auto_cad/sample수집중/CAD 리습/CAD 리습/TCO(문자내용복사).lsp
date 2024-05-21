; 아키모아 운영진 "행복한하루"
; http://cafe.daum.net/archimore

(defun C:TCO(/ dec ent ed ena otex var ss k ed1)
 (princ " \n>> 문자 내용 동일화 (Text All Same...)")
 (princ "\n선택된 문자를 모두 동일한 문자 내용으로 변경합니다!")
 (setq dec (getvar "dimdec"))
 (if (setq ent (entsel "\nOriginal object select:"))
  (progn (redraw (car ent) 3)
   (setq ed (entget (car ent))) 
   (setq ena (cdr (assoc 0 ed)))
   (cond ((or (= ena "TEXT") (= ena "MTEXT")) (setq otex (assoc 1 ed)))
         ((= ena "DIMENSION") 
          (setq var (cdr (assoc 1 ed)))
          (if (= var "") 
           (setq otex (cons 1 (rtos (cdr (assoc 42 ed)) 2 dec)))
           (setq otex (assoc 1 ed))
          )
         )
   )
   (princ "\nAlteration object select:")
   (if (setq ss (ssget (list (cons 0 "text,mtext,dimension"))))
    (progn (setq k 0) 
     (repeat (sslength ss) 
      (setq ed1 (entget (ssname ss k)))
      (entmod (subst otex (assoc 1 ed1) ed1))
      (setq k (1+ k))
     ) ;repeat
    );progn
   );if
  (redraw (car ent) 4)
  );progn
 );if
(princ) 
)


;                                                      
; 선택한 객체의 문자,치수,블럭내문자,블럭내치수를 삭제 
;Text Sellect Delete

(defun delblock ( e / obj blname blocks blobj ee een eename item )
  (setq obj (vlax-ename->vla-object e))
  (setq blname (vla-get-name obj))
  (setq blocks (vla-get-blocks doc))
  (setq blobj (vla-item blocks blname))
  (vlax-for item blobj
    (setq ee (vlax-vla-object->ename item))
    (setq een (entget ee))
    (setq eename (cdr (assoc 0 een)))
    (if (or (= eename "TEXT") (= eename "MTEXT") (= eename "LEADER") (= eename "MULTILEADER") (= eename "DIMENSION")) (vla-delete item))
  )
)

(defun c:tsd ( / ss doc index e en ename )
  (if (setq ss (ssget (list (cons 0 "TEXT,MTEXT,DIMENSION,LEADER,MULTILEADER,INSERT"))))
    (progn
      (setq doc (vla-get-activedocument (vlax-get-acad-object)))
      (vla-startundomark doc)
      (setq index 0)
      (repeat (sslength ss)
	(setq e (ssname ss index))
	(setq en (entget e))
	(setq ename (cdr (assoc 0 en)))
	(cond
	  ((or (= ename "TEXT") (= ename "MTEXT") (= ename "LEADER") (= ename "MULTILEADER") (= ename "DIMENSION")) (entdel e))
	  ((= ename "INSERT") (delblock e))
	)
	(setq index (1+ index))
      )
      (vla-regen doc acAllViewports)
      (vla-endundomark doc)
    )
  )
  (princ)
)
(vl-load-com)
;(prompt "\n[ EB ]")
(princ)
