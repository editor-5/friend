;;=================================================================
;  �ѹ����ϱ�(2007.3.�ָ����)
;  ->���� �Ǵ� ���ڰ� ���Ե� ������ ���߼����Ͽ� ������ ��ġ����ŭ
;     ���� ��Ű�� ��ȣ�� ���� ��ɾ�.ù��° ������ �������� ��.
;     ���õ� ���ڴ� �¿��� ���,������ �Ʒ��� ��ȣ�� ������Ŵ
;  ->���ü���,�۾������ �ɼ� �߰�(2007.4)
;  ->@ss_new_lst.lsp�� ���� �ε���Ѿߵ�
;;------- quick numbering -----------------------------------------
(defun c:qn(/ dw ss st1 st2 st3 elist otxt a0len newlist num
                temp a1len a2len a3len a2snum a3snem step num2 en)
   (prompt " �ѹ����ϱ�...<�������Թ���>")
   (setq ss (ssget '((0 . "text"))))
   (setq a (getstring "\n�ѹ������[���ü�(1)/�۾����(2)] <���ü�>: "))
   (if (or (= a "") (= a "1"))
     (setq dw " ...���ü����� �ѹ�����")(progn
     (setq ss (@ss_new_lst ss))
     (setq dw " ...�۾�������� �ѹ�����")) )
   (setq sslen (sslength ss))
   (setq k 1)
   (setq en1 (ssname ss 0))

;->���ڿ� ���� �����ϱ�(start)
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
         (prin1 st1) (prin1 st2) (prin1 st3) ;���ڱ���
      );progn end
   );if end
;->���ڿ� ���� �����ϱ�(end)

   (setq step (getint "\n������ ��ġ��<1> : "))
   (if (not step) (setq step 1))
   (setq num2 (atoi st2))

   (repeat (- sslen 1)
      (setq num2 (+ num2 step))
      (setq st2 (itoa num2))
      (setq st2len (strlen st2))
      (while (> a2len st2len) ; st2 �ڸ��� ���߱�
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
