;-----
; 자 료 명 : SCALE을 X,Y따로 주는 LISP
; 파 일 명 : DSC.LSP
; 실 행 명 : DSC
; 만 든 이 : 이수문    wwwcivil@netian.com
; 배 포 처 : http://my.netian.com/~daeho71/
;-----

;******************************
;SCALE을 X,Y따로 주는 LISP   
;                            
;    MADE by Lee Soo-moon
;   처음만든날 2000,09,25
;  최종 수정한날 2000,10,03
;******************************

(defun C:XYB (/ A B STR X Y Z R)
  (SETQ A (SSGET))
  (SETQ B (GETPOINT "\nINSERT POINT:\n"))
  (SETQ STR (GETSTRING "\nName of Block:"))
  (SETQ C 1)
    (prompt "\nX Scale Factor <1>:")
      (SETQ X1 (GETREAL))
      (if (= X1 NIL)(setq X C)
          (SETQ X X1)
      ) ;END IF
    (prompt "\nY Scale Factor (default=X):")
      (SETQ Y1 (GETREAL))
      (if (= Y1 NIL)(setq Y X)
          (SETQ Y Y1)
      ) ;END IF 
   ;****************************************************
   ;다음은 3차원에서 Z축의 SCALE를 지정하는 부분입니다.
   ; (prompt "\nZ Scale Factor (default=Y):")
   ;  (SETQ Z1 (GETREAL))
   ;   (if (= Z1 NIL)(setq Z Y)
   ;       (SETQ Z Z1)
   ;   ) ;END IF 
   ;Z축 SCALE지정 끝
   ;****************************************************
    (SETQ RD 0)    
    (prompt "\nRotation angle <0>:")
      (SETQ R1 (GETREAL))
      (if (= R1 NIL)(setq R RD)
          (SETQ R R1)
      ) ;END IF
  (COMMAND "BLOCK" STR B A "")
  (COMMAND "INSERT" STR B X Y R)
  (PRINC)
) ;END DEFUN


