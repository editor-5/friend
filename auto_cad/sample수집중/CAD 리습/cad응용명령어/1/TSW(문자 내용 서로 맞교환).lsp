;;=========================================================
;  ���ڿ� 1:1 �´��� ��ȯ�ϱ�(2011.7.22)  
;  -> ������ �ΰ��� ���ڿ��� ���� �� ��ȯ �����ִ� ��ɾ�
;  -> ������ ���ڿ��� �ΰ��� ��츸 ���� ��
;  -> �������� �����Ͻ� �帲 ���� ���� ���� ���� �ٲٱ�(tsw)�� ���� ��ɾ�
;  -> â���� 7�� 64 bit������ ���� ����
;  -> ��ó : da........@nate.com
;;----------------------------------------------------------

(defun c:TSW (/ ss obj1 obj2 str1 str2) ; ��ɾ� ������ ���ϴ� �ܾ�� �ٲپ ����Ҽ� �� �־��
        (prompt " .........���ڿ� 1:1 �±�ȯ�ϱ�...   A <-> B   ���ù��ڰ� 2���� ��츸 1:1 �±�ȯ�� ")
  (if (and
	(setq ss (ssget '((0 . "TEXT")))) ;���ڸ� �����ض�
	(= (sslength ss) 2) ;������ ���ڰ� �ΰ��ϰ�츸 ������Ѷ�
	(setq obj1 (vlax-ename->vla-object (ssname ss 0)))
	(setq obj2 (vlax-ename->vla-object (ssname ss 1)))
	(setq str1 (vla-get-textstring obj1))
	(setq str2 (vla-get-textstring obj2))
      )
      (progn
	(vla-put-textstring obj1 str2)
	(vla-put-textstring obj2 str1)
      )
  )
)
	