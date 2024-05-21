(defun c:JUML (/ *error* A B1 B2 BDIS DOC ENT OV P1 P2 UFLAG VL)
  (vl-load-com)
  (setq bDis 0.5) ;; 호 반경(Break Distance / 2.0 )

  (defun *error* (msg)
    (and uFlag (vla-EndUndoMark doc))
    (and ov  (mapcar (function setvar) vl ov))
    (and msg (or (wcmatch (strcase msg) "*BREAK,*CANCEL*,*EXIT*")
                 (princ (strcat "\n** Error: " msg " **"))))
    (princ))

  (setq doc (vla-get-ActiveDocument (vlax-get-acad-object))
        vl '("CMDECHO" "OSMODE") ov (mapcar (function getvar) vl))

  (while (and (setq uFlag (not (vla-StartUndoMark doc)))
              (mapcar  (function setvar) vl '(0 32))
              (setq p1 (getpoint "\n삽입점 선택: "))
              (setq ent (entsel "\n끊을 선 선택: ")))

    (setq p2 (osnap (cadr ent) "_nea")
          b1 (polar p1 (setq a (angle p1 p2)) bDis)
          b2 (polar p1 (+ pi a) bDis))
    
    (setvar "OSMODE" 0)
    (command "_.break" b1 b2)
    (if (> a (/ pi 2.))
      (command "_.arc" b2 "_E" b1 "_A" 180.)
      (command "_.arc" b1 "_E" b2 "_A" 180.))

    (setq uFlag (vla-EndUndoMark doc)))

  (*error* nil)  
  (princ)
)

;;;;

(defun c:JUMR (/ *error* A B1 B2 BDIS DOC ENT OV P1 P2 UFLAG VL)
  (vl-load-com)
  (setq bDis 0.5) ;; 호 반경(Break Distance / 2.0 )

  (defun *error* (msg)
    (and uFlag (vla-EndUndoMark doc))
    (and ov  (mapcar (function setvar) vl ov))
    (and msg (or (wcmatch (strcase msg) "*BREAK,*CANCEL*,*EXIT*")
                 (princ (strcat "\n** Error: " msg " **"))))
    (princ))

  (setq doc (vla-get-ActiveDocument (vlax-get-acad-object))
        vl '("CMDECHO" "OSMODE") ov (mapcar (function getvar) vl))

  (while (and (setq uFlag (not (vla-StartUndoMark doc)))
              (mapcar  (function setvar) vl '(0 32))
              (setq p1 (getpoint "\n삽입점 선택: "))
              (setq ent (entsel "\n끊을 선 선택: ")))

    (setq p2 (osnap (cadr ent) "_nea")
          b2 (polar p1 (setq a (angle p1 p2)) bDis)
          b1 (polar p1 (+ pi a) bDis))
    
    (setvar "OSMODE" 0)
    (command "_.break" b1 b2)
    (if (> a (/ pi 2.))
      (command "_.arc" b2 "_E" b1 "_A" 180.)
      (command "_.arc" b1 "_E" b2 "_A" 180.))

    (setq uFlag (vla-EndUndoMark doc)))

  (*error* nil)  
  (princ)
)