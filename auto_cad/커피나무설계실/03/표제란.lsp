; 수정방법 
; 먼저 앞부분의 [ ; ] 표시는 프로그램의 코드와 실행에는 영향을 주지 않는 주석문 입니다.
; 여러분들은 ; 표시를 사용하지말고 아래 소스코드처럼 만들어서 사용하세요
; 예)
;(defun c:msh()   (command "change" pause "" "" "" "STANDARD" "" "" "SHAFT"))
;(defun c:단축명령어()   (command "change" pause "" "" "" "STANDARD" "" "" "표시할 단어나 문장 입력"))

;===============================================================
; [1. 품명부]

(defun c:msh()   (command "change" pause "" "" "" "STANDARD" "" "" "SHAFT"))
(defun c:mpl()   (command "change" pause "" "" "" "STANDARD" "" "" "PLATE"))
(defun c:mbr()   (command "change" pause "" "" "" "STANDARD" "" "" "BRK'T"))
(defun c:mbl()   (command "change" pause "" "" "" "STANDARD" "" "" "BLOCK"))
(defun c:mmp()   (command "change" pause "" "" "" "STANDARD" "" "" "MT'G PLATE"))
(defun c:mmbr()   (command "change" pause "" "" "" "STANDARD" "" "" "MT'G BRK'T"))
(defun c:mmt()   (command "change" pause "" "" "" "STANDARD" "" "" "MT'G"))
(defun c:mgu()   (command "change" pause "" "" "" "STANDARD" "" "" "GUIDE"))

;===============================================================
; [2. 소재부]

(defun c:m41()   (command "change" pause "" "" "" "STANDARD" "" "" "SS41"))
(defun c:m45()   (command "change" pause "" "" "" "STANDARD" "" "" "S45C"))
(defun c:msu()   (command "change" pause "" "" "" "STANDARD" "" "" "SUS304"))

(defun c:SK()   (command "change" pause "" "" "" "STANDARD" "" "" "SKD11"))
(defun c:SU()  M45 (command "change" pause "" "" "" "STANDARD" "" "" "SUJ2"))

(defun c:HG()   (command "change" pause "" "" "" "STANDARD" "" "" "헤어라인"))
(defun c:AL()   (command "change" pause "" "" "" "STANDARD" "" "" "AL6061"))
DK(defun c:AT()   (command "change" pause "" "" "" "STANDARD" "" "" "투명 아크릴"))
(defun c:PC()   (command "change" pause "" "" "" "STANDARD" "" "" "PC(투명)"))
(defun c:mal()   (command "change" pause "" "" "" "STANDARD" "" "" "AL6061"))
(defun c:mpc()   (command "change" pause "" "" "" "STANDARD" "" "" "투명PC"))
(defun c:mdg()   (command "change" pause "" "" "" "STANDARD" "" "" "도금봉"))
(defun c:MC()   (command "change" pause "" "" "" "STANDARD" "" "" "MC NYLON (BLACK)"))

;===============================================================
; [3. 후처리, 열처리부]

(defun c:HRC()  (command "change" pause "" "" "" "STANDARD" "" "" "05. 전체열처리 HRC45이상"))
(defun c:HR()   (command "change" pause "" "" "" "STANDARD" "" "" "Cr도금,열처리"))
(defun c:CR()   (command "change" pause "" "" "" "STANDARD" "" "" "Cr도금"))
(defun c:BB()   (command "change" pause "" "" "" "STANDARD" "" "" "백색아노다이징"))
(defun c:HH()   (command "change" pause "" "" "" "STANDARD" "" "" "하드아노다이징"))

(defun c:mcr()   (command "change" pause "" "" "" "STANDARD" "" "" "크롬도금"))
(defun c:mjh()   (command "change" pause "" "" "" "STANDARD" "" "" "전해연마"))
(defun c:mis()   (command "change" pause "" "" "" "STANDARD" "" "" "인산염"))
(defun c:mish()   (command "change" pause "" "" "" "STANDARD" "" "" "인산염(흑착색)"))
(defun c:mdm()   (command "change" pause "" "" "" "STANDARD" "" "" "단면폴리싱"))bb 
(defun c:mym()   (command "change" pause "" "" "" "STANDARD" "" "" "양면폴리싱"))
(defun c:mjj()   (command "change" pause "" "" "" "STANDARD" "" "" "경질피막"))
(defun c:jjg()   (command "change" pause "" "" "" "STANDARD" "" "" "경질피막(국방색)"))
(defun c:myj()   (command "change" pause "" "" "" "STANDARD" "" "" "연질피막"))

(defun c:NA()   (command "change" pause "" "" "" "STANDARD" "" "" "홍길동"))
(defun c:MI1()  (command "change" pause "" "" "" "STANDARD" "" "" "총2EA중 각1EA씩 대칭가공할것."))
(defun c:MI2() (command "change" pause "" "" "" "STANDARD" "" "" "총4EA중 각2EA씩 대칭가공할것."))
(defun c:MI3() (command "change" pause "" "" "" "STANDARD" "" "" "총6EA중 각3EA씩 대칭가공할것."))
(defun c:MI4() (command "change" pause "" "" "" "STANDARD" "" "" "총8EA중 각4EA씩 대칭가공할것."))



