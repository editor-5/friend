(defun dtr (x) (* pi (/ x 180.0)))
;---------------------------------------
; Prog name : ISO-DIMension
; Prog by   : mskim
; Prog Date : 97.05
; Rev. Date : 02.09
;---------------------------------------
;---화면 그리기 ------------------------
(defun DISP (scp sc col / sp p1 p2 p3 p4)
            ;;외부변수 LX LY HX HY X1 X2 Y1
    ;;
    ;;            hy
    ;;      +-----+-----+         +-----------+
    ;;      |  x1   x2  |         | 1 | 2 | 3 |
    ;;    lx+---+-*-+---+hx       |-----------|
    ;;      |     y1    |         | 4 | 5 | 6 |
    ;;      +-----+-----+         +-----------+
    ;;            ly
    (setq lx (- (car scp) (/ sc 1.0)))
    (setq hx (+ (car scp) (/ sc 1.0)))
    (setq ly (- (cadr scp) (/ sc 2.0)))
    (setq hy (+ (cadr scp) (/ sc 2.0)))

    (grdraw (list lx ly) (list hx ly) col)
    (grdraw (list hx ly) (list hx hy) col)
    (grdraw (list hx hy) (list lx hy) col)
    (grdraw (list lx hy) (list lx ly) col)

    (setq x1 (+ lx (/ sc 1.5)))
    (setq x2 (- hx (/ sc 1.5)))
    (setq y1 (+ ly (/ sc 2.0)))

    (grdraw (list x1 hy) (list x1 ly) col)
    (grdraw (list x2 hy) (list x2 ly) col)
    (grdraw (list lx y1) (list hx y1) col)

    (setq sp (/ sc 8.0))
    ;------- 1,3 --------
    (setq p1 (list (+ lx (* sp 2)) (+ y1 (/ sp 1))))
    (setq p2 (polar p1 (dtr 150) (* sp 1.5)))
    (setq p3 (polar p2 (dtr  30) (* sp 3.0)))
    (setq p4 (polar p3 (dtr 330) (* sp 1.5)))
    (grdraw p1 p2 col)
    (grdraw p2 p3 col)
    (grdraw p3 p4 col)

    (setq p1 (list (- hx (* sp 2)) (+ y1 (* sp 1))))
    (setq p2 (polar p1 (dtr  30) (* sp 1.5)))
    (setq p3 (polar p2 (dtr 150) (* sp 3.0)))
    (setq p4 (polar p3 (dtr 210) (* sp 1.5)))
    (grdraw p1 p2 col)
    (grdraw p2 p3 col)
    (grdraw p3 p4 col)

    ;------- 4,6 --------
    (setq p1 (list (+ lx (* sp 1.3)) (+ ly (/ sp 2))))
    (setq p2 (polar p1 (dtr  90) (* sp 1.5)))
    (setq p3 (polar p2 (dtr  30) (* sp 3.0)))
    (setq p4 (polar p3 (dtr 270) (* sp 1.5)))
    (grdraw p1 p2 col)
    (grdraw p2 p3 col)
    (grdraw p3 p4 col)

    (setq p1 (list (- hx (* sp 1.3)) (+ ly (/ sp 2))))
    (setq p2 (polar p1 (dtr  90) (* sp 1.5)))
    (setq p3 (polar p2 (dtr 150) (* sp 3.0)))
    (setq p4 (polar p3 (dtr -90) (* sp 1.5)))
    (grdraw p1 p2 col)
    (grdraw p2 p3 col)
    (grdraw p3 p4 col)

    ;------- 2,5 --------
    (grdraw (list (+ x1 (* sp 2.0)) (- hy (/ sp 2))) (list (- x2 (* sp 2.0)) (- hy (* sp 1.5))) col)
    (grdraw (list (+ x1 (* sp 2.5)) (- hy sp)) (list (+ x1 (* sp 2.5)) (+ y1 (* sp 1.2))) col)
    (grdraw (list (+ x1 (* sp 2.0)) (+ y1 (* sp 1.5))) (list (- x2 (* sp 2.0)) (+ y1 (/ sp 2))) col)

    (grdraw (list (+ x1 (* sp 2.0)) (- y1 (* sp 1.5))) (list (- x2 (* sp 2.0)) (- y1 (/ sp 2))) col)
    (grdraw (list (- x2 (* sp 2.5)) (- y1 sp)) (list (- x2 (* sp 2.5)) (+ ly (* sp 1.2))) col)
    (grdraw (list (+ x1 (* sp 2.0)) (+ ly (/ sp 2))) (list (- x2 (* sp 2.0)) (+ ly (* sp 1.5))) col)
)

;---------------------------------------
;---MAIN Program.-----------------------
;---------------------------------------
(defun C:idim (/ pt px py)
    (setq col 2)                 ;;-display Color
    (setq menu_size 6)           ;;-display menu Size
    (setq sc (/ (getvar "VIEWSIZE") menu_size))
    (setq scp (cadr (grread 1))) ;;-current mouse Location

    ;;----------------------------
    (princ "\n>>Dimension Type: ")
    (disp scp sc col)
    ;;----------------------------
    (defun *ERROR* (s)
        (princ "\nFunction cancelled!")
        (disp scp sc 0)
        (setq *ERROR* nil)
    )
    (setq pt (grread))
    (setq px (car (cadr pt)))
    (setq py (cadr (cadr pt)))
    (disp scp sc 0)
    (if (and (< lx px hx) (< ly py hy))
        (if (< y1 py)
            (cond ((< px x1) (setq txt_ob -30  dim_ob 210 lin_ob 150)) ;1
                  ((< px x2) (setq txt_ob  30  dim_ob  90 lin_ob 150)) ;2
                  (T         (setq txt_ob  30  dim_ob 150 lin_ob  30)) ;3
            )
            (cond ((< px x1) (setq txt_ob  30  dim_ob 210 lin_ob  90)) ;4
                  ((< px x2) (setq txt_ob -30  dim_ob  90 lin_ob  30)) ;5
                  (T         (setq txt_ob -30  dim_ob 150 lin_ob  90)) ;6
            )
        )
        (exit)
    )
    (setvar "cmdecho" 0)
    (if (null (tblsearch "block" "ISOARROW"))
      (progn
        ;(command "insert" "ISOARROW" "0,0" "" "" "")
        (command "style" "DIM30R" "ROMANS" "0" "1" "30" "n" "n" "n")
        (command "style" "DIM30L" "ROMANS" "0" "1" "-30" "n" "n" "n")
      )
    )
    (if (= txt_ob 30)
      (progn
        (setvar "dimtxsty" "DIM30R") ;;Dimension Text Style
       ;(setvar "dimblk"   "ARROW30R")	여기에서 정의한 치수화살표의 블록이 정의되지 않아서 그런것 같네요 (ARROW30R)
      )
      (progn
        (setvar "dimtxsty" "DIM30L") ;;Dimension Text Style
       ; (setvar "dimblk"   "ARROW30L")	여기에서 정의한 치수화살표의 블록이 정의되지 않아서 그런것 같네요 (ARROW30L)
      )
    )
    (setvar "dimaso" 1)
    (command "dim1" "rotated" dim_ob pause pause pause "")
    (command "dim1" "ob" "l" "" lin_ob)
    ;;(setvar "dimaso" 0)
    (setvar "cmdecho" 1)
    (princ)
)


