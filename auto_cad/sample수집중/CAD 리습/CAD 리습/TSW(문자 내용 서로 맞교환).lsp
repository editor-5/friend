;;=========================================================
;  문자열 1:1 맞대응 교환하기(2011.7.22)  
;  -> 선택한 두개의 문자열을 서로 맞 교환 시켜주는 명령어
;  -> 선택한 문자열이 두개일 경우만 실행 됨
;  -> 아저씨님 개발하신 드림 툴의 문자 내용 서로 바꾸기(tsw)와 같은 명령어
;  -> 창문들 7번 64 bit에서도 실행 가능
;  -> 출처 : da........@nate.com
;;----------------------------------------------------------

(defun c:TSW (/ ss obj1 obj2 str1 str2) ; 명령어 본인이 원하는 단어로 바꾸어서 사용할수 도 있어요
        (prompt " .........문자열 1:1 맞교환하기...   A <-> B   선택문자가 2개인 경우만 1:1 맞교환됨 ")
  (if (and
	(setq ss (ssget '((0 . "TEXT")))) ;문자를 선택해라
	(= (sslength ss) 2) ;선택한 문자가 두개일경우만 실행시켜라
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
	