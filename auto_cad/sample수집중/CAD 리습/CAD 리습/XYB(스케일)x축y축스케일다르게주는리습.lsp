;-----
; �� �� �� : SCALE�� X,Y���� �ִ� LISP
; �� �� �� : DSC.LSP
; �� �� �� : DSC
; �� �� �� : �̼���    wwwcivil@netian.com
; �� �� ó : http://my.netian.com/~daeho71/
;-----

;******************************
;SCALE�� X,Y���� �ִ� LISP   
;                            
;    MADE by Lee Soo-moon
;   ó�����糯 2000,09,25
;  ���� �����ѳ� 2000,10,03
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
   ;������ 3�������� Z���� SCALE�� �����ϴ� �κ��Դϴ�.
   ; (prompt "\nZ Scale Factor (default=Y):")
   ;  (SETQ Z1 (GETREAL))
   ;   (if (= Z1 NIL)(setq Z Y)
   ;       (SETQ Z Z1)
   ;   ) ;END IF 
   ;Z�� SCALE���� ��
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


