;;=================================================================
;  넘버링하기(2007.3.주말농부)
;  ->숫자 또는 숫자가 포함된 문자을 다중선택하여 증가할 수치값만큼
;     증가 시키며 번호을 쓰는 명령어.첫번째 문자을 기준으로 함.
;     선택된 문자는 좌에서 우로,위에서 아래로 번호을 증가시킴
;  ->선택순서,글쓰기순서 옵션 추가(2007.4)
;  ->@ss_new_lst.lsp을 같이 로드시켜야됨
;;------- quick numbering -----------------------------------------
(defun c:qn(/ dw ss st1 st2 st3 elist otxt a0len newlist num
                temp a1len a2len a3len a2snum a3snem step num2 en)
   (prompt " 넘버링하기...<숫자포함문자>")
   (setq ss (ssget '((0 . "text"))))
   (setq a (getstring "\n넘버링방법[선택순(1)/글쓰기순(2)] <선택순>: "))
   (if (or (= a "") (= a "1"))
     (setq dw " ...선택순으로 넘버링됨")(progn
     (setq ss (@ss_new_lst ss))
     (setq dw " ...글쓰기순으로 넘버링됨")) )
   (setq sslen (sslength ss))
   (setq k 1)
   (setq en1 (ssname ss 0))

;->문자와 숫자 구분하기(start)
   (setq elist (entget en1))
   (setq otxt (cdr (assoc 1 elist)))
   (setq a0len (strlen otxt))
   (setq st3 "")
   (setq newlist '())
   (setq num 1)
   (while (>= a0len num)
      (setq temp (substr otxt num 1))
      (if (and (>= (ascii temp) 48) (<= (ascii temp) 57))
         (setq newlist (cons num newlist))
      )
      (setq num (+ num 1))
   );while end
   (if newlist
      (progn
         (setq newlist (reverse newlist))
         (setq a2len (length newlist))
         (setq a2snum (nth 0 newlist))
         (setq a1len (- a2snum 1))
         (if (> a0len (+ a1len a2len) )
            (progn
               (setq a3snum (+ a1len a2len 1))
               (setq a3len (- a0len (+ a1len a2len)))
               (setq st3 (substr otxt a3snum a3len))
            )
         )
         (setq st1 (substr otxt 1 a1len))
         (setq st2 (substr otxt a2snum a2len))
         (prin1 st1) (prin1 st2) (prin1 st3) ;문자구분
      );progn end
   );if end
;->문자와 숫자 구분하기(end)

   (setq step (getint "\n증가할 수치값<1> : "))
   (if (not step) (setq step 1))
   (setq num2 (atoi st2))

   (repeat (- sslen 1)
      (setq num2 (+ num2 step))
      (setq st2 (itoa num2))
      (setq st2len (strlen st2))
      (while (> a2len st2len) ; st2 자릿수 맞추기
         (setq st2 (strcat "0" st2))
         (setq st2len (+ st2len 1))
      )
      (setq en (ssname ss k))
      (setq elist (entget en))
      (setq otxt (cdr (assoc 1 elist)))
      (entmod (subst (cons 1 (strcat st1 st2 st3)) (assoc 1 elist) elist))
      (setq k (+ k 1))
   )(terpri)
   (prin1 dw)
(prin1))
